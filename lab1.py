import winsound

def oblicz_bmi():
    try:
        wzrost = float(input("Podaj swoj wzrost w m/cm: "))
        waga = float(input("Podaj swoja wage w kg: "))

        if wzrost > 100:
            wzrost /= 100

        if wzrost <= 0 or waga <= 0:
            print("Wzrost lub waga musi byc wieksza od 0")
            return

        bmi = waga / (wzrost ** 2)
        print(f"Twoje BMI wynosi: {bmi:.2f}")

        if bmi < 18.5:
            print("Masz niedowage.")
        elif 19 <= bmi < 24.9:
            print("Twoja waga jest prawidlowa.")
            winsound.Beep(440, 500)
        elif 25 <= bmi < 29.9:
            print("Masz nadwage.")
        else:
            print("Masz otylosc.")
            winsound.Beep(440, 500)
    except ValueError:
        print("Tylko liczby.")

while True:
    oblicz_bmi()
    dalej = input("Czy chcesz kontynuowac?").strip().lower()
    if dalej != 'tak':
        break