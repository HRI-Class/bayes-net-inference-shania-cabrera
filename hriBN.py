import numpy as np
import pandas as pd

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Define Bayesian Network structure
model = BayesianNetwork([('F', 'Q'), ('F', 'D'), ('Q', 'W'), ('D', 'W')])

# Define CPDs
cpd_f = TabularCPD(variable='F', variable_card=2, values=[[0.3], [0.7]], state_names={"F":["low", "high"]})
cpd_q = TabularCPD(variable='Q', variable_card=2, values=[[0.5, 0.2], [0.5, 0.8]],
                    evidence=['F'], evidence_card=[2], state_names={"F":["low", "high"], "Q": ["bad", "good"]})
cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.6, 0.3], [0.4, 0.7]],
                    evidence=['F'], evidence_card=[2], state_names={"F":["low", "high"], "D": ["weak", "strong"]})
cpd_w = TabularCPD(variable='W', variable_card=2, 
                    values=[[0.30, 0.5, 0.15, 0.25], [0.70, 0.5, 0.85, 0.75]],
                    evidence=['Q', 'D'], evidence_card=[2, 2], state_names={"Q":["bad", "good"], "D": ["weak", "strong"], "W": ["lose", "win"]})

# Add CPDs to model
model.add_cpds(cpd_f, cpd_q, cpd_d, cpd_w)

# Check Model
assert model.check_model()

_ = [print (cpd) for cpd in model.get_cpds()]

P_w = None

# Calcuate the probabiity of winning and losing 
# and put it in a the P_w variable

# YOUR CODE HERE
raise NotImplementedError()

P_w