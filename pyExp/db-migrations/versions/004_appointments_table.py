from sqlalchemy import Column, String, Integer, DateTime, Table, MetaData, ForeignKey

metadata = MetaData()


apointments_table = Table(
    "appointments",
    metadata,

    Column("appointments_id", Integer, primary_key=True),
    Column("patient_id", Integer, ForeignKey("patient_table.patient_id"), nullable=False),
    Column("staff_id", Integer, ForeignKey("staff_table.staff_id"), nullable=False),
    Column("date_time_of_appointment", DateTime, nullable=False),
    Column("other_details", String(length=140), nullable=True),
)


def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    apointments_table.create()


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    apointments_table.drop()
