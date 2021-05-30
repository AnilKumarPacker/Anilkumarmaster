from nsepy import get_history
from datetime import date

import matplotlib.pyplot as plt
data = get_history(symbol="NIFTY", start=date(2021,4,19), end=date(2021,4,19), index=True)

data['MA20'] = data['Close'].rolling(20).mean()
data['MA50'] = data['Close'].rolling(50).mean()

Buy = []
Sell = []

for i in range(len(data)):
    if data.MA20.iloc[i] > data.MA50.iloc[i] and data.MA20.iloc[i-1] < data.MA50.iloc[i-1]:
        Buy.append(i)
    elif data.MA20.iloc[i] < data.MA50.iloc[i] and data.MA20.iloc[i-1] > data.MA50.iloc[i-1]:
        Sell.append(i)

print(Buy)
print(Sell)

plt.plot(data['Close'], label='Close Price', c='blue')
plt.plot(data['MA20'], label='MA20', c='red')
plt.plot(data['MA50'], label='MA50', c='black')
plt.scatter(data.iloc[Buy].index, data.iloc[Buy]['Close'],marker='^', color='g', s=100)
plt.scatter(data.iloc[Sell].index, data.iloc[Sell]['Close'],marker='^', color='g', s=100)
plt.legend()
plt.show()