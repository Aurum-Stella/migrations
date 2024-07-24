from sqlalchemy import MetaData, Index
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.types import Numeric
from utils.custom_type import *
from utils.utils import get_all_subclasses, deleted_all_data_in_table


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
    plan_sum: Mapped[float] = mapped_column(Numeric(12, 2))
    plan_average_duration: Mapped[float] = mapped_column(Numeric(12, 2), nullable=True)
    fact_count: Mapped[int] = mapped_column(Integer(), nullable=True)
    fact_sum: Mapped[float] = mapped_column(Numeric(12, 2), nullable=True)
    fact_average_duration: Mapped[float] = mapped_column(Numeric(12, 2), nullable=True)

    __table_args__ = (
        Index('ix_id', 'id'),
        Index('ix_created_on', 'created_on'),
        Index('ix_created_on_&_report_type_&_product_type', 'created_on', 'report_type', 'product_type'),

        {'extend_existing': True},)


class AllMailings(Base):
    __tablename__ = 'mailings_2'

    id: Mapped[uuid_pk_auto]
    created_on_record: Mapped[created_on_record_auto]
    update_on_record: Mapped[update_on_record]

    user_id: Mapped[uuid_]
    lead_id: Mapped[int] = mapped_column()
    count_loans: Mapped[int] = mapped_column()
    phone: Mapped[str_20]
    date_sent: Mapped[created_on_datetime]
    campaign_category_id: Mapped[int] = mapped_column()
    campaign_category_name: Mapped[str] = mapped_column()
    campaign_id: Mapped[int] = mapped_column()
    campaign_name: Mapped[str] = mapped_column()
    sms_category_id: Mapped[int] = mapped_column()
    sms_category_name: Mapped[str] = mapped_column()
    sms_id: Mapped[int] = mapped_column()
    sms_name: Mapped[str] = mapped_column()
    campaign_event_id: Mapped[int] = mapped_column()
    sms_stats_id: Mapped[int] = mapped_column(unique=True)
    sms_version_id: Mapped[int] = mapped_column(nullable=True)
    source: Mapped[str] = mapped_column()
    source_id: Mapped[int] = mapped_column()
    status: Mapped[str] = mapped_column()
    promo_code: Mapped[str] = mapped_column(nullable=True)
    promo_code_id: Mapped[uuid_null]
    mailing_type: Mapped[str] = mapped_column()
    mailing_name: Mapped[str] = mapped_column()
    mailing_category: Mapped[str] = mapped_column(nullable=True)
    additional_mailing_category: Mapped[str] = mapped_column(nullable=True)
    event_mailing_date: Mapped[created_on_date_null]
    start_offer_period: Mapped[created_on_date_null]
    end_offer_period: Mapped[created_on_date_null]

    __table_args__ = (

        Index('ix_user_id', 'user_id'),
        Index('ix_lead_id', 'lead_id'),
        Index('ix_phone', 'phone'),
        Index('ix_date_sent', 'date_sent'),
        Index('ix_sms_id', 'sms_id'),

        Index('ix_sms_campaign_event_id', 'campaign_event_id'),
        Index('ix_sms_stats_id', 'sms_stats_id', unique=True),
        Index('ix_sms_version_id', 'sms_version_id'),
        Index('ix_mailing_name', 'mailing_name'),
        Index('ix_mailing_type', 'mailing_type'),
        Index('ix_mailing_category', 'mailing_category'),
        Index('ix_additional_mailing_category', 'additional_mailing_category'),

        {'extend_existing': True},)


tablesUsed = get_all_subclasses(Base)

print(tablesUsed)

deleted_all_data_in_table(AllMailings)

# alembic revision --autogenerate -m "Migration name"
# alembic upgrade head
# alembic downgrade -1
# alembic downgrade base очистить миграции
