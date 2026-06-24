#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Додає YAML front matter до всіх MD файлів в Obsidian vault.
Запускається один раз для структурування існуючих файлів.
"""

import re
import os
from pathlib import Path
from datetime import datetime
import subprocess

VAULT = Path(".")
GROUPS = {
    "networking": [
        "vlan", "ospf", "dhcp", "routing", "маршрут", "rip", "stp", "nat",
        "mac фільтр", "acl", "netbox", "комутатор", "маршрутизатор",
        "мережев", "сітьов", "підмереж", "subnet", "iproute", "spanning",
        "протокол ospf", "протокол rip", "статична маршрутизац"
    ],
    "pentesting": [
        "metasploit", "nmap", "exploit", "вразливост", "сканув",
        "payload", "msfvenom", "meterpreter", "eternal", "bluekeep",
        "routersploit", "osint", "злом", "пентест", "veil", "thefatrat",
        "nessus", "searchsploit", "msfconsole", "брандмауер", "корисна нагрузк"
    ],
    "java_spring": [
        "java", "spring", "hibernate", "hymbernate", "jpa", "maven",
        "gradle", "oop", "ооп", "scrum", "agile", "kanban", "backlog",
        "waterfol", "junit", "mockito", "тестирован", "liquibase",
        "rest запрос", "http метод", "контроллер", "репозитори java",
        "dto", "serializ", "sereliz", "наследован", "полиморфизм",
        "инкапсуляц", "абстрактн", "интерфейс"
    ],
    "linux": [
        "linux", "лінукс", "bash", "systemctl", "sudo", "права",
        "користувач", "процес", "каталог", "змінна середовища",
        "аліас", "ssh", "друк на linux", "утиліт", "запис дозапис",
        "робота з файлами", "робота з процесами", "chmod", "chown",
        "docker", "контейнер"
    ],
}


def get_git_dates(file_path):
    """Отримай дати created/updated з git історії"""
    try:
        # Дата першого коміта (created)
        created = subprocess.check_output(
            ["git", "log", "--follow", "--format=%aI", "--diff-filter=A", file_path],
            stderr=subprocess.DEVNULL
        ).decode().strip().split('\n')[-1][:10]
    except:
        created = datetime.now().strftime("%Y-%m-%d")

    try:
        # Дата останнього коміта (updated)
        updated = subprocess.check_output(
            ["git", "log", "-1", "--format=%aI", file_path],
            stderr=subprocess.DEVNULL
        ).decode().strip()[:10]
    except:
        updated = datetime.now().strftime("%Y-%m-%d")

    return created, updated


def detect_category(filename, content):
    """Визнач категорію файлу по ключовим словам"""
    text = (filename + " " + content).lower()

    for category, keywords in GROUPS.items():
        if any(kw in text for kw in keywords):
            return category

    return "other"


def extract_title(filename, content):
    """Витяг назву з имені файлу або першого heading'у"""
    # Спочатку спробуй перший H1
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()

    # Інакше — з імені файлу
    title = filename.replace(".md", "").strip()
    return title


def extract_tags_from_content(content):
    """Витяг тегів з тексту — ключові слова з першого параграфу"""
    lines = content.split('\n')
    first_para = ""

    for line in lines:
        if line.startswith('#'):
            continue
        if line.strip():
            first_para += line + " "
            if len(first_para) > 200:
                break

    # Базові теги на основі слів
    words = re.findall(r'\b[а-яіїєґa-z]{4,}\b', first_para.lower())
    tags = list(set(words))[:5]  # Top 5 унікальних слів

    return tags if tags else ["general"]


def generate_frontmatter(filename, file_path, content):
    """Генеруй YAML front matter"""
    title = extract_title(filename, content)
    category = detect_category(filename, content)
    tags = extract_tags_from_content(content)
    created, updated = get_git_dates(str(file_path))

    # Визнач якість (0-5) на основі довжини
    lines = len(content.split('\n'))
    quality = min(5, max(1, lines // 100))

    frontmatter = f"""---
title: "{title}"
category: "{category}"
tags: {tags}
status: "published"
created: "{created}"
updated: "{updated}"
ai-processed: false
source: "manual"
quality: {quality}
related-files: []
---

"""

    return frontmatter


def has_frontmatter(content):
    """Перевір чи файл вже має front matter"""
    return content.strip().startswith('---')


def process_vault():
    """Обробка всіх MD файлів в vault"""

    all_files = [
        p for p in VAULT.rglob("*.md")
        if ".obsidian" not in str(p) and "nlm-sources" not in str(p)
        and "scripts" not in str(p)
    ]

    processed = 0
    skipped = 0
    errors = 0

    print(f"Знайдено {len(all_files)} MD файлів")
    print("-" * 50)

    for file_path in sorted(all_files):
        try:
            content = file_path.read_text(encoding="utf-8", errors="ignore")

            # Пропусти якщо вже є front matter
            if has_frontmatter(content):
                skipped += 1
                continue

            # Генеруй front matter
            frontmatter = generate_frontmatter(file_path.name, file_path, content)
            new_content = frontmatter + content

            # Запиши файл
            file_path.write_text(new_content, encoding="utf-8")
            processed += 1

            print(f"✅ {file_path.name[:40]}")

        except Exception as e:
            errors += 1
            print(f"❌ {file_path.name}: {str(e)[:50]}")

    print("-" * 50)
    print(f"\n📊 Результати:")
    print(f"  ✅ Оброблено: {processed}")
    print(f"  ⏭️  Пропущено (вже має FM): {skipped}")
    print(f"  ❌ Помилок: {errors}")
    print(f"  📁 Всього: {len(all_files)}")


if __name__ == "__main__":
    print("🔧 Додаю YAML front matter до всіх файлів...\n")
    process_vault()
    print("\n✨ Готово! Всі файли структуровані.")
    print("\nДалі запусти: python3 scripts/validate_knowledge.py")
