from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a Quantum Circuit
circuit = QuantumCircuit(2, 2)

# Add gates
circuit.h(0)
circuit.cx(0, 1)

# Measurement
circuit.measure([0, 1], [0, 1])

# Use AerSimulator
simulator = AerSimulator()

# Run the circuit
result = simulator.run(circuit, shots=1000).result()

# Get results
counts = result.get_counts()
print("Counts:", counts)

# Draw circuit
circuit.draw('mpl')
plt.show()

# Plot histogram
plot_histogram(counts)
plt.show()