from data.config import YUAN_BOT

# msg_lang = {
#     "shopping_end": {
#         "uz": "✅ Buyurtmangiz ko‘rib chiqish uchun adminlarga yuborildi. 24 soat ichida siz bilan bog'lanamiz.",
#         "ru": "✅ Ваш заказ отправлен админам на рассмотрение. Мы с вами свяжемся в течении сутки."
#     },
#     "shopping_image_err": {
#         "uz": "🚫 Skrinshot yuborishingiz kerak!",
#         "ru": "🚫 Необходимо отправить скриншот!",
#     },
#     "shopping_link": {
#         "uz": "🔗 Buyurtma bermoqchi bo'lgan tovaringizni havolasini yuboring",
#         "ru": "🔗 Отправьте ссылку на товар, который хотите заказать",
#     },
#     "shopping_image": {
#         "uz": "🖼 Razmer, rang va shunga o'xshash parametrlarni tanlagan xolda skrin qilib tashlang",
#         "ru": "🖼 Сделайте скриншот с выбранным вами размером, цветом и подобными параметрами.",
#     },
#     "main_menu": {"uz": "Asosiy menyu", "ru": "Главное меню"},
#     "trek_code": {"uz": "Trek kodni kiriting", "ru": "Введите код трека"},
#     "no_trek_code": {
#         "uz": "🚫 Sizda bunday trek kodga ega buyurtma mavjud emas!",
#         "ru": "🚫 У вас нет заказа с этим трек кодом!",
#     },
#     "taken": {
#         "uz": "Buyurtmangizni allaqachon olgansiz❗️",
#         "ru": "Вы уже получили свой заказ❗️",
#     },
#     "deliver_or_not": {
#         "uz": "Buyurtmangiz O'zbekistonga yetib kelgan.\nBuyurtmani qo'lga kriitish turini tanlang:",
#         "ru": "Ваш заказ прибыл в Узбекистан.\nВыберите тип получения заказа:",
#     },
#     "not_arrived": {
#         "uz": "Buyurtmangiz hali O'zbekistonga yetib kelmadi. Buyurtmangiz yo'lda.",
#         "ru": "Ваш заказ еще не прибыл в Узбекистан. Ваш заказ в пути.",
#     },
#     'buy_yuan': {
#         'uz': f"💳 Yuan sotib olish uchun ushbu botimizdan foydalanishingiz mumkin: @{YUAN_BOT.split('/')[-1]}",
#         'ru': f'💳 Вы можете использовать нашего бота для покупки юаней: @{YUAN_BOT.split("/")[-1]}'
#     },
#     'greeting': {
#         'uz': "Salom {0}! Rasmiy FAD Cargo botiga xush kelibsiz - Xitoydan yetkazib berish!",
#         'ru': "Привет, {0}! Добро пожаловать в официальный бот FAD Cargo - Доставка из Китая!"
#     },
#     'allow': {
#         'uz': "Bu yetkazib berish turidan nimalarni buyurtma qila olmaysiz:",
#         'ru': 'Что нельзя заказать в этом виде доставки:'
#     },
#     "deliver": {
#         "uz": "Buyurtmani jo'natish uchun lokatsiyangizni yuboring 🔽",
#         "ru": "Отправьте свою локацию чтобы получить заказ 🔽",
#     },
#     "success_deliver": {
#         "uz": "Manzil qabul qilindi ✅\nTez orada buyurtmangiz manzilga yetkaziladi)",
#         "ru": "Адрес получен ✅\nВаш заказ будет доставлен в ближайшее время)",
#     },
#     "bring_deliver": {
#         "uz": "Ushbu manzilga kelib, buyurtmangizni olib ketishingiz mumkin.",
#         "ru": "Вы можете прийти по этому адресу и забрать свой заказ.",
#     },
#     "phone_number_checking": {
#         "all_exc": {
#             "uz": 'Telefon raqami "+" belgisi bilan boshlanishi va 12 ta raqamdan iborat bo\'lishi kerak.',
#             "ru": 'Номер телефона должен начинаться с "+" и содержать 12 цифр.',
#         },
#         "with_plus": {
#             "uz": 'Telefon raqami "+" belgisi bilan boshlanishi kerak',
#             "ru": 'Номер телефона должен начинаться со знака "+".',
#         },
#         "with_998": {
#             "uz": "Telefon raqami O‘zbekiston Respublikasiga tegishli bo‘lishi kerak",
#             "ru": "Номер телефона должен принадлежать Республики Узбекистан",
#         },
#         "with_num": {
#             "uz": 'Telefon raqamida "+" dan boshqa belgilar yoki harflar bo\'lmasligi kerak',
#             "ru": 'Номер телефона не должен содержать буквы или знаки кроме "+"',
#         },
#         "example": {"uz": "Масалан: +998001234567", "ru": "Например: +998001234567"},
#     },
#     "not_phone": {
#         "uz": 'Iltimos, "📞 Telefon yuborish" tugmasi orqali yuboring',
#         "ru": 'Пожалуйста, отправьте через кнопку "📞 Отправить телефон".',
#     },
#     "not_address": {
#         "uz": 'Iltimos, "📍 Lokatsiya yuborish" tugmasi orqali yuboring',
#         "ru": 'Пожалуйста, отправьте через кнопку "📍 Отправить локацию".',
#     },
#     "settings": {"uz": "Nimani o'zgartirmoqchisiz?", "ru": "Что вы хотите изменить?"},
#     "choose_lang": {"uz": "Tilni tanlang:", "ru": "Выберите язык:"},
#     "change_phone": {
#         "uz": "Telefon raqamingizni yuboring\nNamuna: +998712002666",
#         "ru": "Отправьте свой номер телефона\nОбразец: +998712002666",
#     },
#     "success_lang": {
#         "uz": "✅ Til muvaffaqiyatli o'zgartirildi",
#         "ru": "✅ Язык успешно изменён",
#     },
#     "success_phone": {
#         "uz": "✅ Telefon raqami muvaffaqiyatli o'zgartirildi",
#         "ru": "✅ Номер телефона успешно изменён",
#     },
#     "auth": {
#         "uz": "<b>Siz botdan foydalanish uchun ro'yxatdan o'tishingiz kerak yoki oldin ro'yxatdan o'tgan bo'lsangiz, eski hisobingizga kirishingiz mumkin!</b>\n\n"
#               "Ro'yxatdan o'tish uchun sizga kerak bo'ladigan ma'lumotlar:\n"
#               "1. To'liq ism-familiya\n"
#               "2. Telefon raqam\n"
#               "3. Passport yoki ID karta rasmi\n"
#               "4. Yetkazib berish uchun O'zbekistondagi manzilingiz\n\n"
#               "Agar sizda yuqoridagi ma'lumotlar tayyor bo'lsa, quyidagi tugmani bosing!",
#         "ru": "<b>Вы должны зарегистрироваться, чтобы использовать бота, или вы можете войти в свою старую учетную запись, если вы уже зарегистрированы!</b>\n\n"
#               "Информация, которая вам потребуется для регистрации:\n"
#               "1. Полное имя-фамилия\n"
#               "2. Номер телефона\n"
#               "3. Фотография паспорта или ID карты\n"
#               "4. Ваш адрес в Узбекистане для доставки\n\n"
#               "Если у вас есть готовая вышеуказанная информация, нажмите кнопку ниже!",
#     },
#     "select_myid": {
#         "uz": "🆔 Sizning ID kodingiz <b>{0}</b>\n\n<em>❗️ Bu ID koddan buyurtma qilish jarayonida foydalanasiz.</em>",
#         "ru": "🆔 Ваш ID код <b>{0}</b>\n\n<em>❗️ Вы будете использовать этот ID код в процессе оформления заказа.</em>",
#     },
#     "leave_comment": {
#         "uz": "Fikrlaringizni yozib qoldiring",
#         "ru": "Оставляйте свои комментарии",
#     },
#     "success_comment": {
#         "uz": "✅ Xabaringiz adminga yetkazildi, tez orada sizga javob qaytariladi!",
#         "ru": "✅ Ваше сообщение передано администратору, мы свяжемся с вами в ближайшее время!",
#     },
#     "error_phone": {
#         "uz": "Bunday telefon raqami allaqachon mavjud. Boshqa telefon raqam bilan ro'yxatdan o'ting",
#         "ru": "Этот номер телефона уже существует. Зарегистрируйтесь с другим номером телефона",
#     },
#     "error_passport": {
#         "uz": "Pasportingizni rasm formatida yuboring",
#         "ru": "Отправьте ваш паспорт в формате изображения",
#     },
#     "error_image": {
#         "uz": "Suratingizni rasm formatida yuboring",
#         "ru": "Отправьте свое фото в формате изображения",
#     },
#     "login": {
#         "phone": {
#             "uz": "Telefon raqamingizni quyida berilgan namunadagi kabi kiriting: +998906651525",
#             "ru": "Введите свой номер телефона, как показано ниже: +998906651525",
#         },
#         "id_code": {"uz": "ID kodingizni kiriting", "ru": "Введите свой ID код"},
#         "error_phone": {
#             "uz": "Bu telefon raqamiga ega foydalanuvchi topilmadi. Roʻyxatdan oʻting yoki boshqa telefon raqami bilan qayta urinib koʻring",
#             "ru": "Пользователь с данным номером телефона не найден. Зарегистрируйтесь или повторите попытку с другим номером телефона",
#         },
#         "error_idcode": {
#             "uz": "Ushbu ID kodiga ega foydalanuvchi topilmadi. Qayta urinib ko'ring yoki ro'yxatdan o'ting",
#             "ru": "Пользователь с таким ID кодом не найден. Попробуйте еще раз или зарегистрируйтесь",
#         },
#     },
#     "register": {
#         "full_name": {
#             "uz": "Ism-familiyangizni to'liq kiriting:\nNamuna: BERDIQULOV DILSHOD VALI O'G'LI",
#             "ru": "Введите свое полное имя:\nПример: БЕРДИҚУЛОВ ДИЛШОД ВАЛИ ЎҒЛИ",
#         },
#         "phone": {
#             "uz": "Murojaat uchun telefon raqamingizni yuboring",
#             "ru": "Отправьте свой номер телефона для связи",
#         },
#         'if_phone2': {
#             'uz': "Qo'shimcha telefon raqami kiritish:",
#             'ru': 'Ввести дополнительный номер телефона:'
#         },
#         'phone2': {
#             'uz': "Murojaat uchun qo'shimcha telefon raqamingizni kiriting\nNamuna: +998712002666",
#             'ru': 'Введите свой дополнительный номер телефона для связи\nОбразец: +998712002666'
#         },
#         "passport1": {
#             "uz": "To'liq ro'yxatdan o'tish uchun passportingizning rasmini jo'natishingiz kerak.\n\nPassport "
#                   "yoki ID kartangizning old tomonini namunadagi kabi rasmga olib jo'nating\n\n⚠ E'tiborli bo'ling, "
#                   "boshqa kargoga berilgan passportni jo'natmang, aks holda yuklaringiz kelmay qolishi mumkin",
#             "ru": "Для полноценной регистрации необходимо отправить фото паспорта.\n\nОтправьте фотографию лицевой "
#                   "стороны своего паспорта или ID карта, как показано в примере\n\n⚠️ Будьте внимательны, не "
#                   "отправляйте выданный паспорт на другой груз, иначе ваш товар может не прийти",
#         },
#         "passport2": {
#             "uz": "Passport yoki ID kartangizning orqa tomonini namunadagi kabi rasmga olib jo'nating",
#             "ru": "Отправьте фотографию обратной стороны своего паспорта или ID карта, как показано в примере",
#         },
#         "image": {
#             "uz": "Shaxsingizni tasdiqlash uchun rasmingizni jo'nating.",
#             "ru": "Отправьте свое фото, чтобы подтвердить свою личность.",
#         },
#         "address": {
#             "uz": "O'zbekistonga kelgan pochtalaringizni yetkazish uchun doim yashaydigan manzilingizni yuboring",
#             "ru": "Для доставки почты в Узбекистан отправьте свой постоянный адрес",
#         },
#         "manzil": {
#             "uz": "Xitoydan yetkazib berish turini tanlang",
#             "ru": "Выберите тип доставки из Китая",
#         },
#     },
#     'address_description': {
#         'uz': 'Manzil turini tanlang',
#         'ru': 'Выберите тип адреса'
#     }
# }

