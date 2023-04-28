with open('pi_100_millions.txt', 'r') as f:
    pi = f.read()
pi = pi.replace('\n', '')
pi_str = str(pi)
num = [2,3,1,0,2,2] #Serie to search (avoid 0 at the beginning or the end of the serie because the algo is not perfect)
var = 0

for index, pi_chiffre in enumerate(pi_str):
    pi_chiffre_int = int(pi_chiffre)
    if pi_chiffre_int == num[var]:
        var += 1
        if var == len(num):
            print('Serie found at the decimal number :', index-len(num)+1)
            break
    else:
        var = 0
else:
    print('No match found')