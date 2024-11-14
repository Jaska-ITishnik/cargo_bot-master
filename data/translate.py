from data.config import YUAN_BOT

msg_lang = {
    "shopping_end": {
        "uz": "✅ Buyurtmangiz ko‘rib chiqish uchun adminlarga yuborildi. 24 soat ichida siz bilan bog'lanamiz.",
        "ru": "✅ Ваш заказ отправлен админам на рассмотрение. Мы с вами свяжемся в течении сутки."
    },
    "shopping_image_err": {
        "uz": "🚫 Skrinshot yuborishingiz kerak!",
        "ru": "🚫 Необходимо отправить скриншот!",
    },
    "shopping_link": {
        "uz": "🔗 Buyurtma bermoqchi bo'lgan tovaringizni havolasini yuboring",
        "ru": "🔗 Отправьте ссылку на товар, который хотите заказать",
    },
    "shopping_image": {
        "uz": "🖼 Razmer, rang va shunga o'xshash parametrlarni tanlagan xolda skrin qilib tashlang",
        "ru": "🖼 Сделайте скриншот с выбранным вами размером, цветом и подобными параметрами.",
    },
    "main_menu": {"uz": "Asosiy menyu", "ru": "Главное меню"},
    "trek_code": {"uz": "Trek kodni kiriting", "ru": "Введите код трека"},
    "no_trek_code": {
        "uz": "🚫 Sizda bunday trek kodga ega buyurtma mavjud emas!",
        "ru": "🚫 У вас нет заказа с этим трек кодом!",
    },
    "taken": {
        "uz": "Buyurtmangizni allaqachon olgansiz❗️",
        "ru": "Вы уже получили свой заказ❗️",
    },
    "deliver_or_not": {
        "uz": "Buyurtmangiz O'zbekistonga yetib kelgan.\nBuyurtmani qo'lga kriitish turini tanlang:",
        "ru": "Ваш заказ прибыл в Узбекистан.\nВыберите тип получения заказа:",
    },
    "not_arrived": {
        "uz": "Buyurtmangiz hali O'zbekistonga yetib kelmadi. Buyurtmangiz yo'lda.",
        "ru": "Ваш заказ еще не прибыл в Узбекистан. Ваш заказ в пути.",
    },
    'buy_yuan': {
        'uz': f"💳 Yuan sotib olish uchun ushbu botimizdan foydalanishingiz mumkin: @{YUAN_BOT.split('/')[-1]}",
        'ru': f'💳 Вы можете использовать нашего бота для покупки юаней: @{YUAN_BOT.split("/")[-1]}'
    },
    'greeting': {
        'uz': "Salom {0}! Rasmiy FAD Cargo botiga xush kelibsiz - Xitoydan yetkazib berish!",
        'ru': "Привет, {0}! Добро пожаловать в официальный бот FAD Cargo - Доставка из Китая!"
    },
    'allow': {
        'uz': "Bu yetkazib berish turidan nimalarni buyurtma qila olmaysiz:",
        'ru': 'Что нельзя заказать в этом виде доставки:'
    },
    "deliver": {
        "uz": "Buyurtmani jo'natish uchun lokatsiyangizni yuboring 🔽",
        "ru": "Отправьте свою локацию чтобы получить заказ 🔽",
    },
    "success_deliver": {
        "uz": "Manzil qabul qilindi ✅\nTez orada buyurtmangiz manzilga yetkaziladi)",
        "ru": "Адрес получен ✅\nВаш заказ будет доставлен в ближайшее время)",
    },
    "bring_deliver": {
        "uz": "Ushbu manzilga kelib, buyurtmangizni olib ketishingiz mumkin.",
        "ru": "Вы можете прийти по этому адресу и забрать свой заказ.",
    },
    "phone_number_checking": {
        "all_exc": {
            "uz": 'Telefon raqami "+" belgisi bilan boshlanishi va 12 ta raqamdan iborat bo\'lishi kerak.',
            "ru": 'Номер телефона должен начинаться с "+" и содержать 12 цифр.',
        },
        "with_plus": {
            "uz": 'Telefon raqami "+" belgisi bilan boshlanishi kerak',
            "ru": 'Номер телефона должен начинаться со знака "+".',
        },
        "with_998": {
            "uz": "Telefon raqami O‘zbekiston Respublikasiga tegishli bo‘lishi kerak",
            "ru": "Номер телефона должен принадлежать Республики Узбекистан",
        },
        "with_num": {
            "uz": 'Telefon raqamida "+" dan boshqa belgilar yoki harflar bo\'lmasligi kerak',
            "ru": 'Номер телефона не должен содержать буквы или знаки кроме "+"',
        },
        "example": {"uz": "Масалан: +998001234567", "ru": "Например: +998001234567"},
    },
    "not_phone": {
        "uz": 'Iltimos, "📞 Telefon yuborish" tugmasi orqali yuboring',
        "ru": 'Пожалуйста, отправьте через кнопку "📞 Отправить телефон".',
    },
    "not_address": {
        "uz": 'Iltimos, "📍 Lokatsiya yuborish" tugmasi orqali yuboring',
        "ru": 'Пожалуйста, отправьте через кнопку "📍 Отправить локацию".',
    },
    "settings": {"uz": "Nimani o'zgartirmoqchisiz?", "ru": "Что вы хотите изменить?"},
    "choose_lang": {"uz": "Tilni tanlang:", "ru": "Выберите язык:"},
    "change_phone": {
        "uz": "Telefon raqamingizni yuboring\nNamuna: +998712002666",
        "ru": "Отправьте свой номер телефона\nОбразец: +998712002666",
    },
    "success_lang": {
        "uz": "✅ Til muvaffaqiyatli o'zgartirildi",
        "ru": "✅ Язык успешно изменён",
    },
    "success_phone": {
        "uz": "✅ Telefon raqami muvaffaqiyatli o'zgartirildi",
        "ru": "✅ Номер телефона успешно изменён",
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
    },
    "select_myid": {
        "uz": "🆔 Sizning ID kodingiz <b>{0}</b>\n\n<em>❗️ Bu ID koddan buyurtma qilish jarayonida foydalanasiz.</em>",
        "ru": "🆔 Ваш ID код <b>{0}</b>\n\n<em>❗️ Вы будете использовать этот ID код в процессе оформления заказа.</em>",
    },
    "leave_comment": {
        "uz": "Fikrlaringizni yozib qoldiring",
        "ru": "Оставляйте свои комментарии",
    },
    "success_comment": {
        "uz": "✅ Xabaringiz adminga yetkazildi, tez orada sizga javob qaytariladi!",
        "ru": "✅ Ваше сообщение передано администратору, мы свяжемся с вами в ближайшее время!",
    },
    "error_phone": {
        "uz": "Bunday telefon raqami allaqachon mavjud. Boshqa telefon raqam bilan ro'yxatdan o'ting",
        "ru": "Этот номер телефона уже существует. Зарегистрируйтесь с другим номером телефона",
    },
    "error_passport": {
        "uz": "Pasportingizni rasm formatida yuboring",
        "ru": "Отправьте ваш паспорт в формате изображения",
    },
    "error_image": {
        "uz": "Suratingizni rasm formatida yuboring",
        "ru": "Отправьте свое фото в формате изображения",
    },
    "login": {
        "phone": {
            "uz": "Telefon raqamingizni quyida berilgan namunadagi kabi kiriting: +998906651525",
            "ru": "Введите свой номер телефона, как показано ниже: +998906651525",
        },
        "id_code": {"uz": "ID kodingizni kiriting", "ru": "Введите свой ID код"},
        "error_phone": {
            "uz": "Bu telefon raqamiga ega foydalanuvchi topilmadi. Roʻyxatdan oʻting yoki boshqa telefon raqami bilan qayta urinib koʻring",
            "ru": "Пользователь с данным номером телефона не найден. Зарегистрируйтесь или повторите попытку с другим номером телефона",
        },
        "error_idcode": {
            "uz": "Ushbu ID kodiga ega foydalanuvchi topilmadi. Qayta urinib ko'ring yoki ro'yxatdan o'ting",
            "ru": "Пользователь с таким ID кодом не найден. Попробуйте еще раз или зарегистрируйтесь",
        },
    },
    "register": {
        "full_name": {
            "uz": "Ism-familiyangizni to'liq kiriting:\nNamuna: BERDIQULOV DILSHOD VALI O'G'LI",
            "ru": "Введите свое полное имя:\nПример: БЕРДИҚУЛОВ ДИЛШОД ВАЛИ ЎҒЛИ",
        },
        "phone": {
            "uz": "Murojaat uchun telefon raqamingizni yuboring",
            "ru": "Отправьте свой номер телефона для связи",
        },
        'if_phone2': {
            'uz': "Qo'shimcha telefon raqami kiritish:",
            'ru': 'Ввести дополнительный номер телефона:'
        },
        'phone2': {
            'uz': "Murojaat uchun qo'shimcha telefon raqamingizni kiriting\nNamuna: +998712002666",
            'ru': 'Введите свой дополнительный номер телефона для связи\nОбразец: +998712002666'
        },
        "passport1": {
            "uz": "To'liq ro'yxatdan o'tish uchun passportingizning rasmini jo'natishingiz kerak.\n\nPassport "
                  "yoki ID kartangizning old tomonini namunadagi kabi rasmga olib jo'nating\n\n⚠ E'tiborli bo'ling, "
                  "boshqa kargoga berilgan passportni jo'natmang, aks holda yuklaringiz kelmay qolishi mumkin",
            "ru": "Для полноценной регистрации необходимо отправить фото паспорта.\n\nОтправьте фотографию лицевой "
                  "стороны своего паспорта или ID карта, как показано в примере\n\n⚠️ Будьте внимательны, не "
                  "отправляйте выданный паспорт на другой груз, иначе ваш товар может не прийти",
        },
        "passport2": {
            "uz": "Passport yoki ID kartangizning orqa tomonini namunadagi kabi rasmga olib jo'nating",
            "ru": "Отправьте фотографию обратной стороны своего паспорта или ID карта, как показано в примере",
        },
        "image": {
            "uz": "Shaxsingizni tasdiqlash uchun rasmingizni jo'nating.",
            "ru": "Отправьте свое фото, чтобы подтвердить свою личность.",
        },
        "address": {
            "uz": "O'zbekistonga kelgan pochtalaringizni yetkazish uchun doim yashaydigan manzilingizni yuboring",
            "ru": "Для доставки почты в Узбекистан отправьте свой постоянный адрес",
        },
        "manzil": {
            "uz": "Xitoydan yetkazib berish turini tanlang",
            "ru": "Выберите тип доставки из Китая",
        },
    },
}

