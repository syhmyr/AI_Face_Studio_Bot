from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def join_channels():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Kanala goşul",
                    url="https://t.me/YourChannel"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✅ Barladym",
                    callback_data="check_join"
                )
            ]
        ]
    )


def admin_panel():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📊 Statistika",
                    callback_data="admin_stats"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 Broadcast",
                    callback_data="admin_broadcast"
                )
            ],
            [
                InlineKeyboardButton(
                    text="👥 Ulanyjylar",
                    callback_data="admin_users"
                )
            ]
        ]
    )
