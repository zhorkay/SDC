# Extended Kalman Filter

import numpy as np

x0 = 0
v0 = 5
dt = 0.5
a0 = -2
S = 20
D = 40
angle = np.arctan(S / D)
y = np.pi / 6

F_k0 = np.array([[1.0, dt], [0.0, 1.0]], dtype=float)
L_k0 = np.array([[1.0, 0.0], [0.0, 1.0]], dtype=float)
H_k0 = np.array([S / (D * D + S * S), 0.0], dtype=float)
M_k0 = np.array([1.0], dtype=float)
Q_k0 = np.array([[0.1, 0.0], [0.0, 0.1]], dtype=float)
X_k0 = np.array([[x0], [v0]], dtype=float)
P_k0 = np.array([[0.01, 0.0], [0.0, 1.0]], dtype=float)

P_k1 = (F_k0.dot(P_k0)).dot(F_k0.T) + (L_k0.dot(Q_k0)).dot(L_k0.T)
print(P_k1)

g_k = np.array([[0.0], [dt]], dtype=float)
w_k = np.array([[0.1, 0.0], [0.0, 1.0]], dtype=float)

