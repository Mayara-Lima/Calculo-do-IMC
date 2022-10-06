print("=== Vamos calcular o Índice de Massa Corporal - IMC: ===")

peso = float(input("Digite o peso:  "))
altura = float(input("Digite a altura:  "))
def imc():
    indice_massa_corporal = peso/(altura*altura)
    print("O IMC é:", indice_massa_corporal)
    if indice_massa_corporal > 0 and indice_massa_corporal <= 18.50:
        return "Abaixo do peso"
    elif indice_massa_corporal > 18.50 and indice_massa_corporal <= 25.00:
        return "Peso considerado normal"
    elif indice_massa_corporal > 25.00 and indice_massa_corporal <= 30.00:
        return "Sobrepeso"
    elif indice_massa_corporal > 30.00:
        return "Obesidade."

print(imc())
print("=== Se o resultado surpreendeu procure um profissional de saúde! ===")