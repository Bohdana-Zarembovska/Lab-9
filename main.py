import random
import string
import datetime
import pytz
from sympy import symbols, Eq, solve

def generate_addition(difficulty="easy"):
    if difficulty == "easy":
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
    elif difficulty == "medium":
        num1 = random.randint(50, 200)
        num2 = random.randint(50, 200)
    else:
        num1 = random.randint(200, 500)
        num2 = random.randint(200, 500)
    return f"{num1} + {num2} = ?", num1 + num2

def generate_subtraction(difficulty="easy"):
    if difficulty == "easy":
        num1 = random.randint(10, 50)
        num2 = random.randint(1, num1)
    elif difficulty == "medium":
        num1 = random.randint(50, 150)
        num2 = random.randint(1, num1)
    else:
        num1 = random.randint(100, 500)
        num2 = random.randint(1, num1)
    return f"{num1} - {num2} = ?", num1 - num2

def generate_multiplication(difficulty="easy"):
    if difficulty == "easy":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif difficulty == "medium":
        num1 = random.randint(10, 20)
        num2 = random.randint(10, 20)
    else:
        num1 = random.randint(20, 50)
        num2 = random.randint(20, 50)
    return f"{num1} * {num2} = ?", num1 * num2

def generate_division(difficulty="easy"):
    if difficulty == "easy":
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 5)
    elif difficulty == "medium":
        num1 = random.randint(20, 100)
        num2 = random.randint(5, 20)
    else:
        num1 = random.randint(100, 500)
        num2 = random.randint(20, 50)
    return f"{num1} / {num2} = ?", round(num1 / num2, 2)

def generate_equation(difficulty="easy"):
    x = symbols('x')
    if difficulty == "easy":
        eq = Eq(random.randint(1, 10) * x + random.randint(1, 10), random.randint(10, 20))
    elif difficulty == "medium":
        eq = Eq(random.randint(1, 20) * x + random.randint(10, 20), random.randint(20, 50))
    else:
        eq = Eq(random.randint(10, 50) * x + random.randint(20, 30), random.randint(50, 100))
    solution = solve(eq, x)
    return f"Розв'яжіть рівняння: {eq}", float(solution[0])

def generate_proportion(difficulty="easy"):
    if difficulty == "easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
        c = random.randint(1, 10)
    elif difficulty == "medium":
        a, b = random.randint(10, 50), random.randint(10, 50)
        c = random.randint(10, 50)
    else:
        a, b = random.randint(50, 200), random.randint(50, 200)
        c = random.randint(50, 200)
    x = symbols('x')
    eq = Eq(a / b, x / c)
    solution = solve(eq, x)
    return f"Знайдіть x у пропорції: {a}/{b} = x/{c}", float(solution[0])

def generate_time_problem(difficulty="easy"):
    if difficulty == "easy":
        hours = random.randint(1, 12)
        minutes = random.randint(1, 59)
        time = datetime.time(hours, minutes)
    elif difficulty == "medium":
        hours = random.randint(1, 23)
        minutes = random.randint(1, 59)
        time = datetime.time(hours, minutes)
    else:
        tz = pytz.timezone('Europe/Kyiv')
        now = datetime.datetime.now(tz)
        hours = random.randint(0, 23)
        minutes = random.randint(0, 59)
        time = datetime.time(hours, minutes)
        time = now.replace(hour=hours, minute=minutes, second=0, microsecond=0)
    return f"Поточний час: {time}"

def generate_test(num_questions=10, difficulty="easy"):
    questions = []
    for _ in range(num_questions):
        problem_type = random.choice([
            'addition', 'subtraction', 'multiplication', 'division', 
            'equation', 'proportion', 'time_problem'
        ])

        if problem_type == 'addition':
            question, answer = generate_addition(difficulty)
        elif problem_type == 'subtraction':
            question, answer = generate_subtraction(difficulty)
        elif problem_type == 'multiplication':
            question, answer = generate_multiplication(difficulty)
        elif problem_type == 'division':
            question, answer = generate_division(difficulty)
        elif problem_type == 'equation':
            question, answer = generate_equation(difficulty)
        elif problem_type == 'proportion':
            question, answer = generate_proportion(difficulty)
        elif problem_type == 'time_problem':
            question = generate_time_problem(difficulty)
            answer = "Вказано вище"

        questions.append((question, answer))

    return questions

def print_test(questions):
    for i, (question, answer) in enumerate(questions, 1):
        print(f"Задача {i}: {question}")
        print(f"Правильна відповідь: {answer}\n")

num_questions = 10
difficulty = "easy"
test = generate_test(num_questions, difficulty)

print("Контрольна робота:")
print_test(test)
