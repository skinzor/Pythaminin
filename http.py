# As Internet; Http, Https, WWW, WWWS
http = ('http://')
https = ('https://')
www = ('http://www.')
wwws = ('https://www.')
# End
# Ask User For domain (input)
get_domain = input('Enter Domain Name: ')
# Get and add info
# Memory + Input
domain = http + get_domain
domains = https + get_domain
# All Outputs
print('As Http : ' + domain)
print('As Https :' + domains)
print('As Http WWW: ' + www + get_domain)
print('As Https WWW: ' + wwws + get_domain)
# End Of section >>>
