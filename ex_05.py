from classes import Ponto, Retangulo

ponto_inicial = Ponto(2, 3)
retangulo1 = Retangulo(5, 4, ponto_inicial)
retangulo2 = Retangulo(3, 6, ponto_inicial)

# Encontrando e imprimindo o centro dos retângulos
centro1 = retangulo1.encontrar_centro()
centro1.imprimir()

centro2 = retangulo2.encontrar_centro()
centro2.imprimir()