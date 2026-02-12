# Alembic Migrations

This directory contains database migration scripts managed by Alembic.

## Usage

### Create a new migration
```bash
alembic revision --autogenerate -m "description of changes"
```

### Apply migrations
```bash
alembic upgrade head
```

### Rollback to previous version
```bash
alembic downgrade -1
```

### View current revision
```bash
alembic current
```

### View migration history
```bash
alembic history
```

## Important Notes

- Always review auto-generated migrations before applying them
- Test migrations on a development database first
- Never edit existing migration files that have been applied to production
- Create new migrations for any schema changes

