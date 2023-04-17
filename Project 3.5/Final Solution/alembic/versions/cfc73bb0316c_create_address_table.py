"""Create address table

Revision ID: cfc73bb0316c
Revises: 4197fee3d64d
Create Date: 2022-04-04 13:28:56.888999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfc73bb0316c'
down_revision = '4197fee3d64d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(), nullable=False),
                    sa.Column('address2', sa.String(), nullable=False),
                    sa.Column('city', sa.String(), nullable=False),
                    sa.Column('state', sa.String(), nullable=False),
                    sa.Column('country', sa.String(), nullable=False),
                    sa.Column('postalcode', sa.String(), nullable=False)
                    )


def downgrade():
    op.drop_table('address')
