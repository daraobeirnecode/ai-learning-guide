#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import unquote
from collections import Counter
import hashlib
import ipaddress
import json
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []
REQUIRED = {
    'README.md', 'SOURCE_INDEX.md', 'LICENSE.md', 'SECURITY.md',
    'guide/MASTER_LEARNING_GUIDE.md', 'manifest/sources.json',
    'manifest/export-report.json', 'manifest/external-links.json',
    'manifest/SHA256SUMS', 'scripts/validate_package.py'
}
EXPECTED_COLLECTIONS = {'Knowledge Hub': 68, 'Inish Labs': 29}
EXPECTED_CHAPTER_ANCHORS = {f'chapter-{i}' for i in range(21)}
ALLOWED_MODES = {'sanitized-copy', 'privacy-stub', 'source-stub'}


def fail(message):
    ERRORS.append(message)


def rel(path):
    return path.relative_to(ROOT).as_posix()


def text(path):
    return path.read_text(encoding='utf-8', errors='replace')


def noncode(value):
    return re.sub(r'```.*?```|~~~.*?~~~|`[^`\n]+`', '', value, flags=re.S)


def github_slug(value):
    value = re.sub(r'<[^>]+>', '', value)
    value = re.sub(r'[`*_~]', '', value).strip().lower()
    value = ''.join(ch for ch in unicodedata.normalize('NFKD', value)
                    if not unicodedata.combining(ch))
    value = re.sub(r'[^\w\- ]', '', value)
    return value.replace(' ', '-')


def anchors_for(path):
    raw = text(path)
    anchors = set(re.findall(r'<a\s+(?:name|id)=["\']([^"\']+)["\']\s*></a>', raw, re.I))
    seen = Counter()
    in_fence = False
    for line in raw.splitlines():
        if re.match(r'^\s*(```|~~~)', line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*\s*$', line)
        if not match:
            continue
        base = github_slug(match.group(1))
        if not base:
            continue
        suffix = seen[base]
        anchors.add(base if suffix == 0 else f'{base}-{suffix}')
        seen[base] += 1
    return anchors


def markdown_targets(raw):
    clean = noncode(raw)
    targets = []
    targets.extend(re.findall(r'\[[^\]]*\]\((?:<)?([^)>\s]+)(?:>)?(?:\s+["\'][^)]*["\'])?\)', clean))
    targets.extend(re.findall(r'^\s*\[[^\]]+\]:\s*<?([^>\s]+)>?', clean, re.M))
    targets.extend(re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\']', clean, re.I))
    return targets


def local_target(source, target):
    if target.startswith(('http://', 'https://', 'mailto:', 'tel:', 'data:', 'javascript:')):
        return None
    target = unquote(target)
    path_part, sep, fragment = target.partition('#')
    candidate = source if not path_part else (source.parent / path_part)
    try:
        resolved = candidate.resolve()
        resolved.relative_to(ROOT.resolve())
    except (ValueError, OSError):
        fail(f'{rel(source)}: path escapes repository: {target}')
        return None
    if not resolved.exists():
        fail(f'{rel(source)}: missing local target: {target}')
        return None
    if fragment and resolved.suffix.lower() == '.md':
        fragment = unquote(fragment).lower()
        if fragment not in {a.lower() for a in anchors_for(resolved)}:
            fail(f'{rel(source)}: missing anchor #{fragment} in {rel(resolved)}')
    return resolved


for required in sorted(REQUIRED):
    if not (ROOT / required).is_file():
        fail(f'missing required file: {required}')

all_files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts]
if any(p.is_symlink() for p in ROOT.rglob('*') if '.git' not in p.parts):
    fail('symlinks are not allowed in the package')
for p in all_files:
    if p.stat().st_size > 1_000_000:
        fail(f'oversized file (>1 MB): {rel(p)}')
    if re.search(r'(^|/)(\.env(?:\..*)?|auth\.json|credentials?(?:\..*)?|secrets?(?:\..*)?|id_(?:rsa|ed25519)|[^/]+\.(?:pem|key))$', rel(p), re.I):
        fail(f'credential-like filename: {rel(p)}')

md_files = sorted(p for p in all_files if p.suffix.lower() == '.md')
local_links_checked = 0
for source in md_files:
    for target in markdown_targets(text(source)):
        if local_target(source, target) is not None:
            local_links_checked += 1