btn_lang = {
    "send_phone": {"uz": "📞 Telefon yuborish", "ru": "📞 Отправить телефон"},
    "send_location": {"uz": "📍 Lokatsiya yuborish", "ru": "📍 Отправить локацию"},
    "choose_manzil": {"uz": "🟢 Tanlash", "ru": "🟢 Выбрать"},
    "register": {"uz": "®️ Ro'yxatdan o'tish", "ru": "®️ Регистрация"},
    "login": {"uz": "📥 Kirish", "ru": "📥 Войти"},
    "main_menu": {
        "trek_code": {"uz": "🔎 Trek kodini tekshirish", "ru": "🔎 Проверка трек-кода"},
        "admin_panel": {"uz": "↩ Adminkaga kirish", "ru": "↩ Войти в админку"},
        "my_bill": {"uz": "💰 Mening hisobim", "ru": "💰 Мой счет"},
        "settings": {"uz": "⚙️ Sozlamalar", "ru": "⚙️ Настройки"},
        "buy_yuan": {"uz": "💳 Yuan sotib olish", "ru": "💳 Купить юань"},
        "my_id": {"uz": "🆔 Mening ID kodim", "ru": "🆔 Мой ID код"},
        "get_address": {"uz": "🎫 Manzil olish", "ru": "🎫 Получить адрес"},
        "comments": {"uz": "💬 Izohlar", "ru": "💬 Комментарии"},
    },
    "settings": {
        "lang": {"uz": "Tilni", "ru": "Язык"},
        "phone": {"uz": "Telefon raqamini", "ru": "Номер телефона"},
    },
    "cancel": {"uz": "Bekor qilish", "ru": "Отмена"},
    "himself": {"uz": "Borib olish", "ru": "Забрать самому"},
    "deliver": {"uz": "Yetkazib berish (dostavka)", "ru": "Доставить"},
    'phone_number2_yes': {
        'uz': '✅ Ha',
        'ru': '✅ Да'
    },
    'phone_number2_no': {
        'uz': "❌ Yo'q",
        'ru': '❌ Нет'
    },
    'buy_yuan': {
        'uz': '💳 Yuan sotib olish',
        'ru': '💳 Купить юань'
    }
}

