# Questão 1 - Python é uma linguagem de programação de alto nível, interpretada, orientada a objetos, de tipagem dinâmica e forte. O que cada uma dessas características significa?
# Programação de alto nível significa que sua sintaxe se aproxima mais da linguagem humana do que da linguagem de máquina, tornando-a mais intuitiva e menos propensa a erros. Interpretada significa que o código é executado linha por linha, sem a necessidade de compilação. Orientada a objetos significa que a linguagem suporta o paradigma de programação orientada a objetos, onde objetos são instâncias de classes que possuem atributos e métodos. Tipagem dinâmica significa que o tipo de uma variável é inferido em tempo de execução, não sendo necessário declarar o tipo de uma variável. Tipagem forte significa que a linguagem não faz conversões automáticas entre tipos de dados, sendo necessário realizar essas conversões explicitamente.


# Questão 2 - Fale sobre as funções input(), print() e o método format(). Além disso, dê exemplo dos principais tipos primitivos de dados em Python.
# input() é uma função que lê uma linha de texto do teclado e a retorna como uma string. print() é uma função que exibe uma mensagem na tela. format() é um método que permite formatar uma string, substituindo os marcadores de posição por valores passados como argumentos. Os principais tipos primitivos de dados em Python são: int (números inteiros, como 10 e 5), float (números de ponto flutuante, como 3.14 e 2.5), str (strings, como "Alice" e "Olá") e bool (valores booleanos, como true e false).


# Questão 3 - Elabore um programa que lê o nome e a nota de um aluno, depois exibe esses dados, mas com a nota formatada para exibir apenas uma casa decimal.
nome = input('Digite o nome do aluno ')
nota = float(input('Digite a nota do aluno'))
print("O aluno {} tirou a nota: {:.1f}".format(nome, nota))


# Questão 4 - Quais são os operadores matemáticos usados em Python? Dê exemplos.
# Os operadores matemáticos usados em Python são: adição (+), subtração (-), multiplicação (*), divisão (/), resto da divisão (%), exponenciação (**). Exemplos:
a = 5
b = 2
print(a + b)  # Soma: 7
print(a - b)  # Subtração: 3
print(a * b)  # Multiplicação: 10
print(a / b)  # Divisão: 2.5
print(a % b)  # Resto da divisão: 1
print(a ** b) # Exponenciação: 25


# Questão 5 - Dê um exemplo de uso da estrutura condicional aninhada (if, elif e else). 
# O exemplo a seguir verifica se um número é positivo, negativo ou zero:
num = float(input("Digite um número: "))
if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")


# Questão 6 - Quais são os operadores comparativos usados em Python? Dê exemplos.
# Os operadores comparativos usados em Python são: igual a (==), diferente de (!=), maior que (>), menor que (<), maior ou igual a (>=), menor ou igual a (<=). Exemplos:
a = 5
b = 2
print(a == b)  # Igual a: False
print(a != b)  # Diferente de: True
print(a > b)   # Maior que: True
print(a < b)   # Menor que: False
print(a >= b)  # Maior ou igual a: True
print(a <= b)  # Menor ou igual a: False


# Questão 7 - Quatro times estão disputando as semifinais de um campeonato de futebol. Leia os gols que cada time marcou em suas partidas e informe qual time saiu vencedor. Em caso de empate em uma das partidas, leia o número de pênaltis cobrados corretamente (valores entre 0 e 5) para cada time. Supondo que haverá dois times vencedores das partidas, exiba-os. Exemplo de mensagem final: “Os times A e B estão na grande final!”.
gols_time_a = int(input("Digite a quantidade de gols do time A: "))
gols_time_b = int(input("Digite a quantidade de gols do time B: "))
gols_time_c = int(input("Digite a quantidade de gols do time C: "))
gols_time_d = int(input("Digite a quantidade de gols do time D: "))

if gols_time_a > gols_time_b:
    vencedor1 = "A"
else:
    vencedor1 = "B"

if gols_time_c > gols_time_d:
    vencedor2 = "C"
else:
    vencedor2 = "D"

if gols_time_a == gols_time_b:
    penaltis_time_a = int(input("Digite a quantidade de pênaltis corretos do time A: "))
    penaltis_time_b = int(input("Digite a quantidade de pênaltis corretos do time B: "))
    if penaltis_time_a > penaltis_time_b:
        vencedor1 = "A"
    else:
        vencedor1 = "B"

if gols_time_c == gols_time_d:
    penaltis_time_c = int(input("Digite a quantidade de pênaltis corretos do time C: "))
    penaltis_time_d = int(input("Digite a quantidade de pênaltis corretos do time D: "))
    if penaltis_time_c > penaltis_time_d:
        vencedor2 = "C"
    else:
        vencedor2 = "D"

print("Os times {} e {} estão na grande final!".format(vencedor1, vencedor2))

# Questão 8 - Faça um programa que leia três números e, em seguida, exiba-os em ordem crescente.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        medio = num2
        maior = num3
    else:
        medio = num3
        maior = num2
elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        medio = num1
        maior = num3
    else:
        medio = num3
        maior = num1
else:
    menor = num3
    if num1 <= num2:
        medio = num1
        maior = num2
    else:
        medio = num2
        maior = num1

print("Os números em ordem crescente são: {}, {} e {}".format(menor, medio, maior))

# ou, simplesmente usando a função sort:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

numeros = [num1, num2, num3]
numeros.sort()

print("Os números em ordem crescente são:", numeros)


# Questão 9 - Elabore um programa que leia o salário mensal de uma pessoa, realize o cálculo do imposto de renda e, por fim, informe se a pessoa deve declarar ou não o imposto de renda. Assuma que será obrigada a apresentar a declaração anual a pessoa que receber rendimentos tributáveis, sujeitos ao ajuste na declaração, cuja soma foi superior a R$ 28.559,70.
salario = float(input("Digite o salário mensal: "))
imposto = 0

if salario <= 1903.98:
    imposto = 0
elif salario <= 2826.65:
    imposto = salario * 0.075
elif salario <= 3751.05:
    imposto = salario * 0.15
elif salario <= 4664.68:
    imposto = salario * 0.225
else:
    imposto = salario * 0.275

print("Imposto de renda a ser pago: R$ {:.2f}".format(imposto))

if salario * 12 > 28559.70:
    print("Deve declarar imposto de renda.")
else:
    print("Não precisa declarar imposto de renda.")


# Questão 10 - Faça um programa que calcule a conta de energia elétrica, solicitando apenas o número de kW/h e levando em consideração:

# a)     O preço do kW/h é R$ 0,56.
# b)     O valor da Geração de energia é 41% do valor do consumo.
# c)     O valor de imposto é de 22,52% do valor do consumo.
# d)     Qual a “bandeira” (acréscimo a cada kWh consumido) tarifária está em vigor:
#                         I.         Amarela: R$ 0,015.
#                        II.         Bandeira vermelha - Patamar 1: R$ 0,040.
#                       III.         Bandeira vermelha - Patamar 2: R$ 0,060.
# Informe o valor final da conta de Energia.
consumo = float(input("Digite o consumo em kW/h: "))
preco_kwh = 0.56
geracao_energia = consumo * 0.41
imposto = consumo * 0.2252
bandeira = 0

if consumo <= 100:
    bandeira = 0
elif consumo <= 150:
    bandeira = 0.015
elif consumo <= 200:
    bandeira = 0.040
else:
    bandeira = 0.060

valor_final = consumo * preco_kwh + geracao_energia + imposto + bandeira
print("O valor final da conta de energia é: R$ {:.2f}".format(valor_final))