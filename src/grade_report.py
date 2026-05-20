"""Student grade report generator."""

from stats_utils import calculate_average, calculate_pass_rate


class GradeReport:
    """Generates grade reports for a class of students."""

    def __init__(self, student_scores):
        """Initialize with a dictionary of {student_name: score}."""
        self.student_scores = student_scores

    def get_class_average(self):
        """Get average score for the class.
        
        Bug: passes empty list to calculate_average when no students exist.
        """
        scores = list(self.student_scores.values())
        return calculate_average(scores)

    def get_pass_rate(self, passing_score=50):
        """Get percentage of students who passed.
        
        Bug: passes total=0 to calculate_pass_rate when no students exist.
        """
        total = len(self.student_scores)
        passed = sum(1 for s in self.student_scores.values() if s >= passing_score)
        return calculate_pass_rate(passed, total)

    def generate_summary(self):
        """Generate full class summary report."""
        return {
            "total_students": len(self.student_scores),
            "class_average": self.get_class_average(),
            "pass_rate": self.get_pass_rate(),
        }


if __name__ == "__main__":
    # Bug trigger: empty class with no students
    report = GradeReport({})
    print(report.generate_summary())
