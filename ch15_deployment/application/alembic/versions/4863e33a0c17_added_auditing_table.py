"""Added Auditing table

Revision ID: 4863e33a0c17
Revises: b81bb3edc213
Create Date: 2020-02-17 14:27:36.742299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4863e33a0c17'
down_revision = 'b81bb3edc213'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auditing',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_auditing_created_date'), 'auditing', ['created_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_auditing_created_date'), table_name='auditing')
    op.drop_table('auditing')
    # ### end Alembic commands ###
