from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
qc = QuantumCircuit(2, 2)

qc.h(0) #superposition
qc.measure(0,0) #measurement of qubit 0
print(qc)
simulator = AerSimulator()
result = simulator.run(qc, shots=10000).result()
counts = result.get_counts(qc)
print("the final measurement of qubit 0 is: ", counts)