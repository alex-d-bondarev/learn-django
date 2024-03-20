from copy import deepcopy

text = 'hi there'
number = 42
example_list = [1, 2, 3]


def print_variables(text_var, number_var, list_var):
    text_var = 'inside function'
    extra_text = 'this is a bonus'
    list_var = list(list_var)
    list_var = list_var[:]
    list_var = list_var.copy()  # IMHO the most readable
    list_var = deepcopy(list_var)
    print(text_var)
    print(extra_text)
    print(number_var)
    print(list_var)
    list_var.append(4)
    print(list_var)


print_variables(text_var=text, number_var=number, list_var=example_list)
print(text)
print(number)
print(example_list)
example_list.append(4)
print(example_list)
