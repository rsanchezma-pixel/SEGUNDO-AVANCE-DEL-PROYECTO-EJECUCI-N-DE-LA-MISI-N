# ============================================================
# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección: [indicar]
# Integrantes: [nombre del estudiante]
# Fecha: [dd/mm/2026]    Versión: 1.0
# Descripción: Gestiona actividades científicas de una misión
# espacial y calcula los recursos y puntos restantes.
# ============================================================

# Constantes: costos y puntajes de las actividades.
ENERGIA_ANALIZAR = 8
PROVISIONES_ANALIZAR = 0
PUNTOS_ANALIZAR = 10

ENERGIA_RECOLECTAR = 12
PROVISIONES_RECOLECTAR = 2
PUNTOS_RECOLECTAR = 20

ENERGIA_OBSERVAR = 5
PROVISIONES_OBSERVAR = 0
PUNTOS_OBSERVAR = 8

# Entrada de datos.
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# Inicialización de contadores, acumulador y variable de control.
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
continuar_exploracion = True

# Ciclo principal de exploración.
while continuar_exploracion:
    print("\n--- ACTIVIDADES DE EXPLORACIÓN ---")
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")

    opcion = int(input("Seleccione una opción (1, 2, 3 o 4): "))

    # Determinar la actividad, su costo y sus puntos.
    if opcion == 1:
        actividad = "Analizar terreno"
        costo_energia = ENERGIA_ANALIZAR
        costo_provisiones = PROVISIONES_ANALIZAR
        puntos_actividad = PUNTOS_ANALIZAR

    elif opcion == 2:
        actividad = "Recolectar muestra"
        costo_energia = ENERGIA_RECOLECTAR
        costo_provisiones = PROVISIONES_RECOLECTAR
        puntos_actividad = PUNTOS_RECOLECTAR

    elif opcion == 3:
        actividad = "Realizar observación"
        costo_energia = ENERGIA_OBSERVAR
        costo_provisiones = PROVISIONES_OBSERVAR
        puntos_actividad = PUNTOS_OBSERVAR

    elif opcion == 4:
        print("Exploración finalizada por la tripulación.")
        continuar_exploracion = False

    else:
        print("Opción no válida.")

    # Verificar recursos y ejecutar actividades válidas.
    if opcion >= 1 and opcion <= 3:
        if energia >= costo_energia and provisiones >= costo_provisiones:

            energia = energia - costo_energia
            provisiones = provisiones - costo_provisiones

            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + puntos_actividad

            # Solo recolectar muestras incrementa este contador.
            if opcion == 2:
                muestras_recolectadas = muestras_recolectadas + 1

            print("Actividad realizada:", actividad + ".",
                  "Puntos obtenidos:", puntos_actividad)

        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            continuar_exploracion = False

# Salida final de resultados.
print("\nActividades realizadas:", actividades_realizadas)
print("Muestras recolectadas:", muestras_recolectadas)
print("Puntos científicos:", puntos_cientificos)
print("Energía restante:", energia, "unidades")
print("Provisiones restantes:", provisiones, "unidades")
