
# if statement
age = input('Ingresa tu edad: ')
#if int(age) >= 18:
    #print("Puedes votar")
#else: 
    #print("No puedes votar")


your_age = int(age)

if your_age < 5:
    ticket_price= 5
elif your_age < 16:
    ticket_price= 10
else:
    ticket_price= 18

#print(f"Pagaras ${ticket_price} por el ticket")


num = int(input("Ingresa un numero "))

if num > 0:
    print("El numero es positivo")
elif num < 0:
    print("El numero es negativo")
else:
    print("El numero es 0")

#ternary operator

ticket_price = 20 if your_age > 18 else 5
print(f"El precio del ticket sera {ticket_price}")

puede_votar = True if your_age >= 18 else False
print("¿Puede votar? ", puede_votar)

es_par = "par" if num % 2 == 0 else "impar"
print("El número es", es_par)

#loop
for index in range(5):
    print(index + 1)

for index in range(0, 11, 2):
    print(index)

sum = 0
for num in range(101):
    sum += num

print(sum)

#While
max = 5
counter = 0
while counter < max:
    print(counter)
    counter += 1


command = ''
while command.lower() != 'quit':
    command = input('>')
    print(f"Echo: {command}")


numeros = []
while len(numeros) < 5:
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
print("Los números ingresados son:", numeros)
