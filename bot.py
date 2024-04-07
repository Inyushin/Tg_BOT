from aiogram import Bot, Dispatcher, F, types
from aiogram.types import CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage
from random import randint
import logging
import asyncio


storage = MemoryStorage()
dp = Dispatcher(storage=storage)


bot = Bot(token='6638541858:AAF6F1PYKLFF9wzg6pI9vDqFgic518tsm3g')
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}!\nЧтобы узнать возможности этого бота - отправь команду /help")


@dp.message(Command('help'))
async def help(message: types.Message):
    math_button = types.InlineKeyboardButton(text="Математика", callback_data="math")
    physics_button = types.InlineKeyboardButton(text="Физика", callback_data="physics")
    key_board = [[math_button], [physics_button]]
    markup = types.InlineKeyboardMarkup(inline_keyboard=key_board)
    await message.answer(text="Этот бот может выводить формулы!\nВыбери по какому предмету:", reply_markup=markup)


@dp.message(Command('thanks'))
async def thanks(message: types.Message):
    photos = ["https://animals.pibig.info/uploads/posts/2023-04/1680313424_animals-pibig-info-p-koti-spokoinoi-nochi-zhivotnie-pinterest-1.jpg", "https://4x4photo.ru/wp-content/uploads/2023/05/7294ce1f-32f4-48c3-a0cb-cfe30ef8f3f8.jpg", "https://sun9-29.userapi.com/impg/6P88ObYLRGE9DCcEXZVfeAc70ZTip5u8YS7DQQ/T3-jClMDIF8.jpg?size=728x728&quality=96&sign=3138231cecaeaae0bd4d3a45d93af2ea&c_uniq_tag=Pq__YiqDQsYn9yHDg9_0i6Rs8ZLZk4_o36hbMxd6KMM&type=album", 'https://img.razrisyika.ru/kart/125/1200/499814-smeshnye-kotiki-2.jpg', 'https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663117727_42-mykaleidoscope-ru-p-kotiki-veselie-pinterest-42.jpg']
    url = photos[randint(0, 4)]
    await bot.send_photo(message.chat.id, url, caption="Всегда рады помочь!")


@dp.callback_query(lambda callback: callback.data == "math")
async def maths_topics(callback: types.CallbackQuery):
    extent_button = types.InlineKeyboardButton(text="Свойства степеней и корней", callback_data="extent")
    multiplication_button = types.InlineKeyboardButton(text="Формулы сокращённого умножения", callback_data="multiplication")
    square_uravnenia_button = types.InlineKeyboardButton(text="Квадратные уравнения", callback_data="square_uravnenia")
    trigonometria_button = types.InlineKeyboardButton(text="Тригонометрия", callback_data="trigonometria")
    module_button = types.InlineKeyboardButton(text="Модуль",callback_data="module")
    vectors_button = types.InlineKeyboardButton(text="Векторы", callback_data="vectors")
    key_board = [[extent_button], [multiplication_button], [square_uravnenia_button], [module_button], [trigonometria_button], [vectors_button]]
    markup = types.InlineKeyboardMarkup(inline_keyboard=key_board)
    await callback.message.answer(text="Выбери тему по математике!", reply_markup=markup)


@dp.callback_query(lambda callback: callback.data == "physics")
async def physics_topics(callback: types.CallbackQuery):
    kinematics_button = types.InlineKeyboardButton(text="Кинематика", callback_data="kinematics")
    dynamics_button = types.InlineKeyboardButton(text="Динамика", callback_data="dynamics")
    static_button = types.InlineKeyboardButton(text="Статика", callback_data="static")
    energy_button = types.InlineKeyboardButton(text="Законы сохранения импульса и энергии", callback_data="energy")
    molecules_button = types.InlineKeyboardButton(text="Молекулы", callback_data="molecules")
    gases_button = types.InlineKeyboardButton(text="Газовые законы", callback_data="gases")
    thermodynamics_button = types.InlineKeyboardButton(text="Термодинамика идеального газа", callback_data="thermodynamics")
    kpd_button = types.InlineKeyboardButton(text="КПД теплового двигателя", callback_data="kpd")
    el_stat_button = types.InlineKeyboardButton(text="Электростатика", callback_data="el_stat")
    tok_button = types.InlineKeyboardButton(text="Постоянный ток", callback_data="tok")
    magnit_button = types.InlineKeyboardButton(text="Магнитное поле", callback_data="magnit")
    key_board = [[kinematics_button], [dynamics_button], [static_button], [energy_button], [molecules_button], [gases_button], [thermodynamics_button], [kpd_button], [el_stat_button], [tok_button], [magnit_button]]
    markup = types.InlineKeyboardMarkup(inline_keyboard=key_board)
    await callback.message.answer(text="Выбери тему по физике!", reply_markup=markup)


@dp.callback_query(lambda callback: callback.data == "extent")
async def extent(callback: types.CallbackQuery, bot : bot):
    photo_url = 'http://motiv51260.ucoz.net/ELECTRONBOOK/user-images/svoystva_step.jpg'
    await bot.send_photo(callback.message.chat.id, photo_url, caption= "Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")

