from classes import BombaCombustivel

bomba = BombaCombustivel("Gasolina", 4.5, 1000)


litros_abastecidos = bomba.abastecer_por_valor(50)
print(f'Foram abastecidos {litros_abastecidos:.2f} litros de {bomba.tipo_combustivel}')

valor_pagar = bomba.abastecer_por_litro(10)
print(f'O valor a ser pago pelo cliente é R${valor_pagar:.2f}')

bomba.alterar_valor(4.8)
bomba.alterar_combustivel("Etanol")
bomba.alterar_quantidade_combustivel(800)

print(f'Quantidade de combustível restante: {bomba.quantidade_combustivel:.2f} litros')