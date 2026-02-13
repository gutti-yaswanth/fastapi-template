"""add new fields to zan_crew table

Revision ID: add_fields_zan_crew
Revises: create_zan_crew
Create Date: 2024-01-01 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'add_fields_zan_crew'
down_revision: Union[str, None] = 'create_zan_crew'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Check if table exists
    from sqlalchemy import inspect
    conn = op.get_bind()
    inspector = inspect(conn)
    tables = inspector.get_table_names()
    
    if 'zan_crew' in tables:
        # Check which columns already exist
        columns = [col['name'] for col in inspector.get_columns('zan_crew')]
        
        # Add new columns only if they don't exist
        if 'radius_km' not in columns:
            op.add_column('zan_crew', sa.Column('radius_km', sa.Float(), nullable=True))
        if 'work_hours' not in columns:
            op.add_column('zan_crew', sa.Column('work_hours', sa.String(), nullable=True))
        if 'kyc_verified' not in columns:
            op.add_column('zan_crew', sa.Column('kyc_verified', sa.String(), nullable=True))
        if 'is_online' not in columns:
            op.add_column('zan_crew', sa.Column('is_online', sa.String(), nullable=True))
        if 'payout_beneficiary_id' not in columns:
            op.add_column('zan_crew', sa.Column('payout_beneficiary_id', sa.String(), nullable=True))
        if 'bank_account' not in columns:
            op.add_column('zan_crew', sa.Column('bank_account', sa.String(), nullable=True))
        if 'ifsc_code' not in columns:
            op.add_column('zan_crew', sa.Column('ifsc_code', sa.String(), nullable=True))
        if 'home_lat' not in columns:
            op.add_column('zan_crew', sa.Column('home_lat', sa.String(), nullable=True))
        if 'home_lng' not in columns:
            op.add_column('zan_crew', sa.Column('home_lng', sa.String(), nullable=True))
        if 'idfy_refs' not in columns:
            op.add_column('zan_crew', sa.Column('idfy_refs', sa.Text(), nullable=True))
        if 'pan_name' not in columns:
            op.add_column('zan_crew', sa.Column('pan_name', sa.String(), nullable=True))
        if 'pan_number_last4' not in columns:
            op.add_column('zan_crew', sa.Column('pan_number_last4', sa.String(), nullable=True))
        if 'aadhaar_verified' not in columns:
            op.add_column('zan_crew', sa.Column('aadhaar_verified', sa.String(), nullable=True))
        if 'aadhaar_last4' not in columns:
            op.add_column('zan_crew', sa.Column('aadhaar_last4', sa.String(), nullable=True))
        if 'aadhar_city' not in columns:
            op.add_column('zan_crew', sa.Column('aadhar_city', sa.String(), nullable=True))
        if 'face_match_score' not in columns:
            op.add_column('zan_crew', sa.Column('face_match_score', sa.Float(), nullable=True))
        if 'face_verified' not in columns:
            op.add_column('zan_crew', sa.Column('face_verified', sa.String(), nullable=True))
        if 'selfie_img_url' not in columns:
            op.add_column('zan_crew', sa.Column('selfie_img_url', sa.Text(), nullable=True))


def downgrade() -> None:
    # Check if table exists
    from sqlalchemy import inspect
    conn = op.get_bind()
    inspector = inspect(conn)
    tables = inspector.get_table_names()
    
    if 'zan_crew' in tables:
        columns = [col['name'] for col in inspector.get_columns('zan_crew')]
        
        # Drop columns only if they exist
        if 'selfie_img_url' in columns:
            op.drop_column('zan_crew', 'selfie_img_url')
        if 'face_verified' in columns:
            op.drop_column('zan_crew', 'face_verified')
        if 'face_match_score' in columns:
            op.drop_column('zan_crew', 'face_match_score')
        if 'aadhar_city' in columns:
            op.drop_column('zan_crew', 'aadhar_city')
        if 'aadhaar_last4' in columns:
            op.drop_column('zan_crew', 'aadhaar_last4')
        if 'aadhaar_verified' in columns:
            op.drop_column('zan_crew', 'aadhaar_verified')
        if 'pan_number_last4' in columns:
            op.drop_column('zan_crew', 'pan_number_last4')
        if 'pan_name' in columns:
            op.drop_column('zan_crew', 'pan_name')
        if 'idfy_refs' in columns:
            op.drop_column('zan_crew', 'idfy_refs')
        if 'home_lng' in columns:
            op.drop_column('zan_crew', 'home_lng')
        if 'home_lat' in columns:
            op.drop_column('zan_crew', 'home_lat')
        if 'ifsc_code' in columns:
            op.drop_column('zan_crew', 'ifsc_code')
        if 'bank_account' in columns:
            op.drop_column('zan_crew', 'bank_account')
        if 'payout_beneficiary_id' in columns:
            op.drop_column('zan_crew', 'payout_beneficiary_id')
        if 'is_online' in columns:
            op.drop_column('zan_crew', 'is_online')
        if 'kyc_verified' in columns:
            op.drop_column('zan_crew', 'kyc_verified')
        if 'work_hours' in columns:
            op.drop_column('zan_crew', 'work_hours')
        if 'radius_km' in columns:
            op.drop_column('zan_crew', 'radius_km')

