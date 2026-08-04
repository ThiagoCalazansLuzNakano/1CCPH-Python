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
#print(eh_sucesso(status[2][4])) -> MAX

print(eh_sucesso(status[0][0]))
print(eh_sucesso(status[0][1]))
print(eh_sucesso(status[0][2]))
print(eh_sucesso(status[0][3]))
print(eh_sucesso(status[0][4]))
print(eh_sucesso(status[1][0]))

