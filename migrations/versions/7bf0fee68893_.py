"""empty message

Revision ID: 7bf0fee68893
Revises: 
Create Date: 2017-11-05 08:44:55.711766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bf0fee68893'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('admin', sa.Boolean(), nullable=False))
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=False))
    op.add_column('users', sa.Column('confirmed_on', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('registered_on', sa.DateTime(), nullable=False))
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_column('users', 'registered_on')
    op.drop_column('users', 'confirmed_on')
    op.drop_column('users', 'confirmed')
    op.drop_column('users', 'admin')
    # ### end Alembic commands ###