import numpy as np
import matplotlib.pyplot as plt

def simpson_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla de Simpson."""
    if n % 2 == 1:
        raise ValueError("El número de subintervalos (n) debe ser par.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # Puntos del intervalo
    fx = f(x)  # Evaluamos la función en esos puntos
    
    # Regla de Simpson
    integral = (h / 3) * (fx[0] + 2 * np.sum(fx[2:n:2]) + 4 * np.sum(fx[1:n:2]) + fx[n])
    
    return integral

# Función a integrar (trabajo del resorte)
def trabajo_resorte(x):
    k = 200  # N/m
    return k * x

# Parámetros del problema
a = 0.1  # m
b = 0.3  # m
n_valores = [6, 10, 20, 30]

# Solución analítica (para comparar)
solucion_analitica = 0.5 * 200 * (b**2 - a**2)

# Resultados numéricos y errores
resultados = []
errores = []

for n in n_valores:
    resultado_num = simpson_rule(trabajo_resorte, a, b, n)
    resultados.append(resultado_num)
    error = abs(resultado_num - solucion_analitica)
    errores.append(error)
    print(f"n = {n}: Trabajo = {resultado_num:.4f} J, Error = {error:.4f} J")

print(f"\nSolución analítica: {solucion_analitica:.4f} J")

# Gráfica de la función y la aproximación (con n = 30)
x_vals = np.linspace(a, b, 100)
y_vals = trabajo_resorte(x_vals)

plt.plot(x_vals, y_vals, label=r"$Trabajo(x) = kx$", color="blue")
plt.fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label="Área aproximada")
plt.scatter(np.linspace(a, b, 30 + 1), trabajo_resorte(np.linspace(a, b, 30 + 1)), color="red", label="Puntos de interpolación")
plt.xlabel("x (m)")
plt.ylabel("Trabajo (J)")
plt.legend()
plt.title("Trabajo realizado por el resorte (Regla de Simpson)")
plt.grid()

# Guardar la figura
plt.savefig("trabajo_resorte_simpson.png")
plt.show()

# Gráfica del error en función de n
plt.plot(n_valores, errores, marker='o')
plt.xlabel("Número de subintervalos (n)")
plt.ylabel("Error (J)")
plt.title("Error en la aproximación del trabajo")
plt.grid()

# Guardar la figura
plt.savefig("error_trabajo_resorte.png")
plt.show()