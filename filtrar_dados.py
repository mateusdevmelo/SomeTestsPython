def filtar_dados():
    def is_primo(numero):
        if numero == 1:
            return False
        for i in range(2, numero):
            if numero % i == 0:
                return False
        
        return True


    numeros = [i for i in range(0, 100)]
    primos = list(filter(is_primo, numeros))
    print(primos)

filtar_dados()