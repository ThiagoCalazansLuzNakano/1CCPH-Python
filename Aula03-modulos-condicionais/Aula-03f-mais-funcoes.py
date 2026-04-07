# FUNÇÃO COM PARAMETRO SEM RETORNO
def boas_vindas(nome):
    print(f"Olá, {nome}! Seja bem-vindo!!")

nome_digitado = input("Digite se nome: ")
boas_vindas(nome_digitado)

# FUNCAO COM PARAM. COM RETORNO
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado_soma = soma(5,9)
print(resultado_soma)
print(type(nome_digitado))
