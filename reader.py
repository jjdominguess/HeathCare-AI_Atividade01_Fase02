import csv

def ler_txt(arquivo_de_frases):
    try:     
        with open(arquivo_de_frases, "r", encoding="utf-8") as arquivo:
            frases = arquivo.readlines()
            print(f"Frases lidas do arquivo '{arquivo_de_frases}':")
            for frase in frases:
                frase = frase.lower()
                # print(frase.strip())
        return frases
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_de_frases}' não foi encontrado.")
    except Exception as erro:
        print(f"Erro ao ler o arquivo: {erro}")

def ler_csv(arquivo_sintomas_doenca):
    try: 
        linhas = []
        with open(arquivo_sintomas_doenca, mode= "r", encoding="utf-8") as arquivo: 
            leitor_csv = csv.reader(arquivo)
            headers = next(leitor_csv)
            print(f"Headers: {headers}")
            for linha in leitor_csv:
                # print(f"Linha: {linha}")
                linhas.append(linha)
        return linhas
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_sintomas_doenca}' não foi encontrado.")

def verificar_sintomas(frases, doenca_sintomas):
    for frase in frases:
        frase = frase.lower()
        doenca_encontrada = set()
        for linha in doenca_sintomas:
            sintoma1 = linha[0]  # Supondo que o sintoma esteja na primeira coluna
            sintoma2 = linha[1]  # Supondo que o sintoma esteja na segunda coluna
            doenca = linha[2]    # Supondo que a doença esteja na terceira coluna         
            if sintoma1.lower() in frase or sintoma2.lower() in frase:
                doenca_encontrada.add(doenca)
        print(f"\nFrase: {frase.strip()}")
        print(f"Possíveis doenças: {list(doenca_encontrada)}")

frases = ler_txt("frases de sintomas.txt")
doenca = ler_csv("sintomas-doenca.csv")

verificar_sintomas(frases, doenca)