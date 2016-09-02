"""Adding users table

Revision ID: f80a0791e44d
Revises: None
Create Date: 2016-08-27 04:18:19.118409

"""

# revision identifiers, used by Alembic.
revision = 'f80a0791e44d'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('fbId', sa.String(length=250), nullable=True),
        sa.Column('email', sa.String(length=250), nullable=True),
        sa.Column('firstName', sa.String(length=250), nullable=True),
        sa.Column('lastName', sa.String(length=250), nullable=True),
        sa.Column('name', sa.String(length=250), nullable=True),
        sa.Column('gender', sa.String(length=250), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('fbId')
    )


def downgrade():
    op.drop_table('users')
