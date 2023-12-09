import random

def MultiplicationTable():
    print("Добро пожаловать в Тренажер Умножения!")
    rightAnswers = 0

    for _ in range(10):
        # Генерация двух случайных чисел от 2 до 9
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)

        # Вычисление правильного ответа
        rightAnswer = num1 * num2

        # Вопрос пользователю
        question = f"Сколько будет {num1} * {num2}? "
        userAnswer = int(input(question))

        # Проверка ответа
        if userAnswer == rightAnswer:
            print("Правильно! Молодец!")
            rightAnswers += 1
        else:
            print(f"Неправильно. Правильный ответ: {rightAnswer}")

    print(f"\nТренировка завершена. Вы дали {rightAnswers} правильных ответов из 10.")

# Запуск тренажера
MultiplicationTable()