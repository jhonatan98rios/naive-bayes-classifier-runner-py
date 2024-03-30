import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Gerar dados aleatórios para as últimas 24 horas da ação
np.random.seed(42)
num_samples = 1000
data = np.random.randint(1000, 2000, size=(num_samples, 24))

# Calcular a inclinação da regressão linear para cada amostra
slope = []
for sample in data:
    X = np.arange(1, 25).reshape(-1, 1)
    y = sample.reshape(-1, 1)
    model = LinearRegression().fit(X, y)
    slope.append(model.coef_[0][0])

# Determinar as labels com base na inclinação da regressão
labels = []
for s in slope:
    if abs(s) > 8:
        if s > 0:
            labels.append(1)
        else:
            labels.append(-1)
    else:
        labels.append(0)

# Criar um DataFrame com os dados e as labels
df = pd.DataFrame(data, columns=[f'hour_{i}' for i in range(1, 25)])
df['action'] = labels

# Salvar o DataFrame em um arquivo CSV
df.to_csv('dados_acao.csv', index=False)
