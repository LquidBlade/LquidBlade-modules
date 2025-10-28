# spam_safe.py
# безопасная версия модуля Spam для LQUIDBLADE

import asyncio
from pyrogram import Client, types

async def answer(message: types.Message, text: str):
    """Функция для ответа вместо utils.answer"""
    await message.reply(text)

class SpamMod:
    """Безопасный модуль спама"""

    async def spam_cmd(self, app: Client, message: types.Message, args: str):
        reply = message.reply_to_message
        if not reply:
            if not args:
                return await answer(message, "Нет аргументов и реплая")
            args_ = args.split(maxsplit=1)
            if len(args_) == 1:
                if args_[0].isdigit():
                    return await answer(message, "Не указан текст для спама")
                return await answer(message, "Не указано кол-во сообщений первым аргументом")
            if not args_[0].isdigit():
                return await answer(message, "Кол-во сообщений должно быть целым числом")
            await message.delete()
            for _ in range(int(args_[0])):
                await message.reply(args_[1], quote=False)
            return

        if not args:
            return await answer(message, "Не указано кол-во сообщений")
        if not args.isdigit():
            return await answer(message, "Кол-во сообщений должно быть целым числом")
        await message.delete()
        for _ in range(int(args)):
            await reply.copy(message.chat.id, reply_to_message_id=reply.message_id)

    async def cspam_cmd(self, app: Client, message: types.Message, args: str):
        reply = message.reply_to_message
        text = args if args else (reply.text if reply and reply.text else reply.caption if reply and reply.caption else "")
        if not text:
            return await answer(message, "Нет аргументов или реплая")
        await message.delete()
        for char in text.replace(" ", ""):
            await message.reply(char, quote=False)

    async def wspam_cmd(self, app: Client, message: types.Message, args: str):
        reply = message.reply_to_message
        text = args if args else (reply.text if reply and reply.text else reply.caption if reply and reply.caption else "")
        if not text:
            return await answer(message, "Нет аргументов или реплая")
        await message.delete()
        for word in text.split():
            await message.reply(word, quote=False)

    async def delayspam_cmd(self, app: Client, message: types.Message, args: str):
        reply = message.reply_to_message
        if not reply:
            if not args:
                return await answer(message, "Нет аргументов и реплая")
            args_ = args.split(maxsplit=2)
            if not args_[0].isdigit():
                return await answer(message, "Не указано кол-во сообщений первым аргументом")
            if len(args_) == 1:
                return await answer(message, "Не указан текст для спама")
            if not args_[1].isdigit():
                return await answer(message, "Задержка должна быть целым числом")
            if len(args_) == 2:
                return await answer(message, "Не указан текст для спама")
            await message.delete()
            for _ in range(int(args_[0])):
                await message.reply(args_[2], quote=False)
                await asyncio.sleep(int(args_[1]))
            return

        if not args:
            return await answer(message, "Не указано кол-во сообщений и задержка")
        args_ = args.split()
        if not args_[0].isdigit():
            return await answer(message, "Кол-во сообщений должно быть целым числом")
        if len(args_) == 1:
            return await answer(message, "Не указана задержка")
        if not args_[1].isdigit():
            return await answer(message, "Задержка должна быть целым числом")
        await message.delete()
        for _ in range(int(args_[0])):
            await reply.copy(message.chat.id, reply_to_message_id=reply.message_id)
            await asyncio.sleep(int(args_[1]))
