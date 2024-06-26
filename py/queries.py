from lxml import etree

#   Agents
def get_agent_with_most_contracts(root, year):
    contracts = root.xpath(f"//contratos/contrato[starts-with(fecha_fin, '{year}')]")
    agent_counts = {}
    for contract in contracts:
        agent_id = contract.find('id_agente').text
        if agent_id in agent_counts:
            agent_counts[agent_id] += 1
        else:
            agent_counts[agent_id] = 1
    max_agent = max(agent_counts, key=agent_counts.get)
    return max_agent, agent_counts[max_agent]

def get_agent_with_most_properties(root):
    agent_property_counts = {}
    properties = root.xpath("/propiedades/propiedad")

    for prop in properties:
        agent_id = prop.find('agente_id').text
        
        if agent_id in agent_property_counts:
            agent_property_counts[agent_id] += 1
        else:
            agent_property_counts[agent_id] = 1
    
    # Encontrar el agente con más propiedades
    max_properties = -1
    top_agent_id = None
    for agent_id, count in agent_property_counts.items():
        if count > max_properties:
            max_properties = count
            top_agent_id = agent_id

    top_agent = root.xpath(f"/agentes/agente[id='{top_agent_id}']")
    if top_agent:
        top_agent = top_agent[0]
        top_agent_name = top_agent.find('nombre').text
        return top_agent_id, top_agent_name, max_properties
    else:
        return None, None, 0


#   Properties
def get_available_properties(root):
    properties = root.xpath("//propiedades/propiedad[estado='Disponible']")
    return properties

def get_properties_in_price_range(root, min_price, max_price):
    properties = root.xpath(f"//propiedades/propiedad[precio >= {min_price} and precio <= {max_price}]")
    return properties

def get_properties_by_type(root, property_type):
    properties = root.xpath(f"//propiedades/propiedad[tipo='{property_type}']")
    return properties

def count_properties_by_type(root):
    property_types = {}
    properties = root.xpath("//propiedades/propiedad/tipo")
    
    for prop_type in properties:
        if prop_type.text in property_types:
            property_types[prop_type.text] += 1
        else:
            property_types[prop_type.text] = 1
    
    return property_types

def count_property_status_by_type(root):
    property_status_counts = {}
    properties = root.xpath("//propiedades/propiedad")
    
    for prop in properties:
        prop_type = prop.find('tipo').text
        prop_status = prop.find('estado').text
        
        if prop_type not in property_status_counts:
            property_status_counts[prop_type] = {}
        
        if prop_status in property_status_counts[prop_type]:
            property_status_counts[prop_type][prop_status] += 1
        else:
            property_status_counts[prop_type][prop_status] = 1
    
    return property_status_counts

#   Clients

def count_total_clients(root):
    clients = root.xpath("//clientes/cliente")
    total_clients = len(clients)
    return total_clients

#   Contrats
def count_contracts_closed_in_year(root, year):
    contracts = root.xpath(f"//contratos/contrato[starts-with(fecha_fin, '{year}')]")
    total_contracts = len(contracts)
    return total_contracts

def count_contracts_by_type(root):
    contract_types = {}
    contracts = root.xpath("//contratos/contrato/tipo")
    
    for contract_type in contracts:
        if contract_type.text in contract_types:
            contract_types[contract_type.text] += 1
        else:
            contract_types[contract_type.text] = 1
    
    return contract_types

def calculate_average_house_price(root):
    houses = root.xpath("//propiedades/propiedad[tipo='Casa']/precio")
    total_houses = len(houses)
    
    if total_houses == 0:
        return None
    
    total_price = sum(float(price.text) for price in houses)
    average_price = total_price / total_houses
    return average_price