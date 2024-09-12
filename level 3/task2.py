# task 2

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("house-prices.csv")

plt.scatter(df['SqFt'], df['Price'], alpha=0.5)
plt.title('House Price vs. Square Footage')
plt.xlabel('Square Footage (SqFt)')
plt.ylabel('Price')
plt.show()
