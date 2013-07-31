"""create user table, user_connection table, 
user_to_lesson table, rating table

Revision ID: 4919f045eddf
Revises: 1a27a3453938
Create Date: 2013-07-30 14:28:07.484773

"""

# revision identifiers, used by Alembic.
revision = '4919f045eddf'
down_revision = '1a27a3453938'

from alembic import op
import sqlalchemy as sa


def upgrade():
	# TODO: check timestamp types
	op.create_table(
		'user',
		sa.Column('id', sa.Integer, primary_key=True),
		# email instead of name
		sa.Column('email', sa.Unicode(), unique=True, nullable=False),
		# TODO: find out specifics of what to save for pw
		sa.Column('password', sa.Unicode(), nullable=False)
		)
	op.create_table(
		'user_connection',
		sa.Column('id', sa.Integer, primary_key=True),
		sa.Column('user_id', sa.Integer),
		sa.Column('service', sa.Unicode(), nullable=False),
		sa.Column('access_token', sa.Unicode(), nullable=False)
		)
	op.create_table(
		'user_to_lesson',
		sa.Column('uid', sa.Integer, foreign_key=True),
		sa.Column('lessonid', sa.Integer, foreign_key=True),
		sa.Column('start_dt', sa.Integer, nullable=False),
		sa.Column('end_dt', sa.Integer, nullable=False)
		)
	op.create_table(
		'rating',
		sa.Column('uid', sa.Integer, foreign_key=True),
		sa.Column('subject_id', sa.Integer),
		sa.Column('subject_type', sa.Unicode()),
		sa.Column('rating', sa.Integer),
		# TODO: find out syntax of timestamp and default to now
		sa.Column('time_stamp', sa.TIME())
		)


def downgrade():
    pass
