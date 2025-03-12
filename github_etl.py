# src/etl/github_etl.py

import requests
import pandas as pd

# === CONFIGURA TU PROPIO REPO SI QUERÉS ===
owner = "bbeta"
repo = "metrics-observability-app"

# URL base de la API
url = f"https://api.github.com/repos/{owner}/{repo}/commits"

# Petición a la API pública (sin autenticación por ahora)
response = requests.get(url)

# Transformar a JSON
data = response.json()

# Extraer los campos que nos interesan
commits = []
for item in data:
    commit = {
        "sha": item.get("sha"),
        "author": item["commit"]["author"]["name"],
        "message": item["commit"]["message"],
        "date": item["commit"]["author"]["date"]
    }
    commits.append(commit)

# Crear un DataFrame
df = pd.DataFrame(commits)

# Guardar en CSV
df.to_csv("data/github_commits.csv", index=False)

print("✅ Commits extraídos y guardados exitosamente en data/github_commits.csv")
