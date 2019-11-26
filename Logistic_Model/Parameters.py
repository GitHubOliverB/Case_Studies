#!/usr/bin/python

"""
Summary:

Here we declare the parameters for the classifier we want to use.
Also we have a random_seed which is fixed to reproduce our results.
"""

import os
import sys

# Fixed for reproductivity
random_seeds = [175]

# Version Name
classifier_name = ["Model"]

# Splitting Parameters
reserve_fraction=0.05
test_fraction = 0.5

# Hyperparameters For Training
max_depth = 5 # We have dummy variables, so our trees will be huge....
min_samples_leaf = 0.05
subsample = 1.0
n_estimators = 250
learning_rate = 0.1

# Learning Curve Validation
n_jobs=4
cv=3