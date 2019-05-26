from sqlalchemy import Column, String, Integer, Date, Table, MetaData

metadata = MetaData()


patient_table = Table(
    "patient",
    metadata,

    Column("patient_id", Integer, primary_key=True),
    Column("first_name", String(32), unique=True, nullable=False),
    Column("last_name", String(32), unique=True, nullable=False),
    Column("dob", Date, nullable=False),
    Column("gender", String(length=1), nullable=False),
    Column("other_details", String(length=140), nullable=True),
)


def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    patient_table.create()


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    patient_table.drop()
