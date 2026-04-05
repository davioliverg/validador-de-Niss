def validar_nif(nif):
    if len(nif) != 9 or not nif.isdigit():
        return False

    total = 0
    peso = 9

    for i in range(8):
        total += int(nif[i]) * peso
        peso -= 1

    resto = total % 11

    if resto < 2:
        digito = 0
    else:
        digito = 11 - resto

    return digito == int(nif[8])


# Teste
nif = input("Digite o NIF: ")

if validar_nif(nif):
    print("NIF válido ✅")
else:
    print("NIF inválido ❌")