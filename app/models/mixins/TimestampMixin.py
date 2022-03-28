from sqlalchemy import Column, func
from sqlalchemy.types import DateTime


class TimestampMixin(object):
    __timestamp__ = True

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
