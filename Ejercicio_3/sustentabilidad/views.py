
from django.shortcuts import render

from emisiones import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    """
    Procesa los registros de consumo y envia las
    metricas al panel web de sustentabilidad.
    """

    registros_consumo = [
        {"planta": "Planta Norte", "consumo_kwh": 1200},
        {"planta": "Planta Sur", "consumo_kwh": 1800},
        {"planta": "Planta Norte", "consumo_kwh": 900},
        {"planta": "Planta Central", "consumo_kwh": 1500}
    ]

    metricas = obtener_metricas_consumo(registros_consumo)

    contexto = {
        "consumo_total_kwh": metricas["consumo_total_kwh"],
        "emisiones_totales_co2": metricas["emisiones_totales_co2"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "registros_consumo": registros_consumo
    }

    return render(request, "sustentabilidad/panel.html", contexto)
