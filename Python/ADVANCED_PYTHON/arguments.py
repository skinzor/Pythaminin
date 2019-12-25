import sys

if 'hi' in sys.argv:
    print('hello')

arguments = sys.argv[1:] # all args
print(f'Recieved Arguments: {arguments}')
