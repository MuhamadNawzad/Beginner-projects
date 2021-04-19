black_lists = ["peter", "john", "smith", "alex"]
student_num = int(input("Enter number of students: "))
student_list = []
white_list = []
for student in range(student_num):
    prompt = input("Input a name: ")
    while prompt == "":
        prompt = input("Input a non-empty name: ")
    student_list.append(prompt)
for student in student_list:
    if student not in black_lists:
        white_list.append(student)
print("These " + str(len(white_list)) + " students are allowed to graduate")
print(*white_list, sep="\n")
