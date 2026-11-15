# zad4 - warunki i pętle

11 zadań z konsoli, wybieranych z menu.

```sh
cd source
uv run python -m zad4.main
```

## Zadania

| # | Zadanie | Gdzie |
|---|---------|-------|
| 1 | Liczba parzysta czy nieparzysta | `conditions.even_or_odd` |
| 2 | Największa z trzech liczb | `conditions.largest_of_three` |
| 3 | Silnia pętlą `while` | `loops.factorial_while` |
| 4 | Liczby od 1 do 100 podzielne przez 3, ale nie przez 5 | `loops.divisible_by_3_not_5` |
| 5 | Sumowanie liczb do wpisania „stop” | `loops.sum_until_stop` |
| 6 | Pierwsza liczba większa niż 10 | `loops.find_first_greater_than_10` |
| 7 | Czy liczba jest pierwsza | `puzzles.check_prime` |
| 8 | Liczby 1-20, co czwarta jako „divisible by 4” | `loops.numbers_to_20` |
| 9 | Liczba dodatnia, ujemna czy zero | `conditions.check_sign` |
| 10 | Zgadywanie liczby 1-10 | `puzzles.guess_number` |
| 11 | Liczby 1-50 bez cyfry 3 | `loops.numbers_without_3` |

## Pliki

- `main.py` - menu
- `conditions.py` - zadania 1, 2, 9
- `loops.py` - zadania 3, 4, 5, 6, 8, 11
- `puzzles.py` - zadania 7 i 10
