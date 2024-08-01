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
        Index('plan_and_fact_pkey', 'id'),
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
    campaign_category_id: Mapped[int] = mapped_column(nullable=True)
    campaign_category_name: Mapped[str] = mapped_column(nullable=True)
    campaign_id: Mapped[int] = mapped_column(nullable=True)
    campaign_name: Mapped[str] = mapped_column(nullable=True)
    sms_category_id: Mapped[int] = mapped_column()
    sms_category_name: Mapped[str] = mapped_column()
    sms_id: Mapped[int] = mapped_column()
    sms_name: Mapped[str] = mapped_column()
    campaign_event_id: Mapped[int] = mapped_column(nullable=True)
    sms_stats_id: Mapped[int] = mapped_column(unique=True)
    sms_version_id: Mapped[int] = mapped_column(nullable=True)
    source: Mapped[str] = mapped_column()
    source_id: Mapped[int] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column()
    promo_code: Mapped[str] = mapped_column(nullable=True)
    promo_code_id: Mapped[uuid_null]
    mailing_type: Mapped[str] = mapped_column()
    mailing_name: Mapped[str] = mapped_column()

    __table_args__ = (
        Index('mailings2_ix_id', 'id'),
        Index('mailings2_ix_user_id', 'user_id'),
        Index('mailings2_ix_lead_id', 'lead_id'),
        Index('mailings2_ix_phone', 'phone'),
        Index('mailings2_ix_date_sent', 'date_sent'),
        Index('mailings2_ix_sms_id', 'sms_id'),
        Index('mailings2_ix_sms_campaign_event_id', 'campaign_event_id'),
        Index('mailings2_ix_sms_stats_id', 'sms_stats_id', unique=True),
        Index('mailings2_ix_sms_version_id', 'sms_version_id'),
        Index('mailings2_ix_mailing_name', 'mailing_name'),
        Index('mailings2_ix_mailing_type', 'mailing_type'),

        {'extend_existing': True},)


class MaillingsEvents(Base):
    __tablename__ = 'mailings_events'

    id: Mapped[uuid_pk_auto]
    created_on_record: Mapped[created_on_record_auto]
    update_on_record: Mapped[update_on_record]
    mailing_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("mailings_2.id"), nullable=True)
    mailing_category: Mapped[str_40] = mapped_column(nullable=True)
    additional_mailing_category: Mapped[str_40] = mapped_column(nullable=True)
    event_mailing_date: Mapped[created_on_datetime]
    type_offer: Mapped[str_40] = mapped_column(nullable=True)
    start_offer_period: Mapped[created_on_datetime]
    end_offer_period: Mapped[created_on_datetime] = mapped_column(nullable=True)
    object_offer_id: Mapped[uuid.UUID] = mapped_column(nullable=True)
    accepted_offer_date: Mapped[created_on_datetime] = mapped_column(nullable=True)
    mailing_group_id: Mapped[uuid.UUID] = mapped_column(nullable=True)

    __table_args__ = (
        Index('mailings_events_ix_mailing_id', 'mailing_id'),
        Index('mailings_events_ix_object_offer_id', 'object_offer_id'),
        Index('mailings_events_ix_object_mailing_group_id', 'mailing_group_id'),
        {'extend_existing': True},
    )


class WriteOffs(Base):
    __tablename__ = 'write_offs'

    id: Mapped[uuid_pk_auto]
    created_on_record: Mapped[created_on_record_auto]
    update_on_record: Mapped[update_on_record]
    user_id: Mapped[uuid.UUID] = mapped_column()
    client_name: Mapped[str] = mapped_column()
    identification_number: Mapped[int] = mapped_column()
    loan_id: Mapped[uuid.UUID] = mapped_column()
    contract_number: Mapped[int] = mapped_column()
    loan_signed_date: Mapped[created_on_datetime] = mapped_column()
    write_off_date: Mapped[created_on_date] = mapped_column()
    contract_amount: Mapped[float] = mapped_column()
    write_off_amount: Mapped[float] = mapped_column()
    write_off_reason: Mapped[str] = mapped_column()
    write_off_comments: Mapped[str] = mapped_column()

    __table_args__ = (
        Index('write_offs_ix_user_id', 'user_id'),
        Index('write_offs_ix_identification_number', 'identification_number'),
        Index('write_offs_ix_loan_id', 'loan_id'),
        Index('write_offs_ix_contract_number', 'contract_number'),
        Index('write_offs_ix_write_off_reason', 'write_off_reason'),
        {'extend_existing': True},)


tablesUsed = get_all_subclasses(Base)

print(tablesUsed)

# deleted_all_data_in_table(AllMailings)

# alembic revision --autogenerate -m "Migration name"
# alembic upgrade head
# alembic downgrade -1
# alembic downgrade base очистить миграции
