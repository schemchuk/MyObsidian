#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validates knowledge base structure: duplicates, metadata, broken links
"""

import re
from pathlib import Path
from datetime import datetime
import yaml
from difflib import SequenceMatcher

VAULT = Path(".")
VALID_CATEGORIES = ["networking", "pentesting", "java_spring", "linux", "other"]


def parse_frontmatter(content):
    """Extract YAML frontmatter"""
    if not content.startswith('---'):
        return None, content

    try:
        end = content.find('---', 3)
        if end == -1:
            return None, content
        fm_text = content[3:end]
        fm = yaml.safe_load(fm_text)
        body = content[end + 3:].strip()
        return fm, body
    except:
        return None, content


def calculate_similarity(text1, text2):
    """Calculate text similarity (0-1)"""
    return SequenceMatcher(None, text1, text2).ratio()


def get_wikilinks(content):
    """Extract all wikilinks [[...]]"""
    return re.findall(r'\[\[([^\]]+)\]\]', content)


class KnowledgeValidator:
    def __init__(self):
        self.files = []
        self.errors = []
        self.warnings = []
        self.stats = {}

    def load_files(self):
        """Load all MD files"""
        all_files = [
            p for p in VAULT.rglob("*.md")
            if ".obsidian" not in str(p) and "nlm-sources" not in str(p)
            and "scripts" not in str(p)
        ]

        for file_path in sorted(all_files):
            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
                fm, body = parse_frontmatter(content)

                self.files.append({
                    'path': file_path,
                    'name': file_path.name,
                    'frontmatter': fm,
                    'body': body,
                    'full_content': content
                })
            except Exception as e:
                self.errors.append(f"[LOAD] {file_path.name}: {str(e)[:50]}")

        print(f"Loaded {len(self.files)} files")

    def check_frontmatter(self):
        """Check presence and validity of frontmatter"""
        for f in self.files:
            if f['frontmatter'] is None:
                self.errors.append(f"[FM] {f['name']}: No YAML frontmatter")
                continue

            fm = f['frontmatter']

            # Check required fields
            required = ['title', 'category', 'tags', 'status']
            for field in required:
                if field not in fm:
                    self.errors.append(f"[FM] {f['name']}: Missing field '{field}'")

            # Check category
            if fm.get('category') not in VALID_CATEGORIES:
                self.warnings.append(
                    f"[FM] {f['name']}: Unknown category '{fm.get('category')}'"
                )

            # Check tags
            tags = fm.get('tags', [])
            if not tags or (isinstance(tags, list) and len(tags) == 0):
                self.warnings.append(f"[FM] {f['name']}: Empty tags")

            # Check status
            valid_statuses = ['draft', 'published', 'archived', 'needs-review']
            if fm.get('status') not in valid_statuses:
                self.warnings.append(
                    f"[FM] {f['name']}: Unknown status '{fm.get('status')}'"
                )

    def check_duplicates(self):
        """Find duplicate content (>70% similarity)"""
        duplicates = []

        for i, f1 in enumerate(self.files):
            for f2 in self.files[i + 1:]:
                similarity = calculate_similarity(
                    f1['body'][:500],
                    f2['body'][:500]
                )

                if similarity > 0.7:
                    duplicates.append({
                        'file1': f1['name'],
                        'file2': f2['name'],
                        'similarity': f"{similarity:.1%}"
                    })

                    self.warnings.append(
                        f"[DUP] {f1['name']} ~ {f2['name']} ({similarity:.1%})"
                    )

        return duplicates

    def check_links(self):
        """Check for broken wikilinks"""
        all_titles = {
            f['frontmatter'].get('title', f['name'].replace('.md', '')): f['name']
            for f in self.files if f['frontmatter']
        }

        for f in self.files:
            wikilinks = get_wikilinks(f['body'])

            for link in wikilinks:
                search_title = link.split('|')[0].strip()

                if search_title not in all_titles:
                    self.warnings.append(
                        f"[LINK] {f['name']}: Broken link [[{link}]]"
                    )

    def generate_stats(self):
        """Collect statistics"""
        categories = {}
        statuses = {}

        for f in self.files:
            if not f['frontmatter']:
                continue

            cat = f['frontmatter'].get('category', 'unknown')
            status = f['frontmatter'].get('status', 'unknown')

            categories[cat] = categories.get(cat, 0) + 1
            statuses[status] = statuses.get(status, 0) + 1

        self.stats = {
            'total_files': len(self.files),
            'categories': categories,
            'statuses': statuses,
            'total_size_mb': sum(f['path'].stat().st_size for f in self.files) / (1024 * 1024)
        }

    def generate_report(self):
        """Generate HTML report"""
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Knowledge Validation Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #333; }}
        .stats {{ background: #f0f0f0; padding: 15px; border-radius: 5px; margin: 20px 0; }}
        .error {{ color: #d32f2f; margin: 5px 0; }}
        .warning {{ color: #f57c00; margin: 5px 0; }}
        .success {{ color: #388e3c; margin: 5px 0; }}
        table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background: #4CAF50; color: white; }}
    </style>
</head>
<body>
    <h1>Knowledge Base Validation Report</h1>
    <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

    <div class="stats">
        <h2>Statistics</h2>
        <table>
            <tr><td>Total Files</td><td>{self.stats['total_files']}</td></tr>
            <tr><td>Total Size</td><td>{self.stats['total_size_mb']:.2f} MB</td></tr>
        </table>

        <h3>By Category</h3>
        <table>
            <tr><th>Category</th><th>Count</th></tr>
"""

        for cat, count in sorted(self.stats['categories'].items()):
            html += f"            <tr><td>{cat}</td><td>{count}</td></tr>\n"

        html += """        </table>

        <h3>By Status</h3>
        <table>
            <tr><th>Status</th><th>Count</th></tr>
"""

        for status, count in sorted(self.stats['statuses'].items()):
            html += f"            <tr><td>{status}</td><td>{count}</td></tr>\n"

        html += f"""        </table>
    </div>

    <h2>Errors ({len(self.errors)} total)</h2>
"""

        if self.errors:
            for error in self.errors[:50]:
                html += f'    <div class="error">• {error}</div>\n'
        else:
            html += '    <div class="success">OK - No errors!</div>\n'

        html += f"""
    <h2>Warnings ({len(self.warnings)} total)</h2>
"""

        if self.warnings:
            for warning in self.warnings[:50]:
                html += f'    <div class="warning">• {warning}</div>\n'
        else:
            html += '    <div class="success">OK - No warnings!</div>\n'

        html += """
    <h2>Validation Complete</h2>
    <p>Next steps:</p>
    <ol>
        <li>Fix all errors</li>
        <li>Review warnings</li>
        <li>Run export: python3 scripts/multi_format_export.py</li>
    </ol>
</body>
</html>
"""

        report_path = Path("reports/validation_report.html")
        report_path.parent.mkdir(exist_ok=True)
        report_path.write_text(html, encoding="utf-8")

        return report_path

    def run(self):
        """Run full validation"""
        print("\nValidating knowledge base...\n")

        self.load_files()
        print("OK - Files loaded\n")

        self.check_frontmatter()
        print("OK - Frontmatter checked\n")

        duplicates = self.check_duplicates()
        print(f"OK - Duplicates checked ({len(duplicates)} found)\n")

        self.check_links()
        print("OK - Links checked\n")

        self.generate_stats()
        print("OK - Stats generated\n")

        report_path = self.generate_report()

        # Summary
        print("=" * 60)
        print(f"ERRORS: {len(self.errors)}")
        print(f"WARNINGS: {len(self.warnings)}")
        print(f"FILES: {self.stats['total_files']}")
        print(f"SIZE: {self.stats['total_size_mb']:.2f} MB")
        print("=" * 60)

        if self.errors:
            print(f"\nFirst 10 errors:")
            for error in self.errors[:10]:
                print(f"  • {error}")

        if self.warnings:
            print(f"\nFirst 10 warnings:")
            for warning in self.warnings[:10]:
                print(f"  • {warning}")

        print(f"\nReport saved: {report_path}")
        print("\nValidation complete!")


if __name__ == "__main__":
    validator = KnowledgeValidator()
    validator.run()
