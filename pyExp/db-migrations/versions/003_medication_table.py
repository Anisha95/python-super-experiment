from sqlalchemy import Column, String, Integer, Table, REAL, MetaData

metadata = MetaData()


medication_table = Table(
    "medication",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("medication_unit_cost", REAL),
    Column("medication_name", String(length=50), unique=True),
    Column("medication_description", String(length=100)),
    Column("other_details", String(length=140)),
)


def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    medication_table.create()


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    medication_table.drop()
