import numbers
from pyscript import display, document

def create_account(e):
    document.getElementById('output').innerHTML = " "

    username = document.getElementById('user').value
    password = document.getElementById('pass').value


    if username == "":
        display(f'Please enter a username.', target='output')
    elif password == "":
        display(f'Please enter a password.', target='output')
    else:
        if len(username) < 7:
            display(f'Username must be at least 7 characters long.', target='output')
        elif len(password) < 10:
            display(f'Password must be at least 10 characters long.', target='output')
        elif not any(c.isalpha() for c in password):
            display(f'Password must contain at least one letter.', target='output')
        elif not any(char.isdigit() for char in password):
            display(f'Password must contain at least one number.', target='output')
        else:            display(f'Account created successfully!', target='output')
