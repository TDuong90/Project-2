DROP TABLE IF EXISTS weather;

CREATE TABLE "weather" (
    "Weather_Date" VARCHAR   NOT NULL,
	"Max" int   NOT NULL,
	"Min" int   NOT NULL,
    "Average" Float   NOT NULL,
	"Precipitation" Float   NOT NULL
)