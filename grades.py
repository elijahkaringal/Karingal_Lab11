grade_list = []
num = 0
usersaysdone = ("done")
passing_counter = 0
failing_counter = 0

while True:
    num += 1
    grade = input(f"Input student grade {num}, type 'done' to finish:")
    
    if grade.lower() == usersaysdone:
        if grade_list:
            average = round (sum(grade_list) / len(grade_list), 2)
            pass_percentage = round (passing_counter / len(grade_list), 2) * 100
            print(f"Average is {average}")
            print(f"Passed subjects: {passing_counter} ")
            print(f"Failed Subjects: {failing_counter}")
            print(f"Passing % is: {pass_percentage}")
            print(grade_list)
            break
        else:
            print("No input entered")
            break
    
    if grade.isdigit():
        grade = int(grade)
        if 40 <= grade <= 100:
            grade_list.append(grade)
        else:
            print ("Invalid Input, must be between 40-100")
            continue
            
        if grade >= 75:
            passing_counter += 1
        else:
            failing_counter += 1
    else:
        print("Please enter a numeric input")
        
        

        
    
    
        