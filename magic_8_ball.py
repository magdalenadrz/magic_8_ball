#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 14:54:12 2022

@author: magdalena
"""
import random
name = 'insert name'
question = 'insert question'
answer = ''

if name == '':
  print('Question: ' + question)
else: 
 print(name + ' asks: ' + question)


random_number = random.randint(1, 11)
#print(random_number)

if question == '':
  print('You did not ask a question, therefore the Magic 8-Ball will not grant you a fortune.')
else:
 print("Magic 8-Ball's answer: " + answer)
if random_number == 1:
  print('Yes - definitely.')
elif random_number == 2:
  print('It is decidedly so.')
elif random_number == 3:
  print('Without a doubt.')
elif random_number == 4:
  print('Reply hazy, try again.')
elif random_number == 5:
  print('Ask again later.')
elif random_number == 6:
  print('Better not tell you now.')
elif random_number == 7:
  print('My sources say no.')
elif random_number == 8:
  print('Outlook not so good.')
elif random_number ==9:
  print('Very doubtful.')
elif random_number == 10:
  print('No chance!')
elif random_number == 11:
  print('Keep dreaming!')
else:
  print('Error')
  
  