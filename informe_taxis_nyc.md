
# 📊 Análisis de Datos de Taxis en NYC (2015-2016)

## 1️⃣ Introducción
Este informe presenta un análisis detallado de los **viajes en taxi en Nueva York** entre **enero de 2015 y enero de 2016**.  
El objetivo es **identificar tendencias de viaje, ingresos, patrones de pago y anomalías** que puedan indicar eventos especiales o problemas en los datos.

A través de una **limpieza y exploración de datos profunda**, se han detectado patrones que pueden ser útiles para la industria del transporte.

---

## 2️⃣ Transformación y Limpieza de Datos
Antes de iniciar el análisis, se realizó un proceso de **limpieza y transformación de datos** para asegurar su calidad.

### 🔍 Pasos clave:
✔ **Corrección de valores inconsistentes**  
   - Eliminación de valores atípicos en **trip_distance, fare_amount, total_amount, trip_duration y speed_mph**.  
✔ **Conversión de formatos de fecha**  
   - Creación de la columna **Year** extrayéndola de `tpep_pickup_datetime`.  
   - Creación de la columna **pickup_date** para análisis temporales.  
✔ **Validación de ingresos**  
   - Cálculo de `total_amount` sumando tarifas, impuestos y propinas cuando faltaban valores.  

Tras estos pasos, el dataset quedó **limpio y listo para su análisis**.

---

## 3️⃣ Análisis Descriptivo y Hallazgos Clave

### 📅 **Día con Más Viajes e Ingresos: 2 de enero de 2016**
Uno de los hallazgos más importantes es que el **2 de enero de 2016** tuvo un **pico anómalo en cantidad de viajes e ingresos**.

📌 **Posibles explicaciones**:
- **Alta demanda post-Año Nuevo** en NYC.
- **Error en la carga de datos** (posible duplicación de registros).
- **Tarifas dinámicas** elevadas debido a la demanda.

🔹 **Recomendación**: Verificar los datos de este día para descartar registros erróneos o duplicaciones.

---

### 🚖 **Comparación: Viajes en Días Laborales vs. Fines de Semana**
Se observó que **los viajes son más frecuentes en días laborables**, aunque la diferencia con los fines de semana no es extrema.

📌 **Interpretación**:
- Se usan más taxis para **desplazamientos al trabajo y actividades diarias**.
- Durante los fines de semana, la demanda sigue alta pero sin grandes diferencias.

🔹 **Oportunidad**: Implementar **tarifas promocionales los fines de semana** para aumentar la demanda.

---

### 💰 **Ingresos Totales y Crecimiento Anual**
- **2016 generó más ingresos que 2015**, lo que sugiere:
  - Un aumento en la tarifa base.
  - Más viajes registrados.
  - Posibles cambios en la regulación del transporte en NYC.

🔹 **Recomendación**: Analizar qué factores impulsaron este crecimiento para replicarlo en otros periodos.

---

### 💳 **Métodos de Pago: Tarjeta vs. Efectivo**
Se encontró que **el pago con tarjeta es el método más utilizado** y que genera **propinas más altas**.

📌 **Conclusiones**:
- Los pasajeros prefieren el pago digital frente al efectivo.
- Las propinas son significativamente mayores con tarjeta.

🔹 **Oportunidad**: Fomentar el uso de pagos digitales con incentivos o descuentos.

---

## 4️⃣ KPIs del Análisis

| **Métrica** | **Valor** |
|-------------|----------|
| **Total de Viajes** | 89,015 |
| **Ingresos Totales** | $1,060,096.70 |
| **Día con Más Viajes** | 2 de enero de 2016 (29,118 viajes) |
| **Día con Más Ingresos** | 2 de enero de 2016 ($849,238.93) |
| **Viajes en Fin de Semana** | 41,205 |
| **Viajes en Días de Semana** | 47,810 |
| **Ingresos en Fin de Semana** | $499,254.30 |
| **Ingresos en Días de Semana** | $560,842.40 |
| **Viajes en Horas Pico** | 51,325 |
| **Viajes fuera de Horas Pico** | 37,690 |
| **Ingresos en Horas Pico** | $619,712.50 |
| **Ingresos fuera de Horas Pico** | $440,384.20 |
| **Velocidad Promedio en Horas Pico** | 13.2 mph |
| **Velocidad Promedio fuera de Horas Pico** | 15.7 mph |

Estos indicadores proporcionan una visión clara de las tendencias en los viajes en taxi en NYC.

---

## 5️⃣ Conclusiones y Recomendaciones

✔ **El 2 de enero de 2016 mostró un pico anómalo en viajes e ingresos.**  
✔ **Los taxis son más usados en días laborables.**  
✔ **Los pagos con tarjeta son los más frecuentes y generan más propinas.**  
✔ **2016 tuvo mayores ingresos que 2015.**  

📌 **Recomendaciones:**
1️⃣ **Revisar la anomalía del 2 de enero de 2016** (posibles datos erróneos).  
2️⃣ **Aprovechar la diferencia entre semana y fines de semana** (promociones).  
3️⃣ **Optimizar pagos digitales** (incentivar el uso de tarjeta).  
4️⃣ **Revisar valores atípicos en duración y velocidad** (filtrar errores de captura).  

---

## 🚀 **Conclusión Final**
Este análisis proporciona **insights clave** para optimizar el servicio de taxis en NYC y maximizar los ingresos.

📢 **Próximos pasos**:
✅ Revisar la anomalía del **2 de enero de 2016**.  
✅ Implementar estrategias de precios dinámicos.  
✅ Incentivar el uso de pagos digitales.  

¡Gracias por leer! 🚖📊
