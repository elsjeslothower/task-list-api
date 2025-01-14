"""adds Goal model

Revision ID: 1bcbd1d13c96
Revises: b2a08c6a0752
Create Date: 2022-11-09 15:46:59.958702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bcbd1d13c96'
down_revision = 'b2a08c6a0752'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###
