"""empty message

Revision ID: 37046e7feb9e
Revises: d9f288d826ba
Create Date: 2024-05-17 16:19:26.917644

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37046e7feb9e'
down_revision: Union[str, None] = 'd9f288d826ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('post_id', sa.Integer(), nullable=False))
    op.drop_constraint('image_product_id_fkey', 'image', type_='foreignkey')
    op.create_foreign_key(None, 'image', 'product', ['product_id'], ['id'])
    op.create_foreign_key(None, 'image', 'post', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'image', type_='foreignkey')
    op.drop_constraint(None, 'image', type_='foreignkey')
    op.create_foreign_key('image_product_id_fkey', 'image', 'post', ['product_id'], ['id'])
    op.drop_column('image', 'post_id')
    # ### end Alembic commands ###
