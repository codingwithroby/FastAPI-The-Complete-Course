"""create address_id to users

Revision ID: 6f5e34c4d2cb
Revises: cfc73bb0316c
Create Date: 2022-04-04 13:37:38.011143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f5e34c4d2cb'
down_revision = 'cfc73bb0316c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table="users", referent_table="address",
                          local_cols=['address_id'], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('address_users_fk', table_name="users")
    op.drop_column('users', 'address_id')
