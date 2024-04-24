import tkinter as tk
#dilyara_shaimerden
def increment_counter():
    global counter
    counter += 1
    label.config(text="Счетчик: " + str(counter))

def decrement_counter():
    global counter
    counter -= 1
    label.config(text="Счетчик: " + str(counter))

counter = 0

root = tk.Tk()
root.title("Реактивный счетчик")

label = tk.Label(root, text="Счетчик: " + str(counter))
label.pack(pady=10)

increment_button = tk.Button(root, text="Увеличить", command=increment_counter)
increment_button.pack(side=tk.LEFT, padx=10)

decrement_button = tk.Button(root, text="Уменьшить", command=decrement_counter)
decrement_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()

def lazy_prime_generator():
    primes = []  # список для хранения простых чисел
    num = 2  # начинаем с первого простого числа

    while True:
        is_prime = True
        for prime in primes:
            if num % prime == 0:  # проверяем, делится ли число на какое-либо из простых чисел
                is_prime = False
                break

        if is_prime:
            yield num  # если число простое, возвращаем его через генератор
            primes.append(num)  # добавляем простое число в список простых чисел

        num += 1  # переходим к следующему числу для проверки

# Пример использования:
prime_gen = lazy_prime_generator()
for _ in range(10):
    print(next(prime_gen))
