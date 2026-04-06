-- Write your query below
SELECT DISTINCT on (student_id) *
FROM exam_results
ORDER BY student_id, score DESC, exam_id