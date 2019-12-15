from random import choice
from time import sleep as threshold
import random

def string():
    spam = ['akaglkekgpoekgpokgpkeghrk', 'bwefawkjgelkgjaklejglk;jg', 'kajflkgjkljglkajglerjglka', 'jdflajflkjlg;kjreksgjabua', 'sadfdagdfsagdfsgdfgdfsggf']

    while True:
        print(choice(spam))
        threshold(.1)

def integer():
    spam = ['64518975484658127989', '46581279891245127346', '12451273465454618724', '54546187245467918154', '54679181546464578154', '64645781549797546134', '97975461348794612457']

    while True:
        print(choice(spam))
        threshold(.1)

while True:
    print(random.random())
    threshold(0.1)