# Generic public-safety checks. User/client-specific deny lists stay in the private exporter,
# not in this public script.
scan_files = [p for p in all_files if rel(p) not in {'scripts/validate_package.py', 'manifest/validation.json'}]
scan_text = '\n'.join(text(p) for p in scan_files if p.suffix.lower() in {'.md', '.json', '.txt', ''})
scan_noncode = noncode(scan_text)
patterns = {
    'private_key': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    'provider_token': r'\b(?:sk-[A-Za-z0-9_-]{12,}|gh[opusr]_[A-Za-z0-9_]{12,}|xox[baprs]-[A-Za-z0-9-]{12,}|AIza[A-Za-z0-9_-]{20,}|hf_[A-Za-z0-9]{12,})\b',
    'email': r'(?<![\w.+-])(?!git@github\.com\b|git@gitlab\.com\b)[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![\w.-])',
    'phone': r'(?<!\d)(?:\+?1[-. ]?)?\(?[2-9]\d{2}\)?[-. ]\d{3}[-. ]\d{4}(?!\d)',
    'telegram_chat_id': r'(?<!\d)-100\d{7,}(?!\d)',
    'bot_handle': r'@[A-Za-z0-9_]+_bot\b',
    'mac_user_path': r'/Users/(?!yourname(?:/|\b)|USER(?:/|\b))[A-Za-z0-9._-]+',
    'windows_user_path': r'[A-Z]:\\Users\\(?!YourName(?:\\|\b)|yourname(?:\\|\b)|USER(?:\\|\b))[A-Za-z0-9._-]+',
    'wsl_user_path': r'/mnt/[a-z]/Users/(?!YourName(?:/|\b)|yourname(?:/|\b)|USER(?:/|\b))[A-Za-z0-9._-]+',
    'source_path_frontmatter': r'(?m)^source_path\s*:',
    'obsidian_uri': r'obsidian://open\?',
    'wikilink': r'\[\[[^\]]+\]\]',
    'remote_pipe_exec': r'(?i)(?:curl|wget)\s+-[^\n|]*\|\s*(?:bash|sh)\b|\birm\s+https?://[^\n|]+\|\s*iex\b',
    'private_key_copy': r'cp\s+~/\.ssh/id_(?:rsa|ed25519)\b',
    'unpinned_global_npm': r'(?m)^\s*npm\s+(?:i|install)\s+-g\b',
}
hits = {name: len(re.findall(pattern, scan_noncode if name in {'obsidian_uri', 'wikilink'} else scan_text, re.I | re.M))
        for name, pattern in patterns.items()}
for name, count in hits.items():
    if count:
        fail(f'{name}: {count} finding(s)')

# Reject all non-documentation IPv4 literals except local bind examples.
allowed_ip_prefixes = ('127.', '0.0.0.0', '192.0.2.', '198.51.100.', '203.0.113.')
ip_findings = []
for match in re.finditer(r'(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])', scan_text):
    value = match.group(0)
    try:
        ipaddress.ip_address(value)
    except ValueError:
        continue
    if not value.startswith(allowed_ip_prefixes):
        ip_findings.append(value)
if ip_findings:
    fail(f'non-documentation IPv4 literals: {len(ip_findings)} finding(s)')

manifest_path = ROOT / 'manifest/sources.json'
manifest = json.loads(text(manifest_path)) if manifest_path.exists() else []
if len(manifest) != 97:
    fail(f'manifest must contain 97 sources, found {len(manifest)}')
collections = Counter(row.get('collection') for row in manifest)
if dict(collections) != EXPECTED_COLLECTIONS:
    fail(f'collection counts mismatch: {dict(collections)}')
required_fields = {'collection', 'public_path', 'title', 'content_mode', 'sha256'}
public_paths = []
for index, row in enumerate(manifest):
    missing = required_fields - set(row)
    if missing:
        fail(f'manifest row {index} missing fields: {sorted(missing)}')
        continue
    if 'source_path' in row:
        fail(f'manifest row {index} exposes private source_path')
    if row['content_mode'] not in ALLOWED_MODES:
        fail(f'manifest row {index} has invalid content_mode: {row["content_mode"]}')
    public_paths.append(row['public_path'])
    p = ROOT / row['public_path']
    try:
        p.resolve().relative_to(ROOT.resolve())
    except ValueError:
        fail(f'manifest row {index} escapes repository')
        continue
    if not p.is_file():
        fail(f'manifest path missing: {row["public_path"]}')
        continue
    digest = hashlib.sha256(p.read_bytes()).hexdigest()
    if digest != row['sha256']:
        fail(f'manifest hash mismatch: {row["public_path"]}')
    raw = text(p)
    for field in ('source_collection:', 'public_export:', 'content_mode:'):
        if field not in raw[:800]:
            fail(f'{row["public_path"]}: missing frontmatter field {field}')
    if 'source_path:' in raw[:800]:
        fail(f'{row["public_path"]}: exposes private source_path')
    if row['content_mode'] == 'privacy-stub' and 'Public-export privacy stub' not in raw:
        fail(f'{row["public_path"]}: malformed privacy stub')
    if row['content_mode'] == 'source-stub' and ('Public-export source stub' not in raw or 'http' not in raw):
        fail(f'{row["public_path"]}: malformed source stub')
