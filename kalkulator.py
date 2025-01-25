def calculator():
    print("Prosty kalkulator")
    print("Wybierz operację:")
    print("1. Dodawanie (+)")
    print("2. Odejmowanie (-)")
    print("3. Mnożenie (*)")
    print("4. Dzielenie (/)")
    
    try:
        choice = int(input("Wybierz (1/2/3/4): "))
        
        if choice not in [1, 2, 3, 4]:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            return

        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))
        
        if choice == 1:
            result = num1 + num2
            operation = "+"
        elif choice == 2:
            result = num1 - num2
            operation = "-"
        elif choice == 3:
            result = num1 * num2
            operation = "*"
        elif choice == 4:
            if num2 == 0:
                print("Błąd: Dzielenie przez zero!")
                return
            result = num1 / num2
            operation = "/"
        
        print(f"Wynik: {num1} {operation} {num2} = {result}")
    except ValueError:
        print("Błąd: Wprowadź poprawne liczby.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

calculator()