# btn_lang = {
#     "send_phone": {"uz": "📞 Telefon yuborish", "ru": "📞 Отправить телефон"},
#     "send_location": {"uz": "📍 Lokatsiya yuborish", "ru": "📍 Отправить локацию"},
#     "choose_manzil": {"uz": "🟢 Tanlash", "ru": "🟢 Выбрать"},
#     "register": {"uz": "®️ Ro'yxatdan o'tish", "ru": "®️ Регистрация"},
#     "login": {"uz": "📥 Kirish", "ru": "📥 Войти"},
#     "main_menu": {
#         "trek_code": {"uz": "🔎 Trek kodini tekshirish", "ru": "🔎 Проверка трек-кода"},
#         "admin_panel": {"uz": "↩ Adminkaga kirish", "ru": "↩ Войти в админку"},
#         "admin_send_message": {"uz": "📨 Xabar yuborish", "ru": "📨 Отправить сообщение"},
#         "my_bill": {"uz": "💰 Mening hisobim", "ru": "💰 Мой счет"},
#         "settings": {"uz": "⚙️ Sozlamalar", "ru": "⚙️ Настройки"},
#         "buy_yuan": {"uz": "💳 Yuan sotib olish", "ru": "💳 Купить юань"},
#         "my_id": {"uz": "🆔 Mening ID kodim", "ru": "🆔 Мой ID код"},
#         "get_address": {"uz": "🎫 Manzil olish", "ru": "🎫 Получить адрес"},
#         "comments": {"uz": "💬 Izohlar", "ru": "💬 Комментарии"},
#     },
#     "settings": {
#         "lang": {"uz": "Tilni", "ru": "Язык"},
#         "phone": {"uz": "Telefon raqamini", "ru": "Номер телефона"},
#     },
#     "cancel": {"uz": "Bekor qilish", "ru": "Отмена"},
#     "himself": {"uz": "Borib olish", "ru": "Забрать самому"},
#     "deliver": {"uz": "Yetkazib berish (dostavka)", "ru": "Доставить"},
#     'phone_number2_yes': {
#         'uz': '✅ Ha',
#         'ru': '✅ Да'
#     },
#     'phone_number2_no': {
#         'uz': "❌ Yo'q",
#         'ru': '❌ Нет'
#     },
#     'buy_yuan': {
#         'uz': '💳 Yuan sotib olish',
#         'ru': '💳 Купить юань'
#     },
#     'address_type': {
#         'avia': {
#             'uz': 'AVIA',
#             'ru': 'АВИА'
#         },
#         'avto': {
#             'uz': 'Avto',
#             'ru': 'АВТО'
#         }
#     }
# }


