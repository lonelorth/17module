from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем движок базы данных
DATABASE_URL = 'sqlite:///taskmanager.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создаем базовый класс
Base = declarative_base()

# Создаем локальную сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
