"""renaming students to scholars

Revision ID: 18fca48523c8
Revises: 791279dd0760
Create Date: 2024-04-01 22:55:19.439283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18fca48523c8'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
