from marshmallow import fields
from sqlalchemy.orm import sessionmaker
from app.app import db
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Binary,
    String,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

Base = declarative_base()
Base.query = db.session.query_property()


class ShortLink(Base):
    __tablename__ = "short_links"

    id = Column(Integer, primary_key=True, autoincrement=True)
    long_url = Column(String(255), nullable=False)
    short_url = Column(String(255), nullable=False)
    hits_count = Column(Integer, default=0)

    def __repr__(self):
        return f"<Link #{self.id}  {self.long_url} => {self.short_url}"


class ShortLinkSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ShortLink
