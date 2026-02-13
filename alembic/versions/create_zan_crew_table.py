"""create zan_crew table

Revision ID: create_zan_crew
Revises: make_phone_required
Create Date: 2024-01-01 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'create_zan_crew'
down_revision: Union[str, None] = 'make_phone_required'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Check if table already exists (in case it was created by SQLAlchemy create_all)
    from sqlalchemy import inspect
    conn = op.get_bind()
    inspector = inspect(conn)
    tables = inspector.get_table_names()
    
    if 'zan_crew' not in tables:
        # Create zan_crew table only if it doesn't exist
        op.create_table(
            'zan_crew',
            sa.Column('zancrew_id', sa.Integer(), nullable=False),
            sa.Column('phone', sa.String(), nullable=False),
            sa.Column('pan_id', sa.String(), nullable=True),
            sa.Column('adhar_id', sa.String(), nullable=True),
            sa.Column('birth_date', sa.DateTime(), nullable=True),
            sa.Column('city', sa.String(), nullable=True),
            sa.Column('state', sa.String(), nullable=True),
            sa.Column('country', sa.String(), nullable=True),
            sa.Column('latitude', sa.String(), nullable=True),
            sa.Column('longitude', sa.String(), nullable=True),
            sa.Column('martial_status', sa.String(), nullable=True),
            sa.Column('zan_user_id', sa.Integer(), nullable=False),
            sa.Column('status', sa.String(), nullable=True),
            sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
            sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
            sa.PrimaryKeyConstraint('zancrew_id'),
            sa.ForeignKeyConstraint(['zan_user_id'], ['zan_user.user_id'], )
        )
    # If table already exists, migration is considered successful (table was created manually or by create_all)


def downgrade() -> None:
    # Check if table exists before dropping
    from sqlalchemy import inspect
    conn = op.get_bind()
    inspector = inspect(conn)
    tables = inspector.get_table_names()
    
    if 'zan_crew' in tables:
        op.drop_table('zan_crew')

