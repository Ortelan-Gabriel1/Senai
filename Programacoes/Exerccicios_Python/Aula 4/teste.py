def produto_dos_digitos(numero):
    # Verifica se o número é zero ou negativo
    if numero <= 0:
        return "Não é possível calcular o produto dos dígitos de um número negativo ou zero."
    
    produto = 1
    
    # Enquanto o número for maior que zero
    while numero > 0:
        # Obtém o último dígito do número
        digito = numero % 10
        # Multiplica o produto pelo dígito
        produto *= digito
        # Remove o último dígito do número
        numero //= 10
    
    return produto

# Entrada do usuário
numero = int(input("Digite um número inteiro positivo: "))

# Chama a função e imprime o resultado
print(produto_dos_digitos(numero))
