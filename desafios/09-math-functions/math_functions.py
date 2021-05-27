# Para rodar o teste mude para a pasta do desafio antes de rodar os testes:
# cd desafios/09-math-functions
# python -m unittest


from math import pi

def circle_area(r):
# Crie um função que retorne a área de um círculo, devendo o usuário indicar o raio para o cáculo
# Fórmula para cálculo de área (pi * (raio**2))
# Indicar TypeError para valores diferentes de inteiro e float (booleano ou string, por exempo)
# Indicar ValueError para valores negativos
  if type(r) not in [int, float]:
    raise TypeError("O valor do raio tem que ser um valor numérico não negativo")
  if r < 0:
    raise ValueError("Valor do raio não pode ser negativo.")
  return pi * r**2
