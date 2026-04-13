import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

#dataset

df = pd.read_csv("Resources/dataset_classificacao.csv")

# Separar dados
# =========================
X = df["frase"]
y = df["situacao"]


vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.3, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

#Avaliação

print("\n Acurácia:", accuracy_score(y_test, y_pred))
print("\n Relatório:")
print(classification_report(y_test, y_pred))

# =========================
while True:
    frase = input("\nDigite uma frase (ou 'sair'): ")
    if frase.lower() == "sair":
        break

    frase_vec = vectorizer.transform([frase])
    pred = model.predict(frase_vec)

    print(f"Classificação: {pred[0]}")