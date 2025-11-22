from sklearn.linear_model import LogisticRegression

def build_model():
    """Construiește și returnează un model simplu de regresie logistică."""
    model = LogisticRegression(max_iter=1000)
    return model