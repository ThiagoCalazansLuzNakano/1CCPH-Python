# REVISÃO: DESAFIO API em Alerta

endpoints = ["/login", "/produtos", "/pedidos"]

status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

#Função para detectar se UM status é sucesso

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <=299

#print(eh_sucesso(401))

#Função que valida na lista de req de um endpoint se tem dois erros sequidos
# status[o] = [200, 200, 401, 200, 500] ---> False
# status[2] = [201, 500, 502, 201, 500] ---> True

# [201, 500, 502, 201, 500] ==> respostas_http
def erros_seguidos(resposta_http):
    for i in range(len(resposta_http) - 1):
        codigo_atual = resposta_http[i]
        prox_codigo = resposta_http[i + 1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

def analizar_endpoint(resposta_http):
    qtd_sucessos = 0

    for cod_http in resposta_http:
        if eh_sucesso(cod_http):
            qtd_sucessos += 1

    qtd_tot_req = len(resposta_http)
    qtd_erros = qtd_tot_req - qtd_sucessos

    percentual_sucessos = (qtd_sucessos / qtd_tot_req) * 100

    tem_erros_seguidos = erros_seguidos(resposta_http)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif percentual_sucessos >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return (qtd_sucessos, qtd_erros, percentual_sucessos, classificacao)

#PERCORRENDO TODA A MATRIX
maior_qtd_erros = -1
endpoint_maior_erros = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    respostas_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analizar_endpoint(respostas_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Respostas http: {respostas_endpoint}")
    print(f"Erros: {erros}")
    print(f"% de sucessos: {percentual}")
    print(f"Classificacao: {classificacao}")
    print("-" * 30)
    print()

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoint_maior_erros = nome_endpoint

print(f"Endpoint com mais erros é: {endpoint_maior_erros} ({maior_qtd_erros})")