students = [['Annie', 79, 87, 65],
            ['Bonnie', 80, 63, 88],
            ['Carol', 81, 95, 99],
            ['Doris', 45, 76, 93]]
each_test_total = []
num_tests = len(students[0]) - 1
num_students = len(students)
for test_index in range(num_tests):
    each_test_total.append(0)
for test_index in range(num_tests):
    for student_index in range(num_students):
        each_test_total[test_index] += students[student_index][test_index + 1]
each_test_avg = []
for test_index in range(num_tests):
    each_test_avg.append(each_test_total[test_index] / len(students))
for test in range(num_tests):
    print('The average of test ' + str(test + 1) + ' is ' + str(each_test_avg[test]))
