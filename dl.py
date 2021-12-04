import requests


def predict(trestbps, chol, fbs, ca, restecg, thalach, cp, exang, oldpeak, slope):
    url = 'http://127.0.0.1:8085/predict'
    params = {
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "ca": ca,
        "restecg": restecg,
        "thalach": thalach,
        "cp": cp,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope
    }
    result = requests.get(url, params=params)
    return float(bytes.decode(result.content))
