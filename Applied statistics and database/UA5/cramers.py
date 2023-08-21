import numpy as np
from scipy.stats import chi2_contingency

# Definindo os dados em forma de tabela de contingência
observed = np.array([[10, 15, 5],
                     [20, 25, 10],
                     [15, 10, 5]])

# Calculando o qui-quadrado e suas estatísticas associadas
chi2, p, dof, expected = chi2_contingency(observed)

# Calculando o coeficiente de Cramér's V
def cramers_v(confusion_matrix):
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
    r_corr = r - ((r - 1)**2) / (n - 1)
    k_corr = k - ((k - 1)**2) / (n - 1)
    return np.sqrt(phi2corr / min((k_corr - 1), (r_corr - 1)))

cramers_v_score = cramers_v(observed)

print("Coeficiente de Cramér's V:", cramers_v_score)