CREATE DATABASE IF NOT EXISTS internship_project;
USE internship_project;

DROP TABLE IF EXISTS evaluations;
DROP TABLE IF EXISTS transcripts;
DROP TABLE IF EXISTS sessions;

CREATE TABLE transcripts (
    transcript_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    file_name VARCHAR(255),
    transcript_text TEXT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE evaluations (
    evaluation_id INT AUTO_INCREMENT PRIMARY KEY,
    transcript_id INT,
    score DECIMAL(5,2),
    feedback TEXT,
    evaluated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (transcript_id) REFERENCES transcripts(transcript_id)
);

CREATE TABLE sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    session_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    session_end TIMESTAMP NULL DEFAULT NULL,
    status VARCHAR(50)
);