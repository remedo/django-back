-- Exported from QuickDBD: https://www.quickdatatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/7AKgqB
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.
-- Reference Database Schema

CREATE TABLE "Patient" (
    "PatientID" int  NOT NULL ,
    "Name" string  NOT NULL ,
    "DOB" date  NOT NULL ,
    "Height" string  NULL ,
    "Weight" string  NULL ,
    "Address" string  NULL ,
    "Phone" int  NOT NULL ,
    "Email" string  NULL ,
    CONSTRAINT "pk_Patient" PRIMARY KEY (
        "PatientID"
    )
)

GO

CREATE TABLE "Doctor" (
    "DoctorID" int  NOT NULL ,
    "Name" string  NOT NULL ,
    "RegNo" string  NOT NULL ,
    "Specialization" string  NOT NULL ,
    "WorkAdd" string  NOT NULL ,
    CONSTRAINT "pk_Doctor" PRIMARY KEY (
        "DoctorID"
    )
)

GO

CREATE TABLE "Prescription" (
    "PrescriptionID" int  NOT NULL ,
    "PatientID" int  NOT NULL ,
    "DoctorID" int  NOT NULL ,
    "timestamp" time  NOT NULL ,
    "medicines" blob  NOT NULL ,
    "reports" blob  NOT NULL ,
    "diagnosis" string  NOT NULL ,
    "other" string  NOT NULL ,
    CONSTRAINT "pk_Prescription" PRIMARY KEY (
        "PrescriptionID"
    )
)

GO

CREATE TABLE "Medicines" (
    "MedicineID" int  NOT NULL ,
    "DOE" date NOT NULL,
    "manufacturer" string  NOT NULL ,
    "Name" string  NOT NULL ,
    CONSTRAINT "pk_Medicines" PRIMARY KEY (
        "MedicineID"
    )
)

GO

CREATE TABLE "Pharmacy" (
    "PharmacyID" int  NOT NULL ,
    "Name" string NOT NULL,
    "medicines" blob  NOT NULL ,
    CONSTRAINT "pk_Pharmacy" PRIMARY KEY (
        "PharmacyID"
    )
)

GO

ALTER TABLE "Prescription" ADD CONSTRAINT "fk_Prescription_PatientID" FOREIGN KEY("PatientID")
REFERENCES "Patient" ("PatientID")
GO

ALTER TABLE "Prescription" ADD CONSTRAINT "fk_Prescription_DoctorID" FOREIGN KEY("DoctorID")
REFERENCES "Doctor" ("DoctorID")
GO

CREATE INDEX "idx_Patient_Name"
ON "Patient" ("Name")
GO

