
from classes import Tamagotchi

bichinho = Tamagotchi("Pikachu", 5, 8, 2)
print(f'O nome do seu Tamagotchi é: {bichinho.retornar_nome()}')
print(f'O {bichinho.retornar_nome()} está com {bichinho.retornar_fome()} de fome')
print(f'O {bichinho.retornar_nome()} está com {bichinho.retornar_saude()} de saúde')
print(f'O {bichinho.retornar_nome()} está com {bichinho.retornar_idade()} anos de idade')

bichinho.alterar_nome("Naruto")
bichinho.alterar_fome(3)
bichinho.alterar_saude(6)
bichinho.alterar_idade(3)

print(f'O nome do seu Tamagotchi agora é: {bichinho.retornar_nome()}')
print(f'O {bichinho.retornar_nome()} está com {bichinho.retornar_fome()} de fome')
print(f'O {bichinho.retornar_nome()} está com {bichinho.retornar_saude()} de saúde')
print(f'O {bichinho.retornar_nome()} está com {bichinho.retornar_idade()} anos de idade')