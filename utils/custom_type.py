import datetime

from typing import Annotated
from sqlalchemy import Table, Column, Integer, String, ForeignKey, text, DateTime, SmallInteger, Date
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column
from sqlalchemy.dialects import postgresql
from typing import Annotated
import uuid
from sqlalchemy import types

int_pk = Annotated[int, mapped_column(primary_key=True)]
uuid_ = Annotated[uuid.UUID, mapped_column()]
uuid_pk = Annotated[uuid.UUID, mapped_column(postgresql.UUID(as_uuid=True),
                                             primary_key=True,
                                             default=uuid.uuid4)]
uuid_pk_auto = Annotated[uuid.UUID, mapped_column(postgresql.UUID(as_uuid=True),
                                                  primary_key=True,
                                                  default=text("gen_random_uuid()"),
                                                  server_default=text("gen_random_uuid()")
                                                  )]
uuid_null = Annotated[uuid.UUID, mapped_column(postgresql.UUID(as_uuid=True),
                                             primary_key=True,
                                             default=uuid.uuid4,
                                             nullable=True)]

created_on_record = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True))]
created_on_record_auto = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True),
                                                                    server_default=text(
                                                                        "TIMEZONE('Europe/Kiev', now())"))]
created_on_datetime = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True))]
created_on_date = Annotated[datetime.date, mapped_column(postgresql.DATE())]
created_on_date_null = Annotated[datetime.date, mapped_column(postgresql.DATE(), nullable=True)]
update_on_record = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('Europe/Kiev', now())"),
    onupdate=datetime.datetime.utcnow(),
)]

str_10 = Annotated[str, 10]
str_20 = Annotated[str, 20]
str_30 = Annotated[str, 30]
str_40 = Annotated[str, 40]
