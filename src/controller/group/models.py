from sqlalchemy import Table, Column, Integer, MetaData, String, ForeignKey
from src.controller.auth.models import users

metadata = MetaData()


groups = Table(
    "groups",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("group_name", String, nullable=False),
    extend_existing=True
)


users_in_groups = Table(
    "users_in_groups",
    metadata,
    Column("user_id", Integer, ForeignKey(users.c.id)),
    Column("group_id", Integer, ForeignKey(groups.c.id)),
    extend_existing=True
)
