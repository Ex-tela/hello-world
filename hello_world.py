def greeter(hi_amount):
    try:
        response = 'Hi ' * int(hi_amount)
    except ValueError:
        response = 'This is not an usable integer. Try again.'
    return response

def truth_teller(truth_choice):
    lower_choice = truth_choice.lower()
    if lower_choice == 'yes':
        return 'You feel dumb all the time. You can be the computer science Einstein, it doesn\'t matter. You feel dumb.'
    elif lower_choice == 'no':
        return 'Ok, then. Bye!'
    else:
        return 'Your answer was supposed to equal \'yes\' or \'no\'. Try again.'
    
def main():
   print('Hello World!')
   user_hi_amount = input('Insert number here: ')
   print(greeter(user_hi_amount))
   user_truth_choice = input('Would you like to hear the truth about programming? Please answer \'yes\' or \'no\': ')
   print(truth_teller(user_truth_choice))

if __name__ == "__main__":
   main()
