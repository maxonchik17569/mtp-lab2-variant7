# Лабораторная работа №2

Ким Максим Сергеевич, группа 221341, вариант 7, лабораторная №2.

## Задания варианта

**Средняя сложность:**

- №7 — подсчёт гласных (`lab2/vowels.py`)
- №9 — минимальный элемент списка (`lab2/minimum.py`)
- №3 — факториал числа (`lab2/factorial.py`)

**Повышенная сложность:**

- №7 — частота слов в файле (`lab2/wordfreq.py`)
- №5 — игра «Угадай число» (`lab2/guess_number.py`)

## Запуск

```bash
python -m lab2
```

## Проверки

```bash
python -m unittest discover -s tests -v
python -m compileall -q lab2 tests
flake8 lab2 tests
```

Подробное описание выполнения — в `docs/report.md`.
