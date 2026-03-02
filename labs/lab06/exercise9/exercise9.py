def find_qualified_students(student_records, required_courses):
    """
    Find students who completed all required courses.
    
    Args:
        student_records: List of tuples (student_id, completed_courses_set)
        required_courses: Set of required course names
    
    Returns:
        Sorted list of student IDs who completed all required courses
    
    Example:
        >>> students = [("S1", {"Math", "CS"}), ("S2", {"Math"})]
        >>> required = {"Math", "CS"}
        >>> find_qualified_students(students, required)
        ["S1"]
    """
    qualified = []
    
    for student_id, completed in student_records:
        common = completed | required_courses
        
        if common == completed:
            qualified.append(student_id)
    
    return sorted(qualified)
    
students = [
            ("Z9", {"A", "B", "C", "Extra1"}),
            ("A1", {"A", "B", "Extra2"}),
            ("M5", {"A", "B", "C", "Extra3"})
        ]
required = {"A", "B"}
find_qualified_students(students, required)