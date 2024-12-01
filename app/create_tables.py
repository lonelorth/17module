from app.backend.db import engine, Base
from models.user import User
from models.task import Task

# Создаем таблицы
Base.metadata.create_all(bind=engine)

# Выводим SQL запросы
print("SQL для User:")
print(User.__table__.create(engine))

print("SQL для Task:")
print(Task.__table__.create(engine))