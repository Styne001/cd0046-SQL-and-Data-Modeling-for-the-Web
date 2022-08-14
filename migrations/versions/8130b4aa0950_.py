"""empty message

Revision ID: 8130b4aa0950
Revises: 8ca219a82ce1
Create Date: 2022-08-13 07:28:28.619553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8130b4aa0950'
down_revision = '8ca219a82ce1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('details',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('show_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['show_id'], ['show.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('artist_id', 'venue_id', 'show_id')
    )
    op.drop_table('venue_artist_show')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venue_artist_show',
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('show_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name='venue_artist_show_artist_id_fkey'),
    sa.ForeignKeyConstraint(['show_id'], ['show.id'], name='venue_artist_show_show_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], name='venue_artist_show_venue_id_fkey'),
    sa.PrimaryKeyConstraint('artist_id', 'venue_id', 'show_id', name='venue_artist_show_pkey')
    )
    op.drop_table('details')
    # ### end Alembic commands ###
