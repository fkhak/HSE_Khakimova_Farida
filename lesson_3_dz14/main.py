#Создайте бот-справочник с красивым меню (используйте KeyBoardButton и ReplyKeyboardMarkup).

from dotenv import load_dotenv
import os
from datetime import datetime
import sqlite3
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

main_menu = ReplyKeyboardMarkup([
    [KeyboardButton('Основы Python'), KeyboardButton('Библиотеки')],
    [KeyboardButton('Примеры кода'), KeyboardButton('Помощь')]
], resize_keyboard=True)

back_menu = ReplyKeyboardMarkup([
    [KeyboardButton('Назад')]
], resize_keyboard=True)


def handle_user(user) -> None:
    """Создание таблиц и добавление пользователя"""
    con = sqlite3.connect('telegram.db')
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS users(
            tgid TEXT PRIMARY KEY, 
            fullname TEXT, 
            username TEXT
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS logs(
            tgid TEXT, 
            activity TEXT, 
            datetime TEXT
        )
    ''')

    result = cur.execute(f"SELECT * FROM users WHERE tgid='{user.id}'")
    if not result.fetchone():
        cur.execute(f"INSERT INTO users VALUES ('{user.id}', '{user.full_name}', '{user.username}')")
        con.commit()
    con.close()


def log_activity(user, activity: str) -> None:
    """Логирование действий пользователя"""
    con = sqlite3.connect('telegram.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO logs VALUES ('{user.id}', '{activity}', '{datetime.now().isoformat()}')")
    con.commit()
    con.close()


def start_command(update: Update, context: CallbackContext):
    """Обработчик команды /start"""
    user = update.effective_user
    handle_user(user)

    welcome_text = f"""Привет, {user.full_name}! 
Добро пожаловать в справочник по Python!

Выберите раздел из меню:"""

    update.message.reply_text(welcome_text, reply_markup=main_menu)
    log_activity(user, 'start_command')


def help_command(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /help"""
    user = update.effective_user
    help_text = """Это бот-справочник по Python. 

Используйте кнопки меню для навигации по разделам:
- Основы Python: базовые концепции языка
- Библиотеки: популярные Python библиотеки  
- Примеры кода: готовые примеры программ
- Помощь: это сообщение

Для возврата в главное меню используйте кнопку 'Назад'."""

    update.message.reply_text(help_text, reply_markup=main_menu)
    log_activity(user, 'help_command')


def text_handler(update: Update, context: CallbackContext) -> None:
    """Обработчик текстовых сообщений"""
    user = update.effective_user
    text = update.message.text

    if text == 'Основы Python':
        response = """📚 **Основы Python**

• **Переменные и типы данных**
• **Условные операторы** 
• **Циклы for и while**
• **Функции и модули**"""

    elif text == 'Библиотеки':
        response = """📖 **Популярные библиотеки Python**

• **requests** - для HTTP-запросов
• **pandas** - для анализа данных  
• **matplotlib** - для визуализации
• **telegram-bot** - для создания ботов"""

    elif text == 'Примеры кода':
        response = """💻 **Примеры кода Python**

**Пример 1: Функция приветствия**
```python
def hello(name):
    return f"Привет, {name}!"
        
**Пример 2: Работа со списком**
```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
```"""

    elif text == 'Помощь':
        help_command(update, context)
        return

    elif text == 'Назад':
        update.message.reply_text('Главное меню:', reply_markup=main_menu)
        log_activity(user, 'back_to_main')
        return

    else:
        response = 'Пожалуйста, используйте кнопки меню для навигации'
        update.message.reply_text(response, reply_markup=main_menu)
        log_activity(user, 'unknown_command')
        return

    update.message.reply_text(response, reply_markup=back_menu)
    log_activity(user, f'section_{text}')


if __name__ == "__main__":
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, text_handler))

    print("Бот-справочник запущен...")
    updater.start_polling()
    updater.idle()