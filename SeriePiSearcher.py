with open('pi_100_millions.txt', 'r') as f:
    pi = f.read()
pi = pi.replace('\n', '')
pi_str = str(pi)
num = [2,3,1,0,2,2]
var = 0

for index, pi_chiffre in enumerate(pi_str):
    pi_chiffre_int = int(pi_chiffre)
    if pi_chiffre_int == num[var]:
        var += 1
        if var == len(num):
            print('Numéro trouvé à la décimale numéro :', index-len(num)+1)
            break
    else:
        var = 0
else:
    print('aucune correspondance')