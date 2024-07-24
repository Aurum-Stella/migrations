"""Change type column for 'mailings_2'

Revision ID: 9e588075ffc2
Revises: edc6a0c77117
Create Date: 2024-07-21 16:22:49.237614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e588075ffc2'
down_revision: Union[str, None] = 'edc6a0c77117'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
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


def downgrade() -> None:
    pass

