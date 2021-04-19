def get_average(a_list):
    total = 0
    for score in a_list:
        total += score
    average = total / len(a_list)
    return average


def get_max(a_list):
    max_value = 0
    for average in a_list:
        if average > max_value:
            max_value = average
    return max_value


marks_list = [[88, 90, 89], [82, 86, 84], [80, 82]]
average_value = []
for marks in marks_list:
    average_value.append(get_average(marks))
max_num = get_max(average_value)
print("the highest average value for " + str(len(marks_list)) + " schools is " + str(max_num))
print("School " + str(average_value.index(max_num) + 1) + " gives the highest number.")