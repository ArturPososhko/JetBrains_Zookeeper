students_group_a = int(input())
students_group_b = int(input())
students_group_c = int(input())

desks_class_a = students_group_a // 2 + students_group_a % 2
desks_class_b = students_group_b // 2 + students_group_b % 2
desks_class_c = students_group_c // 2 + students_group_c % 2

desks_to_buy = desks_class_a + desks_class_b + desks_class_c

print(desks_to_buy)