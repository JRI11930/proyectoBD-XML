from lxml import etree as ET
from utils import generate_unique_id

def add_property(root, **kwargs):
    id = generate_unique_id()
    property_elem = ET.SubElement(root.find('propiedades'), 'propiedad')
    ET.SubElement(property_elem, 'id').text = str(id)
    for key, value in kwargs.items():
        elem = ET.SubElement(property_elem, key)
        elem.text = str(value)

def add_client(root, **kwargs):
    
    id = generate_unique_id()
    # Crear el nuevo elemento 'cliente'
    cliente_elem = ET.SubElement(root.find('clientes'), 'cliente')

    ET.SubElement(cliente_elem, 'id').text = str(id)
    # Crear y agregar subelementos al nuevo cliente

    nombre_elem = ET.SubElement(cliente_elem, 'nombre')
    nombre_elem.text = kwargs.get('nombre')

    email_elem = ET.SubElement(cliente_elem, 'email')
    email_elem.text = kwargs.get('email')

    telefono_elem = ET.SubElement(cliente_elem, 'telefono')
    telefono_elem.text = str(kwargs.get('telefono'))

    direccion_elem = ET.SubElement(cliente_elem, 'direccion')
    direccion_elem.text = kwargs.get('direccion')

    preferencias_elem = ET.SubElement(cliente_elem, 'preferencias')

    tipo_elem = ET.SubElement(preferencias_elem, 'tipo')
    tipo_elem.text = kwargs.get('tipo')

    rango_precio_elem = ET.SubElement(preferencias_elem, 'rango_precio')
    rango_precio_elem.text = kwargs.get('rango_precio')

    habitaciones_elem = ET.SubElement(preferencias_elem, 'habitaciones')
    habitaciones_elem.text = str(kwargs.get('habitaciones'))

def add_agent(root, **kwargs):
    id = generate_unique_id()
    # Crear el nuevo elemento 'agente'
    agent_elem = ET.SubElement(root.find('agentes'), 'agente')

    ET.SubElement(agent_elem, 'id').text = str(id)
    # Crear y agregar subelementos al nuevo cliente

    nombre_elem = ET.SubElement(agent_elem, 'nombre')
    nombre_elem.text = kwargs.get('nombre')

    email_elem = ET.SubElement(agent_elem, 'email')
    email_elem.text = kwargs.get('email')

    telefono_elem = ET.SubElement(agent_elem, 'telefono')
    telefono_elem.text = str(kwargs.get('telefono'))

    props_elem = ET.SubElement(agent_elem, 'propiedades_asignadas')

    propiedad_elem = ET.SubElement(props_elem, 'propiedad_id')
    propiedad_elem.text = str(kwargs.get('propiedad_id'))

def add_contract(root, **kwargs):
    id = generate_unique_id()
    # Crear un nuevo elemento contrato
    contrato_elem = ET.SubElement(root.find('contratos'), 'contrato')
    ET.SubElement(contrato_elem, 'id').text = str(id)
    # Agregar los subelementos con los valores proporcionados
    for key, value in kwargs.items():
        subelement = ET.SubElement(contrato_elem, key)
        subelement.text = str(value)