import aiosqlite
import os
from datetime import datetime

DB_PATH = "data/users.db"


async def connect():
    os.makedirs("data", exist_ok=True)
    return await aiosqlite.connect(DB_PATH)


async def create_tables():
    db = await connect()

    # Users
    await db.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        full_name TEXT,
        balance REAL DEFAULT 0,
        premium INTEGER DEFAULT 0,
        banned INTEGER DEFAULT 0,
        language TEXT DEFAULT 'tm',
        joined_at TEXT,
        last_active TEXT,
        referral_by INTEGER DEFAULT 0
    )
    """)

    # Payments
    await db.execute("""
    CREATE TABLE IF NOT EXISTS payments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount REAL,
        payment_type TEXT,
        status TEXT,
        created_at TEXT
    )
    """)

    # AI History
    await db.execute("""
    CREATE TABLE IF NOT EXISTS ai_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        action TEXT,
        file_id TEXT,
        created_at TEXT
    )
    """)

    # Broadcast
    await db.execute("""
    CREATE TABLE IF NOT EXISTS broadcasts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        admin_id INTEGER,
        text TEXT,
        created_at TEXT
    )
    """)

    # Logs
    await db.execute("""
    CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        level TEXT,
        message TEXT,
        created_at TEXT
    )
    """)

    await db.commit()
    await db.close()


async def add_user(user_id, username, full_name):
    db = await connect()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    await db.execute("""
    INSERT OR IGNORE INTO users(
        user_id,
        username,
        full_name,
        joined_at,
        last_active
    )
    VALUES(?,?,?,?,?)
    """, (
        user_id,
        username,
        full_name,
        now,
        now
    ))

    await db.commit()
    await db.close()

async def get_user(user_id):
    db = await connect()

    cursor = await db.execute("""
        SELECT * FROM users
        WHERE user_id = ?
    """, (user_id,))

    user = await cursor.fetchone()

    await db.close()

    return user


async def update_balance(user_id, amount):
    db = await connect()

    await db.execute("""
        UPDATE users
        SET balance = balance + ?
        WHERE user_id = ?
    """, (amount, user_id))

    await db.commit()
    await db.close()


async def set_balance(user_id, amount):
    db = await connect()

    await db.execute("""
        UPDATE users
        SET balance = ?
        WHERE user_id = ?
    """, (amount, user_id))

    await db.commit()
    await db.close()


async def ban_user(user_id):
    db = await connect()

    await db.execute("""
        UPDATE users
        SET banned = 1
        WHERE user_id = ?
    """, (user_id,))

    await db.commit()
    await db.close()


async def unban_user(user_id):
    db = await connect()

    await db.execute("""
        UPDATE users
        SET banned = 0
        WHERE user_id = ?
    """, (user_id,))

    await db.commit()
    await db.close()


async def set_premium(user_id, status=1):
    db = await connect()

    await db.execute("""
        UPDATE users
        SET premium = ?
        WHERE user_id = ?
    """, (status, user_id))

    await db.commit()
    await db.close()


async def get_users_count():
    db = await connect()

    cursor = await db.execute("""
        SELECT COUNT(*)
        FROM users
    """)

    count = await cursor.fetchone()

    await db.close()

    return count[0]
