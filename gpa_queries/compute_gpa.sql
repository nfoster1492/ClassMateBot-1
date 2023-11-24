SELECT AVG(grade_point)
FROM (
    SELECT grade_point
    FROM letter_grades JOIN (
        SELECT course_grade
        FROM previous_course_grades
        WHERE student_id = '1'
    ) AS student_grades
    ON letter = course_grade

    UNION ALL

    SELECT 3 AS grade_point
) AS ape;