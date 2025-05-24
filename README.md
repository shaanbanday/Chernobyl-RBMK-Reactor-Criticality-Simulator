# RBMK Reactor Criticality Simulator

This Python script simulates the **criticality state** of a nuclear reactor using the **six-factor formula**, a standard expression in nuclear engineering to calculate the effective multiplication factor (k) of a reactor.

The simulation references the **Chernobyl RBMK reactor** and uses light historical allusions to enhance educational engagement.

## 🧮 Six-Factor Formula

The script calculates reactor criticality using the formula: k = η × f × p × ε × p_f × (1 − β)

Where:
- **η** = Neutron reproduction factor  
- **f** = Thermal utilization factor  
- **p** = Resonance escape probability  
- **ε** = Fast fission factor  
- **p_f** = Thermal neutron non-leakage probability  
- **β** = Delayed neutron fraction
