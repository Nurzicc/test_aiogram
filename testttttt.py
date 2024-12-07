from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from config import token
import logging
import random
import asyncio

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=token)
dp = Dispatcher()


start_buttons = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    keyboard=[
        [KeyboardButton(text='Игра'), KeyboardButton(text='Новости')]
    ]
)

buttons = [
    [KeyboardButton(text='Наши курсы'), KeyboardButton(text='Адрес')],
    [KeyboardButton(text='О нас')]
]

keyboard_buttons = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

it_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Backend'), KeyboardButton(text='Frontend')],
    [KeyboardButton(text='Ux-Ui'), KeyboardButton(text='Android Developer'), KeyboardButton(text='Ios Developer')]
], one_time_keyboard=True)

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder='Выберите кнопку')

second_button = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    keyboard=[
        [KeyboardButton(text='Камень, ножницы, бумага'), KeyboardButton(text='Рандомайзер')]
    ]
)

choose_button = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='Камень'), KeyboardButton(text='Ножницы'), KeyboardButton(text='Бумага')]
    ]
)

@dp.message(Command('start'))
async def command_start(message: types.Message):
    await message.answer('Приветствую вас! ', reply_markup=start_buttons)
    await message.answer('Выберите кнопку ')

@dp.message(F.text == 'Игра')
async def command_choose(message: types.Message):
    await message.answer('Выберите игру:', reply_markup=second_button)

@dp.message(F.text == 'Камень, ножницы, бумага')
async def choose_game(message: types.Message):
    await message.answer("Выберите ваш вариант:", reply_markup=choose_button)

@dp.message(F.text == "Камень")
async def rps_result_handler(message: types.Message):
    user_choice = message.text
    bot_choice = random.choice(["Камень", "Ножницы", "Бумага"])
    result = ""

    if user_choice == bot_choice:
        result = "Ничья!"
    elif (user_choice == "Камень" and bot_choice == "Ножницы") or \
         (user_choice == "Ножницы" and bot_choice == "Бумага") or \
         (user_choice == "Бумага" and bot_choice == "Камень"):
        result = "Вы победили!"
    else:
        result = "Вы проиграли!"

    await message.answer(f"Ваш выбор: {user_choice}\nВыбор бота: {bot_choice}\n\n{result}")

@dp.message(F.text == "Ножницы")
async def rps_result_handler(message: types.Message):
    user_choice = message.text
    bot_choice = random.choice(["Камень", "Ножницы", "Бумага"])
    result = ""

    if user_choice == bot_choice:
        result = "Ничья!"
    elif (user_choice == "Камень" and bot_choice == "Ножницы") or \
         (user_choice == "Ножницы" and bot_choice == "Бумага") or \
         (user_choice == "Бумага" and bot_choice == "Камень"):
        result = "Вы победили!"
    else:
        result = "Вы проиграли!"

    await message.answer(f"Ваш выбор: {user_choice}\nВыбор бота: {bot_choice}\n\n{result}")

@dp.message(F.text == "Бумага")
async def rps_result_handler(message: types.Message):
    user_choice = message.text
    bot_choice = random.choice(["Камень", "Ножницы", "Бумага"])
    result = ""

    if user_choice == bot_choice:
        result = "Ничья!"
    elif (user_choice == "Камень" and bot_choice == "Ножницы") or \
         (user_choice == "Ножницы" and bot_choice == "Бумага") or \
         (user_choice == "Бумага" and bot_choice == "Камень"):
        result = "Вы победили!"
    else:
        result = "Вы проиграли!"

    await message.answer(f"Ваш выбор: {user_choice}\nВыбор бота: {bot_choice}\n\n{result}")

@dp.message(F.text == "Новости")
async def news_menu_handler(message: types.Message):
    await message.answer("Выберите пункт:", reply_markup=keyboard_buttons)

@dp.message(F.text == "Назад")
async def back_handler(message: types.Message):
    await message.answer("Вы вернулись в главное меню.", reply_markup=start_buttons)

@dp.message(F.text == "Рандомайзер")
async def randomizer_handler(message: types.Message):
    result = random.choice(["Вы победили!", "Вы проиграли!", "Ничья"])
    await message.answer(result)

@dp.message(F.text=='Адрес')
async def location(message:types.Message):
    await message.reply_location(latitude=40.51931846586533, longitude=72.80297788183063)