# address_options = list(Database().select_address_options())[0]
# period_avia = address_options['period_avia']
# period_avto = address_options['period_avto']
# phone_number = address_options['phone_number']
# mail_address = address_options['mail_address']
# address = address_options['address']


# allows = {
#     0: {
#         'uz': "<b>GIYOHVAND MODDALARGA O'XSHASH MAHSULOTLAR:</b>\n    kimyoviy moddalar, psixatrob\n\n"
#               "<b>MEDITSINAGA TEGISHLI:</b>\n    meditsina mahsulotlari, dorilar\n\n"
#               "<b>TEXNIKA:</b>\n    katta kuchli batareykalar\n\n"
#               "<b>BOSHQALAR:</b>\n    suyuq mahsulotlar",
#         'ru': "<b>НАРКОТИКОВЫЕ ВЕЩИ:</b>\n   химические вещества, психотропные\n\n"
#               "<b>МЕДИЦИНСКИЕ ВЕЩИ:</b>\n    медицинский продукт, препарат\n\n"
#               "<b>ТЕХНИКИ:</b>\n    большие мощные батареи\n\n"
#               "<b>ДРУГИЕ:</b>\n     жидкие продукты"
#     },
#     1: {
#         'uz': "<b>TEXNIKA:</b>\n   powerbank, batareyka, kartridj\n\n"
#               "<b>INTIM MAHSULOTLAR:</b>\n   intim o'yinchoq, intim gel\n\n"
#               "<b>O'SIMLIKLAR:</b>\n    xonaki gullar, urug'lar, ko'chatlar, tirik gullar\n\n"
#               "<b>KOSMETIKA MAHSULOTLARI:</b>\n     shampun, krem,  lak, kosmetika tovarlari, soch bo'yoqi, atir\n\n"
#               "<b>HAR KUNGI MAHSULOTLAR:</b>\n    Havo spreyi, oshxona va hammomni tozalash vositalari, kiyimlarni "
#               "tozalash vositalari. Gugurt, kapsulalarda kir yuvish kukuni, tish pastasi, yelim, avtomobil suyuqliklari, "
#               "oqar suvlarni tozalash mahsulotlari, kukunli mahsulotlar, markerlar, "
#               "suv tomchilari bo'lgan har qanday mahsulotlar, nam salfetka, zajigalka, lazer, linza\n\n"
#               "<b>MEDITSINAGA TEGISHLI:</b>\n    Tibbiy mahsulotlar, dorilar, stomatologik mahsulotlar, tishlarni oqartirish\n\n"
#               "<b>HARBIY MAHSULOTLAR VA QUROLLAR:</b>\n     elektroshoker va sovuq qurollar, uchi uchli kamon o'qlari, "
#               "pnevmatik miltiqlar va boshqa qurollar, barcha turdagi yog'och va temir buyumlar, harbiy buyumlar, "
#               "ratsiyalar, dronlar, pichoqlar\n\n"
#               "<b>OVQATLAR:</b>\n     Oziq-ovqat mahsulotlari, yarim tayyor ovqatlar\n\n"
#               "<b>BOSHQALAR:</b>\n     Qimmat baho metallar, migalka va sirenalar, massaj moyi",
#         'ru': "<b>ТЕХНИКИ:</b>\n    повербанк  батарейка, катридж\n\n"
#               "<b>ИНТИМНЫЕ ТОВАРЫ:</b>\n    интим игрушка, интим гель\n\n"
#               "<b>РAСТЕНИЕ:</b>\n    комнатние растение, семена, растение, "
#               "живые цветы\n\n"
#               "<b>СРЕДСТВО УХОДA ЗA КРAСОТОЙ:</b>\n    шампунь, лак, крем, Косметикa, краскаски для волос, духи\n\n"
#               "<b>ЕЖЕДНЕВНЫЕ ВЕЩИ:</b>\n    Освежители воздуха, средства для чистки кухни и сантехники, средства для "
#               "чистки одежды. Спички запрещены, стиральный порошок в гелевых капсулах, зубная паста, клей, "
#               "автомобильные жидкости, средства для очистки сточных вод, порошковые средства. Маркеры запрещены, "
#               "любые продукты, на которых есть капли воды. влажная салфетка, зажигалка, лазер, линза\n\n"
#               "<b>ЛЕКАРСТВО:</b>\n   "
#               "Медицинские товары, лекарства, Стоматологические товары, отбеливание зубов\n\n"
#               "<b>ВОЕННЫЕ И ОРУЖЕЙНЫЕ ВЕЩИ:</b>\n   Электрошокеры и другое холодное оружие, Арбалеты, "
#               "Пневматические винтовки и другое оружие, Все виды деревянных и железных изделий, Товары военного "
#               "назначения, рации, дроны, ножи\n\n"
#               "<b>ПИТАНИЕ:</b>\n   Продукты питания, полуфабрикаты\n\n"
#               "<b>ДРУГИЕ:</b>\n    Драгоценные металлы, Мигалка и сирены, массажное масло"
#     },
#     2: {
#         'uz': "<b>GIYOHVAND MODDALARGA O'XSHASH MAHSULOTLAR:</b>\n    kimyoviy moddalar, psixatrob\n\n"
#               "<b>MEDITSINAGA TEGISHLI:</b>\n    meditsina mahsulotlari, dorilar",
#         'ru': "<b>НАРКОТИКОВЫЕ ВЕЩИ:</b>\n   химические вещества, психотропные\n\n"
#               "<b>МЕДИЦИНСКИЕ ВЕЩИ:</b>\n    медицинский продукт, препарат"
#     }
# }

