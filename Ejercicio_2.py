
import json


class StockInvalidoError(Exception):
    """Error que se produce cuando el stock es negativo."""
    pass


class DispositivoEcológico:
    def __init__(self, nombre, modelo, costo_unitario, unidades_disponibles):
        self.nombre = nombre
        self.modelo = modelo
        self.costo_unitario = costo_unitario
        self.__stock = 0
        self.establecer_stock(unidades_disponibles)

    def obtener_stock(self):
        return self.__stock

    def establecer_stock(self, cantidad_unidades):
        if cantidad_unidades < 0:
            raise StockInvalidoError(
                f"El stock no puede ser negativo: {cantidad_unidades} unidades."
            )
        self.__stock = cantidad_unidades

    def mostrar_ficha_tecnica(self):
        return {
            "nombre": self.nombre,
            "modelo": self.modelo,
            "costo_unitario": self.costo_unitario,
            "stock": self.obtener_stock()
        }


class PanelSolar(DispositivoEcológico):
    def __init__(self, nombre, modelo, costo_unitario, unidades_disponibles,
                 potencia_nominal_w, eficiencia_porcentaje):
        super().__init__(nombre, modelo, costo_unitario, unidades_disponibles)
        self.potencia_nominal_w = potencia_nominal_w
        self.eficiencia_porcentaje = eficiencia_porcentaje

    def mostrar_ficha_tecnica(self):
        ficha = super().mostrar_ficha_tecnica()
        ficha.update({
            "tipo_dispositivo": "Panel Solar Fotovoltaico",
            "potencia_nominal_w": self.potencia_nominal_w,
            "eficiencia_porcentaje": self.eficiencia_porcentaje
        })
        return ficha


class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        catalogo = []

        for dispositivo in lista_dispositivos:
            catalogo.append(dispositivo.mostrar_ficha_tecnica())

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(catalogo, archivo, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    panel_1 = PanelSolar(
        "Panel Monocristalino", "ECO-SUN-500", 240.0, 30, 500, 22.5
    )
    panel_2 = PanelSolar(
        "Panel Policristalino", "ECO-POLY-350", 160.0, 45, 350, 18.0
    )

    print("=== CONTROL DE STOCK ===")

    try:
        panel_1.establecer_stock(-10)
    except StockInvalidoError as error:
        print(f"Error controlado: {error}")

    print(
        f"Stock conservado de {panel_1.modelo}: "
        f"{panel_1.obtener_stock()} unidades"
    )

    lista_inventario = [panel_1, panel_2]
    gestor = GestorInventario()

    gestor.guardar_catalogo_json(
        lista_inventario, "catalogo_ecotech.json"
    )

    print("=== CATALOGO EXPORTADO ===")

    for dispositivo in lista_inventario:
        print(dispositivo.mostrar_ficha_tecnica())

    print("Archivo generado: catalogo_ecotech.json")
