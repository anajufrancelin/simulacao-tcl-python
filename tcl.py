import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Reprodutibilidade
np.random.seed(42)

# Tamanhos das amostras
sample_sizes = [2, 5, 10, 20, 50, 100, 300]

# Número de amostras
num_samples = 10000

# Populações diferentes
populations = {
    "Uniforme": np.random.uniform(0, 10, 100000),

    "Exponencial": np.random.exponential(
        scale=2,
        size=100000
    ),

    "Qui-Quadrado": np.random.chisquare(
        df=3,
        size=100000
    ),

    "Binomial": np.random.binomial(
        n=10,
        p=0.3,
        size=100000
    ),

    "Normal": np.random.normal(
        loc=0,
        scale=1,
        size=100000
    )
}

for pop_name, population in populations.items():

    fig, axes = plt.subplots(
        2, 4,
        figsize=(18, 8)
    )

    axes = axes.flatten()

    for i, n in enumerate(sample_sizes):

        sample_means = []

        for _ in range(num_samples):

            sample = np.random.choice(
                population,
                size=n,
                replace=True
            )

            sample_means.append(
                np.mean(sample)
            )

        sns.histplot(
            sample_means,
            bins=30,
            kde=True,
            ax=axes[i]
        )

        axes[i].set_title(f"n = {n}")

    fig.suptitle(
        f"TCL - População {pop_name}",
        fontsize=16
    )

    plt.tight_layout()
    plt.show()