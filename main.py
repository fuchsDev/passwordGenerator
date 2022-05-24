#script generates a random password

import random

lower = 'abcdefghijklmnopqrstuvxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
numbers = '0123456789'
symbols = '@!#$%'

all = lower + upper + numbers + symbols

length = 10
password = ''.join(random.sample(all, length))
print(password)