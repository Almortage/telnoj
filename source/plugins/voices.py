import speech_recognition as sr
from pyrogram import Client, filters
from pydub import AudioSegment
from os import remove


@Client.on_message(filters.command(["اكتب$", "وش يقول$"], prefixes=".") & filters.me)
async def speech_to_text(client, message):
    if not message.reply_to_message:
        await message.edit("قم بي الرد علي الصوت اولا")
        return
    await message.edit("جاري تحميل الصوت")
    voice_down = await message.reply_to_message.download("./recyad.wav")
    voice = sr.Recognizer()
    await message.edit("جاري استخراج سورس الصوت")
    sound = AudioSegment.from_ogg(voice_down)
    wav_file = sound.export(voice_down, format="wav")
    with sr.AudioFile(wav_file) as source:
        audio_source = voice.record(source)
    await message.edit("جاري التعرف علي الكلام")
    try:
        text = voice.recognize_google(audio_source, language='ar-EG')
    except Exception as e:
        text = f"فشل التعرف علي الكلام\n{e}"
    await message.edit(text)
    remove("recyad.wav")
