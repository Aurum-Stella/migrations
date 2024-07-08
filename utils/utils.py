from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import delete
from config.connected import settings

# Создаем соединение с базой данных
engine = create_engine(settings.database_url)
Session = sessionmaker(bind=engine)
session = Session()


def deleted_all_data_in_table(table):
    try:
        session.query(table).delete()
        session.commit()
        print("Данные успешно удалены")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при удалении данных: {str(e)}")
    finally:
        session.close()


def get_all_subclasses(cls):
    all_subclasses = []
    all_name = []
    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))
    for subclass in all_subclasses:
        all_name.append(subclass.__tablename__)
    return all_name
