#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flask REST API для доступу до бази знань MyObsidian
Endpoints для пошуку, фільтрації, організації знань
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from pathlib import Path
from functools import lru_cache

app = Flask(__name__)
CORS(app)

API_SOURCES = Path("api-sources")
CLAUDE_SOURCES = Path("claude-sources")


@lru_cache(maxsize=128)
def load_index():
    """Завантаж індекс файлів"""
    try:
        index_path = CLAUDE_SOURCES / "index.json"
        if index_path.exists():
            return json.loads(index_path.read_text(encoding="utf-8"))
    except:
        pass
    return {"documents": [], "categories": []}


def load_category(category):
    """Завантаж документи для категорії"""
    try:
        cat_path = CLAUDE_SOURCES / f"{category}.json"
        if cat_path.exists():
            return json.loads(cat_path.read_text(encoding="utf-8"))
    except:
        pass
    return {"documents": [], "category": category}


@app.route('/')
def index():
    """Головна сторінка API"""
    return jsonify({
        "name": "MyObsidian Knowledge API",
        "version": "1.0",
        "endpoints": {
            "GET /api/health": "Status check",
            "GET /api/categories": "List all categories",
            "GET /api/knowledge/<category>": "Get all documents in category",
            "GET /api/knowledge/<category>/<id>": "Get specific document",
            "GET /api/search?q=<query>": "Full-text search",
            "GET /api/tags": "List all tags",
            "GET /api/stats": "Knowledge base statistics"
        }
    })


@app.route('/api/health')
def health():
    """Health check"""
    return jsonify({"status": "healthy"})


@app.route('/api/categories')
def get_categories():
    """Список всіх категорій"""
    index = load_index()
    return jsonify({
        "categories": index.get("categories", []),
        "count": len(index.get("categories", []))
    })


@app.route('/api/knowledge/<category>')
def get_category(category):
    """Отримай всі документи в категорії"""
    data = load_category(category)

    if not data.get("documents"):
        return jsonify({"error": "Category not found"}), 404

    return jsonify({
        "category": category,
        "count": len(data.get("documents", [])),
        "documents": [
            {
                "id": doc["id"],
                "title": doc["title"],
                "tags": doc.get("tags", []),
                "status": doc.get("status", "published"),
                "url": f"/api/knowledge/{category}/{doc['id']}"
            }
            for doc in data.get("documents", [])
        ]
    })


@app.route('/api/knowledge/<category>/<doc_id>')
def get_document(category, doc_id):
    """Отримай конкретний документ"""
    data = load_category(category)

    for doc in data.get("documents", []):
        if doc["id"] == doc_id:
            return jsonify({
                "id": doc["id"],
                "title": doc["title"],
                "category": category,
                "content": doc.get("content", ""),
                "full_content": doc.get("full_content", ""),
                "tags": doc.get("tags", []),
                "status": doc.get("status", "published"),
                "created": doc.get("created", ""),
                "updated": doc.get("updated", ""),
                "quality": doc.get("quality", 0)
            })

    return jsonify({"error": "Document not found"}), 404


@app.route('/api/search')
def search():
    """Пошук по всій БЗ"""
    query = request.args.get('q', '').lower()
    category_filter = request.args.get('category', '')

    if len(query) < 2:
        return jsonify({"error": "Query too short (min 2 characters)"}), 400

    index = load_index()
    results = []

    for doc in index.get("documents", []):
        # Перевір категорію
        if category_filter and doc.get("category") != category_filter:
            continue

        # Пошук в заголовку та тегах
        title = doc.get("title", "").lower()
        tags = [t.lower() for t in doc.get("tags", [])]

        if query in title or any(query in tag for tag in tags):
            results.append({
                "id": doc["id"],
                "title": doc["title"],
                "category": doc["category"],
                "tags": doc.get("tags", []),
                "url": f"/api/knowledge/{doc['category']}/{doc['id']}"
            })

    return jsonify({
        "query": query,
        "count": len(results),
        "results": results[:20]  # Top 20
    })


@app.route('/api/tags')
def get_tags():
    """Список всіх унікальних тегів"""
    index = load_index()
    all_tags = set()

    for doc in index.get("documents", []):
        all_tags.update(doc.get("tags", []))

    return jsonify({
        "tags": sorted(list(all_tags)),
        "count": len(all_tags)
    })


@app.route('/api/stats')
def get_stats():
    """Статистика бази знань"""
    index = load_index()

    categories = {}
    tag_counts = {}
    status_counts = {}

    for doc in index.get("documents", []):
        cat = doc.get("category", "other")
        categories[cat] = categories.get(cat, 0) + 1

        for tag in doc.get("tags", []):
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

        status = doc.get("status", "published")
        status_counts[status] = status_counts.get(status, 0) + 1

    return jsonify({
        "total_documents": len(index.get("documents", [])),
        "total_tags": len(tag_counts),
        "categories": categories,
        "top_tags": sorted(
            tag_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10],
        "by_status": status_counts
    })


@app.errorhandler(404)
def not_found(error):
    """404 handler"""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """500 handler"""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    print("🚀 MyObsidian Knowledge API запускається...")
    print("📍 http://localhost:5000")
    print("\nДоступні endpoints:")
    print("  GET /api/categories")
    print("  GET /api/knowledge/<category>")
    print("  GET /api/knowledge/<category>/<id>")
    print("  GET /api/search?q=<query>")
    print("  GET /api/tags")
    print("  GET /api/stats")
    print("\nНатисни Ctrl+C для закриття\n")

    app.run(debug=True, port=5000)
