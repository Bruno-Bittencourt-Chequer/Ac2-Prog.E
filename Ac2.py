#EX01: Bháskara em função

import math

def bhaskara(a, b, c):
    delta = b**2 - 4*a*c   # Cálculo do delta
     
    if delta < 0:
        return "Não há raízes reais na equação"
        
    elif delta == 0: 
        x = -b / (2*a)
        return f"As raízes são iguais, com o valor sendo {x}"

    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"as raízes são {x1} e {x2}" 

a=1
b=-3
c=2
print(bhaskara(a,b,c))



#ANO BISSEXTO

def bissexto(ano):
    if ano % 4 == 0 and ano % 100 == 0 or ano % 400 != 0:
        return True
    else:
        return False

def ler_ano():
    return int(input("Digite um ano: "))

ano = ler_ano()

resultado=bissexto(ano)
print(resultado)



#CÁLCULO DE SALÁRIO

def calcula_salario(valor_hora, num_horas, irpf=0.275):
    salario_bruto = valor_hora * num_horas
    salario_liquido = salario_bruto - (salario_bruto * irpf)
    return salario_liquido


valor_hora = 22
num_horas = 165
salario_liquido = calcula_salario(valor_hora, num_horas)
print("Salário líquido:", salario_liquido)

