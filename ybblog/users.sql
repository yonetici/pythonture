BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT,
	"email"	TEXT,
	"username"	TEXT UNIQUE
);
INSERT INTO "users" VALUES (1,'maho','asda@adasd.com','segarrrr');
COMMIT;
