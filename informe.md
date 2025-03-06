# 📊 Análisis de Datos de Taxis en NYC (2015-2016)

## 1️⃣ Introducción
Este informe presenta un análisis detallado de los datos de viajes en taxi en la ciudad de Nueva York entre los años **2015 y 2016**.  
El objetivo es comprender **las tendencias de viaje, ingresos generados, patrones de pago y anomalías** que puedan indicar eventos especiales o errores en los datos.

Puede verse el Dashboard Operativo aquí: https://docs.google.com/spreadsheets/d/1sQaqVd8b7GAaEH-XAyEAvfi1DtNiHaggvaeNOxawse0/edit?gid=1653791227#gid=1653791227

A través de la limpieza y exploración de estos datos, se han identificado patrones interesantes que pueden ser útiles para la industria del transporte y la optimización del servicio de taxis en la ciudad.

---

## 2️⃣ Transformación y Limpieza de Datos
Antes de realizar el análisis, se llevó a cabo un proceso de limpieza y transformación de datos.  
Los pasos realizados fueron los siguientes:

- **Corrección de valores inconsistentes**:
  - Se detectaron valores erróneos en **"trip_distance", "fare_amount", "total_amount", "trip_duration" y "speed_mph"**.
  - Se convirtieron estos valores a formato numérico, eliminando errores de formato.
  
- **Conversión de formatos de fecha**:
  - Se creó la columna **"Year"** extrayéndola de la fecha de recogida (`pickup_date`).
  
- **Validación de ingresos**:
  - Se corrigieron los valores de la columna **"total_amount"**, rellenando valores nulos con la suma de tarifas (`fare_amount`), impuestos y propinas.

Estos pasos garantizaron que el dataset estuviera **completo, limpio y listo para su análisis**.

---

## 3️⃣ Análisis Descriptivo y Hallazgos Clave

### 📅 **Día con Más Viajes e Ingresos: 2 de enero de 2016**
Uno de los hallazgos más relevantes es que el **2 de enero de 2016** se registró un **pico anómalo** en la cantidad de viajes y en los ingresos totales.

🔍 **Posibles explicaciones para este pico**:
- **Evento especial o festividad**: Año Nuevo en Nueva York es un evento que genera una alta demanda de taxis.
- **Error en la carga de datos**: Posible duplicación de registros en esta fecha.
- **Tarifas dinámicas**: Un aumento repentino en la demanda pudo haber activado precios más altos.

📌 **Recomendación**: Validar los datos de este día para asegurarse de que no sean registros duplicados o errores en la carga.

---

### 🚖 **Patrón de Viajes: Días Laborales vs. Fines de Semana**
Se identificó que la cantidad de viajes es **ligeramente mayor en días laborables** comparado con los fines de semana.

📌 **Interpretación**:
- Los taxis en NYC son utilizados como transporte **para trabajo y actividades diarias**.
- Durante los fines de semana, aunque sigue habiendo alta demanda, **no se observan grandes diferencias** respecto a los días laborables.

🔹 **Oportunidad**: Implementar tarifas promocionales en fines de semana para aumentar la demanda.

---

### 💰 **Ingresos Anuales**
- **2016 generó más ingresos que 2015**. Esto puede deberse a:
  - Aumento de tarifas.
  - Mayor número de viajes registrados.
  - Cambios en la regulación del transporte en NYC.

🔹 **Oportunidad**: Analizar qué factores contribuyeron al aumento de ingresos para replicar estrategias en años futuros.

---

### 💳 **Método de Pago Más Utilizado**
Se identificó que **un método de pago es claramente dominante** sobre los demás, lo que sugiere que:
1. **Los pasajeros prefieren pagar con tarjeta en lugar de efectivo**.
2. **El pago con tarjeta está asociado con propinas más altas** en comparación con el pago en efectivo.

🔹 **Oportunidad**: Fomentar el uso de pagos digitales ofreciendo incentivos o descuentos.

---

## 4️⃣ Conclusiones y Recomendaciones

📊 **Resumen de los hallazgos clave**:
✔ **El 2 de enero de 2016 mostró un pico anómalo en viajes e ingresos.** Se recomienda verificar la calidad de estos datos.  
✔ **Los taxis son más usados en días laborables que los fines de semana.**  
✔ **Los ingresos fueron mayores en 2015 que en 2016.**  
✔ **El pago con tarjeta es el más utilizado y genera más propinas que el pago en efectivo.**  

---

📌 **Recomendaciones para optimizar el servicio**:
1️⃣ **Verificación de la anomalía del 2 de enero de 2016**:
   - Analizar si hay registros duplicados o si hay una explicación lógica para el aumento.
   
2️⃣ **Aprovechar el patrón de uso entre semana y fines de semana**:
   - Implementar promociones en días de baja demanda.
   - Ajustar tarifas en horarios pico para maximizar ingresos.

3️⃣ **Optimización del sistema de pagos**:
   - Fomentar el uso de tarjetas mediante descuentos o promociones.
   - Implementar pagos digitales más rápidos para mejorar la experiencia del usuario.

4️⃣ **Análisis futuro**:
   - Comparar con datos de años posteriores para ver si las tendencias se mantienen.
   - Incorporar datos meteorológicos para analizar cómo afecta el clima al uso de taxis.

---

## 🚀 **Conclusión Final**
Este análisis proporciona **información clave sobre el comportamiento de los pasajeros de taxi en NYC**, ayudando a tomar decisiones estratégicas para optimizar los ingresos y mejorar la eficiencia del servicio.

El estudio revela oportunidades claras para la industria del transporte, desde el análisis de patrones de uso hasta la optimización de métodos de pago y precios dinámicos.

📢 **Próximos pasos**:
✅ Revisar la anomalía del **2 de enero de 2016**.  
✅ Implementar estrategias de precios dinámicos.  
✅ Incentivar el uso de pagos digitales.  

Este informe servirá como base para futuras investigaciones en la optimización del servicio de taxis y análisis de demanda en grandes ciudades.

---

### **Autor y Agradecimientos**

* **Autor:** Ana Nieto Carrera  
* **Datos Inspirados:** Proyecto obtenido de la plataforma de Kaggle.
