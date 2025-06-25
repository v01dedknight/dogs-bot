# dogs-bot

Telegram-бот для просмотра списка списка и подробной информации о собаках и связи с заводчиком.
Этот бот носит исключительно информационный характер и не предлагает никаких услуг или продаж.

---

## Функционал

- Просмотр списка собак
- Детальная информация о каждой собаке с фотографиями  
- Контакты заводчика
- Команды: `/start`, `/help`, `/contact`, `/show`

---

## Структура проекта

```

dogsbot/
├── .env               # Файл с переменными окружения (токены, настройки БД)
├── .gitignore         # Игнорируемые файлы
├── bot.py             # Основная логика бота
├── config.py          # Конфигурация для подключения к БД и токен бота
├── db.py              # Работа с базой данных (MySQL)
├── example.env        # Пример файла .env с настройками
├── license.txt        # Лицензионное соглашение (обязательно к ознакомлению)
├── requirements.txt   # Зависимости
├── schema.sql         # Скрипт создания базы данных и таблиц
└── seed.sql           # Скрипт наполнения тестовыми данными

````

---

## Установка и запуск

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/v01dedknight/dogs-bot
cd dogsbot
````

### 2. Создайте виртуальное окружение и установите зависимости

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 3. Создайте базу данных и таблицы

* Подключитесь к MySQL и выполните скрипты:

```sql
source schema.sql;
source seed.sql;
```

### 4. Настройте переменные окружения

* Создайте файл `.env` на основе `example.env` и заполните:

```env
BOT_TOKEN=ваш_токен_бота_из_Telegram
MYSQL_HOST=localhost
MYSQL_USER=ваш_пользователь_БД
MYSQL_PASSWORD=ваш_пароль_БД
MYSQL_DATABASE=dogs_db
```

### 5. Запустите бота

```bash
python bot.py
```

---

## Использование

* Запустите бота в Telegram через команду `/start`
* Используйте кнопки главного меню для навигации:

  * 📋 Look at the dogs — посмотреть список собак
  * 📞 Contact the breeder — контакты заводчика
  * ❓ List of commands — список доступных команд

---

## Зависимости

* Python 3.7+
* aiogram
* python-dotenv
* mysql-connector-python

---

## Лицензия

Проект предоставляется **исключительно для ознакомления**.  
Полные условия использования описаны в файле [license.txt](https://github.com/v01dedknight/dogs-bot/blob/main/license.txt) в корне репозитория.
