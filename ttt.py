# from aiogram import Bot, Dispatcher, F, types
# from aiogram.filters import Command, CommandStart
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.fsm.storage.memory import MemoryStorage
# from email.message import EmailMessage
# from config import token, SMTP_PASSWORD, SMTP_USER
# import aiosmtplib
# import logging

# SMTP_SERVER = 'smtp.gmail.com'
# SMTP_PORT = 587
# SMTP_USER = SMTP_USER
# SMTP_PASSWORD = SMTP_PASSWORD

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=token)
# storage = MemoryStorage()
# dp = Dispatcher(storage=storage)



# class UserState(StatesGroup):
#     choose_option = State()
#     waiting_for_email = State()
#     waiting_for_message = State()
#     waiting_for_photo = State()
#     waiting_for_video = State()
#     waiting_for_audio = State()



# def get_main_keyboard():
#     return InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="Отправить сообщение", callback_data="send_message")],
#         [InlineKeyboardButton(text="Отправить фото", callback_data="send_photo")],
#         [InlineKeyboardButton(text="Отправить видео", callback_data="send_video")],
#         [InlineKeyboardButton(text="Отправить аудио", callback_data="send_audio")],
#     ])



# async def send_email(to_email, subject, body, file=None):
#     message = EmailMessage()
#     message.set_content(body)
#     message['Subject'] = subject
#     message['From'] = SMTP_USER
#     message['To'] = to_email

#     if file:
#         message.add_attachment(file['data'], maintype=file['maintype'], subtype=file['subtype'], filename=file['filename'])

#     try:
#         logging.info(f"Отправка email на {to_email}")
#         await aiosmtplib.send(
#             message,
#             hostname=SMTP_SERVER,
#             port=SMTP_PORT,
#             start_tls=True,
#             username=SMTP_USER,
#             password=SMTP_PASSWORD
#         )
#         logging.info(f"Письмо успешно отправлено на {to_email}")
#     except Exception as e:
#         logging.exception(f"Ошибка при отправке письма: {e}")



# @dp.message(CommandStart())
# async def start(message: types.Message, state: FSMContext):
#     await message.answer("Добро пожаловать! Введите email для отправки сообщений.")
#     await state.set_state(UserState.waiting_for_email)



# @dp.message(UserState.waiting_for_email, F.text.contains('@gmail.com'))
# async def process_email(message: types.Message, state: FSMContext):
#     await state.update_data(email=message.text)
#     await message.answer("Выберите, что хотите отправить:", reply_markup=get_main_keyboard())
#     await state.set_state(UserState.choose_option)



# @dp.message(UserState.waiting_for_email)
# async def invalid_email(message: types.Message):
#     await message.answer("Пожалуйста, введите корректный email (например, example@gmail.com).")



# @dp.callback_query(UserState.choose_option)
# async def choose_option(callback_query: types.CallbackQuery, state: FSMContext):
#     data = callback_query.data
#     if data == "send_message":
#         await callback_query.message.answer("Введите текст сообщения:")
#         await state.set_state(UserState.waiting_for_message)
#     elif data == "send_photo":
#         await callback_query.message.answer("Отправьте фото:")
#         await state.set_state(UserState.waiting_for_photo)
#     elif data == "send_video":
#         await callback_query.message.answer("Отправьте видео:")
#         await state.set_state(UserState.waiting_for_video)
#     elif data == "send_audio":
#         await callback_query.message.answer("Отправьте аудио:")
#         await state.set_state(UserState.waiting_for_audio)
#     await callback_query.answer()



# @dp.message(UserState.waiting_for_message)
# async def send_text_message(message: types.Message, state: FSMContext):
#     user_data = await state.get_data()
#     email = user_data['email']
#     await send_email(to_email=email, subject="Сообщение от бота", body=message.text)
#     await message.answer("Сообщение успешно отправлено!")
#     await state.clear()



# @dp.message(UserState.waiting_for_photo, F.photo)
# async def send_photo(message: types.Message, state: FSMContext):
#     user_data = await state.get_data()
#     email = user_data['email']
#     photo = message.photo[-1]
#     file = await bot.download(photo.file_id)
#     await send_email(
#         to_email=email,
#         subject="Фото от бота",
#         body="Вам отправлено фото.",
#         file={
#             "data": file.read(),
#             "maintype": "image",
#             "subtype": "jpeg",
#             "filename": "photo.jpg"
#         }
#     )
#     await message.answer("Фото успешно отправлено!")
#     await state.clear()



# @dp.message(UserState.waiting_for_video, F.video)
# async def send_video(message: types.Message, state: FSMContext):
#     user_data = await state.get_data()
#     email = user_data['email']
#     video = message.video
#     file = await bot.download(video.file_id)
#     await send_email(
#         to_email=email,
#         subject="Видео от бота",
#         body="Вам отправлено видео.",
#         file={
#             "data": file.read(),
#             "maintype": "video",
#             "subtype": "mp4",
#             "filename": "video.mp4"
#         }
#     )
#     await message.answer("Видео успешно отправлено!")
#     await state.clear()



# @dp.message(UserState.waiting_for_audio, F.audio)
# async def send_audio(message: types.Message, state: FSMContext):
#     user_data = await state.get_data()
#     email = user_data['email']
#     audio = message.audio
#     file = await bot.download(audio.file_id)
#     await send_email(
#         to_email=email,
#         subject="Аудио от бота",
#         body="Вам отправлено аудио.",
#         file={
#             "data": file.read(),
#             "maintype": "audio",
#             "subtype": "mp3",
#             "filename": "audio.mp3"
#         }
#     )
#     await message.answer("Аудио успешно отправлено!")
#     await state.clear()



# async def main():
#     await dp.start_polling(bot)


# if __name__ == '__main__':
#     import asyncio
#     asyncio.run(main())
