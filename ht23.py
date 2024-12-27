#que 1
subjects = {
    "cs_grp": {"sub": "Computer Science", "admission": 40, "fees": 45000},
    "bio_grp": {"sub": "Biology", "admission": 32, "fees": 43000},
    "arts_grp": {"sub": "Arts", "admission": 20, "fees": 39000}
}

latest_fees = {
    "student1": 45000,
    "student2": 43000,
    "student3": 39000
}

def fees_structure(subject_name):
    """Display fee structure for a given subject"""
    if subject_name in subjects:
        subject_info = subjects[subject_name]
        print(f"Your subject is {subject_info['sub']}. The admission capacity is {subject_info['admission']} and fees is {subject_info['fees']}.")
    else:
        print("Admission closed.")

def check_fees(std):
    """Display latest fees for a given standard"""
    if student in latest_fees:
        latest = latest_fees[std]
        print(f"Your latest fees is: {latest}.")
    else:
        print("Admission brochure is not found.")

def report_issue(issue):
    """Report connectivity issues"""
    print("Thank you for choosing our school.")
    print("The information will be sent through mail.")
    print("For any queries, contact: 0123456789")
    print(f"Issue reported: {issue}")

while True:
    print("Welcome to SSSV School")
    print("1. Check your subject details.")
    print("2. Check your latest fees.")
    print("3. Report connectivity issues.")
    print("4. Exit.")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        subject_name = input("Enter the subject name: ")
        fees_structure(subject_name)
    elif choice == 2:
        student= input("Enter the student ID: ")
        check_fees(student)
    elif choice == 3:
        issue = input("Please describe your issue: ")
        report_issue(issue)
    elif choice == 4:
        exit()
    else:
        print("Invalid choice. Please choose again.")
    
    print("_" * 70)
#que02
    import  random
    def quiz_event(question):
        scr=0
        all_questions=len(questions)
        choice={"q1":"1.dhoni\n2.virat","q2":"1.gautham gambir\n2.krunal pandya","q3":"1.gautham gambir\n2.gill"}
        for ques,ans in questions.items():
                print(ques)
                if ques=="who is the captain of csk in 2023":
                    print(choices["q1"])
                elif ques=="which player is having most of century in 2024":
                    print(choices["q2"])
                elif ques=="which captain have fight or aggresive talks with virat":
                    print(choices["q3"])
                player_ans=input("Enter your answer: ").strip()
                if player_ans.lower()==ans.lower():
                    print("Awesome the answer is correct!!")
                    scr+=1
                else:
                    print(f"wrong answer, correct answer is: {ans}")
                    print(f"\n Your scr is: {scr}/{all_questions}")
        def main():
            print("WELCOME TO THE QUIZ...ALL THE BEST:)")
            quiz_questions={
                "who is the captain of csk in 2023":"dhoni"
                "which player is having most of century in 2024":"virat"
                "which captain have fight or aggresive talks with virat":"gautham gambir"
                }
            conduct_quiz(quiz_questions)
            main()

  
                
                 
