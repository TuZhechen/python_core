# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_list = [msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
legal_oper = ['+', '-', '*', '/']


def good_input(x = 0.0, y = 0.0, oper = '+'):
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        return False
    if oper not in legal_oper:
        print(msg_2)
        return False
    return True


def is_one_digit(val):
    if -10 <= val <= 10 and val.is_integer():
        return True
    return False


def check(x, y, oper):
    msg = ""
    # print("x =", x)
    # print("y =", y)
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1 or y == 1) and oper == '*':
        msg += msg_7
    if (x == 0 or y == 0) and (oper == '*' or oper == '+' or oper == '-'):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


memo = 0.0
while True:
    input_string = input(msg_0)
    elements = input_string.split()
    oper = elements[1]
    a = elements[0]
    b = elements[2]

    if a == 'M':
        if b == 'M':
            x, y = memo, memo
        else:
            good_input(y = b, oper = oper)
            x, y = memo, float(b)
    else:
        good_input(x = a, oper = oper)
        if b == 'M':
            x, y = float(a), memo
        else:
            good_input(y = b, oper = oper)
            x, y = float(a), float(b)

    check(x, y, oper)
    if y == 0 and oper == '/':
        print(msg_3)
        continue
    if oper == '+':
        result = x + y
        print(result)
    if oper == '-':
        result = x - y
        print(result)
    if oper == '*':
        result = x * y
        print(result)
    if oper == '/':
        result = x / y
        print(result)

    while True:
        save_or_not = input(msg_4)
        if save_or_not == 'n':
            break
        elif save_or_not == 'y':
            if is_one_digit(result):
                idx = 10
                while idx <= 12:
                    resp = input(msg_list[idx - 1])
                    if resp == 'y':
                        idx += 1
                        continue
                    elif resp == 'n':
                        break
                    else:
                        continue
            if not is_one_digit(result) or idx > 12:
                memo = result
            break
        else:
            continue

    while True:
        redo_or_not = input(msg_5)
        if redo_or_not == 'y' or redo_or_not == 'n':
            break
        else:
            continue

    if redo_or_not == 'y':
        continue
    break
