def generate_truth_table():
    # Encabezado de la tabla de verdad
    print(f"{'A':<6} | {'B':<6} | {'AND':<6} | {'OR':<6} | {'NOT A':<6} | {'XOR':<6}")
    print("-" * 50)
    
    # Combinaciones lógicas posibles para dos variables
    combinations = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    
    # Evaluación de cada fila
    for A, B in combinations:
        and_res = A and B
        or_res = A or B
        not_a = not A
        xor_res = A != B
        
        # Formatear la salida como enteros (1 para True, 0 para False) para estilo matemático
        print(f"{int(A):<6} | {int(B):<6} | {int(and_res):<6} | {int(or_res):<6} | {int(not_a):<6} | {int(xor_res):<6}")

if __name__ == "__main__":
    print("--- Truth Table Generator for Propositional Logic ---")
    generate_truth_table()
