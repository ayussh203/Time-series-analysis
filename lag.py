import math
import numpy as np
import matplotlib.pyplot as plt


graph1 = np.array([0.865257, 2.09646, 3.55949, 5.0869, 6.39701, 7.34355, 7.71642, 7.22113, 5.87831, 3.78083, 1.15362, -1.68, -4.35489, -6.53074, -7.95374, -8.48222, -8.08787, -7.15307, -5.63978, -3.91215])


graph2 = np.array([-0.0413589, -0.0744249, -0.108228, -0.161074, -0.224722, -0.291076, -0.334128, -0.333282, -0.271283, -0.153474, -00000000.260863, 0.153474, 0.271283, 0.333282, 0.334128, 0.291076, 0.224722, 0.161074, 0.108228, 0.0744249])

cross_corr = np.correlate(graph1, graph2, 'full')


max_index = np.argmax(np.abs(cross_corr))

phase_lag_rad = (max_index - len(graph1) + 1) * (2 * math.pi / len(graph1))


phase_lag_deg = math.degrees(phase_lag_rad)

print("Phase Lag (radians):", phase_lag_rad)
print("Phase Lag (degrees):", phase_lag_deg)


shifts = np.arange(len(graph1) - 1, len(graph2))
plt.plot(shifts, cross_corr)
plt.xlabel('Shifts')
plt.ylabel('Cross-correlation')
plt.title('Cross-correlation between Graph 1 and Graph 2')
plt.grid(True)
plt.show()
