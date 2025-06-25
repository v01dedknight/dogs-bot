import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InputFile, InputMediaPhoto, BufferedInputFile
from aiogram.filters import Command
from dotenv import load_dotenv
from db import get_dogs, get_dog_info
import io
import os

# Загрузка переменных из .env
load_dotenv()

# Логирование
logging.basicConfig(level=logging.INFO)

# Создание объектов бота и диспетчера
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📋 Look at the dogs")],
        [KeyboardButton(text="📞 Contact the breeder")],
        [KeyboardButton(text="❓ List of commands")]
    ],
    resize_keyboard=True
)

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    text = (
        "🐶 Hello! I'm here to help you browse dogs and get in touch with the breeder.\n\n"
        "ℹ️ This bot is for informational purposes only and does not offer any services or sales.\n"
        "📞 Contact the breeder for details: @LINK or +9(999)999-99-99"
    )
    
    await message.answer(text, reply_markup=main_menu)

# Обработчик текстовых кнопок
@dp.message()
async def handle_text_buttons(message: Message):
    if message.text == "📋 Look at the dogs":
        await cmd_show(message)
    elif message.text == "📞 Contact the breeder":
        await cmd_contact(message)
    elif message.text == "❓ List of commands":
        await cmd_help(message)

# Обработчик команды /help
@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Available commands:\n/start - Launch bot\n/contact - Contact the breeder\n/show - Look at the dogs\n/help - List of commands")

# Обработчик команды /contact
@dp.message(Command("contact"))
async def cmd_contact(message: Message):
    await message.answer("The following contacts are available:\n\n📞 Phone number: +9(999)999-99-99 (Telegram/WhatsApp)\nWrite to Telegram directly: @LINK\n\nConversation in any language of the world 🌏")

# Функция для загрузки собак
def get_dogs_from_db(limit=10, offset=0):
    return get_dogs(limit, offset)

@dp.message(Command("show"))
async def cmd_show(message: Message, offset=0):
    dogs = get_dogs_from_db(limit=10, offset=offset)

    if not dogs:
        await message.answer("🐕 The list of dogs is over.")
        return

    text = "📋 List of dogs:\n\n"
    buttons = []

    for dog in dogs:
        dog_id, name, gender, birthday = dog
        text += f"🐶 ID {dog_id}: {name} ({gender}, {birthday})\n"
        buttons.append([InlineKeyboardButton(text=f"Choose {name} (ID {dog_id})", callback_data=f"select_{dog_id}")])

    buttons.append([InlineKeyboardButton(text="➡️ Next", callback_data=f"next_{offset+5}")])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer(text, reply_markup=keyboard)

# Обработчик кнопки "Дальше"
@dp.callback_query(lambda c: c.data.startswith("next_"))
async def callback_next_page(callback_query: types.CallbackQuery):
    offset = int(callback_query.data.split("_")[1])
    await cmd_show(callback_query.message, offset)

# Функция для загрузки данных о собаке по ID
def get_dog_info(dog_id):
    return get_dog_info(dog_id)

@dp.callback_query(lambda c: c.data.startswith("select_"))
async def callback_select_dog(callback_query: types.CallbackQuery):
    dog_id = int(callback_query.data.split("_")[1])
    dog = get_dog_info(dog_id)

    if not dog:
        await callback_query.message.answer("⚠️ Dog not found.")
        await callback_query.answer()
        return

    await callback_query.answer("Uploading photo...", show_alert=False)

    dog_info = (
        f"🐶 Name: {dog[1]}\n"
        f"📅 Birthday: {dog[2]}\n"
        f"🎨 Color: {dog[3]}\n"
        f"⚤ Gender: {dog[4]}\n"
        f"⚖ Weight: {dog[5]} kg\n"
        f"✅ Available: {'No, the dog is booked.' if not dog[6] else 'Yes'}\n"
        f"🚚 Worldwide delivery: {'Yes' if dog[7] else 'No'}\n"
    )

    await callback_query.message.answer(dog_info)

    pictures = [dog[i] for i in range(8, 18) if dog[i]]
    media = []

    for pic in pictures:
        pic_io = io.BytesIO(pic)
        pic_io.seek(0)
        media.append(InputMediaPhoto(media=BufferedInputFile(pic_io.read(), filename="dog.jpg")))

    if media:
        await callback_query.message.answer_media_group(media)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
