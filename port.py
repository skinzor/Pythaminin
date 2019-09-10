# Ask User For Port
port = input('Enter A Port: ')
# python -m SimpleHTTPServer_<Port_in_number>
print('python -m SimpleHTTPServer ' + port)
print('Your Site Can Be Accessed Here: http://localhost:' + port )
print('             OR ')
print('Your Site Can Be Accessed Here: http://127.0.0.1:' + port )

# import os then inject into os
