print('Hello World!')

user_hi_amount = input('insert number here: ')

def greeter(hi_amount):
    try:
        response = 'Hi' * int(hi_amount)
    except ValueError:
        response = 'This is not an usable integer.'
    return response

print (greeter(user_hi_amount))
