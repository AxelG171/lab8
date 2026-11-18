def minutos_por_usuario(reproducciones: list) -> dict:
    """
    Input:
        list: list de diccionarios con el usuario, artista y minutos
    Output:
        dict: diccionario con el par nombre - minutos totales de cada usuario
    """
    # Tu codigo empieza aquí. Recuerda eliminar el `pass`
    minutos_totales = {}
    
    for reproduccion in reproducciones:
        usuario = reproduccion["usuario"]
        minutos = reproduccion["minutos"]
        if usuario in minutos_totales:
            minutos_totales[usuario] += minutos
        else:
            minutos_totales[usuario] = minutos
    return minutos_totales

def artistas_por_usuario(reproducciones: list) -> dict:
    """
    Input:
        list: list de diccionarios con el usuario, artista y minutos
    Output:
        dict: diccionario con el par nombre - lista de los artistas de cada usuario
    """
    # Tu codigo empieza aquí. Recuerda eliminar el `pass`
    
    artistas = {}
    
    for reproduccion in reproducciones:
        usuario = reproduccion["usuario"]
        artista = reproduccion["artista"]
        if usuario in artistas:
            artistas[usuario].append(artista)
        else:
            artistas[usuario] = [artista]
    return artistas

def usuario_mas_activo(reproducciones: list) -> str:
    """
    Input:
        list: list de diccionarios con el usuario, artista y minutos
    Output:
        str: nombre del usuario con más minutos
    """
    # Tu codigo empieza aquí. Recuerda eliminar el `pass`
    
    minutos_totales = minutos_por_usuario(reproducciones)
    return max(minutos_totales, key=minutos_totales.get)


if __name__ == "__main__":
    reproducciones = [
        {"usuario" : "sofia" , "artista" : "Wolf Alice"   , "minutos" : 60 },
        {"usuario" : "daniel", "artista" : "Milo J"       , "minutos" : 30 },
        {"usuario" : "sofia" , "artista" : "Fleetwood Mac", "minutos" : 42 },
        {"usuario" : "carlos", "artista" : "Americania"   , "minutos" : 21 },
        {"usuario" : "elena" , "artista" : "Tame Impala"  , "minutos" : 25 },
        {"usuario" : "carlos", "artista" : "Dua Lipa"     , "minutos" : 56 },
        {"usuario" : "sofia" , "artista" : "MGMT"         , "minutos" : 43 },
        {"usuario" : "carlos", "artista" : "Dua Lipa"     , "minutos" : 20 }
    ]

    #print(minutos_por_usuario(reproducciones))  # -> {“sofia” : 145, “daniel” : 30, “carlos” : 97, “elena” : 25} 
    #print(artistas_por_usuario(reproducciones)) # -> {“sofia” : [“Wolf ALice”, “Fleetwood Mac”, MGMT],  
    #                                            #     “daniel” : [“Milo J”],  
    #                                            #     “carlos” : [“Americania”, “Dua Lipa”],  
    #                                            #     “elena”  : [“Tame Impala”]} 
    #print(usuario_mas_activo(reproducciones))   # -> sofia