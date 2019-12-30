"""Add status, remove project_id from batch_job

Revision ID: 72a8672de06b
Revises: 4caad3cdf31e
Create Date: 2018-12-20 03:42:30.993341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72a8672de06b'
down_revision = '4caad3cdf31e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('batch_job', sa.Column('status', sa.VARCHAR(length=15), nullable=True))
    op.drop_column('batch_job', 'project_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('batch_job', sa.Column('project_id', sa.VARCHAR(length=50), server_default=sa.text(u'NULL'), nullable=True))
    op.drop_column('batch_job', 'status')
    # ### end Alembic commands ###