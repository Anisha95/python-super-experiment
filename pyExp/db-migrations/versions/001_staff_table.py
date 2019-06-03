from sqlalchemy import Column, String, Date, Integer, Table, MetaData


metadata = MetaData()


staff_table = Table(
    "staff",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("first_name", String(32), unique=True),
    Column("last_name", String(32), unique=True),
    Column("dob", Date),
    Column("gender", String(length=1),),
    Column("qualifications", String(length=100)),
    Column("other_details", String(length=140), nullable=True),
)


def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    staff_table.create()


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    staff_table.drop()
