def get_student_courses(enrollments, student_id):
    """Return set of courses this student has completed."""
    return {course for sid, course in enrollments if sid == student_id}
    pass

def find_missing_courses(completed_courses, required_courses):
    """Return set of required courses not yet completed."""
    return required_courses - completed_courses
    pass

def build_student_report(students, enrollments, required_courses):
    """Return sorted list of tuples (missing_count, student_id) for students with missing courses."""
    all_students = {sid for sid, _ in enrollments}
    
    report = []
    for student_id in all_students:
        completed = get_student_courses(enrollments, student_id)
        missing = find_missing_courses(completed, required_courses)
        if missing:  # only include students who are missing at least one course
            report.append((len(missing), student_id))
    
    # Sort descending by number of missing courses
    return sorted(report, reverse=True)

def find_incomplete_students(enrollments, required_courses):
    """Find students who haven't completed all required courses."""
    if not enrollments:
        return []

    # Build and return the report
    return build_student_report(enrollments, required_courses)
    pass

