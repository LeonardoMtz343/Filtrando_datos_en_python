DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # '''Vamos a obtener unicamente el nombre de los programadores de python'''
    # all_pyhton_devs = [worker ['name'] for worker in DATA if worker['language'] == 'python']

    # '''Vamos a obtener unicamente los trabajadores de Platzi'''
    # all_workers_platzi = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']

    # '''Vamos a obtener unicamente los adultos >18 años con filter'''
    # all_adults = list(filter(lambda worker: worker['age']>=18, DATA))

    # '''Anadimos un MAP para poder mostrar solo el nombre'''
    # all_adults=list(map(lambda worker: worker['name'], all_adults))

    # '''Aqui se agrega una nueva llave al diccionario all_adults que nos dice si el worker es mayor de 70 años'''
    # old_people =list(map(lambda worker: worker | {'old': worker['age']>70}, DATA))

    # RETO 

    ''' Vamos a obtener unicamente el nombre de los programadores de python usando Filter y map'''

    all_python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))

    all_python_devs = list(map(lambda workers: workers['name'], all_python_devs))




    print('Los desarrolladores de python son: ')
    for worker in all_python_devs:
        print(worker)

    # print('Los trabajadores de platzi son: ')
    # for worker in all_workers_platzi:
    #     print(worker)
    
    # print('Los usuarios adultos son ')
    # for worker in old_people:
    #     print(worker)



if __name__ == '__main__':
    run()
    