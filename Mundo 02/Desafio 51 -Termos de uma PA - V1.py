primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digita a razão: '))
decimo = primeiroTermo + (10 - 1) * razao
for pro in range(primeiroTermo, decimo + razao, razao):
    print(pro)