@dp.message(F.text == 'О нас')
async def command_about(message: types.Message):
    await message.answer_photo('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6lkqYtQ1s_EQNAI_pdjiP20sQjk-gdTCldQ&s')
    await message.answer('''Международная IT-академия Geeks (Гикс) был основан Fullstack-разработчиком Айдаром Бакировым и Android-разработчиком Нургазы Сулаймановым в 2018-ом году в Бишкеке с целью дать возможность каждому человеку, даже без опыта в технологиях, гарантированно освоить IT-профессию. В данный момент более 1200 студентов в возрасте от 12 до 45 лет изучают здесь программирование, дизайн и английский язык. Филиальная сеть образовательного центра представлена в таких городах, как Бишкек, Ош, Ташкент и Кара-Балта. ''')

@dp.message(F.text == 'Наши курсы')
async def command_it(message: types.Message):
    await message.answer('Выберите направление:', reply_markup=it_keyboard)

@dp.message(F.text == 'Backend')
async def command_backend(message: types.Message):
    await message.answer_photo(photo='https://c8.alamy.com/comp/2DB193X/back-end-icon-simple-element-from-website-development-collection-filled-back-end-icon-for-templates-infographics-and-more-2DB193X.jpg')
    await message.answer('''Бэкенд-разработчик — это программист, который работает над внутренней частью веб-ресурсов. Он пишет код, разрабатывает бизнес-логику веб-приложений, задает им алгоритм работы и обеспечивает корректное выполнение пользовательских запросов.''')
    await message.answer('Стоимость этого направления составляет: 12000 сом')
    await message.answer('Время обучения этого направления составляет: 5 месяцев')

@dp.message(F.text == 'Frontend')
async def commannd_front(message: types.Message):
    await message.answer_photo(photo='https://camo.githubusercontent.com/9d6c5d72431a9b20da7515f6b5389dcb68416c437acc96020f62939d47174332/68747470733a2f2f63646e2e7261776769742e636f6d2f7368616e6e6f6e6d6f656c6c65722f66726f6e742d656e642d6c6f676f2f6d61737465722f6578706f7274732f66726f6e742d656e642d6c6f676f2d62772e706e67')
    await message.answer('Frontend-разработчик — это специалист, который занимается разработкой пользовательского интерфейса, то есть той части сайта или приложения, которую видят посетители страницы. Главная задача фронтенд разработчика — перевести готовый дизайн-макет в код так, чтобы все работало правильно.')
    await message.answer('Стоимость этого направления составляет: 12000 сом')
    await message.answer('Время обучения этого направления составляет: 5 месяцев')

@dp.message(F.text == 'Ux-Ui')
async def command_uxui(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdKvOhH1iOUmdb9mVoQmLkUjbSRNzQ9WaCpQ&s')
    await message.answer('UX/UI-дизайнер – IT-специалист, проектирующий и разрабатывающий пользовательский интерфейс приложений, сайтов, программ. В работе анализирует и опирается на пользовательский опыт.')
    await message.answer('Стоимость этого направления составляет: 12000 сом')
    await message.answer('Время обучения этого направления составляет: 4 месяца')

@dp.message(F.text == 'Android Developer')
async def command_android(message: types.Message):
    await message.answer_photo(photo='https://www.clipartmax.com/png/middle/349-3495654_now-we-have-developers-as-customers-android-app-development-logo.png')
    await message.answer('Android-разработчик — это программист, который специализируется на создании мобильных приложений для операционной системы Android. Он разрабатывает приложения с использованием языков программирования Java и Kotlin, интегрирует различные API, работает с базами данных и оптимизирует приложения для разных устройств.')
    await message.answer('Стоимость этого направления составляет: 12000 сом')
    await message.answer('Время обучения этого направления составляет: 7 месяцев')

@dp.message(F.text.lower() == 'ios Developer')  
async def command_ios(message: types.Message):
    await message.answer_photo(photo='https://developer.apple.com/news/images/og/apple-developer-og-twitter.png')
    await message.answer('iOS-разработчик создает приложения для мобильных устройств, работающих на операционной системе iOS. Это iPhone, iPad и другие устройства от Apple. Разработчик должен владеть такими языками программирования, как Swift и Objective-C.')
    await message.answer('Стоимость этого направления составляет: 12000 сом')
    await message.answer('Время обучения этого направления составляет: 7 месяцев')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

