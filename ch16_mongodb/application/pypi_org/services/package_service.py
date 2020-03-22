import sqlalchemy.orm
from typing import List, Optional

from sqlalchemy.orm import Session

from application.pypi_org.data import db_session
from application.pypi_org.data.package import Package
from application.pypi_org.data.releases import Release


def get_latest_releases(limit=10) -> List[Release]:
    session = db_session.create_session()

    releases = session.query(Release). \
        options(sqlalchemy.orm.joinedload(Release.package)). \
        order_by(Release.created_date.desc()). \
        limit(limit). \
        all()
    session.close()

    return releases


def get_package_count() -> int:
    session = db_session.create_session()
    return session.query(Package).count()


def get_release_count() -> int:
    session = db_session.create_session()
    return session.query(Release).count()


def get_package_by_id(package_id: str) -> Optional[Package]:
    if not package_id:
        return None

    package_id = package_id.strip().lower()

    session = db_session.create_session()

    package = session.query(Package) \
        .options(sqlalchemy.orm.joinedload(Package.releases)) \
        .filter(Package.id == package_id) \
        .first()

    session.close()

    return package


def all_packages(limit: int) -> List[Package]:
    session: Session = db_session.create_session()
    try:
        return list(session.query(Package).limit(limit))
    finally:
        session.close()
#
# def test():
#     """
#     My test function for practicing sqlalchemy queries
#     """
#     session = db_session.create_session()
#     result = session.query(Package). \
#         filter(
#         or_(
#             Package.id.like("flask"),
#             Package.id == "boto3")) \
#         .all()
#
#     print(result)
#     return {'message': result}
