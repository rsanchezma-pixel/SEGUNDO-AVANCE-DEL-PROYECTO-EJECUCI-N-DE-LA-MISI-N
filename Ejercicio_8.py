# ============================================================
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1
# Sección: [indicar]
# Integrante: [RONY SANCHEZ MASIS]
# Fecha: 07/11/2026
# Versión: 1.0
# Descripción: Evalúa el regreso a la Tierra y, si falta
# combustible, estima la supervivencia de la tripulación.
# ============================================================

# Constantes: consumo diario de recursos.
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE = 1

# Entrada de datos del estado de la nave después de explorar.
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese los días del viaje de ida: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# Cálculo previo: combustible para todos los días de regreso.
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
consumo_oxigeno_diario = tripulantes * CONSUMO_OXIGENO_TRIPULANTE
consumo_provisiones_diario = tripulantes * CONSUMO_PROVISIONES_TRIPULANTE

# Decisión principal: regresar o estimar supervivencia.
if combustible >= combustible_regreso:

    # CASO A: Simular el regreso día por día.
    dias_completados = 0
    puede_continuar = True

    while dias_completados < dias_viaje and puede_continuar:

        # Verificar los cuatro recursos antes de consumirlos.
        if (combustible >= CONSUMO_COMBUSTIBLE_DIA and
                oxigeno >= consumo_oxigeno_diario and
                energia >= CONSUMO_ENERGIA_DIA and
                provisiones >= consumo_provisiones_diario):

            combustible = combustible - CONSUMO_COMBUSTIBLE_DIA
            oxigeno = oxigeno - consumo_oxigeno_diario
            energia = energia - CONSUMO_ENERGIA_DIA
            provisiones = provisiones - consumo_provisiones_diario

            dias_completados = dias_completados + 1

            print("Día", dias_completados,
                  "| Combustible:", combustible,
                  "| Oxígeno:", oxigeno,
                  "| Energía:", energia,
                  "| Provisiones:", provisiones)

        else:
            # Si falla un recurso, no se consume nada ese día.
            puede_continuar = False

    # Resultados del regreso.
    if dias_completados == dias_viaje:
        print("La tripulación regresó exitosamente a la Tierra.")
        print("Combustible restante:", combustible, "unidades")
        print("Oxígeno restante:", oxigeno, "unidades")
        print("Energía restante:", energia, "unidades")
        print("Provisiones restantes:", provisiones, "unidades")

    else:
        print("El regreso se interrumpió en el día",
              dias_completados + 1, ".", sep="")

        if oxigeno < consumo_oxigeno_diario:
            print("Recurso insuficiente: oxígeno")

        if energia < CONSUMO_ENERGIA_DIA:
            print("Recurso insuficiente: energía")

        if provisiones < consumo_provisiones_diario:
            print("Recurso insuficiente: provisiones")

        print("La tripulación no completó el regreso.")

else:

    # CASO B: La nave no puede iniciar el regreso.
    print("La tripulación quedó varada en el destino.")

    # Calcular días completos de supervivencia.
    dias_oxigeno = oxigeno // consumo_oxigeno_diario
    dias_energia = energia // CONSUMO_ENERGIA_DIA
    dias_provisiones = provisiones // consumo_provisiones_diario

    print("Días por oxígeno:", dias_oxigeno)
    print("Días por energía:", dias_energia)
    print("Días por provisiones:", dias_provisiones)

    # Determinar el menor valor sin utilizar min().
    supervivencia_estimada = dias_oxigeno

    if dias_energia < supervivencia_estimada:
        supervivencia_estimada = dias_energia

    if dias_provisiones < supervivencia_estimada:
        supervivencia_estimada = dias_provisiones

    # Identificar todos los recursos limitantes.
    recursos_limitantes = ""

    if dias_oxigeno == supervivencia_estimada:
        recursos_limitantes = "oxígeno"

    if dias_energia == supervivencia_estimada:
        if recursos_limitantes != "":
            recursos_limitantes = recursos_limitantes + ", "
        recursos_limitantes = recursos_limitantes + "energía"

    if dias_provisiones == supervivencia_estimada:
        if recursos_limitantes != "":
            recursos_limitantes = recursos_limitantes + ", "
        recursos_limitantes = recursos_limitantes + "provisiones"

    print("Supervivencia estimada:",
          supervivencia_estimada, "días")

    print("Recurso(s) limitante(s):", recursos_limitantes)
