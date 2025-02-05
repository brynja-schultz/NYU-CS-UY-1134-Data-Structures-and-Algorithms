from ArrayStack import ArrayStack

OPERATORS = "+-*/"
EXP_DICT = {}  # stores key (variable) value (expression)
STACK = ArrayStack()  # stack to perform calculations (LIFO)


def do_calculation(exp_lst):
    result = None

    for i in range(0, len(exp_lst)):
        if exp_lst[i] not in OPERATORS:  # if character is a value for operation to be performed on

            if exp_lst[i] in EXP_DICT:  # if character is stored variable
                variable_exp = EXP_DICT[exp_lst[i]]   # stores expression associated with that variable (LIST)
                result = do_calculation(variable_exp)  # stores result of variable's expression
                STACK.push(result)

            else:
                STACK.push(exp_lst[i])  # number stored to perform later operation

        else:  # operator found --> performs operation
            arg1 = int(STACK.pop())
            arg2 = int(STACK.pop())

            if exp_lst[i] == "+":
                result = arg1 + arg2

            elif exp_lst[i] == "-":
                result = arg2 - arg1

            elif exp_lst[i] == "*":
                result = arg1 * arg2

            elif exp_lst[i] == "/":
                if arg1 == 0:
                    raise ZeroDivisionError
                result = arg2 / arg1

            STACK.push(result)

    return STACK.pop()


def postfix_calculator(input_exp):
    while input_exp != "done()":  # loop stops when user inputs done
        exp_lst = input_exp.split()  # splits user string into list

        if "=" in exp_lst:  # if assignment expression is inputted
            EXP_DICT[exp_lst[0]] = exp_lst[2:]  # adds key (variable name) value (expression) pair to dict
            print(exp_lst[0])  # prints variable name

        else:
            print(do_calculation(exp_lst))

        input_exp = input("-->")


def main():
    exp = input("-->")

    postfix_calculator(exp)


if __name__ == "__main__":
    main()