# manzils = {
#     'avia': {
#         'uz': """
# Avia {period_avia} kun
# 电话：{phone_number}
# 邮编: {mail_address}
# 详细地址: {address} {phone_number} (AVIA{code})
# 收货人： (AVIA{code})
#         """,
#         'ru': """
# Aвиа Экспресс {period_avia} дней
# 电话：{phone_number}
# 邮编: {mail_address}
# 详细地址: {address} {phone_number} (АВИА{code})
# 收货人： (АВИА{code})
#         """,
#     },
#     'avto': {
#
#         'uz': """
# Avto Caro {period_avto}  kun
# 邮编: {mail_address}
# 详细地址: {address} (АВТО{code})
# 收货人：АВТО({code})
# 联系方式 {phone_number}
#         """,
#         'ru': """
# Авто Каро {period_avto} день
# 邮编: {mail_address}
# 详细地址: {address} (AVTO{code})
# 收货人：AVTO({code})
# 联系方式 {phone_number}
#         """
#     }
# }

msg_lang = {
    "shopping_end": {
        "uz": "✅ Buyurtmangiz ko‘rib chiqish uchun adminlarga yuborildi. 24 soat ichida siz bilan bog'lanamiz.",
        "ru": "✅ Ваш заказ отправлен админам на рассмотрение. Мы с вами свяжемся в течении сутки.",
        "en": "✅ Your order has been sent to the admins for review. We will contact you within 24 hours.",
        "zh": "✅ 您的订单已发送给管理员审核。我们将在24小时内与您联系。"
    },
    "shopping_image_err": {
        "uz": "🚫 Skrinshot yuborishingiz kerak!",
        "ru": "🚫 Необходимо отправить скриншот!",
        "en": "🚫 You need to send a screenshot!",
        "zh": "🚫 您需要发送截图！"
    },
    "shopping_link": {
        "uz": "🔗 Buyurtma bermoqchi bo'lgan tovaringizni havolasini yuboring",
        "ru": "🔗 Отправьте ссылку на товар, который хотите заказать",
        "en": "🔗 Send the link to the product you want to order",
        "zh": "🔗 发送您想订购的商品链接"
    },
    "shopping_image": {
        "uz": "🖼 Razmer, rang va shunga o'xshash parametrlarni tanlagan xolda skrin qilib tashlang",
        "ru": "🖼 Сделайте скриншот с выбранным вами размером, цветом и подобными параметрами.",
        "en": "🖼 Take a screenshot with the selected size, color, and similar parameters.",
        "zh": "🖼 截图选择的尺寸、颜色及类似参数。"
    },
    "main_menu": {
        "uz": "Asosiy menyu",
        "ru": "Главное меню",
        "en": "Main menu",
        "zh": "主菜单"
    },
    "trek_code": {
        "uz": "Trek kodni kiriting",
        "ru": "Введите код трека",
        "en": "Enter the tracking code",
        "zh": "输入追踪码"
    },
    "no_trek_code": {
        "uz": "🚫 Sizda bunday trek kodga ega buyurtma mavjud emas!",
        "ru": "🚫 У вас нет заказа с этим трек кодом!",
        "en": "🚫 You don’t have an order with this tracking code!",
        "zh": "🚫 您没有此追踪码的订单！"
    },
    "taken": {
        "uz": "Buyurtmangizni allaqachon olgansiz❗️",
        "ru": "Вы уже получили свой заказ❗️",
        "en": "You have already received your order! ❗️",
        "zh": "您已经收到您的订单！❗️"
    },
    "deliver_or_not": {
        "uz": "Buyurtmangiz O'zbekistonga yetib kelgan.\nBuyurtmani qo'lga kriitish turini tanlang:",
        "ru": "Ваш заказ прибыл в Узбекистан.\nВыберите тип получения заказа:",
        "en": "Your order has arrived in Uzbekistan.\nChoose the delivery method:",
        "zh": "您的订单已到达乌兹别克斯坦。\n选择接收订单的方式："
    },
    "not_arrived": {
        "uz": "Buyurtmangiz hali O'zbekistonga yetib kelmadi. Buyurtmangiz yo'lda.",
        "ru": "Ваш заказ еще не прибыл в Узбекистан. Ваш заказ в пути.",
        "en": "Your order has not yet arrived in Uzbekistan. It is on the way.",
        "zh": "您的订单尚未到达乌兹别克斯坦。正在途中。"
    },
    'buy_yuan': {
        'uz': f"💳 Yuan sotib olish uchun ushbu botimizdan foydalanishingiz mumkin: @{YUAN_BOT.split('/')[-1]}",
        'ru': f'💳 Вы можете использовать нашего бота для покупки юаней: @{YUAN_BOT.split("/")[-1]}',
        'en': f"💳 You can use our bot to buy yuan: @{YUAN_BOT.split('/')[-1]}",
        'zh': f"💳 您可以使用我们的机器人购买人民币：@{YUAN_BOT.split('/')[-1]}"
    },
    'greeting': {
        'uz': "Salom {0}! Rasmiy FAD Cargo botiga xush kelibsiz - Xitoydan yetkazib berish!",
        'ru': "Привет, {0}! Добро пожаловать в официальный бот FAD Cargo - Доставка из Китая!",
        'en': "Hello {0}! Welcome to the official FAD Cargo bot - Delivery from China!",
        'zh': "您好 {0}！欢迎使用官方 FAD Cargo 机器人 - 从中国运送！"
    },
    'allow': {
        'uz': "Bu yetkazib berish turidan nimalarni buyurtma qila olmaysiz:",
        'ru': 'Что нельзя заказать в этом виде доставки:',
        'en': "What you cannot order with this delivery type:",
        'zh': "这种配送方式不能订购的内容："
    },
    "deliver": {
        "uz": "Buyurtmani jo'natish uchun lokatsiyangizni yuboring 🔽",
        "ru": "Отправьте свою локацию чтобы получить заказ 🔽",
        "en": "Send your location to ship the order 🔽",
        "zh": "发送您的位置以运送订单 🔽"
    },
    "success_deliver": {
        "uz": "Manzil qabul qilindi ✅\nTez orada buyurtmangiz manzilga yetkaziladi)",
        "ru": "Адрес получен ✅\nВаш заказ будет доставлен в ближайшее время)",
        "en": "Address received ✅\nYour order will be delivered soon)",
        "zh": "地址已接收 ✅\n您的订单将很快送达)"
    },
    "bring_deliver": {
        "uz": "Ushbu manzilga kelib, buyurtmangizni olib ketishingiz mumkin.",
        "ru": "Вы можете прийти по этому адресу и забрать свой заказ.",
        "en": "You can come to this address and pick up your order.",
        "zh": "您可以到这个地址领取您的订单。"
    },
    "phone_number_checking": {
        "all_exc": {
            "uz": 'Telefon raqami "+" belgisi bilan boshlanishi va 12 ta raqamdan iborat bo\'lishi kerak.',
            "ru": 'Номер телефона должен начинаться с "+" и содержать 12 цифр.',
            "en": 'The phone number must start with "+" and consist of 12 digits.',
            "zh": '电话号码必须以“+”开头，并包含12位数字。'
        },
        "with_plus": {
            "uz": 'Telefon raqami "+" belgisi bilan boshlanishi kerak',
            "ru": 'Номер телефона должен начинаться со знака "+".',
            "en": 'The phone number must start with the "+" sign.',
            "zh": '电话号码必须以“+”符号开头。'
        },
        "with_998": {
            "uz": "Telefon raqami O‘zbekiston Respublikasiga tegishli bo‘lishi kerak",
            "ru": "Номер телефона должен принадлежать Республики Узбекистан",
            "en": "The phone number must belong to the Republic of Uzbekistan",
            "zh": "电话号码必须属于乌兹别克斯坦共和国"
        },
        "with_num": {
            "uz": 'Telefon raqamida "+" dan boshqa belgilar yoki harflar bo\'lmasligi kerak',
            "ru": 'Номер телефона не должен содержать буквы или знаки кроме "+"',
            "en": 'The phone number must not contain letters or symbols other than "+".',
            "zh": '电话号码不得包含除“+”外的字母或符号。'
        },
        "example": {
            "uz": "Масалан: +998001234567",
            "ru": "Например: +998001234567",
            "en": "For example: +998001234567",
            "zh": "例如：+998001234567"
        },
    },
    "not_phone": {
        "uz": 'Iltimos, "📞 Telefon yuborish" tugmasi orqali yuboring',
        "ru": 'Пожалуйста, отправьте через кнопку "📞 Отправить телефон".',
        "en": 'Please send it via the "📞 Send phone" button.',
        "zh": '请通过“📞 发送电话”按钮发送。'
    },
    "not_address": {
        "uz": 'Iltimos, "📍 Lokatsiya yuborish" tugmasi orqali yuboring',
        "ru": 'Пожалуйста, отправьте через кнопку "📍 Отправить локацию".',
        "en": 'Please send it via the "📍 Send location" button.',
        "zh": '请通过“📍 发送位置”按钮发送。'
    },
    "settings": {
        "uz": "Nimani o'zgartirmoqchisiz?",
        "ru": "Что вы хотите изменить?",
        "en": "What do you want to change?",
        "zh": "您想更改什么？"
    },
    "choose_lang": {
        "uz": "Tilni tanlang:",
        "ru": "Выберите язык:",
        "en": "Choose a language:",
        "zh": "选择语言："
    },
    "change_phone": {
        "uz": "Telefon raqamingizni yuboring\nNamuna: +998712002666",
        "ru": "Отправьте свой номер телефона\nОбразец: +998712002666",
        "en": "Send your phone number\nExample: +998712002666",
        "zh": "发送您的电话号码\n示例：+998712002666"
    },
    "success_lang": {
        "uz": "✅ Til muvaffaqiyatli o'zgartirildi",
        "ru": "✅ Язык успешно изменён",
        "en": "✅ Language successfully changed",
        "zh": "✅ 语言已成功更改"
    },
    "success_phone": {
        "uz": "✅ Telefon raqami muvaffaqiyatli o'zgartirildi",
        "ru": "✅ Номер телефона успешно изменён",
        "en": "✅ Phone number successfully changed",
        "zh": "✅ 电话号码已成功更改"
    },
    "auth": {
        "uz": "<b>Siz botdan foydalanish uchun ro'yxatdan o'tishingiz kerak yoki oldin ro'yxatdan o'tgan bo'lsangiz, eski hisobingizga kirishingiz mumkin!</b>\n\n"
              "Ro'yxatdan o'tish uchun sizga kerak bo'ladigan ma'lumotlar:\n"
              "1. To'liq ism-familiya\n"
              "2. Telefon raqam\n"
              "3. Passport yoki ID karta rasmi\n"
              "4. Yetkazib berish uchun O'zbekistondagi manzilingiz\n\n"
              "Agar sizda yuqoridagi ma'lumotlar tayyor bo'lsa, quyidagi tugmani bosing!",
        "ru": "<b>Вы должны зарегистрироваться, чтобы использовать бота, или вы можете войти в свою старую учетную запись, если вы уже зарегистрированы!</b>\n\n"
              "Информация, которая вам потребуется для регистрации:\n"
              "1. Полное имя-фамилия\n"
              "2. Номер телефона\n"
              "3. Фотография паспорта или ID карты\n"
              "4. Ваш адрес в Узбекистане для доставки\n\n"
              "Если у вас есть готовая вышеуказанная информация, нажмите кнопку ниже!",
        "en": "<b>You must register to use the bot, or you can log in to your old account if you are already registered!</b>\n\n"
              "Information required for registration:\n"
              "1. Full name\n"
              "2. Phone number\n"
              "3. Photo of your passport or ID card\n"
              "4. Your address in Uzbekistan for delivery\n\n"
              "If you have the above information ready, press the button below!",
        "zh": "<b>您必须注册才能使用此机器人，或者如果您已经注册，可以登录到您的旧账户！</b>\n\n"
              "注册所需信息：\n"
              "1. 全名\n"
              "2. 电话号码\n"
              "3. 护照或身份证照片\n"
              "4. 乌兹别克斯坦的送货地址\n\n"
              "如果您已准备好上述信息，请按下面的按钮！"
    },
    "select_myid": {
        "uz": "🆔 Sizning ID kodingiz <b>{0}</b>\n\n<em>❗️ Bu ID koddan buyurtma qilish jarayonida foydalanasiz.</em>",
        "ru": "🆔 Ваш ID код <b>{0}</b>\n\n<em>❗️ Вы будете использовать этот ID код в процессе оформления заказа.</em>",
        "en": "🆔 Your ID code is <b>{0}</b>\n\n<em>❗️ You will use this ID code during the ordering process.</em>",
        "zh": "🆔 您的ID代码是 <b>{0}</b>\n\n<em>❗️ 您将在订购过程中使用此ID代码。</em>"
    },
    "leave_comment": {
        "uz": "Fikrlaringizni yozib qoldiring",
        "ru": "Оставляйте свои комментарии",
        "en": "Leave your comments",
        "zh": "留下您的评论"
    },
    "success_comment": {
        "uz": "✅ Xabaringiz adminga yetkazildi, tez orada sizga javob qaytariladi!",
        "ru": "✅ Ваше сообщение передано администратору, мы свяжемся с вами в ближайшее время!",
        "en": "✅ Your message has been sent to the admin, we will reply to you soon!",
        "zh": "✅ 您的消息已发送给管理员，我们将很快回复您！"
    },
    "error_phone": {
        "uz": "Bunday telefon raqami allaqachon mavjud. Boshqa telefon raqam bilan ro'yxatdan o'ting",
        "ru": "Этот номер телефона уже существует. Зарегистрируйтесь с другим номером телефона",
        "en": "This phone number already exists. Register with a different phone number",
        "zh": "此电话号码已存在。请使用其他电话号码注册"
    },
    "error_passport": {
        "uz": "Pasportingizni rasm formatida yuboring",
        "ru": "Отправьте ваш паспорт в формате изображения",
        "en": "Send your passport in image format",
        "zh": "以图片格式发送您的护照"
    },
    "error_image": {
        "uz": "Suratingizni rasm formatida yuboring",
        "ru": "Отправьте свое фото в формате изображения",
        "en": "Send your photo in image format",
        "zh": "以图片格式发送您的照片"
    },
    "login": {
        "phone": {
            "uz": "Telefon raqamingizni quyida berilgan namunadagi kabi kiriting: +998906651525",
            "ru": "Введите свой номер телефона, как показано ниже: +998906651525",
            "en": "Enter your phone number as shown below: +998906651525",
            "zh": "按以下所示输入您的电话号码：+998906651525"
        },
        "id_code": {
            "uz": "ID kodingizni kiriting",
            "ru": "Введите свой ID код",
            "en": "Enter your ID code",
            "zh": "输入您的ID代码"
        },
        "error_phone": {
            "uz": "Bu telefon raqamiga ega foydalanuvchi topilmadi. Roʻyxatdan oʻting yoki boshqa telefon raqami bilan qayta urinib koʻring",
            "ru": "Пользователь с данным номером телефона не найден. Зарегистрируйтесь или повторите попытку с другим номером телефона",
            "en": "No user with this phone number was found. Register or try again with a different phone number",
            "zh": "未找到使用此电话号码的用户。请注册或使用其他电话号码重试"
        },
        "error_idcode": {
            "uz": "Ushbu ID kodiga ega foydalanuvchi topilmadi. Qayta urinib ko'ring yoki ro'yxatdan o'ting",
            "ru": "Пользователь с таким ID кодом не найден. Попробуйте еще раз или зарегистрируйтесь",
            "en": "No user with this ID code was found. Try again or register",
            "zh": "未找到使用此ID代码的用户。请重试或注册"
        },
    },
    "register": {
        "full_name": {
            "uz": "Ism-familiyangizni to'liq kiriting:\nNamuna: BERDIQULOV DILSHOD VALI O'G'LI",
            "ru": "Введите свое полное имя:\nПример: БЕРДИҚУЛОВ ДИЛШОД ВАЛИ ЎҒЛИ",
            "en": "Enter your full name:\nExample: BERDIQULOV DILSHOD VALI O'G'LI",
            "zh": "输入您的全名：\n示例：BERDIQULOV DILSHOD VALI O'G'LI"
        },
        "phone": {
            "uz": "Murojaat uchun telefon raqamingizni yuboring",
            "ru": "Отправьте свой номер телефона для связи",
            "en": "Send your phone number for contact",
            "zh": "发送您的联系电话号码"
        },
        'if_phone2': {
            'uz': "Qo'shimcha telefon raqami kiritish:",
            'ru': 'Ввести дополнительный номер телефона:',
            'en': "Enter an additional phone number:",
            'zh': "输入额外的电话号码："
        },
        'phone2': {
            'uz': "Murojaat uchun qo'shimcha telefon raqamingizni kiriting\nNamuna: +998712002666",
            'ru': 'Введите свой дополнительный номер телефона для связи\nОбразец: +998712002666',
            'en': "Enter your additional phone number for contact\nExample: +998712002666",
            'zh': "输入您的额外联系电话号码\n示例：+998712002666"
        },
        "passport1": {
            "uz": "To'liq ro'yxatdan o'tish uchun passportingizning rasmini jo'natishingiz kerak.\n\nPassport "
                  "yoki ID kartangizning old tomonini namunadagi kabi rasmga olib jo'nating\n\n⚠ E'tiborli bo'ling, "
                  "boshqa kargoga berilgan passportni jo'natmang, aks holda yuklaringiz kelmay qolishi mumkin",
            "ru": "Для полноценной регистрации необходимо отправить фото паспорта.\n\nОтправьте фотографию лицевой "
                  "стороны своего паспорта или ID карта, как показано в примере\n\n⚠️ Будьте внимательны, не "
                  "отправляйте выданный паспорт на другой груз, иначе ваш товар может не прийти",
            "en": "To fully register, you need to send a photo of your passport.\n\nTake a photo of the front side "
                  "of your passport or ID card as shown in the example and send it\n\n⚠ Be careful not to send a "
                  "passport issued for another cargo, otherwise your goods may not arrive",
            "zh": "要完成注册，您需要发送护照照片。\n\n按照示例拍摄您的护照或身份证正面并发送\n\n⚠ 请注意，不要发送用于其他货物的护照，否则您的货物可能无法到达"
        },
        "passport2": {
            "uz": "Passport yoki ID kartangizning orqa tomonini namunadagi kabi rasmga olib jo'nating",
            "ru": "Отправьте фотографию обратной стороны своего паспорта или ID карта, как показано в примере",
            "en": "Take a photo of the back side of your passport or ID card as shown in the example and send it",
            "zh": "按照示例拍摄您的护照或身份证背面并发送"
        },
        "image": {
            "uz": "Shaxsingizni tasdiqlash uchun rasmingizni jo'nating.",
            "ru": "Отправьте свое фото, чтобы подтвердить свою личность.",
            "en": "Send your photo to verify your identity.",
            "zh": "发送您的照片以验证您的身份。"
        },
        "address": {
            "uz": "O'zbekistonga kelgan pochtalaringizni yetkazish uchun doim yashaydigan manzilingizni yuboring",
            "ru": "Для доставки почты в Узбекистан отправьте свой постоянный адрес",
            "en": "Send your permanent address for delivering mail arriving in Uzbekistan",
            "zh": "发送您的永久地址，以便将到达乌兹别克斯坦的邮件送达"
        },
        "manzil": {
            "uz": "Xitoydan yetkazib berish turini tanlang",
            "ru": "Выберите тип доставки из Китая",
            "en": "Choose the delivery type from China",
            "zh": "选择从中国的配送类型"
        },
    },
    'address_description': {
        'uz': 'Manzil turini tanlang',
        'ru': 'Выберите тип адреса',
        'en': 'Choose the address type',
        'zh': '选择地址类型'
    }
}

