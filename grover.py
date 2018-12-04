import numpy as np
from pyquil import Program, get_qc
from pyquil.gates import H
from pyquil.quil import DefGate
from pyquil.api import WavefunctionSimulator


# working with three qubits
qv = get_qc('3q-qvm')
p = Program(H(0), H(1), H(2))


def one_shot_grover(qubits):