@dp.callback_query(lambda callback: callback.data == "multiplication")
async def multiplication(callback: types.CallbackQuery, bot : bot):
    photo_url = "https://padlet.pics/1/image?t=ar_2,c_lfill,dpr_1,f_jpg,g_auto,h_600,w_1200&url=https%3A%2F%2Fassets.padletcdn.com%2Fstatic%2Fpadlets%2Fdyu7kh56hgbh%2Fexports%2Fpeek%2F1674238982%2FQkFoN0J6b1BjSFZpYkdsalgydGxlVWtpRVdSNWRUZHJhRFUyYUdkaWFBWTZCa1ZVT2d4MlpYSnphVzl1U1NJUE1UWTNOREl6T0RrNE1nWTdCa1k9LS0yNzUzZGYyYWU2ZWI2NTliNzBiZTc1MDFhOWZjN2M1N2IzZTNjNmFi"
    await bot.send_photo(callback.message.chat.id, photo_url, caption= "Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")

@dp.callback_query(lambda callback: callback.data == "square_uravnenia")
async def square_uravnenia(callback: types.CallbackQuery, bot : bot):
    photo_url = "https://megaformula.ru/wp-content/uploads/2018/12/325525345.png"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


@dp.callback_query(lambda callback: callback.data == "trigonometria")
async def trigonometria(callback: types.CallbackQuery, bot: bot):
    photo_url = "https://ege-study.ru/wp-content/uploads/2019/09/161.jpg"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


@dp.callback_query(lambda callback: callback.data == "module")
async def module(callback: types.CallbackQuery, bot: bot):
    photo_url = "https://avatars.dzeninfra.ru/get-zen_doc/3723909/pub_600581c1e0a5593cf7e18c35_6005823b94dcbd4ea686e810/scale_1200"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


@dp.callback_query(lambda callback: callback.data == "vectors")
async def vectors(callback: types.CallbackQuery, bot: bot):
    photo_url = "https://rc74.ru/800/600/http/nice-diplom.ru/uploads/posts/2019-09/1567705606_vect_1.png"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


@dp.callback_query(lambda callback: callback.data == "kinematics")
async def kinematics(callback: types.CallbackQuery, bot: bot):
    photo_url = "https://fizi4ka.ru/wp-content/uploads/2018/01/img_5a68c3c2aa930.png"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


@dp.callback_query(lambda callback: callback.data == "dynamics")
async def dynamics(callback: types.CallbackQuery, bot: bot):
    photo_url = "https://nauchniestati.ru/wp-content/uploads/2019/06/image9-min.png"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


@dp.callback_query(lambda callback: callback.data == "static")
async def static(callback: types.CallbackQuery, bot: bot):
    photo_url = "https://fizi4ka.ru/wp-content/uploads/2018/01/img_5a69d4dd6b163.png"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


@dp.callback_query(lambda callback: callback.data == "energy")
async def energy(callback: types.CallbackQuery, bot: bot):
    photo_url = "https://thepresentation.ru/img/tmb/4/365105/eba9c3dc04703a460e8784a419275f5e-800x.jpg"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


@dp.callback_query(lambda callback: callback.data == "molecules")
async def molecules(callback: types.CallbackQuery, bot: bot):
    photo_url = "https://nauchniestati.ru/wp-content/uploads/2019/06/image17-min.png"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


@dp.callback_query(lambda callback: callback.data == "gases")
async def gases(callback: types.CallbackQuery, bot: bot):
    photo_url = "https://ru-static.z-dn.net/files/dff/637f76ff41412fdb92e004270280063f.jpg"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


@dp.callback_query(lambda callback: callback.data == "thermodynamics")
async def thermodynamics(callback: types.CallbackQuery, bot: bot):
    photo_url = "https://blog.fenix.help/common/upload/ckeditor/2020/09/01/1507c2-osnovnye-formuly-1598956048.jpg"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


@dp.callback_query(lambda callback: callback.data == "kpd")
async def kpd(callback: types.CallbackQuery, bot: bot):
    photo_url = "https://cf2.ppt-online.org/files2/slide/k/kY1BLANzKoh2tfnQjx4HaVUiuv0d5WbpEgI873/slide-11.jpg"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


@dp.callback_query(lambda callback: callback.data == "el_stat")
async def el_stat(callback: types.CallbackQuery, bot: bot):
    photo_url = "https://oooevna.ru/wp-content/uploads/7/b/1/7b1ae8bd56473495332be95f3e9b1bea.jpg"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


@dp.callback_query(lambda callback: callback.data == "tok")
async def tok(callback: types.CallbackQuery, bot: bot):
    photo_url = "https://avatars.dzeninfra.ru/get-zen_doc/5324612/pub_63945ac7882655038c882c44_63945b7bb6662a2b2bfd8b87/scale_1200"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


@dp.callback_query(lambda callback: callback.data == "magnit")
async def magnit(callback: types.CallbackQuery, bot: bot):
    photo_url = "https://www.napishem.ru/wp-content/uploads/2021/11/fizika-03.png"
    await bot.send_photo(callback.message.chat.id, photo_url,
                         caption="Если мы Вам помогли - отправьте команду /thanks\nИли выберите другую тему.")


if __name__ == "__main__":
    asyncio.run(main())
