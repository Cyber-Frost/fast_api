"""add foreign key to posts table

Revision ID: 5af6e13525b9
Revises: 30e378e329e2
Create Date: 2024-01-07 21:31:11.699036

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5af6e13525b9"
down_revision: Union[str, None] = "30e378e329e2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer, nullable=False))
    op.create_foreign_key(
        "posts_users_fkey", "posts", "users", ["owner_id"], ["id"], ondelete="CASCADE"
    )


def downgrade() -> None:
    op.drop_constraint("posts_users_fkey", "posts")
    op.drop_column("posts", "owner_id")
