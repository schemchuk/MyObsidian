#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Валідує структуру знань: дублювання, метаданні, посилання
"""

import re
from pathlib import Path
from datetime import datetime
import yaml
from difflib import SequenceMatcher

VAULT = Path(".")
VALID_CATEGORIES = ["networking", "pentesting", "java_spring", "linux", "other"]


def parse_frontmatter(content):
    """Витяг YAML front matter"""
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
    """Обчисли подібність двох текстів (0-1)"""
    return SequenceMatcher(None, text1, text2).ratio()


def get_wikilinks(content):
    """Витяг всіх wikilinks [[...]]"""
    return re.findall(r'\[\[([^\]]+)\]\]', content)


class KnowledgeValidator:
    def __init__(self):
        self.files = []
        self.errors = []
        self.warnings = []
        self.stats = {}

    def load_files(self):
        """Завантаж всі MD файли"""
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

        print(f"📁 Завантажено {len(self.files)} файлів")

    def check_frontmatter(self):
        """Перевір наявність і коректність front matter"""
        for f in self.files:
            if f['frontmatter'] is None:
                self.errors.append(f"[FM] {f['name']}: Немає YAML front matter")
                continue

            fm = f['frontmatter']

            # Перевір обов'язкові поля
            required = ['title', 'category', 'tags', 'status']
            for field in required:
                if field not in fm:
                    self.errors.append(f"[FM] {f['name']}: Відсутнє поле '{field}'")

            # Перевір категорію
            if fm.get('category') not in VALID_CATEGORIES:
                self.warnings.append(
                    f"[FM] {f['name']}: Невідома категорія '{fm.get('category')}'"
                )

            # Перевір теги
            tags = fm.get('tags', [])
            if not tags or (isinstance(tags, list) and len(tags) == 0):
                self.warnings.append(f"[FM] {f['name']}: Теги порожні")

            # Перевій статус
            valid_statuses = ['draft', 'published', 'archived', 'needs-review']
            if fm.get('status') not in valid_statuses:
                self.warnings.append(
                    f"[FM] {f['name']}: Невідомий статус '{fm.get('status')}'"
                )

    def check_duplicates(self):
        """Знайди дублювання контенту (>70% подібність)"""
        duplicates = []

        for i, f1 in enumerate(self.files):
            for f2 in self.files[i + 1:]:
                similarity = calculate_similarity(
                    f1['body'][:500],  # Перші 500 символів
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
        """Перевір broken wikilinks"""
        all_titles = {
            f['frontmatter'].get('title', f['name'].replace('.md', '')): f['name']
            for f in self.files if f['frontmatter']
        }

        for f in self.files:
            wikilinks = get_wikilinks(f['body'])

            for link in wikilinks:
                # Очисти пошук
                search_title = link.split('|')[0].strip()

                if search_title not in all_titles:
                    self.warnings.append(
                        f"[LINK] {f['name']}: Broken link [[{link}]]"
                    )

    def generate_stats(self):
        """Збери статистику"""
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
        """Генеруй HTML звіт"""
        html = f"""<!DOCTYPE html>
<html lang="uk">
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
    <h1>📊 Knowledge Base Validation Report</h1>
    <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

    <div class="stats">
        <h2>📈 Statistics</h2>
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

        html += """        </table>
    </div>

    <h2>❌ Errors ({} total)</h2>
""".format(len(self.errors))

        if self.errors:
            for error in self.errors[:50]:  # Показуй перші 50
                html += f'    <div class="error">• {error}</div>\n'
        else:
            html += '    <div class="success">✅ No errors found!</div>\n'

        html += f"""
    <h2>⚠️ Warnings ({len(self.warnings)} total)</h2>
"""

        if self.warnings:
            for warning in self.warnings[:50]:
                html += f'    <div class="warning">• {warning}</div>\n'
        else:
            html += '    <div class="success">✅ No warnings!</div>\n'

        html += """
    <h2>✅ Validation Complete</h2>
    <p>Next steps:</p>
    <ol>
        <li>Fix all errors listed above</li>
        <li>Review warnings and decide on actions</li>
        <li>Run: <code>python3 scripts/multi_format_export.py</code></li>
    </ol>
</body>
</html>
"""

        report_path = Path("reports/validation_report.html")
        report_path.parent.mkdir(exist_ok=True)
        report_path.write_text(html, encoding="utf-8")

        return report_path

    def run(self):
        """Запусти всю валідацію"""
        print("\n🔍 Валідація структури знань...\n")

        self.load_files()
        print("✓ Завантажено файли\n")

        self.check_frontmatter()
        print("✓ Перевірено front matter\n")

        duplicates = self.check_duplicates()
        print(f"✓ Шукано дублювання ({len(duplicates)} знайдено)\n")

        self.check_links()
        print("✓ Перевірено посилання\n")

        self.generate_stats()
        print("✓ Зібрана статистика\n")

        report_path = self.generate_report()

        # Виведи сумарі
        print("=" * 60)
        print(f"❌ ПОМИЛОК: {len(self.errors)}")
        print(f"⚠️  ПОПЕРЕДЖЕНЬ: {len(self.warnings)}")
        print(f"📊 ВСЬОГО ФАЙЛІВ: {self.stats['total_files']}")
        print(f"📁 РОЗМІР БД: {self.stats['total_size_mb']:.2f} MB")
        print("=" * 60)

        print(f"\n📄 Звіт збережено: {report_path}")

        if self.errors:
            print(f"\n❌ Перші 10 помилок:")
            for error in self.errors[:10]:
                print(f"  • {error}")

        if self.warnings:
            print(f"\n⚠️  Перші 10 попереджень:")
            for warning in self.warnings[:10]:
                print(f"  • {warning}")

        print("\n✨ Валідація завершена!")
        print("Далі: python3 scripts/multi_format_export.py")


if __name__ == "__main__":
    validator = KnowledgeValidator()
    validator.run()
                  