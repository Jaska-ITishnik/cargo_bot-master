import asyncio
import logging
from mailbox import Message

from aiogram.utils.exceptions import BotBlocked, ChatNotFound, RetryAfter, UserDeactivated, TelegramAPIError

log = logging.getLogger('broadcast')


async def send_message_to_all_clients(user, msg: Message, data, disable_notification: bool = False) -> bool:
    try:
        if msg.photo:
            await msg.bot.send_photo(chat_id=user['tg_id'], photo=msg.photo[0].file_id, caption=msg.caption)
        if msg.video:
            await msg.bot.send_video(chat_id=user['tg_id'], video=msg.video.file_id, caption=msg.caption)
        else:
            if data.get('message'):
                await msg.bot.send_message(chat_id=user['tg_id'], text=data['message'],
                                           disable_notification=disable_notification)
    except BotBlocked:
        log.error(f"Target [ID:{user['tg_id']}]: blocked by user")
    except ChatNotFound:
        log.error(f"Target [ID:{user['tg_id']}]: invalid user ID")
    except RetryAfter as e:
        log.error(f"Target [ID:{user['tg_id']}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await send_message_to_all_clients(user['tg_id'], msg.bot, data)  # Recursive call
    except UserDeactivated:
        log.error(f"Target [ID:{user['tg_id']}]: user is deactivated")
    except TelegramAPIError:
        log.exception(f"Target [ID:{user['tg_id']}]: failed")
    else:
        log.info(f"Target [ID:{user['tg_id']}]: success")
        return True
    return False
