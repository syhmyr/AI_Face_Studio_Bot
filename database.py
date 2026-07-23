import aiosqlite

DB_NAME = "data/users.db"

async def connect():
    return await aiosqlite.connect(DB_NAME)
