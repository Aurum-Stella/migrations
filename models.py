from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from utils.custom_type import *
from utils.utils import get_all_subclasses


class Base(DeclarativeBase):
    metadata = MetaData()


class PlanAndFact(Base):
    __tablename__ = 'plan_and_fact'
    __table_args__ = {'extend_existing': True}
    id: Mapped[uuidpk]
    created_on_record: Mapped[created_on_record]
    update_on_record: Mapped[update_on_record]
    created_on: Mapped[created_on_date]
    report_type: Mapped[str_20]
    product_type: Mapped[str_20]
    plan_count: Mapped[int] = mapped_column()
    plan_sum: Mapped[int] = mapped_column()
    plan_average_duration: Mapped[int] = mapped_column(SmallInteger)
    fact_count: Mapped[int] = mapped_column(Integer(), nullable=True)
    fact_sum: Mapped[int] = mapped_column(Integer(), nullable=True)
    fact_average_duration: Mapped[int] = mapped_column(SmallInteger, nullable=True)


tablesUsed = get_all_subclasses(Base)
print(tablesUsed)


# alembic revision --autogenerate -m "Migration name"
# alembic upgrade head
# alembic downgrade -1
# alembic downgrade base очистить миграции


