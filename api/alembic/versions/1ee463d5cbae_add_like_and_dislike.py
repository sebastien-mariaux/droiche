"""add like and dislike

Revision ID: 1ee463d5cbae
Revises: 
Create Date: 2020-11-08 12:02:52.000292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ee463d5cbae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('subjects', sa.Column('likes_count', sa.Integer))
    op.add_column('subjects', sa.Column('dislikes_count', sa.Integer))

    op.execute('UPDATE subjects SET likes_count=0, dislikes_count=0')


def downgrade():
    op.drop_column('subjects', 'likes_count')
    op.drop_column('subjects', 'dislikes_count')
