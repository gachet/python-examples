PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "entry" ("id" INTEGER NOT NULL PRIMARY KEY, "title" VARCHAR(255) NOT NULL, "slug" VARCHAR(255) NOT NULL, "content" TEXT NOT NULL, "published" INTEGER NOT NULL, "timestamp" DATETIME NOT NULL);
PRAGMA writable_schema=ON;
INSERT INTO sqlite_master(type,name,tbl_name,rootpage,sql)VALUES('table','ftsentry','ftsentry',0,'CREATE VIRTUAL TABLE "ftsentry" USING FTS4 ("entry_id" INTEGER, "content" TEXT NOT NULL)');
CREATE TABLE 'ftsentry_content'(docid INTEGER PRIMARY KEY, 'c0entry_id', 'c1content');
CREATE TABLE 'ftsentry_segments'(blockid INTEGER PRIMARY KEY, block BLOB);
CREATE TABLE 'ftsentry_segdir'(level INTEGER,idx INTEGER,start_block INTEGER,leaves_end_block INTEGER,end_block INTEGER,root BLOB,PRIMARY KEY(level, idx));
CREATE TABLE 'ftsentry_docsize'(docid INTEGER PRIMARY KEY, size BLOB);
CREATE TABLE 'ftsentry_stat'(id INTEGER PRIMARY KEY, value BLOB);
CREATE UNIQUE INDEX "entry_slug" ON "entry" ("slug");
CREATE INDEX "entry_published" ON "entry" ("published");
CREATE INDEX "entry_timestamp" ON "entry" ("timestamp");
PRAGMA writable_schema=OFF;
COMMIT;
