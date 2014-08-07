-- python manage.py sqlall playground
BEGIN;
CREATE TABLE "playground_detector" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(200) NOT NULL,
    "description" varchar(1000) NOT NULL,
    "last_run_date" datetime NOT NULL,
    "run_count" integer NOT NULL,
    "creation_date" datetime NOT NULL
)
;
CREATE TABLE "playground_result" (
    "id" integer NOT NULL PRIMARY KEY,
    "detector_id" integer NOT NULL REFERENCES "playground_detector" ("id"),
    "content" varchar(1000) NOT NULL,
    "value" integer NOT NULL,
    "creation_date" datetime NOT NULL
)
;
CREATE INDEX "playground_result_1141f28e" ON "playground_result" ("detector_id");

COMMIT;
