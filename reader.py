import csv
import unicodedata
from collections import Counter


# Normalização (NLP básico)
# =========================
def normalizar(texto):
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8').lower()


# Ler TXT
# =========================
def ler_txt(arquivo_de_frases):
    try:
        with open(arquivo_de_frases, "r", encoding="utf-8") as arquivo:
            frases = arquivo.readlines()
        return frases
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_de_frases}' não foi encontrado.")
    except Exception as erro:
        print(f"Erro ao ler o arquivo: {erro}")


# Ler CSV
# =========================
def ler_csv(arquivo_sintomas_doenca):
    try:
        linhas = []
        with open(arquivo_sintomas_doenca, mode="r", encoding="utf-8") as arquivo:
            leitor_csv = csv.reader(arquivo)
            headers = next(leitor_csv)
            print(f"Headers: {headers}")
            for linha in leitor_csv:
                linhas.append(linha)
        return linhas
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_sintomas_doenca}' não foi encontrado.")


#  Diagnóstico melhorado
# =========================
def verificar_sintomas(frases, doenca_sintomas):
    for frase in frases:
        frase_original = frase.strip()
        frase = normalizar(frase)

        contador = Counter()

        for linha in doenca_sintomas:
            sintoma1 = normalizar(linha[0])
            sintoma2 = normalizar(linha[1])
            doenca = linha[2]

            if sintoma1 in frase or sintoma2 in frase:
                contador[doenca] += 1

        print(f"\n Frase: {frase_original}")

        if contador:
            print("Diagnóstico sugerido:")
            for doenca, qtd in contador.most_common():
                print(f"  - {doenca} (relevância: {qtd})")
        else:
            print("Nenhum diagnóstico encontrado")


# Execução
# =========================
frases = ler_txt("Resources\\frases de sintomas.txt")
doenca = ler_csv("Resources\\sintomas-doenca.csv")

verificar_sintomas(frases, doenca)