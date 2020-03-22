from typing import List, Optional

from application.pypi_org.nosql.packages import Package
from application.pypi_org.nosql.releases import Release


def get_latest_releases(limit=10) -> List[Release]:
    releases = Release.objects(). \
        order_by("-created_date"). \
        limit(limit). \
        all()
    return releases


def get_package_count() -> int:
    return Package.objects().count()


def get_release_count() -> int:
    return Release.objects().count()


def get_package_by_id(package_id: str) -> Optional[Package]:
    if not package_id:
        return None

    package_id = package_id.strip().lower()

    package = Package.objects().filter(id=package_id).first()

    return package


def all_packages(limit: int) -> List[Package]:
    return list(Package.objects().limit(limit))


def get_packages_by_ids(package_ids: List[str]) -> List[Package]:
    return list(Package.objects(id__in=package_ids))

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
