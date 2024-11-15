# utilizando um trecho da linha verde de sao paulo
estacoes = [
    "Vila Prudente", "Tamanduateí", 
    "Sacomã", "Alto do Ipiranga", 
    "Chácara Klabin", "Ana Rosa",
    "Paraíso", "Brigadeiro", 
    "Trianon-Masp", "Consolação"  
]

n = len(estacoes) #10

matriz = [[0] * n for _ in range(n)]

for i in range(n - 1):
    matriz[i][i + 1] = 1  
    matriz[i + 1][i] = 1  

# exibicao da matriz de adjacencias
print("Matriz de Adjacencias para a Linha 2 - Verde:\n")
for col in matriz:
    print(col)
