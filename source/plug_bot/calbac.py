from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio


reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("عوده",callback_data="backk"),
             ]]
             )


@bot.on_callback_query(filters.regex("^backk$"))
async def back(client, callback_query):
  await callback_query.edit_message_text("◍ اهلا بيك بقائمه الابراج اختر ما تريد\n√ ",reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("الجدي", callback_data="elgadee"),
             InlineKeyboardButton("الدلو", callback_data="eldaloo"),
             ],
             [
             InlineKeyboardButton("الحوت", callback_data="elhout"),
             InlineKeyboardButton("الحمل", callback_data="elhamal"),
             ],
             [
             InlineKeyboardButton("الثور", callback_data="elthawr"),
             InlineKeyboardButton("الجوزاء", callback_data="elgawzaa"),
             ],
             [
             InlineKeyboardButton("السرطان", callback_data="elsaratan"),
             InlineKeyboardButton("الأسد", callback_data="elaasad"),
             ],
             [
             InlineKeyboardButton("العذراء", callback_data="elazraaa"),
             InlineKeyboardButton("الميزان", callback_data="elmezaan"),
             ],
             [
             InlineKeyboardButton("العقرب", callback_data="elaqrab"),
             InlineKeyboardButton("القوس", callback_data="elqoos"),
             ],
             [
            InlineKeyboardButton("✅  قناه السورس  ",url="https://t.me/Tepthon"),
             ]]
             ))




@bot.on_callback_query(filters.regex("^elgadee$"))
async def elgadee(client, callback_query):
   
    abrag_text = """✅برج الجدي
    [⩹━★⊷⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝚀𝚈𝚁𝙰⌯⊶★━⩺](https://t.me/Tepthon)\n
✅من تاريخ 2021-4-1

✅عاطفياً :  حاول ترطيب الأجواء مع الشريك، بعد ثورة الغضب التي انتابتك في الأيام الماضية 

✅صحياً :  لا تنجرّ وراء محاولات استدراجك إلى أن تثور وتغضب لتعريض وضعك الصحي للخطر

✅مهنياً :  يدعوك هذا اليوم المليء بالسلبيات إلى عدم التورط في قضايا أكبر منك، وخصوصاً أن رياح التغيير بدأت تعصف باتجاهك"""
    await callback_query.edit_message_text(abrag_text, reply_markup=reply_markup)


@bot.on_callback_query(filters.regex("^eldaloo$"))
async def eldaloo(client, callback_query):
   
    abrag_text = """✅برج الدلو
    [⩹━★⊷⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝚀𝚈𝚁𝙰⌯⊶★━⩺](https://t.me/Tepthon)\n
✅من تاريخ 2021-4-1

✅عاطفياً :  لا تتسرّع في الموافقة على قرار مهم قبل أن تدرس الوضع من جميع جوانبه، لأن الندم قد لا يفيدك لاحقاً 

✅صحياً :  لكي تحافظ على صحتك السليمة، ما عليك سوى ممارسة الرياضة ثلاث مرات على الأقل في الأسبوع

✅مهنياً :  هذا اليوم يفرض عليك أن تنظر إلى الأمور بطريقة أخرى، وأن تتعلّم كيف تحوّل الخسارة إلى ربح"""
    await callback_query.edit_message_text(abrag_text, reply_markup=reply_markup)


@bot.on_callback_query(filters.regex("^elhout$"))
async def elhout(client, callback_query):
   
    abrag_text = """✅برج الحوت
    [⩹━★⊷⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝚀𝚈𝚁𝙰⌯⊶★━⩺](https://t.me/Tepthon)\n
✅من تاريخ 2021-4-1

✅عاطفياً :  صداقة قديمة تعود إلى الواجهة عن طريق المصادفة، لكنّ الشريك يشعر بالقلق، فسارع إلى توضيح الأمور 

✅صحياً :  لا تستسلم للإحباط بسبب وضعك الصحّي المتردي نوعاً ما، بل كن متسلّحاً بالتفاؤل

✅مهنياً :  يرّوج بعض الزملاء الإشاعات عن وضعك، لكنّك تبقى صلباً وتحديداً في المركز المهم الذي أسنده إليك أرباب العمل"""
    await callback_query.edit_message_text(abrag_text, reply_markup=reply_markup)


