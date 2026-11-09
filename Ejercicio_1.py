
def limpiar_registro_sensor(registro_raw):
    """Normaliza el identificador, la temperatura y la ubicacion del sensor."""

    identificador_sensor = str(registro_raw.get("sensor_id", "")).strip()

    temperatura_recibida = str(registro_raw.get("temperatura", "")).strip()
    temperatura_sin_unidad = temperatura_recibida.replace("°C", "").replace("C", "").strip()
    temperatura_celsius = float(temperatura_sin_unidad)

    ubicacion_planta = str(registro_raw.get("ubicacion") or "").strip()

    if not ubicacion_planta:
        ubicacion_planta = "Ubicacion no especificada"

    return {
        "sensor_id": identificador_sensor,
        "temperatura": temperatura_celsius,
        "ubicacion": ubicacion_planta
    }


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    """Devuelve los sensores en alerta y el promedio de temperatura."""

    sensores_en_alerta = []
    acumulado_termico = 0.0

    for sensor in lista_sensores_limpios:
        temperatura_celsius = sensor["temperatura"]
        acumulado_termico += temperatura_celsius

        if temperatura_celsius > umbral_temperatura:
            sensores_en_alerta.append(sensor["sensor_id"])

    if not lista_sensores_limpios:
        return sensores_en_alerta, 0.0

    promedio_termico = acumulado_termico / len(lista_sensores_limpios)

    return sensores_en_alerta, promedio_termico




if __name__ == "__main__":

    registros_recibidos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5 °C", "ubicacion": " Planta Norte "},
        {"sensor_id": "SENSOR-002", "temperatura": "31.8 °C", "ubicacion": "Planta Sur"},
        {"sensor_id": "SENSOR-003", "temperatura": "27.2 °C", "ubicacion": "Planta Central"},
        {"sensor_id": "SENSOR-004", "temperatura": "35.6 °C", "ubicacion": ""}
    ]

    sensores_normalizados = []

    for lectura_recibida in registros_recibidos:
        sensores_normalizados.append(limpiar_registro_sensor(lectura_recibida))

    limite_temperatura_operativa = 30.0

    sensores_en_alerta, promedio_termico = generar_resumen_sensores(
        sensores_normalizados, limite_temperatura_operativa
    )

    print("=== REPORTE DE SENSORES INDUSTRIALES ===")

    for sensor in sensores_normalizados:
        print(f"{sensor['sensor_id']} | {sensor['ubicacion']} | {sensor['temperatura']} °C")

    print(f"Limite operativo: {limite_temperatura_operativa} °C")
    print(f"Promedio termico: {promedio_termico:.2f} °C")
    print(f"Sensores en alerta: {sensores_en_alerta}")
