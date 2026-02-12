# Database Migration Guide

This project uses Alembic for database migrations. This guide explains how to use it.

## Setup

1. Install Alembic (if not already installed):
```bash
pip install alembic
```

2. Verify Alembic is configured:
```bash
alembic current
```

## Common Commands

### Create a New Migration

To create a new migration after making changes to your models:

```bash
alembic revision --autogenerate -m "description of your changes"
```

Example:
```bash
alembic revision --autogenerate -m "add job_loc and job_status to jobs table"
```

**Important:** Always review the generated migration file before applying it!

### Apply Migrations

To apply all pending migrations:

```bash
alembic upgrade head
```

To apply migrations up to a specific revision:

```bash
alembic upgrade <revision_id>
```

### Rollback Migrations

To rollback the last migration:

```bash
alembic downgrade -1
```

To rollback to a specific revision:

```bash
alembic downgrade <revision_id>
```

### Check Migration Status

View current database revision:

```bash
alembic current
```

View migration history:

```bash
alembic history
```

View detailed history:

```bash
alembic history --verbose
```

## Workflow

### Adding a New Field to an Existing Table

1. Update your model in `infrastructure/db/models.py`
2. Create a migration:
   ```bash
   alembic revision --autogenerate -m "add new_field to table_name"
   ```
3. Review the generated migration file in `alembic/versions/`
4. Apply the migration:
   ```bash
   alembic upgrade head
   ```

### Creating a New Table

1. Create your model in `infrastructure/db/models.py`
2. Import it in `alembic/env.py` (if not already imported)
3. Create a migration:
   ```bash
   alembic revision --autogenerate -m "create new_table"
   ```
4. Review and apply the migration

### Production Deployment

1. **Before deploying:**
   - Test migrations on a staging database
   - Review all migration files
   - Backup your production database

2. **During deployment:**
   ```bash
   alembic upgrade head
   ```

3. **If something goes wrong:**
   ```bash
   alembic downgrade -1  # Rollback last migration
   ```

## Best Practices

1. **Always review auto-generated migrations** - Alembic is smart but not perfect
2. **Test migrations on development/staging first** - Never test on production
3. **One migration per logical change** - Don't bundle unrelated changes
4. **Use descriptive migration messages** - Future you will thank you
5. **Never edit applied migrations** - Create a new migration to fix issues
6. **Keep migrations small and focused** - Easier to review and rollback if needed

## Troubleshooting

### Migration conflicts

If you have migration conflicts (multiple heads):
```bash
alembic merge heads -m "merge migration branches"
```

### Database out of sync

If your database is out of sync with migrations:
```bash
# Check current state
alembic current

# See what migrations are pending
alembic heads

# Apply pending migrations
alembic upgrade head
```

### Reset migrations (Development Only!)

⚠️ **WARNING: Only use this in development!**

If you need to reset migrations in development:
```bash
# Drop all tables (be careful!)
# Then recreate from models
python -c "from core.db import Base, engine; Base.metadata.drop_all(bind=engine); Base.metadata.create_all(bind=engine)"

# Mark as current (if you have an initial migration)
alembic stamp head
```

## Migration File Structure

Migration files are located in `alembic/versions/` and follow this structure:

```python
"""add job_loc and job_status

Revision ID: abc123
Revises: def456
Create Date: 2024-01-01 12:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = 'abc123'
down_revision = 'def456'
branch_labels = None
depends_on = None

def upgrade():
    # Add job_loc column
    op.add_column('jobs', sa.Column('job_loc', sa.String(), nullable=True))
    # Add job_status column
    op.add_column('jobs', sa.Column('job_status', sa.String(), nullable=True))

def downgrade():
    # Remove job_status column
    op.drop_column('jobs', 'job_status')
    # Remove job_loc column
    op.drop_column('jobs', 'job_loc')
```

## Additional Resources

- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

