def square_func(x):
    return x * x


def cube(n):
    return n * n * n


def calcula_media(*args):
    return sum(*args) / len(*args)

# Puedo indicarle el tipo de la variable a la función
def capital_letter(a: str):
    return a.capitalize()