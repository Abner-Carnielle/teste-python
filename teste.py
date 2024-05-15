print("Você se deparou com um enorme dragão aos arredores da montanha, o que você fará?")

import random
escolha = input("Escolha entre a, para lutar com o dragão, e b para fugir do dragão: ")
chance = random.randint(1,100)

while escolha != 'a' or escolha != 'b':
    if escolha == 'a':
        if chance < 40:
            print("Você luta com o dragão e morre facilmente")
            break
        elif chance > 41:
            print("Com esforço você mata o dragão")
            break
    elif escolha == 'b':
        print("Você foge com tudo que pode, e vive para contar a história")
        break
