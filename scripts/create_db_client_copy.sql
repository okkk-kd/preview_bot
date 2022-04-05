CREATE TABLE question (
    id INTEGER PRIMARY KEY,
    id_tg INTEGER NOT NULL,
    nickname TEXT NOT NULL,
    status INTEGER NOT NULL,
    question TEXT
);