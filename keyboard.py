# keyboard.py

# Funkcja do odczytywania napisu (ciągu znaków)
def input_string(message):
    return input(message)

# Funkcja do odczytywania liczby całkowitej
def input_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Nieprawidłowy wpis. Proszę podać liczbę całkowitą.")

# Funkcja do odczytywania liczby zmiennoprzecinkowej
def input_real(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Nieprawidłowy wpis. Proszę podać liczbę zmiennoprzecinkową.")

# Funkcja do odczytywania wartości logicznej
def input_boolean(message):
    while True:
        response = input(message).lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Nieprawidłowy wpis. Proszę podać 'y' lub 'n'.")
