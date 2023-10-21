"""Calculadora de operaciones básicas."""
from pandas import read_csv

from calculadora.operaciones.aditivas import suma, resta
from calculadora.operaciones.multiplicativas.multiplicativas import multiplica, division

from calculadora.utils.fracciones import obtener_fracciones


def main():
    # data = read_csv("sample.csv")
    # print(data)
    res_divide = division(10, 2)
    print(f"Resultado Division: {res_divide}")

    res_multiplica = multiplica(10, 2)
    print(f"Resultado Multiplicacion: {res_multiplica}")

    res_suma = suma(10, 2)
    print(f"Resultado Suma: {res_suma}")

    res_resta = resta(10, 2)
    print(f"Resultado Resta: {res_resta}")
    print(obtener_fracciones("1/2"))


if __name__ == "__main__":
    main()
