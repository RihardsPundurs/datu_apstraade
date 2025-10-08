import numpy as np
import math
import csv
import matplotlib.pyplot as plt

#primitiivais stjuudents
stjudenta_koef_95 = {100:1.984, 80:1.990, 60:2.000, 50:2.009}
def tuvaak(n):
	veertiibas = list(stjudenta_koef_95.keys())
	return min(veertiibas,key=lambda x:abs(x-n))


#datu ievade
pre_array = []
with open("data.csv") as raw_data:
	csvreader = csv.reader(raw_data)
	for i in csvreader:
		for j in i:
			pre_array.append(float(j))


arr = np.array(pre_array)
n = arr.shape[0]

while True:
	average = np.sum(arr)/n
	novirzes_arr = np.subtract(arr, average)
	novirzes_arr_kvad = np.power(novirzes_arr, 2)
	novirzes_arr_kvad_sum = np.sum(novirzes_arr_kvad)
	dispersija = math.sqrt(novirzes_arr_kvad_sum/(n-1))

	ticamiibas_intervaals = dispersija*stjudenta_koef_95[tuvaak(n)] ##pamainiit stjudenta_koef_95 tabulu uz kautko labaaku

	filtered = abs(novirzes_arr) < ticamiibas_intervaals
	arr = arr[filtered]

	if n != arr.shape[0]:
		n = arr.shape[0]
	else:
		n = arr.shape[0]
		break


#kljuudu apreekkins
avg_n_kvad_novirze = dispersija/math.sqrt(n)
avg_n_kvad_novirze = (1/n)*math.sqrt(novirzes_arr_kvad_sum)
gadiijuma_kljuuda = avg_n_kvad_novirze*stjudenta_koef_95[tuvaak(n)]
# 2.626
sistemaatiskaa_kluuda = 0.001
pilna_kluuda = math.sqrt(gadiijuma_kljuuda**2 + sistemaatiskaa_kluuda**2)
relatiivaa_kluuda_procentos = (pilna_kluuda/average)*100


#diagrammas
histogrammas_intervaalu_n = round(math.sqrt(n))
arr.sort()
max_n = float(arr[-1])
min_n = float(arr[0])

fig, ax = plt.subplots()
ax.set_xlabel("L, [mm]")
ax.set_ylabel("n, [mērījumu skaits]")
ax.set_axisbelow(True)
ax.grid(True,linestyle="-",linewidth=1,zorder=0,alpha=0.5)

counts,bins = np.histogram(arr, histogrammas_intervaalu_n)
ax.hist(bins[:-1], bins, weights=counts,linewidth=0.5, edgecolor="white",zorder=1)
h = bins[1] - bins[0]

x = np.linspace(min_n-2*h,max_n+2*h,n)
y = (n*h*np.exp(-((x-average)**2 / (2*dispersija**2))))/(np.sqrt(2*np.pi)*dispersija)
ax.plot(x,y,zorder=2)

print(dispersija)
print(pilna_kluuda)
print(arr.shape[0])
plt.show()
