from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🖼 AI Surat"),
                KeyboardButton(text="🎥 AI Wideo")
            ],
            [
                KeyboardButton(text="👤 Profil"),
                KeyboardButton(text="💰 Balans")
            ],
            [
                KeyboardButton(text="👥 Referral"),
                KeyboardButton(text="🆘 Goldaw")
            ]
        ],
        resize_keyboard=True
    )
