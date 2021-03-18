#Modules

import random, string, pyperclip, time

#Functions

def all_chars_pass(N):
	password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(N))
	pyperclip.copy(password)
	print(password + '\nCopied to clipboard')

def not_all_chars_pass(x, y, z, N):
	password = ''.join(random.choice(x + y + z) for _ in range(N))
	pyperclip.copy(password)
	print(password + '\nCopied to clipboard')

#Get answers

agree = ['Yes', 'yes', 'y']
disagree = ['No', 'no', 'n']

print("Welcome to Iliyan's Password Generator")
time.sleep(0.5)
print("Firstly I want to ask, do you want to include all the available characters in your password? \nType your answer in the next input:")
all_chars_answer = input()
if all_chars_answer in agree:
	print("How long do you want your password to be?")
	size = int(input())
	all_chars_pass(size)
elif all_chars_answer in disagree:
	chars = ''
	digits = ''
	symbols = ''
	print("characters?")
	characters_answer = input()
	if characters_answer in agree:
		chars = string.ascii_letters
	print("symbols?")
	symbols_answer = input()
	if symbols_answer in agree:
		symbols = string.punctuation
	print('numbers?')
	numbers_answer = input()
	if numbers_answer in agree:
		digits = string.digits
	print("How long do you want your password to be?")
	size = int(input())
	not_all_chars_pass(chars, digits, symbols, size)

