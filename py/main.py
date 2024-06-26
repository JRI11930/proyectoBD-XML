from crud import *
from queries import *
from xml_util import load_xml, save_xml

def main():
    # Cargar el archivo XML
    tree, root = load_xml('prueba.xml')

    # Realizar algunas operaciones CRUD
    add_property(root, 
                direccion='Calle Siempre Viva 3',
                tamaño=100,
                precio=100000,
                habitaciones=4,
                tipo='Casa',
                estado='Disponible',
                fecha_registro='20024-06-26',
                descripcion = 'Bonita casa moderna'
                )

    add_client( root, 
                nombre = 'Esteban Quito',
                email = 'equito@gmail.com',
                telefono = 5587945612,
                direccion = 'Avenida Siempre Viva 123',
                tipo = 'Departamento',
                rango_precio = '200000-300000',
                habitaciones = 2
                )

    add_agent(  root,
                nombre = "Ana Gómez",
                email = "ana.gomez@gmail.com",
                telefono = 5587945612,
                propiedad_id = 2
                )
    
    print("Se hicieron los CREATE")
    # Guardar los cambios en el archivo XML
    save_xml(tree, 'inmobiliaria.xml')

    #--------------------------------------------------------------------------------------------------------
    # QUERIES
    
    #   AGENTS
    agente, cuenta = get_agent_with_most_contracts(root, '2023')
    print("El agente con más contratos cerrados para el 2023 tiene el ID: ", agente, "y cerró ", cuenta, "contrato(s)")

    top_agent_id, top_agent_name, max_properties = get_agent_with_most_properties(root)
    if top_agent_id:
        print(f"Agente con más propiedades asignadas: {top_agent_name} (ID: {top_agent_id})")
        print(f"Número de propiedades asignadas: {max_properties}")
    else:
        print("No se encontró ningún agente con propiedades asignadas.")


    #   PROPERTIES
    available_properties = get_available_properties(root)
    print("Propiedades Disponibles:")
    for prop in available_properties:
        print(f"ID: {prop.find('id').text}, Tipo: {prop.find('tipo').text}, Precio: {prop.find('precio').text}")

    properties_in_range = get_properties_in_price_range(root, 50000, 100000)
    print("\nPropiedades en Rango de Precio 50,000 - 100,000:")
    for prop in properties_in_range:
        print(f"ID: {prop.find('id').text}, Tipo: {prop.find('tipo').text}, Precio: {prop.find('precio').text}")

    properties_by_type = get_properties_by_type(root, "Casa")
    print("\nPropiedades del Tipo Casa:")
    for prop in properties_by_type:
        print(f"ID: {prop.find('id').text}, Precio: {prop.find('precio').text}")

    property_counts = count_properties_by_type(root)
    print("Cuenta de cada tipo de propiedad:")
    for prop_type, count in property_counts.items():
        print(f"{prop_type}: {count}")

    property_status_counts = count_property_status_by_type(root)
    print("Cuenta de los estados de la propiedad agrupados por tipo de propiedad:")
    for prop_type, status_counts in property_status_counts.items():
        print(f"{prop_type}:")
        for status, count in status_counts.items():
            print(f"  {status}: {count}")

    #   CLIENTS

    total_clients = count_total_clients(root)
    print(f"Número total de clientes: {total_clients}")

    #CONTRATS
    year = '2023'
    total_contracts = count_contracts_closed_in_year(root, year)
    print(f"Total de contratos cerrados en {year}: {total_contracts}")

    contract_counts = count_contracts_by_type(root)
    print("Cuenta de cada tipo de contrato:")
    for contract_type, count in contract_counts.items():
        print(f"{contract_type}: {count}")

    average_house_price = calculate_average_house_price(root)
    if average_house_price is not None:
        print(f"Precio promedio de las casas: ${average_house_price:.2f}")
    else:
        print("No hay casas registradas en el sistema.")

if __name__ == "__main__":
    main()
