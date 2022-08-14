"""empty message

Revision ID: e6dc8087ac00
Revises: b18d93d3e83c
Create Date: 2022-08-13 04:34:13.686739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6dc8087ac00'
down_revision = 'b18d93d3e83c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('show', 'start_time')
    op.drop_column('show', 'artist_id')
    op.drop_column('show', 'venue_id')
    op.drop_table('show')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('start_time', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
