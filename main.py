import random
def get_usernames(my_file, title_space):
    usernames_only = my_file.readlines()[title_space:]
    return usernames_only

def create_groups (the_file, title_len):
    grouped = list()
    inner_list = list()
    usernames = get_usernames(the_file, title_len)
    j = 0
    num = list(range(0, (len(usernames))))
    student_count = 0
    random.shuffle(num)
    while (student_count < len(usernames)):
        j = 0
        inner_list = list()
        while(j < 6 and student_count < len(usernames)):
            inner_list.append(usernames[num[student_count]])
            j+=1
            student_count+=1
        grouped.append(inner_list)
    
    print(grouped)
    return grouped

def write_to_file(my_grouped_list):
    new_file = open('grouped_students.txt', 'w')
    group_number = 0
    student = 0
    while (group_number <= len(my_grouped_list) - 1):
        new_file.write(f"Group number:{group_number + 1}\n")
        student = 0
        while (student < len(my_grouped_list[group_number]) ):
            new_file.write(my_grouped_list[group_number][student])
            student += 1
        new_file.write("\n")
        group_number += 1

try:
    file_ = open('students.txt')
except FileNotFoundError:
    print("Your file was not found, make sure its in this directory and named students.txt")
else:
    x = int(input("How many lines do you have reserved for your title and headings?"))
    write_to_file(create_groups(file_, x))