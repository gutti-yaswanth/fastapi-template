"""make phone required and other fields optional in zan_user

Revision ID: make_phone_required
Revises: create_zan_user
Create Date: 2024-01-01 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'make_phone_required'
down_revision: Union[str, None] = 'create_zan_user'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Make first_name, last_name, email nullable (optional)
    op.alter_column('zan_user', 'first_name',
                    existing_type=sa.String(),
                    nullable=True)
    op.alter_column('zan_user', 'last_name',
                    existing_type=sa.String(),
                    nullable=True)
    op.alter_column('zan_user', 'email',
                    existing_type=sa.String(),
                    nullable=True)
    
    # Make phone required (not nullable)
    op.alter_column('zan_user', 'phone',
                    existing_type=sa.String(),
                    nullable=False)
    
    # Make is_zancrew nullable (optional)
    op.alter_column('zan_user', 'is_zancrew',
                    existing_type=sa.String(),
                    nullable=True,
                    server_default='false')


def downgrade() -> None:
    # Revert changes - make first_name, last_name, email required
    op.alter_column('zan_user', 'first_name',
                    existing_type=sa.String(),
                    nullable=False)
    op.alter_column('zan_user', 'last_name',
                    existing_type=sa.String(),
                    nullable=False)
    op.alter_column('zan_user', 'email',
                    existing_type=sa.String(),
                    nullable=False)
    
    # Make phone optional again
    op.alter_column('zan_user', 'phone',
                    existing_type=sa.String(),
                    nullable=True)
    
    # Make is_zancrew required again
    op.alter_column('zan_user', 'is_zancrew',
                    existing_type=sa.String(),
                    nullable=False,
                    server_default='false')

