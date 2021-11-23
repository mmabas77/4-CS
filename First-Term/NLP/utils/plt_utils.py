# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn_genetic.plots import plot_fitness_evolution


def plot_genetic_classifier_performance(estimator):

    plot_fitness_evolution(estimator)
    plt.show()
