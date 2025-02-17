from aiogram import Router, Bot, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
import reply_keyboard as kbr
import inline_keyboard as kb
from aiogram.types import FSInputFile

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer('👋 Привет! Добро пожаловать в мир фитнеса с ботом Спортсмен! 💪'
                         '\n\nГотов начать свой путь к здоровью и силе? Нажми на кнопку «Начать», и я помогу тебе выбрать, какую группу мышц ты хочешь развивать!',
                         reply_markup=kb.start)

@router.callback_query(F.data == 'start')
async def start(callback: CallbackQuery):
    await callback.message.answer('🚀',
                                  reply_markup=kbr.main)
    await callback.message.answer('🤔 Где ты хочешь заниматься? Пожалуйста, выбери один из вариантов: \n\n1. 🏡 Дома\n2. 🏋️‍♂️ В спортзале',
                                  reply_markup=kb.home_gym)


@router.message(F.text == 'Тренировка 🏋️‍♂️')
async def start(message: Message):
    await message.answer('🤔 Где ты хочешь заниматься? Пожалуйста, выбери один из вариантов: \n\n1. 🏡 Дома\n2. 🏋️‍♂️ В спортзале',
                         reply_markup=kb.home_gym)


@router.callback_query(F.data == 'home')
async def home(callback: CallbackQuery):
    await callback.message.answer('🔍 Отлично! Какую группу мышц ты хочешь развивать?'
                                  '\n\nВот список основных групп мышц:'
                                  '\n\n1. 💪 Грудные мышцы'
                                  '\n2. 🚴‍♂️ Ноги'
                                  '\n3. 🧗‍♀️ Спина'
                                  '\n4. 🏋️‍♂️ Плечи'
                                  '\n5. 🦾 Бицепсы'
                                  '\n6. 🔥 Трицепсы'
                                  '\n7. 🌟 Пресс'
                                  '\n8. 🍑 Ягодичные мышцы'
                                  '\n\nВыбери одну из групп, и я подберу для тебя упражнения, как для дома, так и для зала!',
                                  reply_markup=kb.types_home)

@router.callback_query(F.data == 'gym')
async def gym(callback: CallbackQuery):
    await callback.message.answer('🔍 Отлично! Какую группу мышц ты хочешь развивать?'
                                  '\n\nВот список основных групп мышц:'
                                  '\n\n1. 💪 Грудные мышцы'
                                  '\n2. 🚴‍♂️ Ноги'
                                  '\n3. 🧗‍♀️ Спина'
                                  '\n4. 🏋️‍♂️ Плечи'
                                  '\n5. 🦾 Бицепсы'
                                  '\n6. 🔥 Трицепсы'
                                  '\n7. 🌟 Пресс'
                                  '\n8. 🍑 Ягодичные мышцы'
                                  '\n\nВыбери одну из групп, и я подберу для тебя упражнения, как для дома, так и для зала!',
                                  reply_markup=kb.types_gym)


