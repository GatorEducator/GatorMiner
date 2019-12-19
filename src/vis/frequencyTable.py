import numpy as np
import matplotlib.pyplot as plt

## Pyplot tutorial used as a base.
# Available from https://pythonspot.com/matplotlib-scatterplot/
# Matplotlib: https://pypi.org/project/matplotlib/
# pip install matplotlib
# pandas: https://pandas.pydata.org/pandas-docs/stable/install.html
# sudo pip3 install pandas

# Will import frequency or ethic scores from external source
N = 60
g1 = (0.6 + 0.6 * np.random.rand(N), np.random.rand(N))
g2 = (0.4 + 0.3 * np.random.rand(N), 0.5 * np.random.rand(N))
g3 = (0.3 * np.random.rand(N), 0.3 * np.random.rand(N))

# Setting data and color to data
data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("Not Ethical", "Somewhat Ethical", "Very Ethical")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, facecolor="1.0")


for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors="none", s=30, label=group)

# labeling and showing plot
plt.title("Ethical Question Scores")
plt.xlabel("Question Responces")
plt.ylabel("Frequency of Ethics")
plt.legend(loc=2)  # positions in top left
plt.show()
