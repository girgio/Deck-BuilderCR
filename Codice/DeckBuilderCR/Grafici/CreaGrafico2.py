import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

f = pd.read_csv('../Dati/Carte.csv', sep=';')
x = f[f.columns[0]]

y_danni = f[f.columns[1]]
y_vita = f[f.columns[2]]


for index in y_vita.index:
    y_vita.loc[index] = y_vita.loc[index]/6

#Calcolo medie
y_media_danni = np.mean(y_danni)
y_media_vita = np.mean(y_vita)
print(y_media_vita)
print(y_media_danni)

plt.figure(figsize=(10,8))

plt.scatter(x,y_danni,label='Danni')
#plt.plot(x,y_danni,linestyle="-",label='Andamento danni')

plt.scatter(x,y_vita,label='Vita')
#plt.plot(x,y_vita,linestyle="-",label='Andamento vita')

plt.title('Grafico vita e danni')
plt.grid(True)

plt.gca().axes.get_xaxis().set_visible(False)
plt.tick_params(axis='x', labelsize=6)
plt.legend()

plt.tight_layout()
plt.savefig('grafico2',dpi=300)
plt.show()