@router.callback_query(F.data == 'chest_home')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>1. Грудные мышцы 💪</b>'
                                  '\n\n- Отжимания (3 подхода по 10-15 повторений)'
                                  '\n- Отжимания с поднятыми ногами (3 подхода по 8-12 повторений)'
                                  '\n- Узкие отжимания (3 подхода по 10-15 повторений)',
                                  reply_markup=kb.home_chest,
                                  parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'legs_home')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>2. Ноги 🚴‍</b>️'
                                  '\n\n- Приседания (3 подхода по 15-20 повторений)'
                                  '\n- Выпады (3 подхода по 10-12 повторений на каждую ногу)'
                                  '\n- Подъемы на носки (3 подхода по 15 раз)',
                                  reply_markup=kb.home_legs,
                                  parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'back_home')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>3. Спина 🧗‍</b>️'
                                  '\n\n- Подтягивания на турнике (3 подхода по 5-10 повторений, если есть возможность)'
                                  '\n- Наклоны с гантелями (3 подхода по 10-12 повторений)'
                                  '\n- Повороты туловища (3 подхода по 15 повторений)',
                                  reply_markup=kb.home_back,
                                  parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'shoulders_home')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>️4. Плечи 🏋️</b>️‍'
                                  '\n\n- Подъемы гантелей в стороны (3 подхода по 12-15 повторений)'
                                  '\n- Жим гантелей стоя (3 подхода по 10-12 повторений)'
                                  '\n- Обратные отжимания от скамьи (3 подхода по 8-10 повторений)',
                                  reply_markup=kb.home_shoulders,
                                  parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'biceps_home')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>️5. Бицепсы 🦾</b>️'
                                  '\n\n- Сгибания с гантелями (3 подхода по 10-15 повторений)'
                                  '\n- Сгибания на узком хвате (3 подхода по 10-12 повторений)'
                                  '\n- Подъемы с бутылками воды или тяжёлым предметом (3 подхода по 10-15 повторений)',
                                  reply_markup=kb.home_biceps,
                                  parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'triceps_home')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>️6. Трицепсы 🔥</b>️'
                                  '\n\n- Отжимания на брусьях (или от мебели) (3 подхода по 8-12 повторений)'
                                  '\n- Жим гантелей стоя (3 подхода по 10-12 повторений)'
                                  '\n- Разгибания гантели за головой (3 подхода по 10-12 повторений)',
                                  reply_markup=kb.home_triceps,
                                  parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'abs_home')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>️7. Пресс 🌟</b>️'
                                  '\n\n- Скручивания (3 подхода по 15-20 повторений)'
                                  '\n- Планка (3 подхода по 30-60 секунд)'
                                  '\n- Ножницы (3 подхода по 15-20 повторений)',
                                  reply_markup=kb.home_abs,
                                  parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'gluteal_home')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>️8. Ягодичные мышцы 🍑</b>️'
                                  '\n\n- Мостик (3 подхода по 15-20 повторений)'
                                  '\n- Выпады назад (3 подхода по 10-12 повторений на каждую ногу)'
                                  '\n- Подъемы на скамейку (3 подхода по 10-15 повторений)',
                                  reply_markup=kb.home_gluteal,
                                  parse_mode=ParseMode.HTML)





@router.callback_query(F.data == 'chest_gym')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>️1. Грудные мышцы 💪</b>️'
                                  '\n\n- Жим лежа на скамье (3 подхода по 8-12 повторений)'
                                  '\n- Жим гантелей на скамье (3 подхода по 10-12 повторений)'
                                  '\n- Разведения гантелей (3 подхода по 12-15 повторений)',
                                  reply_markup=kb.gym_chest,
                                  parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'legs_gym')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>️2. Ноги 🚴‍♂️</b>️'
                                  '\n\n- Жим ногами (3 подхода по 10-12 повторений)'
                                  '\n- Приседания со штангой (3 подхода по 8-12 повторений)'
                                  '\n- Сгибание ног в тренажере (3 подхода по 10-15 повторений)',
                                  reply_markup=kb.gym_legs,
                                  parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'back_gym')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>️3. Спина 🧗‍</b>️'
                                  '\n\n- Тяга штанги в наклоне (3 подхода по 8-12 повторений)'
                                  '\n- Тяга вертикального блока (3 подхода по 10-12 повторений)'
                                  '\n- Тяга гантелей (3 подхода по 10-12 повторений)',
                                  reply_markup=kb.gym_back,
                                  parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'shoulders_gym')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>️4. Плечи 🏋️‍</b>️'
                                  '\n\n- Жим штанги сидя (3 подхода по 8-12 повторений)'
                                  '\n- Подъемы со штангой (3 подхода по 10-12 повторений)'
                                  '\n- Разведения в тренажере (3 подхода по 12-15 повторений)',
                                  reply_markup=kb.gym_shoulders,
                                  parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'biceps_gym')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>️5. Бицепсы 🦾</b>️'
                                  '\n\n- Сгибания штанги (3 подхода по 8-12 повторений)'
                                  '\n- Сгибания гантелей (3 подхода по 10-12 повторений)'
                                  '\n- Концентрационные сгибания (3 подхода по 10-15 повторений)',
                                  reply_markup=kb.gym_biceps,
                                  parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'triceps_gym')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>️6. Трицепсы 🔥</b>️'
                                  '\n\n- Тяга верхнего блока (3 подхода по 10-12 повторений)'
                                  '\n- Разгибания рук с гантелью за головой (3 подхода по 10-12 повторений)'
                                  '\n- Отжимания на брусьях (3 подхода по 8-10 повторений)',
                                  reply_markup=kb.gym_triceps,
                                  parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'abs_gym')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>️7. Пресс 🌟</b>️'
                                  '\n\n- Скручивания на тренажере (3 подхода по 12-15 повторений)'
                                  '\n- Подъемы ног в висе (3 подхода по 10-15 повторений)'
                                  '\n- Планка на фитболе (3 подхода по 30-60 секунд)',
                                  reply_markup=kb.gym_abs,
                                  parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'gluteal_gym')
