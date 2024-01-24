"""Blood table.

Revision ID: 107dd64d47f1
Revises: b488aff91352
Create Date: 2024-01-24 16:59:19.094959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '107dd64d47f1'
down_revision = 'b488aff91352'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blood',
    sa.Column('b_code', sa.Integer(), nullable=False),
    sa.Column('D_id', sa.Integer(), nullable=True),
    sa.Column('packets', sa.Integer(), nullable=True),
    sa.Column('B_group', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('b_code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blood')
    # ### end Alembic commands ###
