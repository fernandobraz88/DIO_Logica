import random

heroi = input('Digite seu nome de heroi:\n')
hp = 10
xp = 0
menu = ''' 1 - TREINAR! ò.ó\n 2 - Comer e descansar =D\n 0 - Sair :( \n'''
nivel_de_heroi = "Ferro"

while True:
    opcao = input(menu)

    if opcao == '0':
        print(f'"O Herói de nome {heroi} está no nível de {nivel_de_heroi}')
        break
    elif opcao == '1':
        xp += random.randint(300, 500)
        hp -= random.randint(1,5)
        if hp <= 0:
            print('você morreu T_T \n\n Game Over')
            break
        elif xp <= 1000:
            nivel_de_heroi = 'Ferro'
        elif xp > 1000 and xp <= 2000:
            nivel_de_heroi = 'Bronze'
        elif xp > 2000 and xp <= 5000:
            nivel_de_heroi = 'Prata'
        elif xp > 5000 and xp <= 7000:
            nivel_de_heroi = 'Ouro'
        elif xp > 7000 and xp <= 8000:
            nivel_de_heroi = 'Platina'
        elif xp > 8000 and xp <= 9000:
            nivel_de_heroi = 'Ascendente'
        elif xp > 9000 and xp <= 10000:
            nivel_de_heroi = 'Imortal'
        else:
            nivel_de_heroi = 'Radiante'

        print(f'um dia longo e arduo se passou \n  HP: {hp} \n  XP:{xp}\n  Level: {nivel_de_heroi}')    

    elif opcao == '2':
        hp += random.randint(7,10)
        print(f'Você descansou! suas feridas foram curadas! \n  HP: {hp} \n  XP:{xp}\n  Level: {nivel_de_heroi}')
    else:
        print('Opção invalida! (escolha 1 - 2 ou 0)')
    