async def training(callback: CallbackQuery):
    await callback.message.answer('<b>️8. Ягодичные мышцы 🍑</b>️'
                                  '\n\n- Жим ногами (3 подхода по 10-12 повторений)'
                                  '\n- Сгибания ног в тренажере (3 подхода по 12-15 повторений)'
                                  '\n- Мертвые тяги (3 подхода по 8-12 повторений)',
                                  reply_markup=kb.gym_gluteal,
                                  parse_mode=ParseMode.HTML)


@router.message(F.text == '🏋️‍♂️ Профессиональные занятия 🏋️‍♀️')
async def start(message: Message):
    await message.answer("""🏋<b>‍♂️ Профессиональные занятия 🏋️‍♀️</b>

Вы выбрали раздел "Профессиональные занятия"! Здесь вы сможете выбрать уровень подготовки и тип тренировки, который подходит именно вам.

<b>🌱 Начальный уровень: </b>
Если вы только начинаете свой путь в фитнесе, этот уровень идеально подходит для вас. Мы научим вас основам и правильной технике выполнения упражнений.

<b>🚀 Средний уровень: </b>
Для тех, кто уже имеет базовые знания и хочет развивать свои навыки. Здесь вы найдете более сложные упражнения и программы тренировок для достижения новых целей.

<b>💪 Жимовые раскладки: </b>
Этот раздел предназначен для тех, кто хочет сосредоточиться на силовых тренировках. Мы предложим вам различные схемы для максимизации ваших результатов.

Выберите уровень, который вам подходит, и начните тренироваться уже сегодня! 💪✨""",
                         reply_markup=kbr.professional_training,
                         parse_mode=ParseMode.HTML)

@router.message(F.text == 'Назад 🔙')
async def start(message: Message):
    await message.answer('Возвращаю...',
                         reply_markup=kbr.main)


@router.message(F.text == 'Начальный уровень 🌱')
async def start(message: Message):
    file = FSInputFile('trainings/Цикл начального уровня.xlsx')
    await message.answer("""🎉 Ваш файл с тренировками готов! 🎉

Вот ваш файл. Начинайте тренироваться и достигайте своих целей! 💪""")
    await message.answer_document(file)


@router.message(F.text == 'Средний уровень 🚀')
async def start(message: Message):
    file = FSInputFile('trainings/Цикл на 4 дня для среднего уровня.xlsx')
    await message.answer("""🎉 Ваш файл с тренировками готов! 🎉

Вот ваш файл. Начинайте тренироваться и достигайте своих целей! 💪""")
    await message.answer_document(file)


@router.message(F.text == 'Жимовые раскладки 💪')
async def start(message: Message):
    file = FSInputFile('trainings/Жимовые раскладки.docx')
    await message.answer("""🎉 Ваш файл с тренировками готов! 🎉

Вот ваш файл. Начинайте тренироваться и достигайте своих целей! 💪""")
    await message.answer_document(file)















