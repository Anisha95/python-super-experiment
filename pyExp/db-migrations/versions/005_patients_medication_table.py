from sqlalchemy import Column, String, Integer, DateTime, Table, MetaData, ForeignKey

metadata = MetaData()


patients_medication_table = Table(
    "patients_medication",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("medication_id", Integer, ForeignKey("medication.id"), nullable=False),
    Column("patient_id", Integer, ForeignKey("patient.id"), nullable=False),
    Column("date_time_administered", DateTime, nullable=False),
    Column("dosage", Integer, nullable=True),
    Column("comments", String(length=100), nullable=True),
    Column("other_details", String(length=140), nullable=True),
)


def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    _medication = Table("medication", metadata, autoload=True)
    _patient = Table("patient", metadata, autoload=True)
    patients_medication_table.create()


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    patients_medication_table.drop()
