import pandas as pd
import numpy as np

def process_taxi_data(file_2015, file_2016, output_file):
    """
    Función para procesar datos de taxis de dos años distintos y combinarlos en un solo dataset.
    
    Parámetros:
    - file_2015: Ruta del archivo CSV con datos de 2015.
    - file_2016: Ruta del archivo CSV con datos de 2016.
    - output_file: Nombre del archivo CSV donde se guardarán los datos procesados.
    """

    try:
        # Cargar datos
        df_2015 = pd.read_csv(file_2015)
        df_2016 = pd.read_csv(file_2016)

        # Verificar columnas necesarias
        required_columns = ["tpep_pickup_datetime", "tpep_dropoff_datetime", "trip_distance", "fare_amount"]
        for df, year in zip([df_2015, df_2016], [2015, 2016]):
            missing_cols = [col for col in required_columns if col not in df.columns]
            if missing_cols:
                print(f"⚠️ Advertencia: Faltan columnas en el dataset de {year}: {missing_cols}. Continuando con los datos disponibles.")

        # Unificar nombres de columnas
        df_2015.rename(columns={"RateCodeID": "RatecodeID"}, inplace=True)

        # Convertir fechas a datetime
        for df in [df_2015, df_2016]:
            df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"], errors='coerce')
            df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"], errors='coerce')

        # Concatenar los datasets
        df_final = pd.concat([df_2015, df_2016], ignore_index=True)

        # Crear nuevas columnas
        df_final["trip_duration"] = (df_final["tpep_dropoff_datetime"] - df_final["tpep_pickup_datetime"]).dt.total_seconds() / 60
        df_final["speed_mph"] = (df_final["trip_distance"] / df_final["trip_duration"]) * 60

        # Manejo de valores extremos en velocidad
        df_final["speed_mph"] = df_final["speed_mph"].replace([np.inf, -np.inf], np.nan)
        df_final["speed_mph"] = df_final["speed_mph"].fillna(df_final["speed_mph"].median())

        # Variables adicionales
        df_final["is_weekend"] = df_final["tpep_pickup_datetime"].dt.weekday.isin([5, 6]).astype(int)
        df_final["rush_hour"] = df_final["tpep_pickup_datetime"].dt.hour.isin([7, 8, 9, 16, 17, 18]).astype(int)
        df_final["fare_per_mile"] = df_final["fare_amount"] / df_final["trip_distance"]
        
        # Manejo de valores nulos en `fare_per_mile`
        df_final["fare_per_mile"] = df_final["fare_per_mile"].replace([np.inf, -np.inf], np.nan)
        df_final["fare_per_mile"] = df_final["fare_per_mile"].fillna(df_final["fare_per_mile"].median())

        # Extraer año y fecha del viaje
        df_final["Year"] = df_final["tpep_pickup_datetime"].dt.year
        df_final["pickup_date"] = df_final["tpep_pickup_datetime"].dt.date

        # Redondear valores numéricos
        numeric_cols = df_final.select_dtypes(include=['float', 'int']).columns
        df_final[numeric_cols] = df_final[numeric_cols].round(2)

        # Guardar el dataset limpio
        df_final.to_csv(output_file, index=False)
        print(f"✅ Archivo guardado en: {output_file}")

    except Exception as e:
        print(f"❌ Error al procesar los datos: {e}")

# Ejecución directa desde línea de comandos (opcional)
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Uso: python clean_taxi_data.py <archivo_2015.csv> <archivo_2016.csv> <archivo_salida.csv>")
    else:
        process_taxi_data(sys.argv[1], sys.argv[2], sys.argv[3])
