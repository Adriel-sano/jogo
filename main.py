from random import randint
monstro = 10
humano = 7
am = 2
ah = 3
while monstro > 0 and humano > 0:
    print(f'vida monstro {monstro} vida humano {humano}')
    faz = input('O que fazer?!!')
    if faz == 'a':
        monstro -= ah
        if randint(0,1) == 1:
            humano -= am
            print('monstro te atacou')
print(f'vida humana {humano} vida monstro {monstro}')