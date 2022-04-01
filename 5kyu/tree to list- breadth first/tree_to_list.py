class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = [] if child_nodes is None else child_nodes

def tree_to_list(tree_root):
    list_ans=[]
    fring=[]
    fring.append(tree_root)
    while(len(fring)):
        list_ans.append(fring[0].data)
        expand(fring)
    return list_ans  
        
def expand(fring):
    deleting_node=fring[0]
    del fring[0]
    for child in deleting_node.child_nodes:
        fring.append(child)
    
        
    
