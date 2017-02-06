fich = open("/etc/passwd","r")
lineas=fich.readlines()
diccionario={}
for linea in lineas:
	login = linea[:linea.find(':')]
	shell = linea[linea.rfind(':')+1:-1 ]
	#Guardo cada login con su shell en un diccionario
	diccionario[login]= shell

#Devuelvo por la terminal el usuario root 
print('login: root ===== shel: ',diccionario['root'])
#utilizando try 
try:print(diccionario['imaginario'])
except KeyError: 
	print('El login introduccido no está en la lista')

 

