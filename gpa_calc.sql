DROP TABLE IF EXISTS letter_grades;
DROP TABLE IF EXISTS previous_course_grades;
DROP TABLE IF EXISTS grade_bounds;

CREATE TABLE letter_grades (
    letter CHAR(2) PRIMARY KEY,
    grade_point FLOAT UNIQUE NOT NULL
);

CREATE TABLE previous_course_grades (
    student_id VARCHAR(32),
    course_id VARCHAR(32),
    course_grade CHAR(2) NOT NULL,
    PRIMARY KEY(student_id, course_id)
);

CREATE TABLE grade_bounds (
    grade_letter CHAR(2) PRIMARY KEY REFERENCES letter_grades(letter) ON UPDATE CASCADE ON DELETE CASCADE,
    lower_bound FLOAT UNIQUE NOT NULL,
    upper_bound FLOAT UNIQUE NOT NULL
);