# from converters import lbs_to_kg -
import converters
from converters import kg_to_lbs
from list_operators import find_max

resultado_1 = converters.lbs_to_kg(150)
# utilizando from ... poderia chamar apenas lbs_to_kg
print(resultado_1)

resultado_2 = kg_to_lbs(67.5)
print(resultado_2)

lista = [4, 6, 15, 10, 3, 32]
maximo_proprio = find_max(lista)
maximo_linguagem = max(lista) # cuidado para não utilizar nomes já existentes na linguagem (Roxo)
print(maximo_proprio)
print(maximo_linguagem)
