def resistencia_serie(resistencias):
    """Calcula la resistencia total en un circuito en serie."""
    return sum(resistencias)

def resistencia_paralelo(resistencias):
    """Calcula la resistencia total en un circuito en paralelo."""
    inversa = sum(1/r for r in resistencias)
    return 1 / inversa

def corriente_total(voltage, resistencia_equivalente):
    """Calcula la corriente total usando la ley de Ohm."""
    return voltage / resistencia_equivalente

def energia_consumida(corriente, resistencia, tiempo):
    """Calcula la energía consumida en un circuito."""
    potencia = corriente ** 2 * resistencia
    return potencia * tiempo

def main():
    tipo_circuito = input("¿Es un circuito en serie o paralelo? (serie/paralelo): ").lower()
    
    resistencias = list(map(float, input("Ingrese las resistencias (en ohmios), separadas por coma: ").split(',')))
    
    voltaje = float(input("Ingrese el voltaje aplicado (en voltios): "))
    
    tiempo = float(input("Ingrese el tiempo de operación (en segundos): "))
    
    if tipo_circuito == "serie":
        resistencia_eq = resistencia_serie(resistencias)
    elif tipo_circuito == "paralelo":
        resistencia_eq = resistencia_paralelo(resistencias)
    else:
        print("Tipo de circuito no válido.")
        return
    
    corriente = corriente_total(voltaje, resistencia_eq)
    
    energia = energia_consumida(corriente, resistencia_eq, tiempo)
    
    print(f"\nResistencia equivalente: {resistencia_eq:.2f} ohmios")
    print(f"Corriente total: {corriente:.2f} amperios")
    print(f"Energía consumida: {energia:.2f} julios")

if __name__ == "__main__":
    main()
