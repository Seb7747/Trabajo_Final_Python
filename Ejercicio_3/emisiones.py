
# EJERCICIO 3
# CALCULO DE EMISIONES DE CARBONO


def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    """
    Calcula las emisiones de CO2 a partir del consumo electrico.
    El factor de emision se expresa en kg de CO2 por kWh.
    """

    if consumo_kwh < 0:
        raise ValueError("El consumo electrico no puede ser negativo.")

    emisiones_co2_kg = consumo_kwh * factor_emision

    return emisiones_co2_kg


def obtener_metricas_consumo(registros):
    """
    Calcula las emisiones totales e identifica la planta
    con mayor consumo electrico acumulado.
    """

    consumo_por_planta = {}
    consumo_total_kwh = 0
    emisiones_totales_co2 = 0

    for registro in registros:
        nombre_planta = registro["planta"]
        consumo_kwh = registro["consumo_kwh"]

        emisiones_registro = calcular_emisiones_carbono(consumo_kwh)

        consumo_total_kwh += consumo_kwh
        emisiones_totales_co2 += emisiones_registro

        if nombre_planta in consumo_por_planta:
            consumo_por_planta[nombre_planta] += consumo_kwh
        else:
            consumo_por_planta[nombre_planta] = consumo_kwh

    planta_mayor_consumo = None

    if consumo_por_planta:
        planta_mayor_consumo = max(
            consumo_por_planta,
            key=consumo_por_planta.get
        )

    return {
        "consumo_total_kwh": consumo_total_kwh,
        "emisiones_totales_co2": emisiones_totales_co2,
        "planta_mayor_consumo": planta_mayor_consumo
    }


if __name__ == "__main__":

    registros_consumo = [
        {"planta": "Planta Norte", "consumo_kwh": 1200},
        {"planta": "Planta Sur", "consumo_kwh": 1800},
        {"planta": "Planta Norte", "consumo_kwh": 900},
        {"planta": "Planta Central", "consumo_kwh": 1500}
    ]

    metricas = obtener_metricas_consumo(registros_consumo)

    print("=== REPORTE DE EMISIONES DE CARBONO ===")
    print(f"Consumo electrico total: {metricas['consumo_total_kwh']} kWh")
    print(f"Emisiones totales de CO2: {metricas['emisiones_totales_co2']:.2f} kg")
    print(f"Planta con mayor consumo: {metricas['planta_mayor_consumo']}")
