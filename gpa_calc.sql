DROP TABLE IF EXISTS previous_course_grades;
DROP TABLE IF EXISTS grade_bounds;
DROP TABLE IF EXISTS letter_grades;

CREATE TABLE letter_grades (
    letter CHAR(2) PRIMARY KEY,
    grade_point FLOAT UNIQUE NOT NULL
);

CREATE TABLE previous_course_grades (
    member_name VARCHAR,
    course_id VARCHAR(32),
    course_grade CHAR(2) NOT NULL,
    PRIMARY KEY(member_name, course_id)
);

CREATE TABLE grade_bounds (
    grade_letter CHAR(2) PRIMARY KEY,
    lower_bound FLOAT UNIQUE NOT NULL,
    upper_bound FLOAT UNIQUE NOT NULL,
    FOREIGN KEY(grade_letter) REFERENCES letter_grades(letter) ON UPDATE CASCADE ON DELETE CASCADE
);