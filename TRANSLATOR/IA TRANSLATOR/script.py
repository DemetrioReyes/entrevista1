import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt


# Palabras clave en español e inglés
SPANISH = {
    "el", "la", "de", "que", "y", "en", "un", "ser", "se", "no", "haber", "por", "con", "una", "los", "las", 
    "este", "como", "más", "pero", "sus", "ya", "muy", "si", "sobre", "entre", "cuando", "todo", "solo", 
    "también", "fue", "porque", "hacer", "o", "está", "yo", "sí", "sin", "hasta", "desde", "nosotros", "te", 
    "uno", "le", "cual", "dos", "gran", "tiempo", "ese", "alguien", "tener", "hacer", "tanto", "otros", "ni", 
    "consecuentemente", "sin embargo", "con respecto a", "a pesar de", "aunque", "por lo tanto", "independientemente", 
    "adicionalmente", "por consiguiente", "en consecuencia", "entonces", "así que", "precisamente", "sin lugar a dudas", 
    "de hecho", "por lo general", "en realidad", "no obstante", "es decir", "en fin"
}

ENGLISH = {
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "it", "for", "not", "on", "with", "as", "I", "at", 
    "this", "but", "by", "from", "they", "we", "you", "say", "her", "she", "or", "an", "will", "my", "one", "all", 
    "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", 
    "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", "people", "into", "year", "your", 
    "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", 
    "consequently", "nevertheless", "therefore", "although", "nonetheless", "hence", "moreover", "furthermore", 
    "in fact", "thus", "regardless", "in addition", "meanwhile", "accordingly", "on the other hand", "as a result", 
    "in conclusion", "in other words", "on the contrary", "subsequently", "similarly", "notwithstanding"
}
# algunos datos para darle el entrenamiento al modelo utilizado
data = [
    ("me gusta la comida", "es"),
    ("I really like womens", "en"),
    ("hoy el dia esta soleado", "es"),
    ("This is an English sentence", "en"),
    ("Me gusta el fútbol y football", "mix"),
    ("I love pizza y la comida colombiana", "mix"),
]

df = pd.DataFrame(data, columns=["text", "label"])


# conteo de palabras clave para luego vectorizarlas
def vectorizacion(text):
    textos = set(text.lower().split())
    count_es = sum(1 for word in textos if word in SPANISH)
    count_en = sum(1 for word in textos if word in ENGLISH)
    return [count_es, count_en]


X = np.array([vectorizacion(text) for text in df["text"]])
y = df["label"]

# Codificar las etiquetas
label_encoder = LabelEncoder()  # convertir etiquetas categóricas en valores numéricos
y_encoded = label_encoder.fit_transform(y)  # transformacion a valores numéricos.

# division del conjunto de entrenamiento
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# inicializar el modelo usando keras
model = tf.keras.Sequential(
    [
        tf.keras.Input(
            shape=(2,)
        ),
        tf.keras.layers.Dense(
            10, activation="relu"
        ),  # relu para convertir valores negativo a 0
        tf.keras.layers.Dense(10, activation="relu"),
        tf.keras.layers.Dense(3, activation="softmax"),  # obtener las probabilidades
    ]
)

model.compile(
    optimizer=tf.keras.optimizers.Adam(0.01),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

print("Comenzando entrenamiento...")
# Entrenar el modelo
history = model.fit(X_train, y_train, epochs=250, validation_split=0.2, verbose=False)
print("Modelo entrenado! \n")


# evaluacion del modelo
loss, accuracy = model.evaluate(X_test, y_test)
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(history.history["loss"])
plt.show()


# Función para detectar el idioma de un texto
def detect_language(text):
    features = np.array(vectorizacion(text)).reshape(1, -1)  # Vectoriza el texto
    prediction = model.predict(
        features
    )  # Realiza una predicción con el modelo entrenado
    return label_encoder.inverse_transform([np.argmax(prediction)])[
        0
    ]  # retornar la prediccion


texto = ["if tu belive en mi, i can mostrarte anything puedo hacer for you"]
for texto in texto:
    # Imprime el texto de ejemplo y el idioma detectado por el modelo
    print(f"Texto: '{texto}' → Idioma: {detect_language(texto)}")
