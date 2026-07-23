import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN
from database import create_tables

# Routers
from users.start import router as start_router
from users.profile import router as profile_router
from users.balance import router as balance_router
from users.referral import router as referral_router
from users.support import router as support_router

from admin.panel import router as admin_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)

dp = Dispatcher()


async def startup():
    await create_tables()
    logging.info("Database taýýar")


def register_routers():
    dp.include_router(start_router)
    dp.include_router(profile_router)
    dp.include_router(balance_router)
    dp.include_router(referral_router)
    dp.include_router(support_router)
    dp.include_router(admin_router)


async def main():
    await startup()

    register_routers()

    logging.info("Bot işe başlady")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
