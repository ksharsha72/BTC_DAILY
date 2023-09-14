import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk
from decision_tree import Decision_Tree

data = pd.read_csv('../../../Donwloads/Covid_Dataset.csv')
label = 'COVID-19'

dt = Decision_Tree(data,label)
