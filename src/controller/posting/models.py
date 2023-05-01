from datetime import date

from sqlalchemy import MetaData, Integer, String, ForeignKey, Table, Column, Text, DATE

from src.controller.auth.models import users
from src.controller.group.models import groups

metadata = MetaData()


posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("author_id", Integer, ForeignKey(users.c.id)),
    Column("group_id", Integer, ForeignKey(groups.c.id)),
    Column("post_name", String, nullable=False),
    Column("date", DATE, default=date.today),
    Column("text", Text),
)


images = Table(
    "images",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("post_id", Integer, ForeignKey(posts.c.id)),

)
