def clasificar_resultado(resultados):
    if all(resultados):
        return "Tautología 🟢"
    elif not any(resultados):
        return "Contradicción 🔴"
    else:
        return "Contingencia 🟡"

def generar_tabla_verdad():
    resultados_totales = []

    print("P     | Q     | Resultado")
    print("-------------------------")

    for P in [True, False]:
        for Q in [True, False]:
            resultado_fila = P and Q
            resultados_totales.append(resultado_fila)
            print(f"{str(P):<5} | {str(Q):<5} | {resultado_fila}")
            
            print("-------------------------")
            
    diagnostico = clasificar_resultado(resultados_totales)
    print(f"DIAGNÓSTICO: {diagnostico}")

if __name__ == "__main__":
    generar_tabla_verdad()


