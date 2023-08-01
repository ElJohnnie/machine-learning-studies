var1 = 0.0
var2 = 0.0
var3 = 0.0

def ler_numeros():
    global var1, var2, var3
    var1 = float(input("Digite o primeiro número: "))
    var2 = float(input("Digite o segundo número: "))
    var3 = float(input("Digite o terceiro número: "))

def calcular_soma(a, b, c):
    soma = a + b + c
    print(soma)

def calcular_media(a, b, c):
    media = (a + b + c) / 3
    print(media)

ler_numeros()
calcular_soma(var1, var2, var3)
calcular_media(var1, var2, var3)
