"""

Show reproducible example of https://github.com/mwaskom/seaborn/issues/3647

"""

import matplotlib.pyplot as plt
import seaborn as sns

#%% Load data.

df = sns.load_dataset('titanic')

print(df['class'].unique())

#%% Create plot.

sns.set_style("whitegrid")

g = sns.FacetGrid(df, col='embark_town')
g.map(sns.boxplot,
      x='sex',
      y='fare',
      hue='class',
      order=['First', 'Second', 'Third'],
      data=df,
      palette=sns.color_palette('pastel', 3),
      log_scale=True
      )

plt.tight_layout()

plt.show()