@bot.on_callback_query(filters.regex("^elhamal$"))
async def elhamal(client, callback_query):
   
    abrag_text = """✅برج الحمل
[⩹━★⊷⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝚀𝚈𝚁𝙰⌯⊶★━⩺](https://t.me/Tepthon)\n
✅من تاريخ 2021-4-1

✅عاطفياً :  يحتاج الشريك اليوم إلى عاطفتك واهتمامك أكثر من أي وقت مضى، فاستمع إليه وأمن له ما يتمنّاه 

✅صحياً :  القيام ببعض التمارين الخفيفة صباحاً تساعد على تليين العضلات وخصوصاً عضلات العنق الكتفين

✅مهنياً :  قد يطرأ اليوم ما يهدد ببعض المشاريع على الصعيد المهني ويكون المناخ ضاغطاً جداً وملبداً بغيوم المشاكل"""
    await callback_query.edit_message_text(abrag_text, reply_markup=reply_markup)


@bot.on_callback_query(filters.regex("^elthawr$"))
async def elthawr(client, callback_query):
   
    abrag_text = """✅برج الثور
[⩹━★⊷⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝚀𝚈𝚁𝙰⌯⊶★━⩺](https://t.me/Tepthon)\n
✅من تاريخ 2021-4-1

✅عاطفياً :  يطلب منك الشريك أن تعطيه جواباً حاسماً بشأن طبيعة العلاقة بينكما، من دون أن يغفل عن أمور تهمكما 

✅صحياً :  ترتاح من تعب أرهقك جداً وأبقاك في حالة صحية متذبذبة ومضطربة بعض الشيء

✅مهنياً :  حاول ألاّ توظف طاقتك في مشاريع صغيرة لا خطط واضحة لها، وانتظر حتى تعرض عليك المشاريع الكبيرة"""
    await callback_query.edit_message_text(abrag_text, reply_markup=reply_markup)


@bot.on_callback_query(filters.regex("^elgawzaa$"))
async def elgawzaa(client, callback_query):
   
    abrag_text = """✅برج الجوزاء
    [⩹━★⊷⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝚀𝚈𝚁𝙰⌯⊶★━⩺](https://t.me/Tepthon)\n
✅من تاريخ 2021-4-1

✅عاطفياً :  مهمة إقناع الشريك بالسير معك حتى النهاية ليست صعبة، وتجاربه السابقة معك مشجعة جداً 

✅صحياً :  أنت المسؤول عما آل إليه وضعك الصحي، لأنك لم تلتزم إرشادات الطبيب ولم تطبقها

✅مهنياً :  يطرأ اليوم ما يبشر بيوم دقيق من التجارب المرة، لكن النجاح يكون حليفك في نهاية المطاف"""
    await callback_query.edit_message_text(abrag_text, reply_markup=reply_markup)


@bot.on_callback_query(filters.regex("^elsaratan$"))
async def elsaratan(client, callback_query):
   
    abrag_text = """✅برج السرطان
    [⩹━★⊷⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝚀𝚈𝚁𝙰⌯⊶★━⩺](https://t.me/Tepthon)\n
✅من تاريخ 2021-4-1

✅عاطفياً :  تمنحك مساندة الحبيب لك في هذه المرحلة الاندفاع والتفاؤل في الحياة والتفكير في الخطوات المقبلة بثقة كبيرة جداً 

✅صحياً :  انتبه لصحتك وانظر إلى الخيارات المتاحة أمامك للمحافظة عليها معافاة

✅مهنياً :  يحمل إليك هذا اليوم كلمات الإطراء والمديح والتهنئة، فيسطع نجمك وتبدأ بمشروع جديد"""
    await callback_query.edit_message_text(abrag_text, reply_markup=reply_markup)


@bot.on_callback_query(filters.regex("^elaasad$"))
async def elaasad(client, callback_query):
   
    abrag_text = """✅برج الاسد
    [⩹━★⊷⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝚀𝚈𝚁𝙰⌯⊶★━⩺](https://t.me/Tepthon)\n
✅من تاريخ 2021-4-1

✅عاطفياً :  لا تحمّل الشريك مسؤولية الأخطاء القديمة، وحاول أن تتخطى ذلك برحابة صدر وبساطة 

✅صحياً :  التدخين والإفراط في شرب الكحول والسهر سرعان ما تظهر نتائجهما على صحتك

✅مهنياً :  قد يجعلك هذا اليوم تتردّد في تسلم مهمة مع أنك تمتلك القدرة على ذلك وتحقيق النجاح المطلوب"""
    await callback_query.edit_message_text(abrag_text, reply_markup=reply_markup)


