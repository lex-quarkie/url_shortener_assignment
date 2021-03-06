"""empty message

Revision ID: 662b7b8b56e4
Revises: 
Create Date: 2020-11-07 07:49:50.806872

"""
from alembic import op
import sqlalchemy as sa


revision = "662b7b8b56e4"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "short_links",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("long_url", sa.String(255), nullable=False),
        sa.Column("short_url", sa.String(255), nullable=False),
        sa.Column("hits_count", sa.Integer(), default=0),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("short_links")
    # ### end Alembic commands ###
