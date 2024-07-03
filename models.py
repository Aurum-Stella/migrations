from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import registry, mapped_column, Mapped, DeclarativeBase
from utils.custom_type import uuidpk
from utils.utils import get_all_subclasses


class Base(DeclarativeBase):
    metadata = MetaData()
    # metadata.reflect(get_test_engine(), only=tablesUsed)


class TestTable1(Base):
    __tablename__ = 'test_table4'
    __table_args__ = {'extend_existing': True}
    id: Mapped[uuidpk] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column()
    user_name: Mapped[str] = mapped_column()

    user_name2: Mapped[str] = mapped_column()

tablesUsed = get_all_subclasses(Base)
print(tablesUsed)


# alembic revision --autogenerate -m "Migration name"
# alembic upgrade head
# alembic downgrade -1
# alembic downgrade base очистить миграции


