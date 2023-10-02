import numpy as np
import matplotlib.pyplot as plt

# Paramètres du modèle
sigma = 5.67e-8         # Constante de Stefan-Boltzmann (W/m^2/K^4)
t0 = 0
t1 = 100                # Durée de la simulation (années)

# Conditions initiales

Ts = 255    # température de surface (K)

t = [t0]

Ts_array = [Ts]

L = 1370        # constante solaire
I = L / 4       # irradiance globale
alpha = 0.3     # albedo planetaire
beta = 0.3      # fraction de lumière absorbée par l'atmosphère
gamma = 0.21    # fraction de chaleur non radiative
omega = 0.10    # fraction de chaleur radiative qui s'échappe vers l'espace
delta = 0.77    # proportion de chaleur radiative émise par l'atmosphère et qui revient vers la surface
epsilon = 0.95  # émissivité de la surface terrestre


q0 = I * (1-alpha) * (1-beta)       # quantité de chaleur fournie par le soleil et reçue au niveau de la surface terreste
qa = I * beta * (1-alpha)           # quantité de chaleur absorbée par l'atmosphère

print (f"L   {L:.1f}")
print (f"I   {I:.1f}")
print (f"q0  {q0:.1f}")
print (f"qa  {qa:.1f}")


qs = q0
Ts0 = 100
tt = t0

print(f"t \tqs \tq1 \tq2 \tq3 \tq4 \tq5 \tq6 \tTs ")


# Boucle de simulation
while True:    
    q1 = gamma * qs                    # chaleur sensible + chaleur latente
    q2 = (1-gamma) * qs                # chaleur radiative
    q3 = omega * q2                    # chaleur radiative de la surface qui s'échappe vers l'espace
    q4 = (1-omega) * q2 + qa           # chaleur radiative de la surface captée par l'atmosphère
    q5 = q4 * delta                    # chaleur radiative de l'atmosphère qui revient vers la surface
    q6 = q4 * (1-delta)                # chaleur radiative de l'atmosphère qui s'échapppe vers l'espace
    
    qs = q0 + q5
    
    Ts = (q2 / (epsilon*sigma)) ** (1/4)

    print(f"{tt:.1f}\t{qs:.1f}\t{q1:.1f}\t{q2:.1f}\t{q3:.1f}\t{q4:.1f}\t{q5:.1f}\t{q6:.1f}\t{Ts:.1f}K\t{Ts-273.15:.1f}°C")
    
    t.append(tt)
    Ts_array.append(Ts)
    
    tt += 1
    if tt > t1:
        break
    if abs(Ts-Ts0)<0.05:
        break
    
    Ts0 = Ts
    
 
# Tracer les résultats
plt.figure(figsize=(10, 6))
plt.plot(t, Ts_array, label='Température de surface')
plt.xlabel('Temps')
plt.ylabel('Température (K)')
plt.legend()
plt.title('Modélisation de l\'effet de serre')
plt.grid(True)
plt.show()
