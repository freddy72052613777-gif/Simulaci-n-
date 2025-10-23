# ============================================
# CALCULADORA DE DISTRIBUCIONES Y VARIABLES
# Autor: Freddy Ortiz
# Lenguaje: Python 3
# Librerías necesarias:
# pip install numpy scipy matplotlib
# ============================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, expon, gamma, norm, weibull_min, erlang

def menu():
    print("============================================")
    print("     CALCULADORA DE DISTRIBUCIONES")
    print("============================================")
    print("1. Distribución Uniforme")
    print("2. Distribución Erlang")
    print("3. Distribución Exponencial")
    print("4. Distribución Gamma")
    print("5. Distribución Normal")
    print("6. Distribución Weibull")
    print("============================================")
    opcion = int(input("Seleccione una opción (1-6): "))
    return opcion

def grafico(x, y, title):
    plt.figure(figsize=(8,5))
    plt.plot(x, y, label='Función de densidad (PDF)')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def grafico_histograma(data, title):
    plt.figure(figsize=(8,5))
    plt.hist(data, bins=30, color='skyblue', edgecolor='black', density=True)
    plt.title(f"Histograma - {title}")
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia relativa')
    plt.grid(True)
    plt.show()

# ==============================
# DISTRIBUCIONES
# ==============================

def uniforme():
    a = float(input("Ingrese el límite inferior (a): "))
    b = float(input("Ingrese el límite superior (b): "))
    dist = uniform(a, b - a)
    media, varianza = dist.mean(), dist.var()
    print(f"\nMedia = {media:.4f}")
    print(f"Varianza = {varianza:.4f}")
    x = np.linspace(a, b, 100)
    grafico(x, dist.pdf(x), "Distribución Uniforme")
    data = dist.rvs(size=1000)
    grafico_histograma(data, "Distribución Uniforme")

def erlang_dist():
    k = int(input("Ingrese el parámetro de forma k (entero): "))
    lmbda = float(input("Ingrese el parámetro de escala (λ): "))
    dist = erlang(k, scale=1/lmbda)
    media, varianza = dist.mean(), dist.var()
    print(f"\nMedia = {media:.4f}")
    print(f"Varianza = {varianza:.4f}")
    x = np.linspace(0, media*3, 100)
    grafico(x, dist.pdf(x), "Distribución Erlang")
    data = dist.rvs(size=1000)
    grafico_histograma(data, "Distribución Erlang")

def exponencial():
    lmbda = float(input("Ingrese el parámetro λ (tasa): "))
    dist = expon(scale=1/lmbda)
    media, varianza = dist.mean(), dist.var()
    print(f"\nMedia = {media:.4f}")
    print(f"Varianza = {varianza:.4f}")
    x = np.linspace(0, media*5, 100)
    grafico(x, dist.pdf(x), "Distribución Exponencial")
    data = dist.rvs(size=1000)
    grafico_histograma(data, "Distribución Exponencial")

def gamma_dist():
    alpha = float(input("Ingrese el parámetro de forma α: "))
    beta = float(input("Ingrese el parámetro de escala β: "))
    dist = gamma(alpha, scale=beta)
    media, varianza = dist.mean(), dist.var()
    print(f"\nMedia = {media:.4f}")
    print(f"Varianza = {varianza:.4f}")
    x = np.linspace(0, media*3, 100)
    grafico(x, dist.pdf(x), "Distribución Gamma")
    data = dist.rvs(size=1000)
    grafico_histograma(data, "Distribución Gamma")

def normal():
    mu = float(input("Ingrese la media μ: "))
    sigma = float(input("Ingrese la desviación estándar σ: "))
    dist = norm(mu, sigma)
    media, varianza = dist.mean(), dist.var()
    print(f"\nMedia = {media:.4f}")
    print(f"Varianza = {varianza:.4f}")
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
    grafico(x, dist.pdf(x), "Distribución Normal")
    data = dist.rvs(size=1000)
    grafico_histograma(data, "Distribución Normal")

def weibull():
    c = float(input("Ingrese el parámetro de forma β: "))
    escala = float(input("Ingrese el parámetro de escala α: "))
    dist = weibull_min(c, scale=escala)
    media, varianza = dist.mean(), dist.var()
    print(f"\nMedia = {media:.4f}")
    print(f"Varianza = {varianza:.4f}")
    x = np.linspace(0, media*3, 100)
    grafico(x, dist.pdf(x), "Distribución Weibull")
    data = dist.rvs(size=1000)
    grafico_histograma(data, "Distribución Weibull")

# ==============================
# PROGRAMA PRINCIPAL
# ==============================

if __name__ == "__main__":
    opcion = menu()
    if opcion == 1:
        uniforme()
    elif opcion == 2:
        erlang_dist()
    elif opcion == 3:
        exponencial()
    elif opcion == 4:
        gamma_dist()
    elif opcion == 5:
        normal()
    elif opcion == 6:
        weibull()
    else:
        print("Opción no válida.")
    print("\nPrograma finalizado. ¡Gracias por usar la calculadora!")
