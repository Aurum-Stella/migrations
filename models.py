from sqlalchemy import MetaData, Index
from sqlalchemy.orm import DeclarativeBase
from utils.custom_type import *
from utils.utils import get_all_subclasses


class Base(DeclarativeBase):
    metadata = MetaData()


class PlanAndFact(Base):
    __tablename__ = 'plan_and_fact'

    id: Mapped[uuid_pk_auto]
    created_on_record: Mapped[created_on_record_auto]
    update_on_record: Mapped[update_on_record]
    created_on: Mapped[created_on_date]
    report_type: Mapped[str_20]
    product_type: Mapped[str] = mapped_column(String(20), nullable=True)
    plan_count: Mapped[int] = mapped_column()
    plan_sum: Mapped[int] = mapped_column()
    plan_average_duration: Mapped[int] = mapped_column(SmallInteger)
    fact_count: Mapped[int] = mapped_column(Integer(), nullable=True)
    fact_sum: Mapped[int] = mapped_column(Integer(), nullable=True)
    fact_average_duration: Mapped[int] = mapped_column(SmallInteger, nullable=True)

    __table_args__ = (
        Index('ix_id', 'id'),
        Index('ix_created_on', 'created_on'),
        Index('ix_created_on_&_report_type_&_product_type', 'created_on', 'report_type', 'product_type'),

        {'extend_existing': True},)


tablesUsed = get_all_subclasses(Base)
print(tablesUsed)

# alembic revision --autogenerate -m "Migration name"
# alembic upgrade head
# alembic downgrade -1
# alembic downgrade base очистить миграции
