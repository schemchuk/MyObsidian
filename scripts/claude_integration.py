#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Інтеграція з Claude для додавання нових знань через GitHub webhook.
Приймає JSON з новим знанням, створює MD файл з proper front matter.
"""

import json
import sys
from pathlib import Path
from datetime import datetime
import re

VAULT = Path(".")
INCOMING = VAULT / "Входящие"  # Inbox папка


def sanitize_filename(text):
    """Очисти текст для імені файлу"""
    text = text.lower().replace(' ', '_')
    text = re.sub(r'[^a-z0-9_а-яіїєґ]', '', text)
    return text[:50]


def create_markdown_file(data):
    """
    Створи новий MD файл з Claude input.

    Очікуваний JSON формат:
    {
        "title": "Назва статті",
        "content": "Основний контент статті",
        "category": "networking",  # optional, auto-detect if not provided
        "tags": ["tag1", "tag2"],  # optional
        "summary": "Короткий опис"  # optional
    }
    """

    # Валідація обов'язкових полів
    required = ['title', 'content']
    for field in required:
        if field not in data:
            return False, f"Відсутнє обов'язкове поле: {field}"

    title = data['title']
    content = data['content']
    category = data.get('category', 'other')
    tags = data.get('tags', ['ai-generated', 'claude'])
    summary = data.get('summary', '')

    # Переконайся що Inbox існує
    INCOMING.mkdir(exist_ok=True)

    # Генеруй ім'я файлу
    safe_name = sanitize_filename(title)
    filename = f"{safe_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    filepath = INCOMING / filename

    # Генеруй YAML front matter
    frontmatter = f"""---
title: "{title}"
category: "{category}"
tags: {tags}
status: "needs-review"
created: "{datetime.now().strftime('%Y-%m-%d')}"
updated: "{datetime.now().strftime('%Y-%m-%d')}"
ai-processed: true
source: "claude"
quality: 3
related-files: []
---

"""

    if summary:
        frontmatter += f"## Summary\n{summary}\n\n"

    frontmatter += f"## Content\n{content}\n"

    # Запиши файл
    try:
        filepath.write_text(frontmatter, encoding="utf-8")
        return True, f"✅ Файл створений: {filename}"
    except Exception as e:
        return False, f"❌ Помилка запису: {str(e)}"


def process_webhook(webhook_data):
    """Обробка webhook від GitHub Actions"""

    if isinstance(webhook_data, str):
        try:
            webhook_data = json.loads(webhook_data)
        except json.JSONDecodeError:
            return False, "Invalid JSON"

    # Перевір тип вебхука
    event_type = webhook_data.get('type', 'knowledge_input')

    if event_type == 'knowledge_input':
        success, message = create_markdown_file(webhook_data.get('payload', {}))
        return success, message

    elif event_type == 'knowledge_update':
        # TODO: Implement update logic
        return True, "Update handling not yet implemented"

    else:
        return False, f"Unknown event type: {event_type}"


def main():
    """Головна функція"""

    if len(sys.argv) < 2:
        print("Використання: python3 claude_integration.py '{json_string}'")
        print("\nПриклад:")
        print("""
python3 claude_integration.py '{
  "title": "Docker для новачків",
  "content": "Docker це...",
  "category": "linux",
  "tags": ["docker", "containers"],
  "summary": "Основи Docker"
}'
        """)
        sys.exit(1)

    # Читай JSON з аргументу
    json_str = sys.argv[1]
    print(f"📨 Обробляю вхідне знання від Claude...\n")

    success, message = process_webhook(json_str)

    print(message)

    if success:
        print("\n✨ Файл додано до папки 'Входящие'")
        print("Наступно: перевір файл, відредагуй якщо потрібно, переміст до основної папки")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
