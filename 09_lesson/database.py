import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# ---- Строка подключения (ваши данные: логин postgres, пароль 1234567890, БД postgres) ----
DATABASE_URL = "postgresql://postgres:1234567890@localhost:5432/postgres"

# ---- Создаём движок ----
engine = create_engine(DATABASE_URL)

# ---- Фабрика сессий ----
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ---- Базовый класс для моделей ----
Base = declarative_base()

# ---- Определяем модель "Студент" ----
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"

# ---- Создаём таблицу в БД (если её нет) ----
Base.metadata.create_all(bind=engine)

