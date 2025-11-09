class Calculator:
    def __init__(self, op1: float | int, op2: float | int):
        if not isinstance(op1, (int, float)) or not isinstance(op2, (int, float)):
            raise TypeError("Oba argumenty muszą być liczbami (int lub float)")
        self.__op1 = float(op1)
        self.__op2 = float(op2)

    @property
    def op1(self):
        return self.__op1

    @property
    def op2(self):
        return self.__op2

    def sum(self):
        return self.__op1 + self.__op2

    def sub(self):
        return self.__op1 - self.__op2

    def mul(self):
        return self.__op1 * self.__op2

    def div(self):
        try:
            return self.__op1 / self.__op2
        except ZeroDivisionError:
            return "Błąd: nie można dzielić przez zero"

if __name__ == "__main__":
    #zgodny typ danych:
    print("Przykładowe działania kalkulatora:\n")

    calc1 = Calculator(10, 5)
    print("10 + 5 =", calc1.sum())
    print("10 - 5 =", calc1.sub())
    print("10 * 5 =", calc1.mul())
    print("10 / 5 =", calc1.div())

    #dzielenie przez zero:
    calc2 = Calculator(7, 0)
    print("\n7 / 0 =", calc2.div())

    #błędny typ danych:
    try:
        calc3 = Calculator("abc", 2)
        print("abc + 2 =", calc3.sum())
    except TypeError as e:
        print("\nabc + 2 = Błąd typu danych konstruktora klasy Calculator; przykład string", f"\n {e}")

    try:
        calc4 = Calculator(3, None)
        print("3 + None =", calc4.sum())
    except TypeError as e:
        print("\n3 + None = Błąd typu danych konstruktora klasy Calculator: przykład None", f"\n {e}")

    #AttributeError - przykłady użycia atrybutów klasy Calculator:
    calc = Calculator(10, 5)

    print("\nop1 =", calc.op1," -> dostęp do atrybutów klasy Calculator działa poprawnie")

    try:
        calc.op1 = 99
    except AttributeError as e:
        print("\ncalc.op1 = 99 -> Błąd: próba nadpisania atrybutu op1 klasy Claculator:", e)

    try:
        print(calc.nie_istnieje)
    except AttributeError as e:
        print("\nprint(calc.nie_istnieje) -> Błąd: próba dostępu do nieistniejącego atrybutu:", e)
