class NaiveBayes:
    def __init__(self):
        self.class_probs = {}  # Probabilidades das classes
        self.feature_probs = {}  # Probabilidades condicionais dos atributos

    def fit(self, X, y):
        # Calcula as probabilidades das classes
        total_samples = len(y)
        for class_label in set(y):
            class_samples = X[y == class_label]
            self.class_probs[class_label] = len(class_samples) / total_samples

            # Calcula as probabilidades condicionais dos atributos para cada classe
            for feature in range(X.shape[1]):
                feature_values = class_samples[:, feature]
                unique_values, counts = np.unique(feature_values, return_counts=True)
                probs = counts / len(class_samples)
                self.feature_probs[(feature, class_label)] = dict(zip(unique_values, probs))

    def predict(self, X):
        predictions = []
        for sample in X:
            max_prob = -1
            predicted_class = None

            # Calcula a probabilidade para cada classe
            for class_label, class_prob in self.class_probs.items():
                prob = class_prob

                # Calcula a probabilidade condicional para cada atributo
                for feature, value in enumerate(sample):
                    if (feature, class_label) in self.feature_probs:
                        if value in self.feature_probs[(feature, class_label)]:
                            prob *= self.feature_probs[(feature, class_label)][value]

                # Atualiza a classe predita se encontrarmos uma probabilidade maior
                if prob > max_prob or predicted_class is None:
                    max_prob = prob
                    predicted_class = class_label

            predictions.append(predicted_class)

        return predictions
