from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Начать 🚀', callback_data='start')
        ]
    ]
)

home_gym = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🏡 Дома', callback_data='home')
        ],
        [
            InlineKeyboardButton(text='🏋️‍♂️ В спортзале', callback_data='gym')
        ]
    ]
)

types_home = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='💪 Грудные мышцы', callback_data='chest_home')
        ],
        [
            InlineKeyboardButton(text='🚴‍♂️ Ноги', callback_data='legs_home')
        ],
        [
            InlineKeyboardButton(text='🧗‍♀️ Спина', callback_data='back_home')
        ],
        [
            InlineKeyboardButton(text='🏋️‍♂️ Плечи', callback_data='shoulders_home')
        ],
        [
            InlineKeyboardButton(text='🦾 Бицепсы', callback_data='biceps_home')
        ],
        [
            InlineKeyboardButton(text='🔥 Трицепсы', callback_data='triceps_home')
        ],
        [
            InlineKeyboardButton(text='🌟 Пресс', callback_data='abs_home')
        ],
        [
            InlineKeyboardButton(text='🍑 Ягодичные мышцы', callback_data='gluteal_home')
        ],
    ]
)

types_gym = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='💪 Грудные мышцы', callback_data='chest_gym')
        ],
        [
            InlineKeyboardButton(text='🚴‍♂️ Ноги', callback_data='legs_gym')
        ],
        [
            InlineKeyboardButton(text='🧗‍♀️ Спина', callback_data='back_gym')
        ],
        [
            InlineKeyboardButton(text='🏋️‍♂️ Плечи', callback_data='shoulders_gym')
        ],
        [
            InlineKeyboardButton(text='🦾 Бицепсы', callback_data='biceps_gym')
        ],
        [
            InlineKeyboardButton(text='🔥 Трицепсы', callback_data='triceps_gym')
        ],
        [
            InlineKeyboardButton(text='🌟 Пресс', callback_data='abs_gym')
        ],
        [
            InlineKeyboardButton(text='🍑 Ягодичные мышцы', callback_data='gluteal_gym')
        ],
    ]
)

home_chest = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/rTA_aRCfD0M?si=GV8JkEDD1qI6cCS2')
        ]
    ]
)

home_legs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/H21pTB9nJ7I?si=g7Kkp16kY8LZ_hQT')
        ]
    ]
)

home_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/BNwrJmQauyU?si=azpJBehpM1L6Xh2t')
        ]
    ]
)

home_shoulders = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/TF8u3yMsygs?si=lVjdL-yVwr0cS0zi')
        ]
    ]
)

home_biceps = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/tIU6zuAL9mE?si=OhvRUKlok33cz6Y2')
        ]
    ]
)

home_triceps = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/W5b-0EVNtQQ?si=DZUrzEbW0M7rD7pa')
        ]
    ]
)

home_abs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/OfmzNF4QFR8?si=vt0Ef4aMFshdbCwJ')
        ]
    ]
)

home_gluteal = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/PvWUe_ovTm4?si=g-pCXil2vfTOA5HE')
        ]
    ]
)




gym_chest = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/y91cEJH5au8?si=89Uoj9GYvKJIRhlI')
        ]
    ]
)

gym_legs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/9UAW39h9AwY?si=aQ3vKnqhl_My_T4J')
        ]
    ]
)

gym_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/6rr4sfFVCNo?si=8svG9QH13v9O7wLt')
        ]
    ]
)

gym_shoulders = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/gW2r_pvzlrQ?si=Eg0rqVTNYhW42ufj')
        ]
    ]
)

gym_biceps = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/IWqg46qVJ6Y?si=njkuv0NRSpnzn3Mg')
        ]
    ]
)

gym_triceps = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/UhAt45tuirk?si=xdqnkNrrhTnoqX2j')
        ]
    ]
)

gym_abs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/YWmlHqxypQk?si=2bYzgAmJUoFmXKDf')
        ]
    ]
)

gym_gluteal = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотри тренировку здесь 📲', url='https://youtu.be/4mtBUYQqXrQ?si=ymCtid4NWXZOilBr')
        ]
    ]
)















