import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta función devuelve la lista de palabras que empiezan por una letra que alfabéticamente está antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """

    # La lista con el resultado se creaba dentro del bucle for, por lo que el contenido
    # de este era reseteado después de cada ciclo.
    # LO he solucionado definiendo la lista resultado fuera del bucle

    resultado=[]
    for clave in diccionario:
        for palabra in diccionario[clave]:
            if palabra[0] < letra:
                resultado.append(palabra)
    return resultado

def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta función inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    # La declaración era redundante, se añadía el valor de nif como nueva posición dos veces.
    # Para resolverlo, eliminé la segunda declaración del nif

    clients_list[nif] = {
          'name': name,
          'address': address,
          'phone': phone,
          'email': email
        }

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un número de repeticiones, esta función selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """  

    # La lista cartas_aleatorias se declara de tal forma que es un puntero a cartas_iniciales
    # por lo que al remover un elemento de una, se remueve también de otra.
    # Intenté resolverlo añadiendo manualmente, con append(), los elementos de una lista en otra
    
    combinaciones={}
    for i in range(1,repeticiones+1):

      cartas_aleatorias = []
      for j in range(len(cartas_iniciales)):
        cartas_aleatorias.append(cartas_iniciales[j])

      combinaciones["repeticion"+str(i)]=[]

      for j in range(0,5):
          carta=random.choice(cartas_aleatorias)
          combinaciones["repeticion"+str(i)].append(carta)
          cartas_aleatorias.remove(carta)

    return combinaciones