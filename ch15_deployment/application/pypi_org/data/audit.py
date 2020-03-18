import datetime
import sqlalchemy

from application.pypi_org.data.modelbase import SqlAlchemyBase


class Audit(SqlAlchemyBase):
    __tablename__ = 'auditing'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    description = sqlalchemy.Column(sqlalchemy.String)
