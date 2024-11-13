import random
import os

from aiogram.types import InputFile

from data.translate import msg_lang

from loader import bot

MEDIA_DIR = "/var/www/cargo_bot-master/root/cargo_admin/media"

def get_idcode():
    var = "".join([str(random.randint(0, 10000) % 10) for _ in range(4)])
    return var


async def download_user_passport(file_id):
    file_info = await bot.get_file(file_id)
    core_path = os.path.join(MEDIA_DIR, "/var/www/cargo_bot-master/root/cargo_admin/media/users/passports")
    if not os.path.exists(core_path):
        os.makedirs(core_path)
    file_path = os.path.join(
        MEDIA_DIR, "users/passports", file_info.file_path.split("/")[1]
    )
    image_path = file_info.file_path
    file = await bot.download_file(image_path)
    print(file)

    with open(file_path, "wb") as new_file:
        f = new_file.write(file.read())
        print(f)
    return os.path.join("users/passports", file_info.file_path.split("/")[1])


async def download_user_image(file_id):
    file_info = await bot.get_file(file_id)
    core_path = os.path.join(MEDIA_DIR, "users/image")
    if not os.path.exists(core_path):
        os.makedirs(core_path)
    file_path = os.path.join(
        MEDIA_DIR, "users/image", file_info.file_path.split("/")[1]
    )
    image_path = file_info.file_path
    file = await bot.download_file(image_path)
    with open(file_path, "wb") as new_file:
        new_file.write(file.read())
    return os.path.join("users/image", file_info.file_path.split("/")[1])


def get_passport1():
    return InputFile('/var/www/cargo_bot-master/root/cargo_admin/media/users/passports/file_0.jpg')


def get_passport2():
    file = "/var/www/cargo_bot-master/root/cargo_admin/media/users/passports/file_1.jpg"
    return InputFile(file)


def valid_phone(phone_number: str, lang: str) -> str:
    if len(phone_number) != 13:
        return f"{msg_lang['phone_number_checking']['all_exc'][lang]}\n{msg_lang['phone_number_checking']['example'][lang]}"
    elif phone_number[:1] != "+":
        return msg_lang["phone_number_checking"]["with_plus"][lang]
    elif phone_number[1:4] != "998":
        return msg_lang["phone_number_checking"]["with_998"][lang]
    elif not phone_number[1:].isnumeric():
        return msg_lang["phone_number_checking"]["with_num"][lang]
    return phone_number
