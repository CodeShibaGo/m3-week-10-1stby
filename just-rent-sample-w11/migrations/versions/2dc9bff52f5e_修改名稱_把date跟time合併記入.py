"""修改名稱，把date跟time合併記入

Revision ID: 2dc9bff52f5e
Revises: e78fab029d81
Create Date: 2024-05-08 16:03:46.888727

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2dc9bff52f5e'
down_revision = 'e78fab029d81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pick_up_datetime', sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column('return_datetime', sa.DateTime(), nullable=False))
        batch_op.drop_column('return_time')
        batch_op.drop_column('pick_up_time')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pick_up_time', mysql.DATETIME(), nullable=False))
        batch_op.add_column(sa.Column('return_time', mysql.DATETIME(), nullable=False))
        batch_op.drop_column('return_datetime')
        batch_op.drop_column('pick_up_datetime')

    # ### end Alembic commands ###
