from classes import Carro

fusca = Carro(15)
fusca.adicionar_gasolina(20)
fusca.andar(100)
print(f'Nível de combustível: {fusca.obter_gasolina()} litros')