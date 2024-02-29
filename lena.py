import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 1. Загрузка данных из CSV файла
data = pd.read_csv("cats_dataset.csv")

# Удалим столбец 'Name', так как он не несет информационной нагрузки для обучения модели
data.drop(columns=['Name'], inplace=True)

# Предположим, что в столбце 'Breed' содержится целевая переменная - порода кошки
# Преобразование текстовых значений пород кошек в числовые индексы с помощью метода pd.factorize()
data['Breed'], breed_mapping = pd.factorize(data['Breed'])

# Создание словаря, где ключами будут числовые индексы, а значениями - соответствующие им текстовые значения пород кошек
breed_index_to_name = {index: breed for index, breed in enumerate(breed_mapping)}

# Разделение данных на признаки (X) и целевую переменную (y)
X = data.drop(columns=['Breed']).values
y = data['Breed'].values

# 2. Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Создание многослойного персептрона
model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(10,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 выходных нейронов для 10 пород кошек
])

# Компиляция модели
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 4. Обучение сети
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# 5. Оценка производительности модели на тестовых данных
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print('Test accuracy:', test_accuracy)

# Визуализация кривой обучения (learning curve)
plt.figure(figsize=(10, 5))
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend()
plt.show()

# Предсказания модели для тестовых данных
y_pred = model.predict(X_test)

data_new = pd.read_csv("test_dataset.csv")
X_new = data_new.drop(columns=['Breed','Name']).values

# Вызов метода predict() для модели и передача новых данных X_new
predictions = model.predict(X_new)

# Преобразование числовых предсказаний в текстовые значения пород кошек с использованием соответствия
predicted_breeds_index = [np.argmax(prediction) for prediction in predictions]
predicted_breeds = [breed_index_to_name[index] for index in predicted_breeds_index]

# Создание DataFrame с характеристиками кошек и предсказанными породами
predicted_data = pd.DataFrame(X_new, columns=data.columns[1:])  # Создаем DataFrame с характеристиками кошек без столбца 'Name'
predicted_data['Predicted Breed'] = predicted_breeds  # Добавляем предсказанные породы в DataFrame

# Вывод DataFrame с предсказанными породами
print(predicted_data)
