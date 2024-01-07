"""add content column to posts table

Revision ID: 7e678c15e692
Revises: fc1e2e261244
Create Date: 2024-01-07 21:15:38.032739

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7e678c15e692"
down_revision: Union[str, None] = "fc1e2e261244"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
