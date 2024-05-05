"""add cars table

Revision ID: 122b86e489c0
Revises: 15a405c0b27f
Create Date: 2024-04-15 11:04:22.648668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '122b86e489c0'
down_revision = '15a405c0b27f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cars', schema=None) as batch_op:
        batch_op.add_column(sa.Column('displacement', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('Fuel_tank', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('suitcase', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cars', schema=None) as batch_op:
        batch_op.drop_column('suitcase')
        batch_op.drop_column('Fuel_tank')
        batch_op.drop_column('displacement')

    # ### end Alembic commands ###