btn_lang = {
    "send_phone": {
        "uz": "📞 Telefon yuborish",
        "ru": "📞 Отправить телефон",
        "en": "📞 Send phone",
        "zh": "📞 发送电话"
    },
    "send_location": {
        "uz": "📍 Lokatsiya yuborish",
        "ru": "📍 Отправить локацию",
        "en": "📍 Send location",
        "zh": "📍 发送位置"
    },
    "choose_manzil": {
        "uz": "🟢 Tanlash",
        "ru": "🟢 Выбрать",
        "en": "🟢 Choose",
        "zh": "🟢 选择"
    },
    "register": {
        "uz": "®️ Ro'yxatdan o'tish",
        "ru": "®️ Регистрация",
        "en": "®️ Register",
        "zh": "®️ 注册"
    },
    "login": {
        "uz": "📥 Kirish",
        "ru": "📥 Войти",
        "en": "📥 Log in",
        "zh": "📥 登录"
    },
    "main_menu": {
        "trek_code": {
            "uz": "🔎 Trek kodini tekshirish",
            "ru": "🔎 Проверка трек-кода",
            "en": "🔎 Check tracking code",
            "zh": "🔎 检查追踪码"
        },
        "admin_panel": {
            "uz": "↩ Adminkaga kirish",
            "ru": "↩ Войти в админку",
            "en": "↩ Enter admin panel",
            "zh": "↩ 进入管理面板"
        },
        "admin_send_message": {
            "uz": "📨 Xabar yuborish",
            "ru": "📨 Отправить сообщение",
            "en": "📨 Send message",
            "zh": "📨 发送消息"
        },
        "my_bill": {
            "uz": "💰 Mening hisobim",
            "ru": "💰 Мой счет",
            "en": "💰 My account",
            "zh": "💰 我的账户"
        },
        "settings": {
            "uz": "⚙️ Sozlamalar",
            "ru": "⚙️ Настройки",
            "en": "⚙️ Settings",
            "zh": "⚙️ 设置"
        },
        "buy_yuan": {
            "uz": "💳 Yuan sotib olish",
            "ru": "💳 Купить юань",
            "en": "💳 Buy yuan",
            "zh": "💳 购买人民币"
        },
        "shopping": {
            "uz": "🛍 Xarid qilish",
            "ru": "🛍 Покупать",
            "en": "🛍 Shopping",
            "zh": "🛍 购物"
        },
        "my_id": {
            "uz": "🆔 Mening ID kodim",
            "ru": "🆔 Мой ID код",
            "en": "🆔 My ID code",
            "zh": "🆔 我的ID代码"
        },
        "get_address": {
            "uz": "🎫 Manzil olish",
            "ru": "🎫 Получить адрес",
            "en": "🎫 Get address",
            "zh": "🎫 获取地址"
        },
        "comments": {
            "uz": "💬 Izohlar",
            "ru": "💬 Комментарии",
            "en": "💬 Comments",
            "zh": "💬 评论"
        },
    },
    "settings": {
        "lang": {
            "uz": "Tilni",
            "ru": "Язык",
            "en": "Language",
            "zh": "语言"
        },
        "phone": {
            "uz": "Telefon raqamini",
            "ru": "Номер телефона",
            "en": "Phone number",
            "zh": "电话号码"
        },
    },
    "cancel": {
        "uz": "Bekor qilish",
        "ru": "Отмена",
        "en": "Cancel",
        "zh": "取消"
    },
    "himself": {
        "uz": "Borib olish",
        "ru": "Забрать самому",
        "en": "Pick up myself",
        "zh": "自己领取"
    },
    "deliver": {
        "uz": "Yetkazib berish (dostavka)",
        "ru": "Доставить",
        "en": "Deliver",
        "zh": "配送"
    },
    'phone_number2_yes': {
        'uz': '✅ Ha',
        'ru': '✅ Да',
        'en': '✅ Yes',
        'zh': '✅ 是'
    },
    'phone_number2_no': {
        'uz': "❌ Yo'q",
        'ru': '❌ Нет',
        'en': '❌ No',
        'zh': '❌ 否'
    },
    'buy_yuan': {
        'uz': '💳 Yuan sotib olish',
        'ru': '💳 Купить юань',
        'en': '💳 Buy yuan',
        'zh': '💳 购买人民币'
    },
    'address_type': {
        'avia': {
            'uz': 'AVIA',
            'ru': 'АВИА',
            'en': 'AVIA',
            'zh': '航空'
        },
        'avto': {
            'uz': 'Avto',
            'ru': 'АВТО',
            'en': 'Auto',
            'zh': '汽车'
        }
    }
}

