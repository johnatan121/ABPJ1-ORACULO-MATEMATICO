potencia = float(input('digite a potencia do eletro (em watts); '))
horas = int(input('digite o numero de horas de uso por dias: ' ))
dias = int(input('digite o numero de dias de uso: '))
tarifa = float(input('digite o valor da tarifa de energia (R$/kwh) '))


consumo = (potencia*horas*dias)/1000
custo = consumo*tarifa

print(f'consumo total: {consumo:.2f} kwh')
print(f'custo total:{custo:.2f}')
