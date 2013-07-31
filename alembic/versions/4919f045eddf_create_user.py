"""create user table, user_connection table, 
user_to_lesson table

Revision ID: 4919f045eddf
Revises: 1a27a3453938
Create Date: 2013-07-30 14:28:07.484773

"""

# revision identifiers, used by Alembic.
revision = '4919f045eddf'
down_revision = '1a27a3453938'

from alembic import op
import sqlalchemy as sa
from datetime import datetime


def upgrade():
	op.create_table(
		'user',
		sa.Column('id', sa.Integer, primary_key=True),
		sa.Column('email', sa.Unicode(), unique=True, nullable=False),
		sa.Column('password_digest', sa.Unicode(), nullable=False)
		)
	op.create_table(
		'connection',
		sa.Column('id', sa.Integer, primary_key=True),
		sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id')),
		sa.Column('service', sa.Unicode(), nullable=False),
		sa.Column('access_token', sa.Unicode(), nullable=False)
		)
	# TODO: implement the association between user and lesson
	op.create_table(
		'user_to_lesson',
		sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id')),
		sa.Column('lesson_id', sa.Integer, sa.ForeignKey('lesson.id')),
		sa.Column('start_dt', sa.DateTime(timezone=True),
			default=datetime.utcnow()),
		sa.Column('end_dt', sa.DateTime(timezone=True))
		)
	# TODO: Redesign steps/lessons to make them disjoin subtypes
	#       This will enable relationship Rating -> (step | lesson)

	# op.create_table(
	# 	'rating',
	# 	sa.Column('uid', sa.Integer, foreign_key=True),
	# 	sa.Column('subject_id', sa.Integer),
	# 	sa.Column('subject_type', sa.Unicode()),
	# 	sa.Column('rating', sa.Integer),
	# 	# TODO: find out syntax of timestamp and default to now
	# 	sa.Column('time_stamp', sa.TIME())
	# 	)


def downgrade():
	op.drop_table('user')
	op.drop_table('connection')
	op.drop_table('user_to_lesson')
