"""modify jobs table with new structure

Revision ID: modify_jobs_table
Revises: add_fields_zan_crew
Create Date: 2024-01-01 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'modify_jobs_table'
down_revision: Union[str, None] = 'add_fields_zan_crew'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Check if table exists
    from sqlalchemy import inspect
    
    conn = op.get_bind()
    inspector = inspect(conn)
    tables = inspector.get_table_names()
    
    if 'jobs' not in tables:
        return  # Table doesn't exist, nothing to migrate
    
    columns = [col['name'] for col in inspector.get_columns('jobs')]
    
    # Helper function to execute SQL with savepoint for error handling
    def execute_with_savepoint(sql_text):
        """Execute SQL in a savepoint to handle errors gracefully"""
        savepoint = conn.begin_nested()
        try:
            conn.execute(sa.text(sql_text))
            savepoint.commit()
        except Exception as e:
            savepoint.rollback()
            # Only print if it's not a "does not exist" type error
            if 'does not exist' not in str(e).lower() and 'already exists' not in str(e).lower():
                print(f"Warning: {e}")
    
    # Drop old columns if they exist
    for col_name in ['job_description', 'assigned_amount', 'job_loc', 'job_status']:
        if col_name in columns:
            execute_with_savepoint(f'ALTER TABLE jobs DROP COLUMN IF EXISTS {col_name}')
    
    # Drop old foreign key constraints
    fk_constraints = inspector.get_foreign_keys('jobs')
    for fk in fk_constraints:
        if 'user_id' in fk['constrained_columns']:
            execute_with_savepoint(f"ALTER TABLE jobs DROP CONSTRAINT IF EXISTS {fk['name']}")
    
    # Add new required columns
    new_required_columns = {
        'task_title': 'VARCHAR',
        'polished_task': 'TEXT',
        'location_address': 'TEXT',
        'latitude': 'VARCHAR',
        'longitude': 'VARCHAR',
        'scheduled_at': 'TIMESTAMP',
        'duration_hours': 'INTEGER',
        'duration_minutes': 'INTEGER',
        'estimated_cost_pence': 'INTEGER',
        'people_required': 'INTEGER',
        'actions': 'VARCHAR',
        'tags': 'VARCHAR',
        'payment_mode': 'VARCHAR',
        'payment_status': 'VARCHAR',
        'currency': 'VARCHAR',
        'pickup_adress': 'TEXT',
        'pickup_latitude': 'VARCHAR',
        'pickup_longitude': 'VARCHAR'
    }
    
    for col_name, col_type in new_required_columns.items():
        if col_name not in columns:
            execute_with_savepoint(f'ALTER TABLE jobs ADD COLUMN IF NOT EXISTS {col_name} {col_type}')
    
    # Add optional columns
    new_optional_columns = {
        'assigned_zancrew_user_id': 'INTEGER',
        'short_title': 'VARCHAR',
        'imp_notes': 'TEXT',
        'bucket': 'VARCHAR',
        'chat_room_id': 'VARCHAR'
    }
    
    for col_name, col_type in new_optional_columns.items():
        if col_name not in columns:
            execute_with_savepoint(f'ALTER TABLE jobs ADD COLUMN IF NOT EXISTS {col_name} {col_type}')
    
    # Ensure user_id column exists and is the correct type
    # First, verify zan_user table exists
    if 'zan_user' not in tables:
        print("Warning: zan_user table does not exist. Foreign key constraint will not be created.")
    else:
        # Check if user_id column exists in jobs table
        if 'user_id' not in columns:
            # Add user_id column if it doesn't exist
            execute_with_savepoint('ALTER TABLE jobs ADD COLUMN user_id INTEGER')
        
        # Drop old foreign key constraints that reference users table
        fk_constraints = inspector.get_foreign_keys('jobs')
        for fk in fk_constraints:
            if 'user_id' in fk['constrained_columns']:
                # Check if it references the old users table
                if fk.get('referred_table') == 'users':
                    execute_with_savepoint(f"ALTER TABLE jobs DROP CONSTRAINT IF EXISTS {fk['name']}")
        
        # Add new foreign key constraint to reference zan_user (only if it doesn't exist)
        inspector = inspect(conn)
        existing_fks = inspector.get_foreign_keys('jobs')
        fk_exists = any(
            fk['name'] == 'fk_jobs_zan_user_id' or 
            (fk.get('referred_table') == 'zan_user' and 'user_id' in fk['constrained_columns'])
            for fk in existing_fks
        )
        
        if not fk_exists:
            # Use explicit constraint creation
            savepoint = conn.begin_nested()
            try:
                conn.execute(sa.text(
                    "ALTER TABLE jobs ADD CONSTRAINT fk_jobs_zan_user_id "
                    "FOREIGN KEY (user_id) REFERENCES zan_user(user_id)"
                ))
                savepoint.commit()
                print("Successfully created foreign key constraint: fk_jobs_zan_user_id")
            except Exception as e:
                savepoint.rollback()
                # Check if constraint already exists with different name
                if 'already exists' in str(e).lower() or 'duplicate' in str(e).lower():
                    print(f"Foreign key constraint already exists: {e}")
                else:
                    print(f"Warning: Could not create foreign key constraint: {e}")
                    # Try to verify if constraint exists with different name
                    inspector = inspect(conn)
                    existing_fks = inspector.get_foreign_keys('jobs')
                    zan_user_fk = [fk for fk in existing_fks if fk.get('referred_table') == 'zan_user']
                    if zan_user_fk:
                        print(f"Foreign key to zan_user already exists: {zan_user_fk[0]['name']}")
    
    # Make required columns NOT NULL (only if column exists and has no NULL values)
    # Refresh inspector to get updated column list
    inspector = inspect(conn)
    columns = [col['name'] for col in inspector.get_columns('jobs')]
    
    required_cols = list(new_required_columns.keys())
    for col_name in required_cols:
        if col_name in columns:
            savepoint = conn.begin_nested()
            try:
                # First check if there are any NULL values
                result = conn.execute(sa.text(f"SELECT COUNT(*) FROM jobs WHERE {col_name} IS NULL"))
                null_count = result.scalar()
                if null_count == 0:
                    conn.execute(sa.text(f'ALTER TABLE jobs ALTER COLUMN {col_name} SET NOT NULL'))
                    savepoint.commit()
                else:
                    savepoint.rollback()
                    print(f"Warning: Column {col_name} has {null_count} NULL values. Cannot set NOT NULL.")
            except Exception as e:
                savepoint.rollback()
                print(f"Warning: Could not set NOT NULL for {col_name}: {e}")


def downgrade() -> None:
    # This is a complex migration, downgrade would require restoring old structure
    # For safety, we'll just note that downgrade is not fully supported
    pass

