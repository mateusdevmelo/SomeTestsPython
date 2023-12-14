def acessar_chave_dicionario(dicionario):
    valor = dicionario.get('x', None) #já retorna None, então é opcional
    print(valor)