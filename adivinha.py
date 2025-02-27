from random import randint

print("####-------------- Vamos Jogar ? -------------####")

min = 0
max = 100
random = randint(min,max)
chute = 0
chances = 10

while chute != random:
    chute = input(f'Chute um numeor entre {min} a {max}: ')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        if chute == random:
            print(' :) :) :) ;) ;) : )')

            print('Parabéns, voce venceu!O numero era {} e voce tinha {} chances.'.format (random,chances))

            print(':) :) :) :) :) :) :)')
            break;
        else:
            print('')
            if chute> random:
                print('Voce Errou!! Dica: é um numero menor!')
            else:
                print('Voce Errou!! Dica: é um numero maior!')
            print('Você ainda possui {} chances.'.format(chances))
            print('')
        if chances == 0:
            print('')
            print('Suas chances acabaram! Você perdeu! :c')
            print('')
            break
print("#### --------------------- GAME OVER ------------- #####")
