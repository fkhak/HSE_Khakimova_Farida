# Выполнение задания вариантом без библиотеки

import re
import json
from datetime import datetime

with open('А40-183194-2015.ics', 'r', encoding='utf-8') as f:
    content = f.read()

events = re.split(r'BEGIN:VEVENT\r?\n', content)[1:]
real_events = []

for event in events:
    if 'DTSTART;VALUE=DATE:00010101' in event:
        continue

    data = {
        "case_number": "A40-183194/2015",
        "start": None,
        "end": None,
        "location": None,
        "description": None
    }

    # Извлечение дат и преобразование в ISO-формат
    dtstart_match = re.search(r'DTSTART(?:;[^\r\n:]+)?:([^\r\n]+)', event)
    dtend_match = re.search(r'DTEND(?:;[^\r\n:]+)?:([^\r\n]+)', event)

    if dtstart_match and dtend_match:
        try:
            # Парсинг даты из формата "YYYYMMDDTHHMMSS"
            dt_start = datetime.strptime(dtstart_match.group(1), "%Y%m%dT%H%M%S")
            dt_end = datetime.strptime(dtend_match.group(1), "%Y%m%dT%H%M%S")

            # Преобразование в ISO-формат с часовым поясом UTC+3 (Москва)
            data["start"] = dt_start.isoformat() + "+03:00"
            data["end"] = dt_end.isoformat() + "+03:00"
        except ValueError:
            continue  # Пропустить некорректные даты
    else:
        continue

    # Обработка локации
    location_match = re.search(r'LOCATION[^:]*:(.*?)(?=\r?\n[A-Z]|$)', event, re.DOTALL)
    if location_match:
        location = location_match.group(1).strip()
        location = re.sub(r'^[^:]*:', '', location)
        location = re.sub(r'\\n|\\,|\\"', '', location)
        location = re.sub(r'\s+', ' ', location).strip()
        data["location"] = location
    else:
        continue

    # Обработка описания
    description_match = re.search(r'DESCRIPTION:(.*?)(?=\r?\n[A-Z]|$)', event, re.DOTALL)
    if description_match:
        description = description_match.group(1).strip()
        description = re.sub(r'\r?\n', r'\\n', description)
        data["description"] = description

    real_events.append(data)

with open('court_dates.json', 'w', encoding='utf-8') as f:
    json.dump(real_events, f, ensure_ascii=False, indent=4)

print(f"Сохранено {len(real_events)} заседаний. Проверьте файл court_dates.json.")