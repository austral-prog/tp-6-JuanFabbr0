sample_input = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

def remove_elements(sample_input):
	
	if len(sample_input) >= 6:
		del sample_input[(0)]
		del sample_input[(3)]
		del sample_input[(3)]
		return(sample_input)
	elif len(sample_input) > 4 and len(sample_input) < 6:
		del sample_input [(0)]
		del sample_input[(3)]
		return(sample_input)
	elif len(sample_input) <=4 and len(sample_input) >= 1:
		del sample_input [(0)]
		return(sample_input)
	else:
		return(sample_input)

remove_elements(sample_input)


lista = ['Red', 'Green', 'White', 'Black']

def add_elements(lista):
	

	lista.append("Yellow")
	lista.insert(0, "Pink")
	return(lista)

add_elements(lista)


listado = []
def is_empty(listado):


	if len(listado) < 1:
		listado = True
	else:
		listado = False
	return(listado)

is_empty(listado)



list1 = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White'] 
list2 = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']

cal = len(list1)
culo = len(list2)

def check_lists(list1, list2):

	cal = len(list1)
	culo = len(list2)
	
	if cal < 3  or culo < 3:
		rta = False 
	else:
		if list2[2] != list1[2]:
			rta = False
		else:
			rta = True

	return(rta)

check_lists(list1, list2)

lista_de_listas = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]

def list_of_lists(lista_de_listas):
	lista01 = lista_de_listas[0]
	lista02 = lista_de_listas[1]
	lista03 = lista_de_listas[2]

	if len(lista01) >= 3:
		lista01 = lista01[:2]
	else:
		lista01 = lista01[:]

	if len(lista02) >= 4:
		lista02 = lista02[1:4]
	else:
		lista02 = lista02[1:]
	
	lista03 = lista03[-2:]
	
	nueva_lista_de_listas = [lista01, lista02, lista03]
	return(nueva_lista_de_listas)

list_of_lists(lista_de_listas)
