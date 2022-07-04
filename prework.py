# Q1
def hello_name(user_name):
    print(f"hello_{user_name.title()}")

#Q2
def first_odds():
    for number in range(1,101):
        if number % 2 != 0:
            print(number)

#Q3
def max_num_in_list(a_list):
    max_num = max(a_list)


#Q4
def is_leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 5 == 0:
        return True