@bot.on_callback_query(filters.regex("^elazraaa$"))
async def elazraaa(client, callback_query):
   
    abrag_text = """✅برج العذراء
    [⩹━★⊷⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝚀𝚈𝚁𝙰⌯⊶★━⩺](https://t.me/Tepthon)\n
✅من تاريخ 2021-4-1

✅عاطفياً :  تشعر بقوة العاطفة وتزداد رغبتك في التقرّب من الشريك الذي تكنّ له الحب الكبير 

✅صحياً :  إذا أحسست أن وضعك الصحي يتحسّن، فهذا جراء تطبيق إرشادات أصحاب الاختصاص في مجال التغذية

✅مهنياً :  يولّد هذا اليوم كلاماً غير مقنع أو لا يتمتّع بمصداقية، فتحاول معرفة الأسباب الكامنة وراء كل ما يحصل وتنجح في ذلك"""
    await callback_query.edit_message_text(abrag_text, reply_markup=reply_markup)


@bot.on_callback_query(filters.regex("^elmezaan"))
async def elmezaan(client, callback_query):
   
    abrag_text = """✅برج الميزان
    [⩹━★⊷⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝚀𝚈𝚁𝙰⌯⊶★━⩺](https://t.me/Tepthon)\n
✅من تاريخ 2021-4-1

✅عاطفياً :  تمرّ بظرف صعب اليوم وأنت بأمسّ الحاجة إلى مساندة الشريك لتجاوز ما تواجهه بأقل ضرر ممكن 

✅صحياً :  تنضم إلى إحدى الفرق أو المجموعات الرياضية وتواظب على المشاركة في جميع أنشطتها فتستفيد صحياً

✅مهنياً :  يجعلك هذا اليوم تشغل نفسك بأمور صغيرة لن تنفعك بشيء، بل بالعكس قد تضيّع لك وقتك، وأنت بحاجة ماسة إلى كل ثانية"""
    await callback_query.edit_message_text(abrag_text, reply_markup=reply_markup)


@bot.on_callback_query(filters.regex("^elaqrab$"))
async def elaqrab(client, callback_query):
   
    abrag_text = """✅برج العقرب
    [⩹━★⊷⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝚀𝚈𝚁𝙰⌯⊶★━⩺](https://t.me/Tepthon)\n
✅من تاريخ 2021-4-1

✅عاطفياً :  كثرة التأجيل في حسم الأمور المصيرية تهدد علاقتك بالشريك، وتدفعها إلى المزيد من التأزم 

✅صحياً :  قد تشعر بضيق في النفس وباضطراب مفاجئ في الرئتين بسبب إدمانك التدخين

✅مهنياً :  قد يعرقل طارئ هذا اليوم تقدمك في مجالك المهني، لكنك قادر على تخطي المصاعب مهما تكن شديدة"""
    await callback_query.edit_message_text(abrag_text, reply_markup=reply_markup)


@bot.on_callback_query(filters.regex("^elqoos$"))
async def elqoos(client, callback_query):
   
    abrag_text = """✅برج القوس
    [⩹━★⊷⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝚀𝚈𝚁𝙰⌯⊶★━⩺](https://t.me/Tepthon)\n
✅من تاريخ 2021-4-1

✅عاطفياً :  كن طويل البال مع الشريك وامنحه مزيداً من الوقت، فهو ساعدك كثيراً ويستحق منك بعض التضحية 

✅صحياً :  تجنّب قدر الإمكان الأماكن الرطبة ولا سيما أنك تعاني الربو وضيقاً في التنفس

✅مهنياً :  قد يفقدك هذا اليوم الظروف المشجعة على التحرّك والاستثمار وتوظيف الأموال وتحقيق الأرباح"""
    await callback_query.edit_message_text(abrag_text, reply_markup=reply_markup)
