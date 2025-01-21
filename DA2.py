"""Example: One_way ANOVAimport"""
import numpy as np
from scipy.stats import f_oneway
#data for the groups
group_a=np.array([20,30,40,50,10])
group_b=np.array([20,30,45,55,15])
group_c=np.array([25,15,30,45,50])

#perform oneway anova
f_stat,p_value=f_oneway(group_a,group_b,group_c)

#print results
print(f"F-Statistics:{f_stat:.4f}")
print(f"P-Value:{p_value:.4f}")

#significance level
alpha=0.05

if p_value<alpha:
    print("Result:At least one group mean is significantly different.")
else:
    print("Result:No significant difference between group means")