import pandas as pd
import numpy as np
import os

# 📌 1. Función para cargar datos con manejo de errores
def cargar_datos(ruta_2015, ruta_2016):
    """
    Carga los datasets de 2015 y 2016 desde archivos CSV.
    """
    try:
        df_2015 = pd.read_csv(ruta_2015)
        df_2016 = pd.read_csv(ruta_2016)
        print("✅ Datos cargados correctamente.")
        return df_2015, df_2016
    except FileNotFoundError:
        print("❌ Error: Uno o ambos archivos no fueron encontrados.")
        return None, None

# 📌 2. Función para limpiar datos
def limpiar_datos(df):
    """
    Realiza la limpieza del dataset:
    - Convierte fechas a formato datetime.
    - Elimina valores nulos y outliers en 'trip_distance' y 'fare_amount'.
    """
    if df is None:
        print("❌ Error: El dataset no fue cargado correctamente.")
        return None

    # Convertir fechas a datetime
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"], errors='coerce')
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"], errors='coerce')

    # Eliminar valores nulos en columnas clave
    df.dropna(subset=["tpep_pickup_datetime", "tpep_dropoff_datetime", "trip_distance", "fare_amount"], inplace=True)

    # Eliminar valores atípicos en 'trip_distance' y 'fare_amount'
    df = df[(df["trip_distance"] > 0) & (df["fare_amount"] > 0)]

    print("✅ Datos limpiados correctamente.")
    return df

# 📌 3. Función para manejar outliers usando el método IQR
def manejar_outliers(df, columnas):
    """
    Elimina outliers usando el método IQR.
    """
    if df is None:
        print("❌ Error: El dataset no fue cargado correctamente.")
        return None

    for col in columnas:
        if col in df.columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

    print("✅ Outliers gestionados correctamente.")
    return df

# 📌 4. Función para transformar datos (sin inplace=True)
def transformar_datos(df):
    """
    Realiza transformaciones:
    - Calcula 'trip_duration'.
    - Calcula 'speed_mph'.
    - Crea variables adicionales como 'is_weekend' y 'rush_hour'.
    """
    if df is None:
        print("❌ Error: El dataset no fue cargado correctamente.")
        return None

    # Calcular duración del viaje
    df["trip_duration"] = (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]).dt.total_seconds() / 60

    # Calcular velocidad promedio
    df["speed_mph"] = (df["trip_distance"] / df["trip_duration"]) * 60

    # Manejo de valores extremos en velocidad (sin inplace=True)
    df["speed_mph"] = df["speed_mph"].replace([np.inf, -np.inf], np.nan)
    df["speed_mph"] = df["speed_mph"].fillna(df["speed_mph"].median())

    # Crear variables adicionales
    df["is_weekend"] = df["tpep_pickup_datetime"].dt.weekday.isin([5, 6]).astype(int)
    df["rush_hour"] = df["tpep_pickup_datetime"].dt.hour.isin([7, 8, 9, 16, 17, 18]).astype(int)
    df["fare_per_mile"] = df["fare_amount"] / df["trip_distance"]

    # Manejo de valores nulos en 'fare_per_mile' (sin inplace=True)
    df["fare_per_mile"] = df["fare_per_mile"].replace([np.inf, -np.inf], np.nan)
    df["fare_per_mile"] = df["fare_per_mile"].fillna(df["fare_per_mile"].median())

    # Extraer año y fecha del viaje
    df["Year"] = df["tpep_pickup_datetime"].dt.year
    df["pickup_date"] = df["tpep_pickup_datetime"].dt.date

    # Redondear valores numéricos
    numeric_cols = df.select_dtypes(include=['float', 'int']).columns
    df[numeric_cols] = df[numeric_cols].round(2)

    print("✅ Transformaciones aplicadas correctamente.")
    return df

# 📌 5. Función para procesar datos y guardar CSV sin warnings
def procesar_datos(ruta_2015, ruta_2016):
    """
    Ejecuta todo el pipeline de limpieza, transformación y guardado de datos.
    Guarda el CSV con el nombre fijo 'cleaned_taxi_data.csv' en la misma carpeta.
    """
    df_2015, df_2016 = cargar_datos(ruta_2015, ruta_2016)

    if df_2015 is not None and df_2016 is not None:
        df = pd.concat([df_2015, df_2016], ignore_index=True)
        df = limpiar_datos(df)
        df = manejar_outliers(df, ["trip_distance", "fare_amount"])
        df = transformar_datos(df)

        # Definir el nombre del archivo de salida en la misma carpeta
        output_file = "cleaned_taxi_data.csv"

        # Guardar el dataset limpio sin warnings
        df.to_csv(output_file, index=False)
        print(f"✅ Dataset final guardado como: {output_file}")
        return df, output_file

    return None, None

# 📌 6. Ejecutar el script desde línea de comandos y guardar CSV
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python clean_taxi_data_no_warnings.py <archivo_2015.csv> <archivo_2016.csv>")
    else:
        df, output_file = procesar_datos(sys.argv[1], sys.argv[2])

        if df is not None:
            print(f"✅ Archivo generado en la carpeta actual: {output_file}")
        else:
            print("❌ No se pudo generar el archivo.")
