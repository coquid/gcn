import numpy as np
import pickle as pkl
import networkx as nx
import scipy.sparse as sp
from scipy.sparse.linalg.eigen.arpack import eigsh
import sys

"""
    Loads input data from gcn/data directory

    ind.dataset_str.x => the feature vectors of the training instances as scipy.sparse.csr.csr_matrix object;
    ind.dataset_str.tx => the feature vectors of the test instances as scipy.sparse.csr.csr_matrix object;
    ind.dataset_str.allx => the feature vectors of both labeled and unlabeled training instances
        (a superset of ind.dataset_str.x) as scipy.sparse.csr.csr_matrix object;
    ind.dataset_str.y => the one-hot labels of the labeled training instances as numpy.ndarray object;
    ind.dataset_str.ty => the one-hot labels of the test instances as numpy.ndarray object;
    ind.dataset_str.ally => the labels for instances in ind.dataset_str.allx as numpy.ndarray object;
    ind.dataset_str.graph => a dict in the format {index: [index_of_neighbor_nodes]} as collections.defaultdict
        object;
    ind.dataset_str.test.index => the indices of test instances in graph, for the inductive setting as list object.

    All objects above must be saved using python pickle module.

    :param dataset_str: Dataset name
    :return: All data input files loaded (as well the training/test data).
    """


def load_data(dataset_str):
    """
    N = number of nodes (vertices)
    D = number of features per node (force,prev_vel,prev_force,prev_position,etc...)
    Adj Mat = N X N
    x = N X D
    y = N X 3
    """
    adj_list_file = dataset_str+".adj_list"
    input_file = dataset_str+".input"
    output_file = dataset_str+".output"
    info_file = dataset_str+".luis_info"

    # adj dic 생성 완료~~~!!!!
    adj_dic = {}
    with open(adj_list_file) as f:
        for line in f:
            if(line.isspace()==False):
                key , temp_val = line.strip().split(":")
                val = temp_val.strip().split(" ")
                adj_dic[int(key)] = list(map(int,val))
    
    # ind.dataset_str.x => the feature vectors of the training instances as scipy.sparse.csr.csr_matrix object;
    # N X D

    # system matrix ( for adj mat & )

    # data_x = sp.csr.csr_matrix()
    # data_tx = sp.csr.csr_matrix()
    # data_allx = sp.csr.csr_matrix()
    
    # data_y = sp.csr.csr_matrix()
    # data_ty = sp.csr.csr_matrix()
    # data_ally = sp.csr.csr_matrix()
    
    # data_graph = collections.defaultdict()
    

    pass
def save_data(dataset_str):


    pass
def process_whole_data(dataset_str):
    load_data(dataset_str)
    save_data(dataset_str)

if __name__ == "__main__":
    # load_data("./my_data/"+sys.argv[1])
    load_data("my_data/"+"hanging")
else:
    pass