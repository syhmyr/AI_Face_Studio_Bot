from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from database import add_user, update_last_active
from keyboards.reply import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    await add_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        full_name=message.from_user.full_name
    )

    await update_last_active(message.from_user.id)

    text = f"""
👋 Salam, <b>{message.from_user.full_name}</b>

🤖 AI Face Studio botuna hoş geldiň.

Bu bot arkaly:

🖼 AI Surat
🎥 AI Wideo
👤 Profil
💰 Balans
👥 Referral
🆘 Goldaw

ulanyp bilersiň.

Aşakdaky menýudan dowam et.
"""

    await message.answer(
        text,
        reply_markup=main_menu()
    )


@router.message(F.text == "👤 Profil")
async def profile(message: Message):

    await update_last_active(message.from_user.id)

    await message.answer(
        "👤 Profil bölümi taýýarlanýar..."
    )


@router.message(F.text == "💰 Balans")
async def balance(message: Message):

    await update_last_active(message.from_user.id)

    await message.answer(
        "💰 Balans bölümi taýýarlanýar..."
    )


@router.message(F.text == "👥 Referral")
async def referral(message: Message):

    await update_last_active(message.from_user.id)

    await message.answer(
        "👥 Referral bölümi taýýarlanýar..."
    )


@router.message(F.text == "🆘 Goldaw")
async def support(message: Message):

    await update_last_active(message.from_user.id)

    await message.answer(
        "🆘 Goldaw bölümi taýýarlanýar..."
    )
