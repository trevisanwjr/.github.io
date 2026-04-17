import os
from datetime import datetime

data = datetime.now().strftime("%Y-%m-%d")

filename = f"jobs/new_jobs_cards_gerente_de_projetos_{data}.html"

html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Vagas</title>
</head>
<body>
<h1>Vagas Geradas Automaticamente - {data}</h1>
</body>
</html>
"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(html)

print("Arquivo gerado:", filename)
