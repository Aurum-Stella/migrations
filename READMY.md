### Модели и миграции.
Идея в том что бы хранить и создавать метаданные - модель таблицы ее структуру, поля, индексы связи, соединяем ее с другими таблицами,  
делаем миграции. Тут будет храниться и обновляться схема всей базы.
*(Не всей базы, а определенных таблиц, об этом ниже)*


### Структура:
##### Подкаталог `config` содержит конфигурации по подключению и работе с AWS_Lambda.  По большей части там менять ничего не нужно:
1. `config/aws_settings.py` - настройки для AWS-Lambda. Они - нужны, зачем - не знаю.
2. `config/connected.py` - содержит класс Settings который создает нужное подключение к БД.
##### Подкаталог `migrations` содержит файлы миграций и их конфиги.
1. `/versions/` - каталог который содержит инфу о том, что произойдет после применении миграции, ну и собственно все  
примененный миграции по базе. Обязательно проверять что там указано перед применением миграции;
2. Остальные файлы в этом каталоге это конфиги миграций и тд. Об этом лучше почитать в документации `Alembic`;
* Файл `models.py` хранит в себе модели.
* Файл `alembic.ini` это конфигурация алембика, трогать не нужно.




https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html
```python
import datetime

from sqlalchemy import BIGINT, Integer, NVARCHAR, String, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, registry


class Base(DeclarativeBase):
    type_annotation_map = {
        int: BIGINT,
        datetime.datetime: TIMESTAMP(timezone=True),
        str: String().with_variant(NVARCHAR, "mssql"),
    }


class SomeClass(Base):
    __tablename__ = "some_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime.datetime]
    status: Mapped[str]
```