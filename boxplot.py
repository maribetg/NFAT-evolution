import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Data
data = pd.read_csv("data.csv")

#boxplot
sns.set(font_scale=1.4)
sns.set_style("white")

colors = ['purple', 'darkgreen', 'lightgreen', 'blue', 'red']
sns.set_palette(colors)

ax = sns.catplot(data = data, kind = 'box', sym = '', x = 'phyla', y = 'duplication')
ax.set(ylabel = 'Duplication ratio', xlabel = '')
plt.show()

#save
ax.figure.savefig("duplication.png")