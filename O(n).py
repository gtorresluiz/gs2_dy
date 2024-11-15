import time

#O(n)
def encontrar_duplicados_n(lista):
    vistos = set()
    duplicados = set()
    for item in lista:
        if item in vistos:
            duplicados.add(item)
        else:
            vistos.add(item)
    return list(duplicados)

#O(n^2)
def encontrar_duplicados_n2(lista):
    duplicados = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados

lista = [50,100,150,200,250]
i = 1
while i <= 1000:
    lista.append(i)
    i+=1

# teste de medicao de tempo para a funcao O(n)
inicio_n = time.time()
encontrar_duplicados_n(lista)
fim_n = time.time()
tempo_n = fim_n - inicio_n
print(f"Tempo de execucao de encontrar_duplicados_n (O(n)): {tempo_n} segundos")

# teste de medicao de tempo para a funcao O(n^2)
inicio_n2 = time.time()
encontrar_duplicados_n2(lista)
fim_n2 = time.time()
tempo_n2 = fim_n2 - inicio_n2
print(f"\nTempo de execucao de encontrar_duplicados_n2 (O(n^2)): {tempo_n2} segundos")