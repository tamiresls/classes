from classes import Retangulo

base_local = float(input('Digite a medida da base do seu local: '))
altura_local = float(input('Digite a medida da altura do seu local: '))

local = Retangulo(base_local, altura_local)

area_local = local.calcular_area()
quantidade_pisos = area_local

perimetro_local = local.calcular_perimetro()
quantidade_rodapes = perimetro_local

print(f'A quantidade de pisos necessários é: {quantidade_pisos} m2')
print(f'A quantidade de rodapés necessários é: {quantidade_rodapes} m')