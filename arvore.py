from dicionario import paises

def criar_no(pais, ranking):
    return {'pais': pais, 'ranking': ranking, 'esquerda': {}, 'direita': {}}

def inserir(arvore, pais, ranking):
    if not arvore:  
        return criar_no(pais, ranking)
    elif ranking < arvore['ranking']:  
        arvore['esquerda'] = inserir(arvore['esquerda'], pais, ranking)
    else:  
        arvore['direita'] = inserir(arvore['direita'], pais, ranking)
    return arvore

def buscar_pais(arvore, PAIS):
        if PAIS in arvore:
            return print(f"{PAIS}:\n{arvore[PAIS]}")
        else:
            return None

def buscar_arvore(arvore, chave):
    if not arvore:
        return None
    elif chave == arvore['pais']:
        return arvore  
    elif chave < arvore['pais']:
        return buscar_arvore(arvore['esquerda'], chave)
    else:
        return buscar_arvore(arvore['direita'], chave)

def exibir_arvore(arvore, nivel=0):
    if not arvore:
        return ""
    
    resultado = ""
    resultado += exibir_arvore(arvore['esquerda'], nivel + 1) 
    resultado += " " * 4 * nivel + f"{arvore['pais']} - Ranking: {arvore['ranking']}\n" 
    resultado += exibir_arvore(arvore['direita'], nivel + 1)
  
    return resultado

arvore = {}
for pais, dados in paises.items():
    ranking = dados["Ranking_Energia_Sustentavel"]
    arvore = inserir(arvore, pais, ranking)

#buscar pais especifico
buscar_pais(paises, "ALEMANHA")

# Exibindo a arvore geral com ranking 
print("\nEstrutura geral de ranking:")
print(exibir_arvore(arvore))

#exemplo de insercao
pais_novo = "VENEZUELA"
arvore = inserir(arvore, pais_novo, 21) #ranking ficticio 
print("\nArvore atualizada com pais inserido:\n")
print(exibir_arvore(arvore))

# Exibindo um arvore gerada apartir do input 
arvore_input = buscar_arvore(arvore, 'CHINA')
print("Avore gerada do input:\n", exibir_arvore(arvore_input))