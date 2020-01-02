"""
@author: Mohamed Amine Chadli
"""

#implementation of a recursif function to calculate the output of the neural network

#importing the sigmoid function
from sigmoid import sigmoid

def forward_pass(node, input_values_dict, connexion_weights_dict):
    """
    this function calculate the forward pass value for any given hidden or output node

    :param node: the node that we want to calculate its value
    :param input_values_dict: a dictionary containing all the input values
    :param connexion_weights_dict: a dictionary containing all connexions between nodes and their respective weight values
    :return: the output value of the forward pass for the specified node
    """
    summation = 0
    for i, w in connexion_weights_dict[str(node)].items():
        if i in input_values_dict:
            summation += w * input_values_dict[str(i)]
        else:
            summation += w * forward_pass(i, input_values_dict, connexion_weights_dict)
    return sigmoid(summation)