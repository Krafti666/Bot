from random import choice
from ast import literal_eval
import asyncio
import logging
from aiogram import types
from aiogram import Bot,Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message,CallbackQuery
from config import token
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from kb import *

from peewee import *
bot = Bot(token=token)
dp = Dispatcher()

last_message_id = None

is_customized = False
offset_base = 0 #какая модель щя
which_photo_is_now = 0

class Models(Model):
    Id = AutoField(primary_key=True)
    name = CharField()
    description =  CharField()
    photos = CharField()

    class Meta:

        database = SqliteDatabase("Bot_data.sqlite")
        table_name = "Models"
Models.create_table()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOXr8JqnQSpu71JiVDLAC9RyuKEQCLMwjXp3CzCMY6_g&s",
        caption="""Добро пожаловать в SecretRoom!

У нас вы можете найти лучших девочек для интимных встреч.

Выдача адресов происходит круглосуточно через бота или, в крайних случаях, через куратора!

Внимательней проверяйте адрес Telegram, остерегайтесь мошенников, спасибо, что выбираете нас!""",
        reply_markup=kb_basic)

# ------------------------------------------- Права администратора

@dp.message(Command("customize"))
async def customize(message:Message):
    global is_customized
    await message.answer("Введите ключ чтобы изменять данные бота:")
    is_customized = True

@dp.message(F.text == "0512")
async def customize_data(message:Message):
    global is_customized

    if is_customized:
        await message.answer("Что сделать?",reply_markup=kb_what_to_do)

# -------------------------------------------- Права администратора

@dp.callback_query(F.data == "Models")
async def Models_main(callback:CallbackQuery):
    await callback.answer("")
    photo = literal_eval(Models.select().order_by(Models.Id).offset(offset_base).limit(1).first().photos)
    description = (Models.select().order_by(Models.Id).offset(offset_base).limit(1).first().name)
    otziv = literal_eval(Models.select().order_by(Models.Id).offset(offset_base).limit(1).first().description)

    await callback.message.edit_media(media=types.InputMediaPhoto(media=photo[which_photo_is_now],caption=description),reply_markup=kb_models_first)
    # (, caption="Напишите администратору по поводу оформления"), reply_markup = kb_models_middle)

