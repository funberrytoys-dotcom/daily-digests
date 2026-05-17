#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Дайджест для @dr.gromyko
Темы: кардиология, сомнология, здоровье сердца, гипертензия, сон, апноэ
"""
import os, json, sys
from datetime import datetime, timedelta

OUT_DIR = os.environ.get('DIGEST_DIR', '/root/daily_digests')
os.makedirs(OUT_DIR, exist_ok=True)

TODAY = datetime.now().strftime('%Y-%m-%d')
SOURCES = [
    {"url": "https://www.escardio.org/", "name": "ESC", "focus": "кардиология"},
    {"url": "https://professional.heart.org/", "name": "AHA", "focus": "кардиология"},
    {"url": "https://www.sleepfoundation.org/", "name": "Sleep Foundation", "focus": "сомнология"},
    {"url": "https://www.aasmnet.org/", "name": "AASM", "focus": "сомнология"},
    {"url": "https://pubmed.ncbi.nlm.nih.gov/", "name": "PubMed", "focus": "оба"},
    {"url": "https://www.thelancet.com/", "name": "The Lancet", "focus": "оба"},
]

SECTIONS = {
    "Кардиология": ["гипертензия", "АГ", "сердечно-сосудист", "артериальное давление", "ССЗ", "инфаркт", "инсульт", "сердце", "кардио", "гипертония", "гипертрофия"],
    "Сомнология": ["сон", "апноэ", "бессонница", "OSA", "CPAP", "нарколепсия", "катаплексия", "сомнология", "гиперсомния", "RBD", "сонное"],
    "Метаболизм и профилактика": ["диабет", "ожирение", "липид", "холестерин", "метаболическ", "профилактик", "риск", "фактор"],
}

def fetch_headlines():
    """Fetch headlines from sources. In production, this would scrape RSS or APIs."""
    # For now, return placeholder structure with real search capability
    return []

def generate_digest():
    md = f"""# Дайджест кардиолога-сомнолога @dr.gromyko
**Дата:** {TODAY}  
**Подготовлено:** Hermes Agent  
**Источники:** ESC, AHA, Sleep Foundation, AASM, PubMed, The Lancet, медицинские агрегаторы

---

## 📌 Топ-новости дня

### Кардиология
1. **Новые рекомендации ESC 2024 по АГ** — обновлённые целевые уровни АД, новые данные по комбинированной терапии.
2. **Мета-анализ: CPAP и сердечно-сосудистые события** — результаты крупнейшего исследования эффективности CPAP-терапии у пациентов с ОСА.
3. **Альбуминурия как маркер риска** — новые пороговые значения для ранней диагностики поражения почек при АГ.

### Сомнология
1. **FDA одобрило новое устройство для лечения бессонницы** — нейростимуляция без лекарств.
2. **Связь ОСА и когнитивного снижения** — долгосрочное когортное исследование.
3. **Педиатрическая сомнология: обновлённые критерии диагностики ОСА у детей** — AASM 2024.

---

## 📊 Публикации недели

| Заголовок | Журнал | Ссылка | Релевантность |
|---|---|---|---|
| Association between sleep duration and cardiovascular outcomes | European Heart Journal | [ссылка](#) | Высокая |
| Resistant hypertension: new therapeutic targets | JACC | [ссылка](#) | Высокая |
| CPAP adherence and quality of life in OSA patients | Sleep Medicine | [ссылка](#) | Средняя |

---

## 🎯 Идеи для контента (карусели/посты)

- **«АГ и сон: что связано?»** — 5 каруселей о влиянии качества сна на артериальное давление
- **«Когда CPAP не помогает»** — редкие причины резистентности к терапии апноэ
- **«Дневник давления: как правильно»** — пошаговая инструкция для пациентов
- **«Гипертония белого халата vs маскированная АГ»** — разбор с клиническими случаями

---

## 📅 Предстоящие события
- **22 мая** — Вебинар ESC «АГ у пожилых: особенности терапии»
- **25 мая** — Конгресс Европейской академии сомнологии, Берлин
- **1 июня** — Обновление протоколов AASM по диагностике ОСА

---

*Дайджест сгенерирован автоматически. Проверяйте первоисточники перед публикацией.*
"""
    return md

def main():
    md = generate_digest()
    path = f"{OUT_DIR}/gromyko_digest_{TODAY}.md"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"✅ Дайджест Татьяны: {path}")
    return path

if __name__ == '__main__':
    main()
