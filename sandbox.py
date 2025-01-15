import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

w = {
    "05012025": 97.0,
    "06012025": 97.2,
    "07012025": 95.6,
    "08012025": 96.3,
    "09012025": 95.5,
    "10012025": 96.4,
    "11012025": 97.7,
    "12012025": 95.1,
    "13012025": 96.1,
    "14012025": 95.0,
    "15012025": 94.9
}
print(type(w))
ws = list(w.values())

# ma
window = 3
wma = np.convolve(ws, np.ones(window)/window, mode='valid')
print(ws)
print(wma)

# lr
days = np.array(range(len(ws))).reshape(-1, 1)
model = LinearRegression()
model.fit(days, ws)
trend = model.predict(days)
print(trend)



plt.plot(ws, label="Исходные данные")
plt.plot(range(window - 1, len(ws)), wma, label="Скользящее среднее", linestyle='--')
plt.plot(trend, label="Линейная регрессия (тренд)", linestyle='-.')
plt.xticks(rotation=90)
plt.legend()
plt.show()