manzils = {
    'avia': {
        'uz': """
Avia {period_avia} kun 
电话：{phone_number}                                       
邮编: {mail_address} 
详细地址: {address} {phone_number} (AVIA{code})  
收货人： (AVIA{code})
        """,
        'ru': """
Aвиа Экспресс {period_avia} дней
电话：{phone_number}                                       
邮编: {mail_address} 
详细地址: {address} {phone_number} (АВИА{code})  
收货人： (АВИА{code})
        """,
        'en': """
Avia Express {period_avia} days
Phone: {phone_number}                                       
Postal code: {mail_address} 
Detailed address: {address} {phone_number} (AVIA{code})  
Recipient: (AVIA{code})
        """,
        'zh': """
航空快递 {period_avia} 天
电话：{phone_number}                                       
邮编: {mail_address} 
详细地址: {address} {phone_number} (航空{code})  
收货人：(航空{code})
        """
    },
    'avto': {
        'uz': """
Avto Caro {period_avto}  kun
邮编: {mail_address} 
详细地址: {address} (АВТО{code})
收货人：АВТО({code})
联系方式 {phone_number}
        """,
        'ru': """
Авто Каро {period_avto} день
邮编: {mail_address}
详细地址: {address} (AVTO{code})
收货人：AVTO({code})
联系方式 {phone_number}
        """,
        'en': """
Auto Caro {period_avto} days
Postal code: {mail_address} 
Detailed address: {address} (AUTO{code})
Recipient: AUTO({code})
Contact: {phone_number}
        """,
        'zh': """
汽车卡罗 {period_avto} 天
邮编: {mail_address} 
详细地址: {address} (汽车{code})
收货人：汽车({code})
联系方式：{phone_number}
        """
    }
}
