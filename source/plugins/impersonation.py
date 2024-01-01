from pyrogram import Client, filters
from config import *
from os import remove
from autoname import main as name


@Client.on_message(filters.command("انتحال$", prefixes=f".") & filters.me)
async def copy_user(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        id = message.reply_to_message.from_user.id
    else:
        return await message.edit("• قم بي الرد علي العضو")
    if message.reply_to_message.from_user.id in sudo_command:
        return await message.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    await message.edit("• جاري انتحاله ..")
    r.delete(f"{sudo_id}clockk")
    if not r.get(f'{sudo_id}:copy_user'):
        me_info = await client.get_chat(sudo_id)
        r.set(f'{sudo_id}:copy_user', '3yad')
        if me_info.bio:
            r.set(f'{sudo_id}:copy_user:bio', me_info.bio)
        if me_info.last_name:
            r.set(f'{sudo_id}:copy_user:first_name', me_info.last_name)
        else:
            r.set(f'{sudo_id}:copy_user:first_name', me_info.first_name)
        if me_info.photo:
            async for photo in app.get_chat_photos("me"):
                me_photo = photo.file_id
                r.set(f'{sudo_id}:copy_user:photo', me_photo)
                break
    us_info = await client.get_chat(id)
    if us_info.photo:
        async for photos in app.get_chat_photos(id):
            his_photo = photos.file_id
            await client.download_media(his_photo, file_name="./his_photo.jpg")
            await client.set_profile_photo(photo="./his_photo.jpg")
            remove("./his_photo.jpg")
            break
    await client.update_profile(first_name=us_info.first_name)
    if us_info.bio:
        await client.update_profile(bio=us_info.bio)
    else:
        await client.update_profile(bio="")
    if us_info.last_name:
        await client.update_profile(last_name=us_info.last_name)
    else:
        await client.update_profile(last_name="")
    await message.edit("• تم الانتحال")


@Client.on_message(filters.command("رجوع$", prefixes=f".") & filters.me)
async def uncopy_user(client, message):
    if not r.get(f'{sudo_id}:copy_user'):
        return await message.edit("• لم تقم بانتحال احد")
    await message.edit("• جاري الرجوع الي الاعدادات الافتراضيه ..")
    first_name = r.get(f'{sudo_id}:copy_user:first_name')
    bio = r.get(f'{sudo_id}:copy_user:bio')
    r.delete(f'{sudo_id}:copy_user')
    if bio:
        await client.update_profile(bio=bio)
    else:
        await client.update_profile(bio="")
    if first_name:
        await client.update_profile(first_name=first_name)
    if r.get(f'{sudo_id}:copy_user:photo'):
        async for photo in app.get_chat_photos("me"):
            my_photo = photo.file_id
            await client.delete_profile_photos(my_photo)
            break
    r.delete(f"{sudo_id}:copy_user:photo")
    r.set(f"{sudo_id}clockk", first_name)
    await message.edit("• تم الرجوع الي الاعدادات الافتراضيه")
    await name()
