import math

#calculates reactor crtiticality (k) using the six-factor formula.
def calculate_k(eta, f, p, epsilon, p_f, beta):
    return eta * f * p * epsilon * p_f * (1 - beta)

#determines reactor state based on crtiticality 
def assess_criticality(k):
    if k < 1:
        return "Subcritical: AZ-5 pressed. The reactor is shutting down."
    elif k == 1:
        return "Critical: Reactor in a steady state. Anatoly Dyatlov approves."
    else:
        return "Supercritical: Reactor power violently increasing. Get out now!"

def main():
    print("\nChernobyl RBMK Reactor Criticality Simulator\n")
    
    # User inputs for six factors
    eta = float(input("Neutron reproduction factor (eta): "))  # Number of neutrons produced per neutron absorbed in fuel
    f = float(input("Thermal utilization factor (f): "))  # Fraction of neutrons absorbed in fuel vs. other materials
    p = float(input("Resonance escape probability (p): "))  # Probability of a neutron avoiding resonance capture
    epsilon = float(input("Fast fission factor (epsilon): "))  # Additional neutrons from fast fission
    p_f = float(input("Thermal neutron non-leakage probability (p_f): "))  # Probability of thermal neutron staying in reactor
    beta = float(input("Delayed neutron fraction (beta): "))  # Fraction of neutrons emitted by delayed processes
    
    # Compute keff
    kChernobyl = calculate_k(eta, f, p, epsilon, p_f, beta)
    
    # Output results
    print(f"\nReactor Criticality (k): {kChernobyl:.4f}")
    print(assess_criticality(kChernobyl))
    
if __name__ == "__main__":
    main()