manzils = {
    0: {
        'uz': "Avia Ekspress  1/4 kun \n\n北京市门头沟区门头沟黑山A4区2号楼2单元17层1703  A({code})收货人： A({code})联系方式 17800293735",
        'ru': "Aвиа Экспресс 1/4 дней \n\n北京市门头沟区门头沟黑山A4区2号楼2单元17层1703  A({code})收货人： A({code})联系方式 17800293735"
    },
    1: {
        'uz': "Avia Standart  7/10 kun \n\n北京市门头沟区门头沟黑山A4区2号楼2单元17层1703  B({code})收货人： B({code}) 联系方式 17800293735",
        'ru': "Aвиа Cтандарт  7/10 дней \n\n北京市门头沟区门头沟黑山A4区2号楼2单元17层1703  B({code})收货人： B({code}) 联系方式 17800293735"
    },
    2: {
        'uz': "Avto Caro  15/25 kun  \n北京市门头沟区门头沟黑山A4区2号楼2单元17层1703   C({code})收货人：C({code})联系方式 17800293735",
        'ru': "Aвто Kаро  15/25 дней  \n北京市门头沟区门头沟黑山A4区2号楼2单元17层1703   C({code})收货人：C({code})联系方式 17800293735"
    }
}

allows = {
    0: {
        'uz': "<b>GIYOHVAND MODDALARGA O'XSHASH MAHSULOTLAR:</b>\n    kimyoviy moddalar, psixatrob\n\n"
              "<b>MEDITSINAGA TEGISHLI:</b>\n    meditsina mahsulotlari, dorilar\n\n"
              "<b>TEXNIKA:</b>\n    katta kuchli batareykalar\n\n"
              "<b>BOSHQALAR:</b>\n    suyuq mahsulotlar",
        'ru': "<b>НАРКОТИКОВЫЕ ВЕЩИ:</b>\n   химические вещества, психотропные\n\n"
              "<b>МЕДИЦИНСКИЕ ВЕЩИ:</b>\n    медицинский продукт, препарат\n\n"
              "<b>ТЕХНИКИ:</b>\n    большие мощные батареи\n\n"
              "<b>ДРУГИЕ:</b>\n     жидкие продукты"
    },
    1: {
        'uz': "<b>TEXNIKA:</b>\n   powerbank, batareyka, kartridj\n\n"
              "<b>INTIM MAHSULOTLAR:</b>\n   intim o'yinchoq, intim gel\n\n"
              "<b>O'SIMLIKLAR:</b>\n    xonaki gullar, urug'lar, ko'chatlar, tirik gullar\n\n"
              "<b>KOSMETIKA MAHSULOTLARI:</b>\n     shampun, krem,  lak, kosmetika tovarlari, soch bo'yoqi, atir\n\n"
              "<b>HAR KUNGI MAHSULOTLAR:</b>\n    Havo spreyi, oshxona va hammomni tozalash vositalari, kiyimlarni "
              "tozalash vositalari. Gugurt, kapsulalarda kir yuvish kukuni, tish pastasi, yelim, avtomobil suyuqliklari, "
              "oqar suvlarni tozalash mahsulotlari, kukunli mahsulotlar, markerlar, "
              "suv tomchilari bo'lgan har qanday mahsulotlar, nam salfetka, zajigalka, lazer, linza\n\n"
              "<b>MEDITSINAGA TEGISHLI:</b>\n    Tibbiy mahsulotlar, dorilar, stomatologik mahsulotlar, tishlarni oqartirish\n\n"
              "<b>HARBIY MAHSULOTLAR VA QUROLLAR:</b>\n     elektroshoker va sovuq qurollar, uchi uchli kamon o'qlari, "
              "pnevmatik miltiqlar va boshqa qurollar, barcha turdagi yog'och va temir buyumlar, harbiy buyumlar, "
              "ratsiyalar, dronlar, pichoqlar\n\n"
              "<b>OVQATLAR:</b>\n     Oziq-ovqat mahsulotlari, yarim tayyor ovqatlar\n\n"
              "<b>BOSHQALAR:</b>\n     Qimmat baho metallar, migalka va sirenalar, massaj moyi",
        'ru': "<b>ТЕХНИКИ:</b>\n    повербанк  батарейка, катридж\n\n"
              "<b>ИНТИМНЫЕ ТОВАРЫ:</b>\n    интим игрушка, интим гель\n\n"
              "<b>РAСТЕНИЕ:</b>\n    комнатние растение, семена, растение, "
              "живые цветы\n\n"
              "<b>СРЕДСТВО УХОДA ЗA КРAСОТОЙ:</b>\n    шампунь, лак, крем, Косметикa, краскаски для волос, духи\n\n"
              "<b>ЕЖЕДНЕВНЫЕ ВЕЩИ:</b>\n    Освежители воздуха, средства для чистки кухни и сантехники, средства для "
              "чистки одежды. Спички запрещены, стиральный порошок в гелевых капсулах, зубная паста, клей, "
              "автомобильные жидкости, средства для очистки сточных вод, порошковые средства. Маркеры запрещены, "
              "любые продукты, на которых есть капли воды. влажная салфетка, зажигалка, лазер, линза\n\n"
              "<b>ЛЕКАРСТВО:</b>\n   "
              "Медицинские товары, лекарства, Стоматологические товары, отбеливание зубов\n\n"
              "<b>ВОЕННЫЕ И ОРУЖЕЙНЫЕ ВЕЩИ:</b>\n   Электрошокеры и другое холодное оружие, Арбалеты, "
              "Пневматические винтовки и другое оружие, Все виды деревянных и железных изделий, Товары военного "
              "назначения, рации, дроны, ножи\n\n"
              "<b>ПИТАНИЕ:</b>\n   Продукты питания, полуфабрикаты\n\n"
              "<b>ДРУГИЕ:</b>\n    Драгоценные металлы, Мигалка и сирены, массажное масло"
    },
    2: {
        'uz': "<b>GIYOHVAND MODDALARGA O'XSHASH MAHSULOTLAR:</b>\n    kimyoviy moddalar, psixatrob\n\n"
              "<b>MEDITSINAGA TEGISHLI:</b>\n    meditsina mahsulotlari, dorilar",
        'ru': "<b>НАРКОТИКОВЫЕ ВЕЩИ:</b>\n   химические вещества, психотропные\n\n"
              "<b>МЕДИЦИНСКИЕ ВЕЩИ:</b>\n    медицинский продукт, препарат"
    }
}
