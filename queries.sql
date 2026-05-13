USE internship_project;

DELETE FROM evaluations;
DELETE FROM transcripts;
DELETE FROM sessions;

ALTER TABLE transcripts AUTO_INCREMENT = 1;
ALTER TABLE evaluations AUTO_INCREMENT = 1;
ALTER TABLE sessions AUTO_INCREMENT = 1;

INSERT INTO transcripts (user_id, file_name, transcript_text)
VALUES (1, 'sample.pdf', 'This is a demo transcript text.');

INSERT INTO evaluations (transcript_id, score, feedback)
VALUES (1, 88.5, 'Clear and well-structured communication.');

INSERT INTO sessions (user_id, session_start, session_end, status)
VALUES (1, NOW(), NULL, 'Active');

SELECT * FROM transcripts;
SELECT * FROM evaluations;
SELECT * FROM sessions;

SELECT t.file_name, e.score, e.feedback
FROM transcripts t
JOIN evaluations e ON t.transcript_id = e.transcript_id;