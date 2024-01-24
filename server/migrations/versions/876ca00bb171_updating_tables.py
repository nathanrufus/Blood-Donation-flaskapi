"""updating tables.

Revision ID: 876ca00bb171
Revises: 3e2d33e8fae9
Create Date: 2024-01-24 17:32:20.628020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '876ca00bb171'
down_revision = '3e2d33e8fae9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('donor',
    sa.Column('D_id', sa.Integer(), nullable=False),
    sa.Column('Dname', sa.String(length=100), nullable=True),
    sa.Column('Demail', sa.String(length=100), nullable=True),
    sa.Column('sex', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('donor_Date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('D_id')
    )
    op.drop_table('doners')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doners',
    sa.Column('D_id', sa.INTEGER(), nullable=False),
    sa.Column('Dname', sa.VARCHAR(length=100), nullable=True),
    sa.Column('Demail', sa.VARCHAR(length=100), nullable=True),
    sa.Column('sex', sa.VARCHAR(length=100), nullable=True),
    sa.Column('address', sa.VARCHAR(length=100), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('weight', sa.INTEGER(), nullable=True),
    sa.Column('donor_Date', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('D_id')
    )
    op.drop_table('donor')
    # ### end Alembic commands ###
