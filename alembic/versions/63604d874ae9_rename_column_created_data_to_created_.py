"""Rename column created_data to created_date in blogs table

Revision ID: 63604d874ae9
Revises: 6d2bafab7237
Create Date: 2021-07-01 11:40:14.475228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63604d874ae9'
down_revision = '6d2bafab7237'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('created_date', sa.DateTime(), nullable=True))
    op.drop_column('blogs', 'created_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('created_data', sa.DATETIME(), nullable=True))
    op.drop_column('blogs', 'created_date')
    # ### end Alembic commands ###