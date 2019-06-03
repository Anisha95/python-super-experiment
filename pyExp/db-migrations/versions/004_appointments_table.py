from sqlalchemy import Column, String, Integer, DateTime, Table, MetaData, ForeignKey

metadata = MetaData()


appointments_table = Table(
    "appointments",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("patient_id", Integer, ForeignKey("patient.id"), nullable=False),
    Column("staff_id", Integer, ForeignKey("staff.id"), nullable=False),
    Column("date_time_of_appointment", DateTime, nullable=False),
    Column("other_details", String(length=140), nullable=True),
)


def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    _staff = Table("staff", metadata, autoload=True)
    _patient = Table("patient", metadata, autoload=True)
    appointments_table.create()


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    appointments_table.drop()
