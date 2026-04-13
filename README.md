# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>


# Atividade 01- Fiap Inteligência Artificial Cardiologica #


## 👨‍🎓 Integrantes:
- João José Domingues Siva
- William Xavier
- Murílo Santana
- William Ferreira



## 👩‍🏫 Professores:
### Tutor(a)
- Caique Nonato da Silva Bezerra
### Coordenador(a)
- André Godoi

---

## 📜 Descrição
  
Este projeto faz parte do desafio CardioIA e tem como objetivo simular um sistema de diagnóstico automatizado utilizando Inteligência Artificial.

A solução desenvolvida integra técnicas de **Processamento de Linguagem Natural (NLP)** e **Machine Learning** para:

- Identificar sintomas em frases relatadas por pacientes  
- Sugerir possíveis diagnósticos com base em um mapa de conhecimento  
- Classificar o nível de risco (alto ou baixo) em um cenário de triagem clínica

##  Parte 1 – Extração de Sintomas

  Foi desenvolvido um sistema capaz de analisar frases em linguagem natural e identificar sintomas relevantes.
  
  A partir de um arquivo `.csv` contendo associações entre sintomas e doenças, o sistema sugere diagnósticos com base na presença de palavras-chave.
  
  Essa abordagem simula sistemas de apoio à decisão clínica utilizados em ambientes hospitalares.

---

## Parte 2 – Classificação de Risco com IA

Foi implementado um modelo de Machine Learning para classificar frases médicas em:

- **Alto risco**
- **Baixo risco**

### Técnicas utilizadas:
- TF-IDF (vetorização de texto)
- Regressão Logística (classificação)

O modelo apresentou uma acurácia aproximada de **91%**, demonstrando boa capacidade de identificar padrões mesmo com um conjunto de dados reduzido.

---

## Interpretação dos Resultados

O modelo apresentou alta precisão na identificação de casos de alto risco, o que é desejável em contextos clínicos, onde a priorização de pacientes mais graves é essencial.

Essa abordagem pode ser aplicada em sistemas de triagem automatizada, auxiliando profissionais de saúde na tomada de decisão.


## 📁 Estrutura de Pastas

<b>Resources/<b> <br>
├── frases de sintomas.txt  <br>
├── sintomas-doenca.csv <br>
├── dataset_classificacao.csv <br>
 <br>
reader.py <br>
classificador.py <br>
classificador.ipynb <br>

## 🗃 Histórico de lançamentos

* 14 de abril de 2026
  - release: 0.0.1   

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

> Projeto desenvolvido para fins acadêmicos, seguindo boas práticas de ciência de dados e aprendizado de máquina.

