import json
nombre_archivo="markers_data.txt"#definimos el nombre del archivo a crear json
aux=open(nombre_archivo,'r')#abrimos el archivo
data=json.load(aux)#cargamos el archivo
aux.close()
archivo=open("markers_data.json","w")#creamos el nuevo json
conjunto={}
archivo.write("[")
a=0
for i in data:#Este proceso crea el json a partir de un txt para luego poder cargarlo a la BD
	a+=1
	print(a)
	if 	i["name"] not in conjunto.keys():
		conjunto[i["name"]]="nada"
		linea=str(i)
		linea.replace("'",'"')
		archivo.write('{"name":"'+str(i["name"])+'","lat":'+str(i["lat"])+',"lng":'+str(i["lng"])+',"tipo":"'+str(i["tipo"])+'"},\n')
	else:
		print("Duplicado")
archivo.write("]")
