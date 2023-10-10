"""Renaming students to scholars

Revision ID: 5c58a02461f3
Revises: 791279dd0760
Create Date: 2023-10-10 10:46:56.644241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c58a02461f3'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('students', 'scholars')
