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
