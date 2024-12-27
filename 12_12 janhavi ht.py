class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def validate_details(self):
        if not self.student_id.startswith("STU") or not self.student_id[3:].isdigit() or len(self.student_id) != 7:
            return "Invalid student_id. Format must be STU1234."
        
        if len(self.name) < 2 or not all(char.isalpha() or char.isspace() for char in self.name):
            return "Invalid name. It must be at least 2 characters long and contain only alphabets and spaces."
        
        valid_grades = [f"{i}th Grade" for i in range(1, 13)]
        if self.grade not in valid_grades:
            return "Invalid grade. Must follow the format '<number>th Grade' (e.g., '1st Grade', ..., '12th Grade')."
        
        return "All details are valid."

    def display_details(self):
        """Displays the student's details."""
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
