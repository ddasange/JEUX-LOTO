import random

i = 0
while i < 10:
    input('Entrer votre numero entre 0 et 100\n ')
    i = i +1
  
        


numerosGagnant = list(range(1,100))

for k in range(99):
    hasard = random.randint(0,99)
    numerosGagnant[k],numerosGagnant[hasard]=[hasard],numerosGagnant[k]

    print('Les numeros gagnants sont', numerosGagnant[:6])
    break
