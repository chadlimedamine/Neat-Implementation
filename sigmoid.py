#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 14:19:28 2020

@author: Mohamed Amine Chadli
"""

import numpy as np

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))