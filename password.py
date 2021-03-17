import random, string, pyperclip
password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(12))
pyperclip.copy(password)
print(password + '\nCopied to clipboard')
