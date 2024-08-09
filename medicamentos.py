soma_preço = 0
soma_quantidade = 0
menor_preço = 0
n_menor_preço =                                                                                                                                                                                                  

while quantidade_med < 5:
n = (input("digite o nome do medicamento:")
p = float(input("digite o preço do medicamento:"))

soma_preço += preço
quantidade_med += 1
 if preço < menor_preço:
  menor_preço = preço
  n_menor_preço = n
media_preço = soma_preço / quantidade_med
print(f" a media dos medicamentos e {media_preço}")
print(f" o medicamento mais barato e {n_menor_preço} e o preço de reais {menor_preço}")
