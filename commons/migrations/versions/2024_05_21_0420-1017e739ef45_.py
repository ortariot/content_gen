"""empty message

Revision ID: 1017e739ef45
Revises: f3a45ddb8bf0
Create Date: 2024-05-21 04:20:14.866253

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1017e739ef45'
down_revision: Union[str, None] = 'f3a45ddb8bf0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('in_progress', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('image', 'in_progress')
    # ### end Alembic commands ###
