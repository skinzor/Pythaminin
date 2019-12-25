import sys
print ("the script has the name %s" % (sys.argv[0])
if 'hi' in sys.argv:
    print('hello')

arguments = sys.argv[1:] # all args
print(f'Recieved Arguments: {arguments}')
