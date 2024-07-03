import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from crud import *
from queries import *
from xml_util import load_xml, save_xml

def actualizar_datos(root):
    add_property(root, 
                direccion='Calle Siempre Viva 3',
                tamaño=100,
                precio=100000,
                habitaciones=0,
                tipo='Terreno',
                estado='Disponible',
                fecha_registro='20024-06-26',
                descripcion = 'Terreno en gran ubicación'
                )
    add_property(root, 
                direccion='Avenida Principal 123',
                tamaño=150,
                precio=250000,
                habitaciones=0,
                tipo='Terreno',
                estado='Disponible',
                fecha_registro='2024-05-15',
                descripcion = 'Excelente precio'
                )
    add_property(root, 
                direccion='Plaza Central 45',
                tamaño=200,
                precio=300000,
                habitaciones=6,
                tipo='Casa',
                estado='Disponible',
                fecha_registro='2024-06-01',
                descripcion='Casa espaciosa en la mejor zona de la ciudad'
                )
    add_client( root, 
                nombre = 'Esteban Quito',
                email = 'equito@hotmail.com',
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
    add_contract(root, 
             id_propiedad='10',
             id_cliente='5',
             id_agente='3',
             fecha_inicio='2024-07-01',
             fecha_fin='2025-07-01',
             tipo='Alquiler',
             monto='3000')
    add_contract(root, 
             id_propiedad='9',
             id_cliente='5',
             id_agente='2',
             fecha_inicio='2024-07-01',
             fecha_fin='2025-07-01',
             tipo='Venta',
             monto='3000')
    add_contract(root,
             id_propiedad='3',
             id_cliente='4',
             id_agente='2',
             fecha_inicio='2024-07-01',
             fecha_fin='2025-07-01',
             tipo='Alquiler',
             monto='3000')

def consultar_agentes(root):
    agente, cuenta = get_agent_with_most_contracts(root, '2023')
    print("El agente con más contratos cerrados para el 2023 tiene el ID: ", agente, "y cerró ", cuenta, "contrato(s)")

    top_agent_id, top_agent_name, max_properties = get_agent_with_most_properties(root)
    if top_agent_id:
        print(f"Agente con más propiedades asignadas: {top_agent_name} (ID: {top_agent_id})")
        print(f"Número de propiedades asignadas: {max_properties}")
    else:
        print("No se encontró ningún agente con propiedades asignadas.")

def consultar_propiedades(root):
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

def consultar_clientes(root):
    total_clients = count_total_clients(root)
    print(f"Número total de clientes: {total_clients}")

def consultar_contratos(root):
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

def submenuConsultas(root):
    while True:
        print("\n----- REALIZAR CONSULTAS -----")
        print("1.- Agentes")
        print("2.- Propiedades")
        print("3.- Clientes")
        print("4.- Contratos")
        print("5.- Volver al menú principal")
        opcion_submenu = input("\nSeleccione una opción del submenu: ")
        
        if opcion_submenu == '1':
            consultar_agentes(root)
        elif opcion_submenu == '2':
            consultar_propiedades(root)
        elif opcion_submenu == '3':
            consultar_clientes(root)
        elif opcion_submenu == '4':
            consultar_contratos(root)
        elif opcion_submenu == '5':
            break
        else:
            print("\nOpción no válida, por favor intente de nuevo.")

def visualizar_datos():

    #Extracción de los datos
    df_propiedades = pd.read_xml('inmobiliaria.xml', xpath='.//propiedad')
    df_clientes = pd.read_xml('inmobiliaria.xml', xpath='.//cliente')
    df_agentes = pd.read_xml('inmobiliaria.xml', xpath='.//agente')
    df_contratos = pd.read_xml('inmobiliaria.xml', xpath='.//contrato')
    
    df_clientes = df_clientes.drop(['preferencias'], axis=1)
    
    print(" ----- PROPIEDADES -----\n")
    print(df_propiedades.head(), "\n")
    print(df_propiedades.shape, "\n") 

    print("----- CLIENTES -----\n")
    print(df_clientes.head(),"\n")
    print(df_clientes.shape, "\n")

    print("----- AGENTES-----\n")
    print(df_agentes.head(),"\n")
    print(df_agentes.shape, "\n") 

    print("----- CONTRATOS-----\n")
    print(df_contratos.head(),"\n")
    print(df_contratos.shape, "\n")

    df_agentes_contratos = df_contratos.groupby('id_agente').size().reset_index(name='contratos')
    df_agentes_contratos = df_agentes_contratos.merge(df_agentes[['id', 'nombre']], left_on='id_agente', right_on='id')
    df_agentes_contratos = df_agentes_contratos.sort_values(by='contratos', ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(y='nombre', x='contratos', data=df_agentes_contratos, palette='viridis')
    plt.ylabel('Agente')
    plt.xlabel('Cantidad de Contratos')
    plt.title('Cantidad de Contratos Cerrados por Agente')
    plt.xticks(range(df_agentes_contratos['contratos'].max() + 2))
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='tipo', y='precio', data=df_propiedades, palette='viridis')
    plt.xlabel('Tipo de Propiedad')
    plt.ylabel('Precio')
    plt.title('Distribución de Precios de las Propiedades por Tipo')
    plt.tight_layout()
    plt.show()

    df_casas_disponibles = df_propiedades[df_propiedades['tipo']== 'Casa']
    conteo_estado = df_casas_disponibles['estado'].value_counts()

    plt.figure(figsize=(10,6))
    plt.subplot(1,3,1)
    conteo_estado.plot(kind='pie', autopct='%1.1f%%', colors = ['orange','red'], startangle = 90, ylabel='Casas', shadow = True)

    df_departamentos_disponibles = df_propiedades[df_propiedades['tipo']== 'Departamento']
    conteo_estado = df_departamentos_disponibles['estado'].value_counts()
    plt.subplot(1,3,2)
    conteo_estado.plot(kind='pie', autopct='%1.1f%%', colors =['red','orange'], startangle=90, ylabel='Departamentos', shadow = True)

    df_terrenos_disponibles = df_propiedades[df_propiedades['tipo']== 'Terreno']
    conteo_estado = df_terrenos_disponibles['estado'].value_counts()
    plt.subplot(1,3,3)
    conteo_estado.plot(kind='pie', autopct='%1.1f%%', colors =['orange','red'], startangle = 90, ylabel='Terrenos', shadow = True)

    plt.suptitle("Distribución de propiedades Disponibles y Vendidas según el tipo")
    plt.show()
    
def validar_documento():
    with open('prueba.xsd', 'rb') as f:
        schema_root = ET.XML(f.read())
        schema = ET.XMLSchema(schema_root)

    # Cargar el documento XML como bytes
    with open('inmobiliaria.xml', 'rb') as f:
        xml_doc = ET.XML(f.read())

    # Validar el documento XML
    try:
        schema.assertValid(xml_doc)
        print("El documento XML es válido.")
    except ET.DocumentInvalid as e:
        print("El documento XML no es válido.")
        print(e)

def main():
    tree, root = load_xml('prueba.xml')
    while True:
        
        print("\n ----- PROYECTO FINAL -----")
        print("\n1.- Actualizar datos")    
        print("\n2.- Realizar consultas")
        print("\n3.- Visualizar datos")
        print("\n4. Validar documento")
        print("\n5.- SALIR")
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            actualizar_datos(root)
            save_xml(tree, 'inmobiliaria.xml')
        elif opcion == '2':
            submenuConsultas(root)
        elif opcion == '3':
            visualizar_datos()
        elif opcion == '4':
            validar_documento()
        elif opcion == '5':
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()