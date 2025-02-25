"""Created table 'plan_and_fact'

Revision ID: e4332761c305
Revises: 
Create Date: 2024-07-03 17:05:20.901780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4332761c305'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plan_and_fact',
    sa.Column('id', sa.UUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('created_on_record', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('Europe/Kiev', now())"), nullable=False),
    sa.Column('update_on_record', sa.DateTime(), server_default=sa.text("TIMEZONE('Europe/Kiev', now())"), nullable=False),
    sa.Column('created_on', sa.DATE(), nullable=False),
    sa.Column('report_type', sa.String(), nullable=False),
    sa.Column('product_type', sa.String(), nullable=False),
    sa.Column('plan_count', sa.Integer(), nullable=False),
    sa.Column('plan_sum', sa.Integer(), nullable=False),
    sa.Column('plan_average_duration', sa.SmallInteger(), nullable=False),
    sa.Column('fact_count', sa.Integer(), nullable=True),
    sa.Column('fact_sum', sa.Integer(), nullable=True),
    sa.Column('fact_average_duration', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plan_and_fact')
    # ### end Alembic commands ###
