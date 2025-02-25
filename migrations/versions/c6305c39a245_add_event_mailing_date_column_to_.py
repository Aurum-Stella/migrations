"""add event_mailing_date column to 'mailings_2'

Revision ID: c6305c39a245
Revises: 2efd4e043667
Create Date: 2024-07-22 21:22:26.639377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6305c39a245'
down_revision: Union[str, None] = '2efd4e043667'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mailings_2', sa.Column('event_mailing_date', sa.DATE(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mailings_2', 'event_mailing_date')
    # ### end Alembic commands ###
