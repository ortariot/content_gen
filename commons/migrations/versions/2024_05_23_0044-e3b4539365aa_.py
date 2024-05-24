"""empty message

Revision ID: e3b4539365aa
Revises: 14ff749886f5
Create Date: 2024-05-23 00:44:04.586853

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3b4539365aa'
down_revision: Union[str, None] = '14ff749886f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('updated_at', sa.DateTime(), nullable=False))
    op.add_column('post', sa.Column('updated_at', sa.DateTime(), nullable=False))
    op.add_column('product', sa.Column('updated_at', sa.DateTime(), nullable=False))
    op.add_column('subject', sa.Column('updated_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subject', 'updated_at')
    op.drop_column('product', 'updated_at')
    op.drop_column('post', 'updated_at')
    op.drop_column('image', 'updated_at')
    # ### end Alembic commands ###
