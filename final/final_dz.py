# Найдите информацию об организациях.
# Получите список ИНН из файла traders.txt.
# Найдите информацию об организациях с этими ИНН в файле traders.json.
# Сохраните информацию об ИНН, ОГРН и адресе организаций из файла traders.txt в файл traders.csv.
# Напишите регулярное выражение для поиска email-адресов в тексте.


with open('traders.txt', 'r', encoding='utf-8') as file:
    inn_list = [line.strip() for line in file if line.strip()]

import json

with open('traders.json', 'r', encoding='utf-8') as file:
    traders = json.load(file)

filtered_data = []
for trader in traders:
    if trader.get('inn') in inn_list:
        filtered_data.append({
            'ИНН': trader.get('inn'),
            'ОГРН': trader.get('ogrn'),
            'Адрес': trader.get('address')
        })


import csv

with open('traders.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['ИНН', 'ОГРН', 'Адрес'])
    writer.writeheader()
    writer.writerows(filtered_data)

import re

def find_emails(text: str) -> list:
    pattern = r'\b[\w.%+-]+@[\w.-]+\.[A-Za-z]{2,}\b'
    return re.findall(pattern, text)

    # Загрузка данных
with open('1000_efrsb_messages.json', 'r', encoding='utf-8') as file:
    messages = json.load(file)

emails_dict = {}

for msg in messages:
    inn = msg.get('publisher_inn')
    text = msg.get('msg_text', '')
    emails = find_emails(text)

    if inn and emails:
        if inn not in emails_dict:
            emails_dict[inn] = set()
        emails_dict[inn].update(emails)

# Конвертация множеств в списки для JSON
emails_dict = {k: list(v) for k, v in emails_dict.items()}

# Сохранение в emails.json
with open('emails.json', 'w', encoding='utf-8') as file:
    json.dump(emails_dict, file, ensure_ascii=False, indent=4)

try:
    with open('traders.txt', 'r', encoding='utf-8') as file:
        inn_list = [line.strip() for line in file if line.strip()]
# код
except FileNotFoundError:
    print("Файл не найден!")