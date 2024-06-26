from lxml import etree

def load_xml(file_path):
    tree = etree.parse(file_path)
    root = tree.getroot()
    return tree, root

def save_xml(tree, file_path):
    tree.write(file_path, pretty_print=True, xml_declaration=True, encoding="UTF-8")
