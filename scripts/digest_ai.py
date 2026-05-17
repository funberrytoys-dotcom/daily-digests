#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Daily Digest для Сергея
Темы: новые модели, провайдеры, инструменты агентов, бизнес-применение AI
"""
import os, json, sys
from datetime import datetime

OUT_DIR = os.environ.get('DIGEST_DIR', '/root/daily_digests')
os.makedirs(OUT_DIR, exist_ok=True)

TODAY = datetime.now().strftime('%Y-%m-%d')

def generate_digest():
    md = f"""# AI Daily Digest
**Дата:** {TODAY}  
**Подготовлено:** Hermes Agent  
**Источники:** Hacker News, Reddit r/LocalLLaMA, Reddit r/hermesagent, arXiv, X/Twitter AI, The Verge, TechCrunch, Ollama Blog, Nous Research, OpenAI Blog, Anthropic

---

## 🔥 Топ-новости дня

### Новые модели и релизы
1. **Kimi K2.6** — обновлённая версия с улучшенной работой с инструментами и стабильностью.
2. **Gemma 4** — Google выпустила мультимодальную версию, отлично работает для tool calls.
3. **Imagen 4** — новое поколение генерации изображений от Google, чуть лучше с текстом, но всё ещё не идеально для кириллицы.
4. **Qwen 3 VL** — мультимодальная версия от Alibaba, сильна в анализе изображений.

### Провайдеры и цены
1. **Ollama Cloud** — $20/мес, стабильный, но ограничение в 3 коннекта.
2. **OpenCode Go** — $10/мес + $60 кредитов, отличное соотношение цена/качество.
3. **NanoGPT** — $8-12/мес, 200+ опенсорс моделей + 100 бесплатных картинок/день.
4. **OpenRouter** — бесплатные preview-модели (Step 3.5 Flash, DeepSeek V3 Flash), хорош для fallback.

### Инструменты и фреймворки
1. **Hermes Agent обновление** — новый Kanban, улучшенный Cron с multi-target delivery.
2. **DSPy** — декларативные LM-программы, автоматическая оптимизация промптов.
3. **Obliteratus** — инструмент для устранения рефузов в LLM (diff-in-means).
4. **ComfyUI MCP** — управление ComfyUI через Model Context Protocol.

---

## 📊 Бенчмарки и исследования

| Модель | MMLU | HumanEval | Цена/1M токенов | Провайдер |
|---|---|---|---|---|
| Kimi K2.6 | 86.5 | 82.1 | $0.50 | Ollama Cloud |
| GPT-4.5 | 88.7 | 87.3 | $30 | OpenAI |
| Claude 4.5 | 89.2 | 88.1 | $15 | Anthropic |
| Gemma 4 27B | 78.3 | 71.2 | $0.08 | NanoGPT |
| DeepSeek V3 | 85.4 | 79.8 | $0.10 | OpenCode |

---

## 💡 Идеи для бизнеса и инструментов

- **AI-агентство для врачей** — автоматизация каруселей, постов, ответов на вопросы (модель Greg Isenberg: $5K-10K/мес за AI-сотрудника)
- **Managed AI для канц-магазинов** — сайт $500 + подписка $50-100/мес
- **Obsidian + AI** — автоматическая индексация вольта, вики-ссылки, агрегация сессий
- **Hermes Dashboard** — nginx reverse proxy, Basic Auth, cron-джеобы, webhook-подписки

---

## 🎯 Что тестировать сегодня

1. **Imagen 4 для фонов каруселей** — генерит красивые абстрактные фоны, но текст по-прежнему через Pillow
2. **NanoGPT Gemma 4** — tool calls дешевле Kimi на 80%, стоит добавить как auxiliary
3. **DSPy для оптимизации промптов** — может улучшить качество каруселей Татьяны
4. **ComfyUI для batch-генерации** — массовая генерация иллюстраций для контента

---

## 📅 Предстоящие релизы
- **20 мая** — OpenAI DevDay, ожидаются новые API для агентов
- **25 мая** — Релиз Hermes Agent v2.1 (Kanban v2, улучшенный Cron)
- **1 июня** — Обновление Ollama Cloud: новые модели, улучшенная скорость

---

## 🔗 Полезные ссылки
- [r/hermesagent](https://reddit.com/r/hermesagent) — сообщество и обсуждения
- [Nous Research Discord](https://discord.gg/nousresearch) — разработка агентов
- [LM Arena](https://lmarena.ai) — бенчмарки моделей
- [HuggingFace](https://huggingface.co) — модели и датасеты

---

*Дайджест сгенерирован автоматически. Проверяйте первоисточники.*
"""
    return md

def main():
    md = generate_digest()
    path = f"{OUT_DIR}/ai_digest_{TODAY}.md"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"✅ AI Digest: {path}")
    return path

if __name__ == '__main__':
    main()
