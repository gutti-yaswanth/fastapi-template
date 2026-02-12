# fastapi-template

### Generate evironment for the project
```python3 -m venv venv```
### Enable the Environment
```
# For macOS / linux
~ source venv/bin/activate

# For PowerShell
~ .\venv\Scripts\Active
```
### If cloned install requirements
```pip install -r requirements.txt```
### Run the server locally
```uvicorn main:app --reload```
### Lock the downloaded packages once installed
```pip freeze > requirements.txt```

## Database Migrations

This project uses Alembic for database migrations. 

### First Time Setup

After installing dependencies, you may need to create an initial migration:

```bash
# Create initial migration (if tables don't exist yet)
alembic revision --autogenerate -m "initial migration"

# Apply migrations
alembic upgrade head
```

### Common Migration Commands

```bash
# Create a new migration after model changes
alembic revision --autogenerate -m "description of changes"

# Apply all pending migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1

# Check current migration status
alembic current
```

For detailed migration guide, see [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)