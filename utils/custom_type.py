import datetime

from typing import Annotated
from sqlalchemy import Table, Column, Integer, String, ForeignKey, text, DateTime, SmallInteger, Date
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column
from sqlalchemy.dialects import postgresql
from typing import Annotated
import uuid
from sqlalchemy import types

intpk = Annotated[int, mapped_column(primary_key=True)]
uuidpk = Annotated[uuid.UUID, mapped_column(postgresql.UUID(as_uuid=True),
                                            primary_key=True,
                                            default=uuid.uuid4)]
created_on_record = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True))]
created_on_datime = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True))]
created_on_date = Annotated[datetime.date, mapped_column(postgresql.DATE())]
update_on_record = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('Europe/Kiev', now())"),
    onupdate=datetime.datetime.utcnow(),
)]

str_10 = Annotated[str, 10]
str_20 = Annotated[str, 20]
str_30 = Annotated[str, 30]
str_40 = Annotated[str, 40]
