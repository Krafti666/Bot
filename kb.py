from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


kb_basic = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💝Модели", callback_data="Models")],
        [InlineKeyboardButton(text="👤Профиль", callback_data="Profile"),InlineKeyboardButton(text="🔍Информация", callback_data="Info")],
        [InlineKeyboardButton(text="👩‍💻Техническая поддержка", callback_data="Help")]])

kb_info = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛡Гарантии", url="https://telegra.ph/Polzovatelskoe-soglashenie-dlya-klientov-09-11")],
        [InlineKeyboardButton(text="Вернутся", callback_data="Return_to_main_menu")]])

kb_help = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Писать по вопросам", url="http://t.me/Krafti777")],
        [InlineKeyboardButton(text="Вернутся", callback_data="Return_to_main_menu")]])

kb_profile = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌍Язык", callback_data="lanuguage")],
        [InlineKeyboardButton(text="🏙Город", callback_data="city")],
        [InlineKeyboardButton(text="Вернутся", callback_data="Return_to_main_menu")]])

kb_what_to_do = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Добавить модель", callback_data="Do_model")],
        [InlineKeyboardButton(text="Вернутся", callback_data="Return_to_main_menu")]])


kb_models_first = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥Заказать", callback_data="Zakazat")],
        [InlineKeyboardButton(text="📨Написать", callback_data="Napisat")],
        [InlineKeyboardButton(text="💕Отзывы", callback_data="Otzivs")],
        [InlineKeyboardButton(text="Следущее фото📸", callback_data="Next_photo")],
        [InlineKeyboardButton(text="Следущая➡️", callback_data="Next_tyan")],
        [InlineKeyboardButton(text="↩️Вернутся", callback_data="Return_to_main_menu")]])

kb_models_middle = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥Заказать", callback_data="Zakazat")],
        [InlineKeyboardButton(text="📨Написать", callback_data="Napisat")],
        [InlineKeyboardButton(text="💕Отзывы", callback_data="Otzivs")],
        [InlineKeyboardButton(text="Следущее фото📸", callback_data="Next_photo")],
        [InlineKeyboardButton(text="⬅️Предыдущая", callback_data="Previous_tyan"),InlineKeyboardButton(text="Следущая➡️", callback_data="Next_tyan")],
        [InlineKeyboardButton(text="↩️В главное меню", callback_data="Return_to_main_menu")]])


kb_models_last = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥Заказать", callback_data="Zakazat")],
        [InlineKeyboardButton(text="📨Написать", callback_data="Napisat")],
        [InlineKeyboardButton(text="💕Отзывы", callback_data="Otzivs")],
        [InlineKeyboardButton(text="Следущее фото📸", callback_data="Next_photo")],
        [InlineKeyboardButton(text="⬅️Предыдущая", callback_data="Previous_tyan")],
        [InlineKeyboardButton(text="↩️Вернутся", callback_data="Return_to_main_menu")]])


kb_models_photo_middle_plus_model_middle = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥Заказать", callback_data="Zakazat")],
        [InlineKeyboardButton(text="📨Написать", callback_data="Napisat")],
        [InlineKeyboardButton(text="💕Отзывы", callback_data="Otzivs")],
        [InlineKeyboardButton(text="Предыдущее фото📸", callback_data="Previous_photo"),InlineKeyboardButton(text="Следущее фото📸", callback_data="Next_photo")],        [InlineKeyboardButton(text="⬅️Предыдущая", callback_data="Previous_tyan"),InlineKeyboardButton(text="Следущая➡️", callback_data="Next_tyan")],
        [InlineKeyboardButton(text="↩️Вернутся", callback_data="Return_to_main_menu")]])

kb_models_photo_last_plus_model_last = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥Заказать", callback_data="Zakazat")],
        [InlineKeyboardButton(text="📨Написать", callback_data="Napisat")],
        [InlineKeyboardButton(text="💕Отзывы", callback_data="Otzivs")],
        [InlineKeyboardButton(text="Предыдущее фото📸", callback_data="Previous_photo"),InlineKeyboardButton(text="Следущее фото📸", callback_data="Next_photo")],
        [InlineKeyboardButton(text="⬅️Предыдущая", callback_data="Previous_tyan")],
        [InlineKeyboardButton(text="↩️Вернутся", callback_data="Return_to_main_menu")]])


kb_models_photo_first = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥Заказать", callback_data="Zakazat")],
        [InlineKeyboardButton(text="📨Написать", callback_data="Napisat")],
        [InlineKeyboardButton(text="💕Отзывы", callback_data="Otzivs")],
        [InlineKeyboardButton(text="Следущее фото📸", callback_data="Next_photo")],
        [InlineKeyboardButton(text="Следущая➡️", callback_data="Next_tyan")],
        [InlineKeyboardButton(text="↩️Вернутся", callback_data="Return_to_main_menu")]])

kb_models_photo_middle = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥Заказать", callback_data="Zakazat")],
        [InlineKeyboardButton(text="📨Написать", callback_data="Napisat")],
        [InlineKeyboardButton(text="💕Отзывы", callback_data="Otzivs")],
        [InlineKeyboardButton(text="Предыдущее фото📸", callback_data="Previous_photo"),InlineKeyboardButton(text="Следущее фото📸", callback_data="Next_photo")],
        [InlineKeyboardButton(text="Следущая➡️", callback_data="Next_tyan")],
        [InlineKeyboardButton(text="↩️Вернутся", callback_data="Return_to_main_menu")]])





kb_models_photo_last = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥Заказать", callback_data="Zakazat")],
        [InlineKeyboardButton(text="📨Написать", callback_data="Napisat")],
        [InlineKeyboardButton(text="💕Отзывы", callback_data="Otzivs")],
        [InlineKeyboardButton(text="Предыдущее фото📸", callback_data="Previous_photo")],
        [InlineKeyboardButton(text="Следущая➡️", callback_data="Next_tyan")],
        [InlineKeyboardButton(text="↩️Вернутся", callback_data="Return_to_main_menu")]])

kb_otzivi = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Другой отзыв", callback_data="Otzivs")],
        [InlineKeyboardButton(text="Написать отзыв", callback_data="otzivs_write")],
        [InlineKeyboardButton(text="↩️Назад", callback_data="Models")]])

kb_zakazat = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Администратор", callback_data="http://t.me/Krafti777")],
        [InlineKeyboardButton(text="↩️Назад", callback_data="Models")]])