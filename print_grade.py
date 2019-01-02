def create_grades_dict(filename):
    number_test = 4
    my_file = open(filename, "r")
    my_list = my_file.readlines()
    my_file.close()
    grade_list = [0 for k in range(number_test)]
    grade_dict = {}
    for line in my_list:
        if line[0] != '#' and line[0] != "\n":
            splited_line = line.strip().split(',')
            for j in range(len(splited_line)):
                splited_line[j] = splited_line[j].strip()
            for i in range(number_test):
                test_num = "Test_" + str(i+1)
                if test_num in splited_line:
                    grade_list[i] = int(splited_line[splited_line.index(test_num) + 1])
            grade_dict.update({splited_line[0]: [splited_line[1]] + grade_list + [sum(grade_list) / len(grade_list)]})
            grade_list = [0 for k in range(number_test)]
    return grade_dict


def print_grades(file_name):
    grades_dict = create_grades_dict(file_name)
    key_list = list(grades_dict.keys())
    key_list.sort()
    print("{0:^10s} | {1:^16s} | {2:^6s} | {3:^6s} | {4:^6s} | {5:^6s} | {6:^6s} |".format(
        'ID', 'Name', 'Test_1', 'Test_2', 'Test_3', 'Test_4', 'Avg.'))
    for key in key_list:
        print("{0:10s} | {1:16s} | {2:6d} | {3:6d} | {4:6d} | {5:6d} | {6:6.2f} |".format(key, grades_dict[key][0],
            grades_dict[key][1], grades_dict[key][2], grades_dict[key][3], grades_dict[key][4], grades_dict[key][5]))


print_grades('print_grade.text')
