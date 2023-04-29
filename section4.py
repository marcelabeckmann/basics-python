#python functions
def greet(name):
    print(f"Hola {name}")
greet('Marcela')


def sum(a, b):
    return a + b

total = sum(10,20)
print(total)

def invertir_cadena(cadena):
    cadena_invertida = ''
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

resultado = invertir_cadena("Hola mundo")
print(resultado)

#default
def greet(name='there', message='Hi'):
    return f"{message} {name}"

greeting = greet()
print(greet("Marcela", "Hola"))

print(greet("Marcela"))

print(greeting)

#keyword arguments
def get_net_price(price, discount):
    return price * (1-discount)

net_price = get_net_price(discount=0.1, price=100)
print(net_price)


def get_net_price(price, tax=0.07, discount=0.05):
    return price * (1 + tax - discount)

net_price = get_net_price(price=100, discount=0.06)
print(net_price)

net_price = get_net_price(100, tax=0.08, discount=0.06)
print(net_price)