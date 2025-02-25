"""delete some columns 'mailings_2'

Revision ID: 5fdce3479302
Revises: a02df0705e8b
Create Date: 2024-07-24 17:45:21.138561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5fdce3479302'
down_revision: Union[str, None] = 'a02df0705e8b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_additional_mailing_category', table_name='mailings_2')
    op.drop_index('ix_mailing_category', table_name='mailings_2')
    op.drop_column('mailings_2', 'additional_mailing_category')
    op.drop_column('mailings_2', 'end_offer_period')
    op.drop_column('mailings_2', 'event_mailing_date')
    op.drop_column('mailings_2', 'mailing_category')
    op.drop_column('mailings_2', 'start_offer_period')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    op.add_column('mailings_2', sa.Column('start_offer_period', sa.DATE(), autoincrement=False, nullable=True))
    op.add_column('mailings_2', sa.Column('mailing_category', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('mailings_2', sa.Column('event_mailing_date', sa.DATE(), autoincrement=False, nullable=True))
    op.add_column('mailings_2', sa.Column('end_offer_period', sa.DATE(), autoincrement=False, nullable=True))
    op.add_column('mailings_2', sa.Column('additional_mailing_category', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('ix_mailing_category', 'mailings_2', ['mailing_category'], unique=False)
    op.create_index('ix_additional_mailing_category', 'mailings_2', ['additional_mailing_category'], unique=False)
    # ### end Alembic commands ###
