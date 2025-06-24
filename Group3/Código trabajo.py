import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Cargar el archivo Excel
df = pd.read_excel(r"C:\Users\USER\Desktop\Universidad\Tercer curso\Primer cuatrimestre\Visual analytics\Group3\globalterrorism_processed.xlsx")

# Seleccionar columnas numéricas para el PCA
numericas = df.select_dtypes(include=[np.number]).drop(columns=["nkill"]).dropna()

# Escalar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(numericas)

# Aplicar PCA (2 componentes)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Crear DataFrame con resultados y países
df_pca = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
df_pca["country"] = df["country_txt"].iloc[df_pca.index]
df_pca.to_csv(r"C:\Users\USER\Desktop\Universidad\Tercer curso\Primer cuatrimestre\Visual analytics\Group3\pca_result.csv", index=False)

