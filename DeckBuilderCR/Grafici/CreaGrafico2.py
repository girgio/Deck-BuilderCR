import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

f = pd.read_csv('../Dati/Carte.csv', sep=';')
x = f[f.columns[0]]

y_velocita = f[f.columns[6]]
y_costo = f[f.columns[3]]
y_effetti = f[f.columns[9]]

#Calocolo valori medi
y_media_danni = np.mean(f[f.columns[1]])
y_media_vita = np.mean(f[f.columns[2]])

plt.figure(figsize=(10,8))

#plt.scatter(x,y_costo,label='Costo')
plt.plot(x,y_costo,linestyle="-",label='Andamento costo')

#plt.scatter(x,y_effetti,label='Effetti')
plt.plot(x,y_effetti,linestyle="-",label='Andamento effetti')

#plt.scatter(x,y_velocita,label='Velocita')
plt.plot(x,y_velocita,linestyle="-",label='Andamento velocita')

plt.title('Grafico costo,velocita ed effetti')
plt.grid(True)

plt.gca().axes.get_xaxis().set_visible(False)
plt.tick_params(axis='x', labelsize=6)
plt.legend()

plt.tight_layout()
plt.savefig('grafico2',dpi=300)
plt.show()