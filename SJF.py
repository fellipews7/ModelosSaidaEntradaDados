import time

contadorP1 = 0
contadorP2 = 0
contadorP3 = 0

processo1 = [1, 2, -1, 1, -2, 1]
processo2 = [2, 1, -1, 2, 1]
processo3 = [-2, 1, -1, -2, 1]

contadorSequencia = 0

vetorSequencia = []


processoSequencia = ['P1', 'P2', 'P3']

while len(processo1) > contadorP1 or len(processo2) > contadorP2 or len(processo3) > contadorP3:
    processo = ''

    if (sum(processo1) < sum(processo2) or sum(processo2) == 0) and (sum(processo1) < sum(processo3) or sum(processo3) == 0) and len(processo1) > contadorP1:
        contadorSequencia = 0
    elif (sum(processo2) < sum(processo1) or sum(processo1) == 0) and (sum(processo2) < sum(processo3) or sum(processo3) == 0) and len(processo2)> contadorP2:
        contadorSequencia = 1
    elif (sum(processo3) < sum(processo1) or sum(processo1) == 0) and (sum(processo3) < sum(processo2) or sum(processo2) == 0) and len(processo3)> contadorP3:
        contadorSequencia = 2

    if (len(processo1) > contadorP1 and processo1[contadorP1] < 0):
        processo1[contadorP1] += 1

    if len(processo2) > contadorP2 and (processo2[contadorP2] < 0):
        processo2[contadorP2] += 1

    if (len(processo3) > contadorP3 and processo3[contadorP3] < 0):
        processo3[contadorP3] += 1

    if (len(processo1) > contadorP1 and processo1[contadorP1] > 0 and processoSequencia[contadorSequencia] == 'P1'):
        processo1[contadorP1] -= 1
        processo = 'P1'
    elif (len(processo2) > contadorP2 and processo2[contadorP2] > 0 and processoSequencia[contadorSequencia] == 'P2'):
        processo2[contadorP2] -= 1
        processo = 'P2'
    elif (len(processo3) > contadorP3 and processo3[contadorP3] > 0 and processoSequencia[contadorSequencia] == 'P3'):
        processo3[contadorP3] -= 1
        processo = 'P3'

    if (len(processo1) > contadorP1 and processo1[contadorP1] == 0):
        contadorP1 += 1

    elif (len(processo2) > contadorP2 and processo2[contadorP2] == 0):
        contadorP2 += 1

    elif (len(processo3) > contadorP3 and processo3[contadorP3] == 0):
        contadorP3 += 1


    if(processo != ''):
        vetorSequencia.append(processo)

print(vetorSequencia)

