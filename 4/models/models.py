from datetime import datetime
from sqlalchemy import JSON, TIMESTAMP, MetaData, String, Integer, Column, Table, ForeignKey

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permission", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("login", String, nullable=False),
    Column("password", String, nullable=False),
    Column("register_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("roles.id")),
)
