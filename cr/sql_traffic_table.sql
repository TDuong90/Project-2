DROP TABLE IF EXISTS crashes;

CREATE TABLE "crashes" (
    "DR_Number" int   NOT NULL,
	"Date" VARCHAR    NOT NULL,
	"Time_of_Day" VARCHAR  NOT NULL,
	"Date_Occurred" VARCHAR   NOT NULL,
	"Time_Occurred" int   NOT NULL,
    "Area_ID" int   NOT NULL,
	"Area_Name" VARCHAR   NOT NULL,
	"Reporting_District" int   NOT NULL,
	"Crime_Code" int   NOT NULL,
	"Crime_Code_Description" VARCHAR   NOT NULL,
    "MO_Codes" VARCHAR   NOT NULL,
	"Victim_Age" Float   NOT NULL,
	"Victim_Sex" VARCHAR   NOT NULL,
	"Premise_Code" Float   NOT NULL,
	"Premise_Description" VARCHAR   NOT NULL,
	"Address"  VARCHAR   NOT NULL,
    "Cross_Street" VARCHAR   NOT NULL,
	"Location" VARCHAR   NOT NULL,
	"Latitude" VARCHAR   NOT NULL,
	"Longitude" VARCHAR   NOT NULL
)
