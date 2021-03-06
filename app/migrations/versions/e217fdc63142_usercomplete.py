"""usercomplete

Revision ID: e217fdc63142
Revises: 85c806d0a6ab
Create Date: 2020-06-19 05:22:22.788594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e217fdc63142'
down_revision = '85c806d0a6ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('firstname', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('lastname', sa.String(length=80), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'firstname')
    # ### end Alembic commands ###
