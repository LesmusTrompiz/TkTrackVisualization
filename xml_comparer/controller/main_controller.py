from views.main_view import MainView
from tkinter import Tk, filedialog
from model.xml_comparer import extract_file_content, different_subtrees, print_tree
from copy import deepcopy

    
class MainController:
    def __init__(self, main_view: MainView) -> None:
        self.view = main_view
        self.view.frame_f1.button_select.configure(command=self.open_file_1)
        self.view.frame_f2.button_select.configure(command=self.open_file_2)
        self.view.frame_f3.button_select.configure(command=self.compare_file_1_2)
        self.view.frame_f4.button_select.configure(command=self.compare_file_2_1)
        
        
        self.t1 = None
        self.t2 = None
        
        
    def open_file_1(self):
        filename = filedialog.askopenfilename(initialdir="./")
        if filename:
            self.t1 = extract_file_content(filename)
            tree_text = f'TAG {self.t1.tag} ATTRIBUTES {self.t1.attrib.keys()}'
            root_id = self.view.frame_f1.tree_view.insert('', 0, text=tree_text)
            self.insert_subtree(self.t1, root_id, self.view.frame_f1.tree_view)
        
    def open_file_2(self):
        filename = filedialog.askopenfilename(initialdir="./")
        if filename:
            self.t2 = extract_file_content(filename)
            tree_text = f'TAG {self.t2.tag} ATTRIBUTES {self.t2.attrib.keys()}'
            root_id = self.view.frame_f2.tree_view.insert('', 0, text=tree_text)
            self.insert_subtree(self.t2, root_id, self.view.frame_f2.tree_view)    
        
    def compare_file_1_2(self):
        if self.t1 == None or self.t2 == None: return
        auxt1 = deepcopy(self.t1)
        auxt2 = deepcopy(self.t2)
        
        if different_subtrees(auxt1 , auxt2):
            tree_text = f'TAG {auxt1.tag} ATTRIBUTES {auxt1.attrib.keys()}'
            root_id = self.view.frame_f3.tree_view.insert('', 0, text=tree_text)
            self.insert_subtree(auxt1, root_id, self.view.frame_f3.tree_view)    
  
    def compare_file_2_1(self):
        if self.t1 == None or self.t2 == None: return
        auxt1 = deepcopy(self.t2)
        auxt2 = deepcopy(self.t1)
        
        if different_subtrees(auxt1 , auxt2):
            tree_text = f'TAG {auxt1.tag} ATTRIBUTES {auxt1.attrib.keys()}'
            root_id = self.view.frame_f4.tree_view.insert('', 0, text=tree_text)
            self.insert_subtree(auxt1, root_id, self.view.frame_f4.tree_view)         
        
    def insert_subtree(self, tree, tree_id, tree_view):
        for subtree in tree:
            subtree_text = f'TAG {subtree.tag} ATTRIBUTES {subtree.attrib.keys()}'
            subtree_key = tree_view.insert(tree_id, 'end', text=subtree_text)
            self.insert_subtree(subtree, subtree_key, tree_view)
            