"""Created new table 'mailings_2'

Revision ID: edc6a0c77117
Revises: 962111077d92
Create Date: 2024-07-20 19:00:14.204272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edc6a0c77117'
down_revision: Union[str, None] = '962111077d92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mailings_2',
    sa.Column('id', sa.UUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('created_on_record', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('Europe/Kiev', now())"), nullable=False),
    sa.Column('update_on_record', sa.DateTime(), server_default=sa.text("TIMEZONE('Europe/Kiev', now())"), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('lead_id', sa.Integer(), nullable=False),
    sa.Column('count_loans', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('date_sent', sa.DateTime(timezone=True), nullable=False),
    sa.Column('campaign_category_id', sa.Integer(), nullable=False),
    sa.Column('campaign_category_name', sa.String(), nullable=False),
    sa.Column('campaign_id', sa.Integer(), nullable=False),
    sa.Column('campaign_name', sa.String(), nullable=False),
    sa.Column('sms_category_id', sa.Integer(), nullable=False),
    sa.Column('sms_category_name', sa.String(), nullable=False),
    sa.Column('sms_id', sa.Integer(), nullable=False),
    sa.Column('sms_name', sa.String(), nullable=False),
    sa.Column('campaign_lead_event_log_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('sms_stats_id', sa.Integer(), nullable=False),
    sa.Column('sms_version_id', sa.Integer(), nullable=True),
    sa.Column('source', sa.String(), nullable=False),
    sa.Column('source_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('promo_code', sa.String(), nullable=False),
    sa.Column('promo_code_id', sa.Integer(), nullable=False),
    sa.Column('mailing_type', sa.String(), nullable=False),
    sa.Column('mailing_name', sa.String(), nullable=False),
    sa.Column('mailing_category', sa.String(), nullable=True),
    sa.Column('additional_mailing_category', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_additional_mailing_category', 'mailings_2', ['additional_mailing_category'], unique=False)
    op.create_index('ix_date_sent', 'mailings_2', ['date_sent'], unique=False)
    op.create_index('ix_event_id', 'mailings_2', ['event_id'], unique=False)
    op.create_index('ix_lead_id', 'mailings_2', ['lead_id'], unique=False)
    op.create_index('ix_mailing_category', 'mailings_2', ['mailing_category'], unique=False)
    op.create_index('ix_mailing_name', 'mailings_2', ['mailing_name'], unique=False)
    op.create_index('ix_mailing_type', 'mailings_2', ['mailing_type'], unique=False)
    op.create_index('ix_phone', 'mailings_2', ['phone'], unique=False)
    op.create_index('ix_sms_id', 'mailings_2', ['sms_id'], unique=False)
    op.create_index('ix_sms_stats_id', 'mailings_2', ['sms_stats_id'], unique=True)
    op.create_index('ix_sms_version_id', 'mailings_2', ['sms_version_id'], unique=False)
    op.create_index('ix_user_id', 'mailings_2', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_id', table_name='mailings_2')
    op.drop_index('ix_sms_version_id', table_name='mailings_2')
    op.drop_index('ix_sms_stats_id', table_name='mailings_2')
    op.drop_index('ix_sms_id', table_name='mailings_2')
    op.drop_index('ix_phone', table_name='mailings_2')
    op.drop_index('ix_mailing_type', table_name='mailings_2')
    op.drop_index('ix_mailing_name', table_name='mailings_2')
    op.drop_index('ix_mailing_category', table_name='mailings_2')
    op.drop_index('ix_lead_id', table_name='mailings_2')
    op.drop_index('ix_id', table_name='mailings_2')
    op.drop_index('ix_event_id', table_name='mailings_2')
    op.drop_index('ix_date_sent', table_name='mailings_2')
    op.drop_index('ix_additional_mailing_category', table_name='mailings_2')
    op.drop_table('mailings_2')
    # ### end Alembic commands ###
