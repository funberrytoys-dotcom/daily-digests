# Daily Digests — Автоматические дайджесты для Hermes Agent

Ежедневные отчёты: медицина + AI. Генерируются автоматически, отправляются в Telegram, хранятся в Markdown для Obsidian.

---

## 📁 Структура

```
daily-digests/
├── scripts/
│   ├── digest_gromyko.py    # Дайджест для @dr.gromyko (кардио + сомнология)
│   └── digest_ai.py         # AI Daily Digest (новости, модели, инструменты)
└── output/                  # Сгенерированные .md файлы
    ├── gromyko_digest_YYYY-MM-DD.md
    └── ai_digest_YYYY-MM-DD.md
```

---

## ⏰ Cron-джобы

| Название | Время | Что делает |
|---|---|---|
| **gromyko-daily-digest** | 08:00 UTC | Медицинские новости, публикации, идеи для контента |
| **ai-daily-digest** | 08:05 UTC | AI-новости, бенчмарки, релизы, идеи для бизнеса |

---

## 🔧 Установка и настройка

### 1. Скрипты
Скопируй файлы из `scripts/` в `~/.hermes/scripts/daily_digests/`

### 2. Cron через Hermes CLI
```bash
hermes cron create --name gromyko-daily-digest \
  --schedule "0 8 * * *" \
  --script daily_digests/digest_gromyko.py \
  --prompt "Run digest and send summary to Telegram"

hermes cron create --name ai-daily-digest \
  --schedule "5 8 * * *" \
  --script daily_digests/digest_ai.py \
  --prompt "Run AI digest and send summary to Telegram"
```

### 3. Obsidian-интеграция
- Смонтируй `/root/daily_digests/` как Obsidian vault (или подпапку)
- Используй dataview для агрегации по датам
- Теги: `#digest`, `#gromyko`, `#ai-news`

---

## 📊 Дайджест @dr.gromyko

### Темы
- **Кардиология:** гипертензия, АГ, ССЗ, инфаркт, инсульт, сердечная недостаточность
- **Сомнология:** апноэ, бессонница, CPAP, нарколепсия, гиперсомния
- **Метаболизм:** диабет, ожирение, липиды, холестерин

### Источники
- ESC, AHA, Sleep Foundation, AASM
- PubMed, The Lancet
- Медицинские агрегаторы (планируется RSS)

### Структура
1. Топ-новости дня (3-5 пунктов)
2. Публикации недели (таблица)
3. Идеи для контента (карусели, посты)
4. Предстоящие события

---

## 🤖 AI Daily Digest

### Темы
- Новые модели LLM (Kimi, GPT, Claude, Gemini, Qwen)
- Провайдеры API и цены (Ollama, OpenCode, NanoGPT, OpenRouter)
- Инструменты для агентов (Hermes, DSPy, ComfyUI)
- Бенчмарки и исследования
- Бизнес-применение AI

### Источники
- Hacker News, Reddit r/LocalLLaMA, r/hermesagent
- arXiv, X/Twitter AI
- The Verge, TechCrunch
- Ollama Blog, Nous Research, OpenAI/Anthropic blogs

### Структура
1. Топ-новости дня
2. Бенчмарки (таблица)
3. Идеи для бизнеса и инструментов
4. Что тестировать сегодня
5. Предстоящие релизы

---

## 🚀 TODO

- [ ] Добавить реальный RSS-скрейпинг (escardio.org, aasmnet.org)
- [ ] Подключить arXiv API для поиска по ключевым словам
- [ ] Интеграция с Obsidian — auto-import через folder sync
- [ ] Добавить TL;DR секцию (3 предложения для быстрого просмотра)
- [ ] Сделать HTML-версию для email-рассылки
- [ ] Добавить ручную доработку через Telegram inline

---

## 📦 Зависимости

```bash
pip install requests beautifulsoup4 feedparser
```

---

**Создано:** Hermes Agent  
**Для:** @dr.gromyko + Сергей Пинин  
**Дата:** 2026-05-17