if len(public_paths) != len(set(public_paths)):
    fail('manifest has duplicate public_path values')
source_files = {rel(p) for p in (ROOT / 'sources').rglob('*.md')}
if source_files != set(public_paths):
    fail(f'manifest/source reverse completeness mismatch: missing={sorted(source_files-set(public_paths))}, extra={sorted(set(public_paths)-source_files)}')

mode_counts = Counter(row.get('content_mode') for row in manifest)
redaction_totals = Counter()
for row in manifest:
    for key, value in row.get('redaction_counts', {}).items():
        if not isinstance(value, int) or value < 0:
            fail(f'{row.get("public_path")}: invalid redaction count {key}={value!r}')
        else:
            redaction_totals[key] += value
export_report = json.loads(text(ROOT / 'manifest/export-report.json'))
if export_report.get('content_modes') != dict(mode_counts):
    fail('export-report content_modes do not match sources manifest')
if export_report.get('redactions') != dict(redaction_totals):
    fail('export-report redactions do not match summed manifest redaction_counts')

readme_text = text(ROOT / 'README.md')
readme_targets = set(markdown_targets(readme_text))
if 'guide/MASTER_LEARNING_GUIDE.md' not in readme_targets:
    fail('README start route does not target guide/MASTER_LEARNING_GUIDE.md')
expected_readme_summary = (
    f'**{len(manifest)} directly linked source routes** under `sources/`: '
    f'{mode_counts["sanitized-copy"]} sanitized educational copies, '
    f'{mode_counts["privacy-stub"]} privacy stubs and '
    f'{mode_counts["source-stub"]} third-party source stubs.'
)
if expected_readme_summary not in readme_text:
    fail('README source-route composition summary does not match sources manifest')

source_index = ROOT / 'SOURCE_INDEX.md'
index_paths = set()
for target in markdown_targets(text(source_index)):
    resolved = local_target(source_index, target)
    if resolved and resolved.suffix.lower() == '.md' and 'sources' in resolved.parts:
        index_paths.add(rel(resolved))
if index_paths != set(public_paths):
    fail('SOURCE_INDEX links do not exactly match manifest public paths')

guide = ROOT / 'guide/MASTER_LEARNING_GUIDE.md'
guide_source_paths = set()
for target in markdown_targets(text(guide)):
    resolved = local_target(guide, target)
    if resolved and resolved.suffix.lower() == '.md' and 'sources' in resolved.parts:
        guide_source_paths.add(rel(resolved))
if guide_source_paths != set(public_paths):
    fail('master guide unique source links do not exactly match manifest public paths')
guide_anchors = anchors_for(guide)
if not EXPECTED_CHAPTER_ANCHORS.issubset(guide_anchors):
    fail(f'missing explicit chapter anchors: {sorted(EXPECTED_CHAPTER_ANCHORS-guide_anchors)}')

external = json.loads(text(ROOT / 'manifest/external-links.json'))
if len(external) != 22:
    fail(f'external link report must contain 22 records, found {len(external)}')
for row in external:
    status = row.get('status')
    if not isinstance(status, int) or not 200 <= status < 400:
        fail(f'unhealthy external link record: {row.get("url")} status={status}')

checksum_path = ROOT / 'manifest/SHA256SUMS'
checksum_rows = {}
for line in text(checksum_path).splitlines():
    match = re.match(r'^([0-9a-f]{64})  (.+)$', line)
    if not match:
        fail(f'malformed checksum line: {line}')
        continue
    checksum_rows[match.group(2)] = match.group(1)
expected_checksum_files = {rel(p) for p in all_files if p != checksum_path}
if set(checksum_rows) != expected_checksum_files:
    fail('SHA256SUMS does not exactly cover all package files except itself')
for name, expected in checksum_rows.items():
    p = ROOT / name
    if p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest() != expected:
        fail(f'checksum mismatch: {name}')

report = {
    'files': len(all_files),
    'markdown_files': len(md_files),
    'local_links_checked': local_links_checked,
    'manifest_sources': len(manifest),
    'collections': dict(collections),
    'content_modes': dict(Counter(row.get('content_mode') for row in manifest)),
    'unique_guide_sources': len(guide_source_paths),
    'chapter_anchors': len(EXPECTED_CHAPTER_ANCHORS & guide_anchors),
    'external_links_healthy': sum(1 for row in external if isinstance(row.get('status'), int) and 200 <= row['status'] < 400),
    'sensitive_hits': hits,
    'errors': ERRORS,
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(1 if ERRORS else 0)
