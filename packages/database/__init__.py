from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from config import Config
from packages.database.models.base import Base

USER_DATABASE = Config.GetValue("DATABASE_USER")
PASS_DATABASE = Config.GetValue("DATABASE_PASS")
HOST_DATABASE = Config.GetValue("DATABASE_HOST")
PORT_DATABASE = Config.GetValue("DATABASE_PORT")
NAME_DATABASE = Config.GetValue("DATABASE_NAME")

URL_DATABASE = f"postgresql+asyncpg://{USER_DATABASE}:{PASS_DATABASE}@{HOST_DATABASE}:{PORT_DATABASE}/{NAME_DATABASE}"

engine = create_async_engine(URL_DATABASE, echo=False)

async_session_maker = async_sessionmaker(
    engine,
    # class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

@asynccontextmanager
async def get_session():
    session = async_session_maker()
    try:
        yield session
        await session.commit()

    except Exception as e:
        await session.rollback()
        raise e
    
    finally:
        await session.close()