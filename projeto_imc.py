## Solicitando ao usuário o peso e altura para realização dos cálculos
print("Programa de cálculo IMC (Obs: Coloque um ponto quando colocar vírgula | Ex: 1.70)")
peso = float(input("Programa de IMC: Qual o seu peso em quilogramas: "))
altura = float(input("E qual a sua altura em metros: "))


## Cálculo do IMC (IMC = Peso em quilogramas / Altura em metros x Altura em metros)
# Para diminuição do código foi utilizado (** | Variável para calcular a potência) para que não precisasse colocar duas multiplicações
imc = peso / (altura ** 2)


## Retornando o resultado para o usuário
# Utilizado a variável (.format) para a diminuição das casas decimais do resultado do IMC (Ex: 30,9999999999999999999)
print("Seu IMC é: {:.1f}".format(imc))


## Classificações de peso com base na tabela IMC
# Abaixo do peso normal (Menor que 18,5)
if imc < 18.5:
    print("Você está abaixo do peso normal")


# Peso normal (Entre 18,5 e 24,9)
elif 18.5 <= imc < 24.9:
    print("Você está com um peso normal")


# Excesso de peso (Entre 25 e 29,9)
elif 25 <= imc < 29.9:
    print("Você está com excesso de peso")


# Obesidade moderada (Grau I) (Entre 30 e 34,9)
elif 30 <= imc < 34.9:
    print("Você está com uma obesidade moderada")


# Obesidade severa (Grau II) (Entre 35 e 39,9)
elif 35 <= imc < 39.9:
    print("Você está com uma obesidade severa")


# Obesidade mórbida (Grau III) (Igual ou Maior que 40)
else:
    print("Você está com uma obesidade mórbida")


# Quando executamos o arquivo "Projeto IMC.py" se não inserirmos o input abaixo, o programa fechará logo em seguida do resultado
input("Pressione enter para sair...")