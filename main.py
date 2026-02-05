potencia = float(input('digite a potencia do eletro (em watts); '))
horas = int(input('digite o numero de horas utilizado durante o dia: ' ))
dias = int(input('digite o numero de dias utilizado durante o mês: '))
tarifa = float(input('digite o valor da tarifa de energia (R$/kwh) '))


consumo = (potencia*horas*dias)/1000
custo = consumo*tarifa

print(f'consumo total: {consumo:.2f} kwh')
print(f'custo total:{custo:.2f}')
