"""rename department

Revision ID: d56eac7674ae
Revises: 47c1b38285d7
Create Date: 2024-04-07 12:47:24.707525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd56eac7674ae'
down_revision = '47c1b38285d7'
branch_labels = None
depends_on = None


op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###