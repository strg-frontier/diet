import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

mesured_data = pd.read_csv("diet.csv")
mesured_data.head(5)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
y1=mesured_data["Mesured"]
x1=pd.to_datetime(mesured_data["Date"])
ax.plot(x1,y1)
plt.ylim([70,90])
plt.show()