@dp.callback_query(F.data == "Profile")
async def Profile(callback:CallbackQuery):
    await callback.answer("")
    await callback.message.edit_media(media=types.InputMediaPhoto(media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOXr8JqnQSpu71JiVDLAC9RyuKEQCLMwjXp3CzCMY6_g&s",caption=f"""👤 Профиль:

❕ Ваш ID - 423

🏙️ Текущий город -

🗂 Всего заказов - 75096
⭐️ Ваш рейтинг - 5
🔮 Свободных моделей - {Models.select(fn.MAX(Models.Id)).scalar()}"""),reply_markup=kb_profile)

@dp.callback_query(F.data == "Info") # Сделал
async def Info(callback:CallbackQuery):
    await callback.answer("")
    await callback.message.edit_media(media=types.InputMediaPhoto(media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOXr8JqnQSpu71JiVDLAC9RyuKEQCLMwjXp3CzCMY6_g&s",caption="""
Дорогие пользователи,

Хотелось бы поделиться информацией о нашем проекте, который разработан для обеспечения быстрого и комфортного поиска. Теперь вам больше не потребуется затрачивать значительное количество времени и усилий на поиск идеального способа провести досуг.

Мы создали структуру нашего сервиса с учетом удобства для каждого пользователя. Это позволяет сделать выбор быстрее и более простым, убирая лишние сложности.

Почему бы вам не избежать дополнительных трудностей в поисках удовольствия?

Особое внимание следует уделить тому, что мы придерживаемся политики полной анонимности для наших клиентов и не требуем предоставления персональных данных.

С уважением,
Команда технической поддержки вашего эскорт агентства"""),
                                      reply_markup=kb_info)



@dp.callback_query(F.data == "Help")  # Сделал
async def Help(callback:CallbackQuery):
    await callback.answer("")
    await callback.message.edit_media(media=types.InputMediaPhoto(media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOXr8JqnQSpu71JiVDLAC9RyuKEQCLMwjXp3CzCMY6_g&s",
        caption="""Техническая поддержка эскорт-агентства всегда готова помочь в случае возникновения любых технических проблем. Обращайтесь в неё, если у вас возникли трудности с доступом к платформе, проблемы с оплатой услуг, вопросы по функциональности бота. 

Чтобы получить качественную помощь, соблюдайте следующие правила:
1. При описании проблемы будьте максимально информативны. Укажите детали, ошибки, которые привели к проблеме.
2. Соблюдайте уважительное и корректное общение с сотрудниками поддержки.
3. Если проблема касается конфиденциальной информации, не раскрывайте личные данные в открытой переписке.

Сроки ответа технической поддержки колеблются:
- Первый уровень (10 минут): Быстрые ответы на общие вопросы и проблемы, которые могут быть решены быстро.
- Второй уровень (30 минут - 1 час): Сложные проблемы, требующие более глубокого анализа и решения.

Обращение в техническую поддержку позволит вам оперативно решить возникшие технические сложности и продолжить пользоваться услугами эскорт-агентства без перебоев."""),
        reply_markup=kb_help)

@dp.callback_query(F.data == "Return_to_main_menu")
async def Return_to_main_mani(callback: CallbackQuery):
    global offset_base
    offset_base = 0
    await callback.answer("")
    await callback.message.edit_media(media=types.InputMediaPhoto(media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOXr8JqnQSpu71JiVDLAC9RyuKEQCLMwjXp3CzCMY6_g&s",
        caption="""Добро пожаловать в SecretRoom!

У нас вы можете найти лучших девочек для интимных встреч.

Выдача адресов происходит круглосуточно через бота или, в крайних случаях, через куратора!

Внимательней проверяйте адрес Telegram, остерегайтесь мошенников, спасибо, что выбираете нас!"""),
        reply_markup=kb_basic)


# Добавление модели
# ---------------------------------------------------------------------------
class ModelStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_description = State()
    waiting_for_photos = State()


@dp.callback_query(F.data == "Do_model")
async def start_model_creation(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите описание модели:")
    await state.set_state(ModelStates.waiting_for_name)

@dp.message(ModelStates.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите отзывы о моделе в list-формате(['например 1 отзыв','2 отзыв'] и сами отзывы писать в скобочках по такому прицнипу:\n ['соска','пушка','имбуля']):")
    await state.set_state(ModelStates.waiting_for_description)

@dp.message(ModelStates.waiting_for_description)
async def process_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Отлично! Теперь отправьте до 10 фото модели. Когда закончите, напишите 'Готово':")
    await state.update_data(photos=[])
    await state.set_state(ModelStates.waiting_for_photos)

@dp.message(ModelStates.waiting_for_photos, F.photo)
async def process_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    photos = data.get('photos', [])

    if len(photos) < 10:
        photo = message.photo[-1]
        photos.append(photo.file_id)
        await state.update_data(photos=photos)
        await message.answer(
            f"Фото {len(photos)} добавлено. Вы можете отправить еще до {10 - len(photos)} фото или написать 'Готово'.")
    else:
        await message.answer("Вы уже добавили максимальное количество фото (10). Напишите 'Готово' для завершения.")


@dp.message(ModelStates.waiting_for_photos, F.text.casefold() == "готово")
async def finalize_model(message: Message, state: FSMContext):
    data = await state.get_data()
    photos = data.get('photos', [])

    if not photos:
        await message.answer("Вы не добавили ни одного фото. Пожалуйста, добавьте хотя бы одно фото.")
        return

    await message.answer(
        f"Модель сохранена:\nИмя: {data['name']}\nОписание: {data['description']}\nКоличество фото: {len(photos)}")

    for photo_id in photos:
        await message.answer_photo(photo=photo_id)

    Models.insert(data).execute()
# ---------------------------------------------------------------------------

@dp.callback_query(F.data == "Next_photo")
async def Models_next_photo(callback: CallbackQuery):
    global which_photo_is_now
    await callback.answer("")
    which_photo_is_now += 1

    photo = literal_eval(Models.select().order_by(Models.Id).offset(offset_base).limit(1).first().photos)
    description = (Models.select().order_by(Models.Id).offset(offset_base).limit(1).first().name)

    if len(photo) >= which_photo_is_now + 1:
        if len(photo) != which_photo_is_now + 1:
            if offset_base + 1 == Models.select(fn.MAX(Models.Id)).scalar():
                await callback.message.edit_media(media=types.InputMediaPhoto(media=photo[which_photo_is_now], caption=description),reply_markup=kb_models_photo_last_plus_model_last)
            elif offset_base >= 1:
                await callback.message.edit_media(media=types.InputMediaPhoto(media=photo[which_photo_is_now], caption=description),reply_markup=kb_models_photo_middle_plus_model_middle)
            else:
                await callback.message.edit_media(media=types.InputMediaPhoto(media=photo[which_photo_is_now],caption=description),reply_markup=kb_models_photo_middle)
        else:
            await callback.message.edit_media(media=types.InputMediaPhoto(media=photo[which_photo_is_now],caption=description),reply_markup=kb_models_photo_last)




@dp.callback_query(F.data == "Previous_photo")
async def Models_next_photo(callback: CallbackQuery):
    global which_photo_is_now
    await callback.answer("")
    which_photo_is_now -= 1

    photo = literal_eval(Models.select().order_by(Models.Id).offset(offset_base).limit(1).first().photos)
    description = (Models.select().order_by(Models.Id).offset(offset_base).limit(1).first().name)

    if 0 <= which_photo_is_now:
        if which_photo_is_now != 0:
            await callback.message.edit_media(media=types.InputMediaPhoto(media=photo[which_photo_is_now],caption=description),reply_markup=kb_models_photo_middle)
        else:
            await callback.message.edit_media(media=types.InputMediaPhoto(media=photo[which_photo_is_now], caption=description),reply_markup=kb_models_photo_first)




@dp.callback_query(F.data == "Next_tyan")
async def Next_tyan(callback:CallbackQuery):
    global offset_base,which_photo_is_now
    which_photo_is_now = 0
    offset_base += 1

    await callback.answer("")

    photo = literal_eval(Models.select().order_by(Models.Id).offset(offset_base).limit(1).first().photos)
    description = (Models.select().order_by(Models.Id).offset(offset_base).limit(1).first().name)

    if Models.select(fn.MAX(Models.Id)).scalar() >= offset_base +1:
        if Models.select(fn.MAX(Models.Id)).scalar() != offset_base +1:
            await callback.message.edit_media(media=types.InputMediaPhoto(media=photo[which_photo_is_now],caption=description),reply_markup=kb_models_middle)
        else:
            await callback.message.edit_media(media=types.InputMediaPhoto(media=photo[which_photo_is_now], caption=description),reply_markup=kb_models_last)


@dp.callback_query(F.data == "Previous_tyan")
async def Previous_tyan(callback:CallbackQuery):
    global offset_base, which_photo_is_now
    which_photo_is_now = 0
    offset_base -= 1

    await callback.answer("")

    photo = literal_eval(Models.select().order_by(Models.Id).offset(offset_base).limit(1).first().photos)
    description = (Models.select().order_by(Models.Id).offset(offset_base).limit(1).first().name)

    if 0 <= offset_base:
        if offset_base != 0:
            await callback.message.edit_media(media=types.InputMediaPhoto(media=photo[which_photo_is_now], caption=description),reply_markup=kb_models_middle)

        else:
            await callback.message.edit_media(media=types.InputMediaPhoto(media=photo[which_photo_is_now], caption=description),reply_markup=kb_models_first)



@dp.callback_query(F.data == "Otzivs")
async def Otzvivi(callback:CallbackQuery):
    global which_otziv_is_now

    await callback.answer("")

    photo = literal_eval(Models.select().order_by(Models.Id).offset(offset_base).limit(1).first().photos)
    otzivi = literal_eval(Models.select().order_by(Models.Id).offset(offset_base).limit(1).first().description)

    await callback.message.edit_media(media=types.InputMediaPhoto(media=photo[which_photo_is_now], caption=f"""💕Отзывы о модели: \n\n{choice(otzivi)}"""),reply_markup=kb_otzivi)

@dp.callback_query(F.data == "otzivs_write")
async def Otzvivi_wite(callback:CallbackQuery):
    await callback.answer("Написать отзыв можно только после заказа модели!")

class Form(StatesGroup):
    message = State()

@dp.callback_query(F.data == "Napisat")
async def Napisat(callback:CallbackQuery):
    global last_message_id
    await callback.answer("")
    await callback.message.answer("📤Введи сообщение для модели.")

@dp.callback_query(F.data == "Zakazat")
async def Napisat(callback:CallbackQuery):
    await callback.answer("")
    photo = literal_eval(Models.select().order_by(Models.Id).offset(offset_base).limit(1).first().photos)
    await callback.message.edit_media(media=types.InputMediaPhoto(media=photo[which_photo_is_now], caption="Напишите администратору по поводу оформления"),reply_markup=kb_models_middle)











async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())