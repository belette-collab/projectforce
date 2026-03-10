print("Test de PIN...")

correct_pin = "123456"

with open("bruteforce_6digit_pin.txt", "r") as file:
    for pin in file:
        pin = pin.strip()
        print("Test:", pin)

        if pin == correct_pin:
            print("PIN trouvé :", pin)
            break

