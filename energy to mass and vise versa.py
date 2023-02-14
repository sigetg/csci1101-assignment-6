SPEED_OF_LIGHT = 299792458

def energy_to_mass(E):
    m = E / (SPEED_OF_LIGHT**2)
    return m

def mass_to_energy(m):
    E = m * (SPEED_OF_LIGHT**2)
    return E

print(f"Mass = {energy_to_mass(100000)}")
print(f"Energy = {mass_to_energy(1)}")
