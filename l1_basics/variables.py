# print() prints the text from brackets

example_variable = "Some text"
print(example_variable)

example_variable = "Other text"
print(example_variable)

# input() saves user input
user_input = input()
print(user_input)

# If text is added to brackets inside input() than the user can see it
user_input = input("User will see this text")
print(user_input)

# Concatenation means joining the text together.
# It can be done by putting plus character "+" between 2 texts
user_input = input("This text will be concatenated with 'User input was:'")
print('User input was:' + user_input)

# Text can be formatted using special characters. For example:
print('Use "\\t" to add tabs. Before tab\tAfter tab')
print('Use "\\n" to create new lines. Before new line\nAfter new line')
