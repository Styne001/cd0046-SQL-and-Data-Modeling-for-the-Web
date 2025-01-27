"""empty message

Revision ID: 0d7c4eb3bb1a
Revises: 844f29251f1b
Create Date: 2022-08-13 20:45:34.776162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d7c4eb3bb1a'
down_revision = '844f29251f1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('details')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('details',
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('show_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name='details_artist_id_fkey'),
    sa.ForeignKeyConstraint(['show_id'], ['show.id'], name='details_show_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], name='details_venue_id_fkey'),
    sa.PrimaryKeyConstraint('artist_id', 'venue_id', 'show_id', name='details_pkey')
    )
    # ### end Alembic commands ###
