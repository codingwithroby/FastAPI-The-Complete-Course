"""create phone number for user col

Revision ID: 4197fee3d64d
Revises: 
Create Date: 2022-04-04 12:59:01.829969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4197fee3d64d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade():
    op.drop_column('users', 'phone_number')
