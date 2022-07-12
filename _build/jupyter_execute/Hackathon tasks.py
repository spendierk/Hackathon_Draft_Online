#!/usr/bin/env python
# coding: utf-8

# # Your Tasks for this Hackathon
# 
# This was a first glimpse of the workflow from the design of a quantum circuit to its execution. There is much more to discover by looking at an entire series of example notebooks for `pytket`
# available on the [pytket github](https://github.com/CQCL/pytket/tree/master/examples).
# 
# Recommended examples applicable to this Hackathon you can go through as a continuation of this introduction include:
# - [Run a circuit on the backends](https://github.com/CQCL/pytket/blob/master/examples/backends_example.ipynb)
# - [Circuit Optimization](https://github.com/CQCL/pytket/blob/master/examples/compilation_example.ipynb)
# - [Advanced techniques for creating circuits](https://github.com/CQCL/pytket/blob/master/examples/circuit_generation_example.ipynb)

# ## Your task
# 
# The costs for using quantum hardware platforms depend on different parameters such as runtime, the number of gates in a program, the complexity of the gates used, and the number of shots. Based on the known pricing of different gate-based quantum computing hardware providers, you are tasked to find the cheapest solution for your company to perform a selection of quantum computations. 
# 
# For this challenge, you will use the TKET compiler, which integrates with Qiskit. TKET is a platform agnostic quantum software toolkit that will help you compile and optimize your quantum programs to target a range of hardware and find the most valuable solution for your company. 
# 
# For IonQ and Quantinuum pricing, see here: 
# [Azure Quantum providers pricing](https://docs.microsoft.com/en-us/azure/quantum/pricing?tabs=tabid-AQcredits%2Ctabid-AQcreditsQ%2Ctabid-payasgo%2Ctabid-learndevelop&pivots=ide-computing)
# 
# For IBM pricing, see here: 
# [Qiskit Runtime (Beta) - IBM Cloud](https://cloud.ibm.com/catalog/services/quantum-computing)
# 
# For Amazon Bracket Pricing of many others, see here: 
# [Amazon Bracket Pricing](https://aws.amazon.com/braket/pricing/)

# ## Previous tasks (ETH Zürich, 8th April - 10th April, 2022)
# You are now ready for the _real_ challenges!
# For this hackathon, we have prepared two different tasks that you can try to
# tackle with TKET:
#  1. "[Estimating phases with Hadamard Test and Cat States](https://github.com/CQCL/ethz-hackathon22/blob/main/hadamard_test.md)". This problem explores some of the more theoretical questions around building applications of quantum computing for quantum chemistry and Hamiltonian simulation. A bit more maths and physics heavy.
#  2. "[World-class routing](https://github.com/CQCL/ethz-hackathon22/blob/main/routing.md)". Dive into the state-of-the-art of quantum circuit compilation. This problem is more applied, open-ended and programming-heavy: you'll have to come up with your own implementations and benchmark your results.
# 
# It is NOT expected that you solve both, so do pick your favourite!
# 
# 

# Good luck! Don't hesitate to reach out to us if you have any questions.

# In[ ]:




