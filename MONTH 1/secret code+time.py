import time

while True:
    user_input = input('Enter The Secret Code: ')
    if user_input == '6969':
        print('Checking...')
        time.sleep(1)
        print('Correct!')
        break
    print('Incorrect!')
