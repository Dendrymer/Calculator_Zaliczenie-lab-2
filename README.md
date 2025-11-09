To jest repozytorium zawierające kod na zaliczenie lab 2 z wybranych zagadnień inżynierii oprogramowania
# 🧮 Calculator — Prosty kalkulator w Pythonie

Ten projekt zawiera klasę `Calculator`, która umożliwia wykonywanie podstawowych operacji matematycznych na dwóch liczbach. Kod został napisany z myślą o czytelności, bezpieczeństwie typów i obsłudze błędów.

---

## 📦 Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/Dendrymer/Calculator_Zaliczenie-lab-2.git
cd Calculator_Zaliczenie-lab-2

### 🖥️ Przyklad działania
Kod:
calc1 = Calculator(10, 5)
print("10 + 5 =", calc1.sum())
print("10 - 5 =", calc1.sub())
print("10 * 5 =", calc1.mul())
print("10 / 5 =", calc1.div())
Wynik w konsoli:
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0

####⚠️ Obsługa błędów
Kalkulator zawiera podstawową walidację typów oraz obsługę dzielenia przez zero.
Kod:
calc2 = Calculator(7, 0)
print("\n7 / 0 =", calc2.div())
Wynik w konsoli:
7 / 0 = Błąd: nie można dzielić przez zero





