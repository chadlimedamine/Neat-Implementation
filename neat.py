#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 12:50:08 2020

@author: Mohamed Amine Chadli
"""

#import the forward pass function to calculate the output values of the network
from feed_forwad import forward_pass

input_nodes = {1,2,3}
output_nodes = {4}
hidden_nodes = {5, 6}

input_values = {'1': 0.8, '2': 0.3, '3': 0.6}

#calculate the number of nodes in this network
node_number = len(input_nodes) + len(output_nodes) + len(hidden_nodes)

con = {'5':{'1':0.2,'2':1.4},'4':{'1':-1.5,'6':-0.7,'5':1.8},'6':{"3":-0.3,'5':0.9}}
"""
    this con variable contains the weight values for each connexion
    the Key of this dictionary is the destinated node and the value for 
    this dictionary is the source node and its weight value as this example:
    con = {'destination node': {'source node': weight value}}
"""

print(forward_pass(node=4, input_values_dict=input_values, connexion_weights_dict=con))