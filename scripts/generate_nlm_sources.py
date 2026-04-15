#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates topic-grouped .txt files from the Obsidian vault for NotebookLM.
Run by GitHub Actions on every push to main.
Output goes to nlm-sources/
"""
import re
from pathlib import Path

VAULT = Path(".")
OUT = Path("nlm-sources")
OUT.mkdir(exist_ok=True)

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
        "робота з файлами", "робота з процесами", "chmod", "chown"
    ],
}

def matches_group(stem: str, content: str, keywords: list) -> bool:
    text = (stem + " " + content).lower()
    return any(kw in text for kw in keywords)

all_files = [
    p for p in VAULT.rglob("*.md")
    if ".obsidian" not in str(p) and "nlm-sources" not in str(p)
    and "scripts" not in str(p)
]

assigned = set()
stats = {}

for group_name, keywords in GROUPS.items():
    parts = []
    for f in all_files:
        if str(f) in assigned:
            continue
        try:
            content = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if len(content.strip()) < 20:
            continue
        if matches_group(f.stem, content, keywords):
            parts.append(f"# {f.stem}\n\n{content}\n\n---\n\n")
            assigned.add(str(f))

    if parts:
        combined = "".join(parts)
        (OUT / f"{group_name}.txt").write_text(combined, encoding="utf-8")
        stats[group_name] = len(parts)

# Решта — other
other_parts = []
for f in all_files:
    if str(f) in assigned:
        continue
    try:
        content = f.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    if len(content.strip()) < 20:
        other_parts.append(f"# {f.stem}\n\n{content}\n\n---\n\n")

if other_parts:
    (OUT / "other.txt").write_text("".join(other_parts), encoding="utf-8")
    stats["other"] = len(other_parts)

for name, count in stats.items():
    print(f"{name}: {count} files")

print(f"Total assigned: {sum(stats.values())} files")
