def run():
    # mi_diccionario = {
    #     'llave1': 1,
    #     'llave2': 2,
    #     'llave3': 3
    # }
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44948712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }
    # print(poblacion_paises['Argesntina'])

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for poblacion in poblacion_paises.values():
    #     print(poblacion)

    for pais, poblacion in poblacion_paises.items():
        print('Poblacion de ' + pais + ': ' + str(poblacion))


if __name__ == "__main__":
    run()
