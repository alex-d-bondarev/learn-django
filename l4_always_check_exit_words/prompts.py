def get_input_or_exit(message=''):
    user_input = input(message)

    if user_input in ['exit', 'quit', 'stop']:
        print('Thank you for using our app. Have a lovely day!')
        exit()

    return user_input

