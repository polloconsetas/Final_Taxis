# 📊 Análisis de Datos de Taxis en NYC (2015-2016)

## 1️⃣ Introducción
Este informe presenta un análisis detallado de los datos de viajes en taxi en la ciudad de Nueva York entre los años **2015 y 2016**.  
El objetivo es identificar **tendencias de viaje, ingresos generados, patrones de pago y anomalías** que puedan indicar eventos especiales o errores en los datos.

📊 **Dashboard Operativo:** [Google Sheets](https://docs.google.com/spreadsheets/d/1sQaqVd8b7GAaEH-XAyEAvfi1DtNiHaggvaeNOxawse0/edit?gid=1653791227#gid=1653791227)

A través de la limpieza y exploración de estos datos, se han identificado patrones clave que pueden ser útiles para la industria del transporte y la optimización del servicio de taxis.

---

## 2️⃣ Transformación y Limpieza de Datos
Antes del análisis, se realizó un proceso de limpieza y transformación de datos para garantizar su calidad.  
Los pasos clave fueron:

- **Corrección de valores inconsistentes**:
  - Se detectaron y corrigieron valores erróneos en **"trip_distance", "fare_amount", "total_amount", "trip_duration" y "speed_mph"**.
  - Se eliminaron valores atípicos extremos para mejorar la precisión del análisis.
  
- **Conversión de formatos de fecha**:
  - Se creó la columna **"Year"** extrayéndola de `tpep_pickup_datetime`.
  - Se añadió **"pickup_date"** para facilitar análisis temporales.

- **Validación de ingresos**:
  - Se rellenaron valores nulos en **"total_amount"** sumando tarifas (`fare_amount`), impuestos y propinas.

Gracias a estos pasos, el dataset quedó **completo, limpio y listo para su análisis**.

---

## 3️⃣ Análisis Descriptivo y Hallazgos Clave

### 📅 **Día con Más Viajes e Ingresos: 2 de enero de 2016**
Uno de los hallazgos más relevantes es que el **2 de enero de 2016** presentó un **pico anómalo** en cantidad de viajes e ingresos totales.

🔍 **Posibles explicaciones**:
- **Alta demanda post-Año Nuevo** en NYC.
- **Error en la carga de datos** (duplicación de registros).  
- **Tarifas dinámicas** elevadas por demanda extrema.

📌 **Recomendación:** Validar los datos de este día para descartar registros erróneos o duplicaciones.

---

### 🚖 **Patrón de Viajes: Días Laborales vs. Fines de Semana**
Se observó que la cantidad de viajes es **mayor en días laborables**, aunque la diferencia no es extrema.

📌 **Interpretación**:
- Los taxis son usados principalmente para **desplazamientos laborales y actividades diarias**.
- Durante los fines de semana, la demanda se mantiene alta pero sin grandes diferencias.

🔹 **Oportunidad**: Implementar tarifas promocionales en fines de semana para aumentar la demanda.

---

### 💰 **Ingresos Anuales**
- **2016 generó más ingresos que 2015**, lo que sugiere:
  - Un aumento en la tarifa base.
  - Mayor cantidad de viajes registrados.
  - Cambios en la regulación del transporte en NYC.

🔹 **Oportunidad**: Analizar los factores que impulsaron este crecimiento para replicar estrategias en años futuros.

---

### 💳 **Método de Pago Más Utilizado**
Se identificó que **el pago con tarjeta es el método dominante**, lo que sugiere que:
1. **Los pasajeros prefieren pagar con tarjeta en lugar de efectivo**.  
2. **El pago con tarjeta está asociado con propinas más altas** en comparación con el pago en efectivo.  

🔹 **Oportunidad**: Fomentar el uso de pagos digitales con incentivos o descuentos.

---

# 📊 Análisis Estadístico de los Datos de Taxi

Este análisis incluye medidas de **tendencia central** y **dispersión** para entender el comportamiento de las variables clave.

## 📈 Interpretación de los Resultados

- **Tarifa promedio:** **$14.75**, con una mediana de **$10.00** (indica que la mayoría de los viajes cuestan alrededor de $10).  
- **Duración promedio de un viaje:** **15.16 minutos**, aunque algunos casos extremos superan las **10,000 minutos** (posibles errores).  
- **Distancia promedio:** **2.72 millas**, con valores atípicos que superan las **99 millas**.  
- **Velocidad promedio:** **14.64 mph**, con una gran variabilidad.  
- **Valor total promedio de un viaje:** **$22.02**, incluyendo propinas y recargos.  

📌 **Conclusión:** Los datos reflejan patrones consistentes con el tráfico urbano en NYC, aunque algunos valores extremos requieren revisión.

---

## 4️⃣ Conclusiones y Recomendaciones

📊 **Hallazgos Clave**:
✔ **El 2 de enero de 2016 mostró un pico anómalo en viajes e ingresos.** Requiere verificación.  
✔ **Los taxis son más usados en días laborables que en fines de semana.**  
✔ **2016 tuvo mayores ingresos que 2015.**  
✔ **El pago con tarjeta es el más utilizado y genera más propinas.**  

📌 **Recomendaciones**:
1️⃣ **Verificar la anomalía del 2 de enero de 2016**: Posibles datos erróneos o duplicados.  
2️⃣ **Aprovechar la diferencia entre semana y fines de semana**: Ofrecer promociones en días de menor demanda.  
3️⃣ **Optimizar pagos digitales**: Incentivar su uso con descuentos y opciones rápidas.  
4️⃣ **Revisar valores atípicos en duración y velocidad**: Filtrar posibles errores de captura de datos.  

---

## 🚀 **Conclusión Final**
Este informe proporciona **insights clave sobre el comportamiento de los pasajeros de taxi en NYC**, permitiendo decisiones estratégicas para optimizar ingresos y eficiencia del servicio.

📢 **Próximos pasos**:
✅ Revisar la anomalía del **2 de enero de 2016**.  
✅ Implementar estrategias de precios dinámicos.  
✅ Incentivar el uso de pagos digitales.  

Este análisis servirá como base para futuras optimizaciones del servicio de taxis en NYC.

---

### **Autor y Agradecimientos**

* **Autor:** Ana Nieto Carrera  
* **Datos Inspirados:** Proyecto obtenido de Kaggle.
