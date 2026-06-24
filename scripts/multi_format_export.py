#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Експортує знання в різні формати для різних AI систем:
- NotebookLM (груповані .txt файли)
- Claude (JSON з метаданими)
- REST API (структурований JSON)
- Knowledge Graph (для Neo4j/GraphQL)
"""

import re
import json
from pathlib import Path
from datetime import datetime
import yaml

VAULT = Path(".")
OUT_NLM = Path("nlm-sources")
OUT_CLAUDE = Path("claude-sources")
OUT_API = Path("api-sources")
OUT_GRAPH = Path("graph-sources")

GROUPS = {
    "networking": [
        "vlan", "ospf", "dhcp", "routing", "маршрут", "rip", "stp", "nat",
        "mac фільтр", "acl", "netbox", "комутатор", "маршрутизатор",
        "мережев", "сітьов", "підмереж", "subnet", "iproute", "spanning",
    ],
    "pentesting": [
        "metasploit", "nmap", "exploit", "вразливост", "сканув",
        "payload", "msfvenom", "meterpreter", "eternal", "bluekeep",
        "osint", "злом", "пентест", "veil",
    ],
    "java_spring": [
        "java", "spring", "hibernate", "jpa", "maven",
        "gradle", "oop", "ооп", "scrum", "agile", "junit",
    ],
    "linux": [
        "linux", "лінукс", "bash", "systemctl", "sudo", "права",
        "користувач", "процес", "ssh", "docker",
    ],
}


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


def simple_hash(text):
    """Простий хеш для embedding-подібного представлення"""
    return sum(ord(c) for c in text[:100]) % 1000000


def matches_group(filename, content, keywords):
    """Перевір чи файл належить до групи"""
    text = (filename + " " + content).lower()
    return any(kw in text for kw in keywords)


class KnowledgeExporter:
    def __init__(self):
        self.files = []
        self.load_files()

    def load_files(self):
        """Завантаж всі MD файли"""
        all_files = [
            p for p in VAULT.rglob("*.md")
            if ".obsidian" not in str(p) and "nlm-sources" not in str(p)
            and "scripts" not in str(p) and "claude-sources" not in str(p)
            and "api-sources" not in str(p) and "graph-sources" not in str(p)
        ]

        for file_path in sorted(all_files):
            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
                fm, body = parse_frontmatter(content)

                if len(body.strip()) < 20:
                    continue

                self.files.append({
                    'path': file_path,
                    'name': file_path.name,
                    'stem': file_path.stem,
                    'frontmatter': fm,
                    'body': body,
                    'full_content': content
                })
            except:
                pass

        print(f"📁 Завантажено {len(self.files)} валідних файлів\n")

    def export_for_notebooklm(self):
        """Експорт для NotebookLM (груповані .txt)"""
        print("📤 Експортую для NotebookLM...")

        OUT_NLM.mkdir(exist_ok=True)
        assigned = set()

        for group_name, keywords in GROUPS.items():
            parts = []

            for f in self.files:
                if f['path'] in assigned:
                    continue

                if matches_group(f['name'], f['body'], keywords):
                    parts.append(f"# {f['stem']}\n\n{f['body']}\n\n---\n\n")
                    assigned.add(f['path'])

            if parts:
                combined = "".join(parts)
                (OUT_NLM / f"{group_name}.txt").write_text(combined, encoding="utf-8")
                print(f"  ✓ {group_name}: {len(parts)} файлів")

        # Решта
        other_parts = []
        for f in self.files:
            if f['path'] not in assigned:
                other_parts.append(f"# {f['stem']}\n\n{f['body']}\n\n---\n\n")

        if other_parts:
            (OUT_NLM / "other.txt").write_text("".join(other_parts), encoding="utf-8")
            print(f"  ✓ other: {len(other_parts)} файлів")

        print(f"  📁 Збережено в {OUT_NLM}\n")

    def export_for_claude(self):
        """Експорт для Claude (JSON з metadata)"""
        print("📤 Експортую для Claude...")

        OUT_CLAUDE.mkdir(exist_ok=True)
        by_category = {}

        for f in self.files:
            fm = f['frontmatter'] or {}
            category = fm.get('category', 'other')

            if category not in by_category:
                by_category[category] = []

            by_category[category].append({
                'id': f['stem'],
                'title': fm.get('title', f['stem']),
                'content': f['body'][:5000],  # Перші 5000 символів
                'full_content': f['body'],
                'category': category,
                'tags': fm.get('tags', []),
                'status': fm.get('status', 'published'),
                'created': fm.get('created', ''),
                'updated': fm.get('updated', ''),
                'quality': fm.get('quality', 3),
                'embedding_hash': simple_hash(f['body']),
            })

        # Запиши по категоріях
        for category, items in by_category.items():
            output = {
                'category': category,
                'count': len(items),
                'generated': datetime.now().isoformat(),
                'documents': items
            }
            (OUT_CLAUDE / f"{category}.json").write_text(
                json.dumps(output, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )
            print(f"  ✓ {category}: {len(items)} документів")

        # Глобальний індекс
        all_docs = []
        for items in by_category.values():
            all_docs.extend(items)

        index = {
            'total': len(all_docs),
            'categories': list(by_category.keys()),
            'generated': datetime.now().isoformat(),
            'documents': [
                {
                    'id': d['id'],
                    'title': d['title'],
                    'category': d['category'],
                    'tags': d['tags'],
                }
                for d in all_docs
            ]
        }
        (OUT_CLAUDE / "index.json").write_text(
            json.dumps(index, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

        print(f"  📁 Збережено в {OUT_CLAUDE}\n")

    def export_for_rest_api(self):
        """Експорт для REST API (структурований)"""
        print("📤 Експортую для REST API...")

        OUT_API.mkdir(exist_ok=True)

        # Документи по категоріях
        by_category = {}

        for f in self.files:
            fm = f['frontmatter'] or {}
            category = fm.get('category', 'other')

            if category not in by_category:
                by_category[category] = []

            by_category[category].append({
                'id': f['stem'],
                'title': fm.get('title', f['stem']),
                'category': category,
                'tags': fm.get('tags', []),
                'status': fm.get('status', 'published'),
                'created': fm.get('created', ''),
                'updated': fm.get('updated', ''),
                'summary': f['body'][:200] + "...",
                'url': f"/api/knowledge/{category}/{f['stem']}"
            })

        # Запиши каталог для кожної категорії
        for category, items in by_category.items():
            output = {
                'category': category,
                'count': len(items),
                'items': items
            }
            (OUT_API / f"{category}.json").write_text(
                json.dumps(output, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )
            print(f"  ✓ API catalog: {category}")

        # Createй також search-friendly index
        search_index = []
        for f in self.files:
            fm = f['frontmatter'] or {}
            # Витяг ключові речення
            sentences = re.split(r'[.!?]+', f['body'])[:3]

            search_index.append({
                'id': f['stem'],
                'title': fm.get('title', f['stem']),
                'category': fm.get('category', 'other'),
                'keywords': ' '.join(fm.get('tags', [])),
                'excerpt': ' '.join(sentences)[:300],
            })

        (OUT_API / "search_index.json").write_text(
            json.dumps(search_index, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

        print(f"  📁 Збережено в {OUT_API}\n")

    def export_graph(self):
        """Експорт для Knowledge Graph"""
        print("📤 Експортую для Knowledge Graph...")

        OUT_GRAPH.mkdir(exist_ok=True)

        nodes = []
        edges = []

        # Створи вузли для файлів та тегів
        seen_tags = set()

        for f in self.files:
            fm = f['frontmatter'] or {}

            # Вузол файлу
            nodes.append({
                'id': f['stem'],
                'type': 'document',
                'label': fm.get('title', f['stem']),
                'category': fm.get('category', 'other'),
                'status': fm.get('status', 'published'),
                'created': fm.get('created', ''),
            })

            # Вузли тегів та зв'язки
            for tag in fm.get('tags', []):
                tag_id = f"tag_{tag}"

                if tag_id not in seen_tags:
                    nodes.append({
                        'id': tag_id,
                        'type': 'tag',
                        'label': tag,
                    })
                    seen_tags.add(tag_id)

                edges.append({
                    'source': f['stem'],
                    'target': tag_id,
                    'type': 'has_tag'
                })

            # Вузол категорії
            cat = fm.get('category', 'other')
            cat_id = f"cat_{cat}"

            edges.append({
                'source': f['stem'],
                'target': cat_id,
                'type': 'in_category'
            })

        # Додай категорії як вузли
        for group_name in GROUPS.keys():
            nodes.append({
                'id': f'cat_{group_name}',
                'type': 'category',
                'label': group_name,
            })

        graph = {
            'nodes': nodes,
            'edges': edges,
            'generated': datetime.now().isoformat(),
            'stats': {
                'total_nodes': len(nodes),
                'total_edges': len(edges),
                'document_nodes': sum(1 for n in nodes if n['type'] == 'document'),
                'tag_nodes': sum(1 for n in nodes if n['type'] == 'tag'),
            }
        }

        (OUT_GRAPH / "knowledge_graph.json").write_text(
            json.dumps(graph, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

        print(f"  ✓ Knowledge Graph: {len(nodes)} вузлів, {len(edges)} зв'язків")
        print(f"  📁 Збережено в {OUT_GRAPH}\n")

    def run(self):
        """Запусти всі експорти"""
        print("\n🚀 Експортую знання в різні формати...\n")
        print("=" * 60)

        self.export_for_notebooklm()
        self.export_for_claude()
        self.export_for_rest_api()
        self.export_graph()

        print("=" * 60)
        print("✨ Все експортовано!")
        print("\nДирекорії:")
        print(f"  📄 nlm-sources/ — для NotebookLM")
        print(f"  📄 claude-sources/ — для Claude")
        print(f"  📄 api-sources/ — для REST API")
        print(f"  📄 graph-sources/ — для Knowledge Graph")
        print("\nДалі: git add . && git commit && git push")


if __name__ == "__main__":
    exporter = KnowledgeExporter()
    exporter.run()
