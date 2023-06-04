import xml.etree.ElementTree as ET

def print_tree(subtree: ET.ElementTree, depth=0):
    print(depth * "\t" + f"| TAG {subtree.tag} Attrib {subtree.attrib} Text {subtree.text}")
    for son in subtree:
        print_tree(son, depth+1)


def seach_same_son_in_subtree(son: ET.ElementTree, subtree: ET.ElementTree):
    candidates = []
    for possible_candidate in subtree:
        if son.tag == possible_candidate.tag and son.attrib == possible_candidate.attrib:
            candidates += [possible_candidate]
    
    if not candidates:
        return None            

    if len(candidates) > 1:
        print("Mas candidatos de los debidos")
    return candidates[0]
    
    
    
def strip_sons(subtree):
    sons = [son for son in subtree]
    for s in sons:
        subtree.remove(s)
        
    
    
def different_subtrees(subtree1: ET.ElementTree, subtree2: ET.ElementTree):
    different = False
    equal_subtrees = []
    for son1 in subtree1:
        son2 = seach_same_son_in_subtree(son1, subtree2)
        if son2 != None:
            if different_subtrees(son1, son2):
                different = True
            else:
                subtree2.remove(son2)
                equal_subtrees += [son1]
        else:
            different = True
            try:
                strip_sons(son1)
            except:
                print(f"EXCEPT {son1.tag}")
    for e in equal_subtrees:
        subtree1.remove(e)
    return different


def extract_file_content(filepath):
    tree1 = ET.parse(filepath)
    root1 = tree1.getroot()
    return root1


'''
tree1 = ET.parse('./xml_comparer/xmls/country_1.xml')
root1 = tree1.getroot()
tree2 = ET.parse('./xml_comparer/xmls/country_2.xml')
root2 = tree2.getroot()
root1.remove
different_subtrees(root1, root2)
ET.dump(root1)
'''









