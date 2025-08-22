def main():
    plate = input("plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")

def Two_char(s):
    if s[0:2].isalpha():
        return True
    else:
        return False

def length_correct(s):
    if len(s) <= 6 and len(s) >= 2:
        return True
    else:
        return False

def correct_digit(s):
    if not any(char.isdigit()for char in s):
        return True
    digits_start = False 
    for char in s:
        if char.isdigit():
            digits_start = True
        elif digits_start:
            return False
    return True
def not_zero(s):
    for char in s:
        if char.isdigit():
            if char == "0":
                return False
            else:
                return True
    return True
def no_digits(s):
    if not s.isdigit():
        return True
    else:
        return False
def only_alnum(s):
    return s.isalnum()

def is_valid(s):
    check1 = Two_char(s)
    check2 = length_correct(s)
    check3 = correct_digit(s)
    check4 = not_zero(s)
    check5 = only_alnum(s)
    return check1 and check2  and check3 and check4 and check5

main()

