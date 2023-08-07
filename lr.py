#########################################################################################
#
# Jason McDonald - Case Study 1
#
# Build linear regression models with L1 and L2 regularization to predict the critical
# temperature as closely as possible.  Include which variable carries the most importance.
#
#########################################################################################

import numpy as np
import pandas as pd

df_train = pd.read_csv('train.csv')
df_unique_m = pd.read_csv('unique_m.csv')

