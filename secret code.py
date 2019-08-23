while True:
    user_input = input('Giv secret key: ')
    if user_input == '0':
        print('You are allowed to enter!')
        break
    print('Wrong key!')
