lista_email = "fulano@gmail.com", "joao.silva@fiap.com.br", "maria.souza@fiap.com.br", "ana.paula@fiap.com.br"

for email in lista_email:
#    print(email)
    usuario, dominio = email.split("@")
    print(usuario)
    print(dominio)
def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dict_contagem = count_letters(dominio)
print(dict_contagem)

