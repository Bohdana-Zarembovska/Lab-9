import pytest

from main import (
    generate_addition,
    generate_subtraction,
    generate_multiplication,
    generate_division,
    generate_equation,
    generate_proportion,
    generate_time_problem,
    generate_test
)

def test_addition():
    question, answer = generate_addition(difficulty="easy")
    assert " + " in question
    assert isinstance(answer, int)

def test_subtraction():
    question, answer = generate_subtraction(difficulty="medium")
    assert " - " in question
    assert isinstance(answer, int)

def test_multiplication():
    question, answer = generate_multiplication(difficulty="hard")
    assert " * " in question
    assert isinstance(answer, int)

def test_division():
    question, answer = generate_division(difficulty="easy")
    assert " / " in question
    assert isinstance(answer, float)

def test_equation():
    question, answer = generate_equation(difficulty="medium")
    assert "x" in question
    assert isinstance(answer, (int, float))

def test_proportion():
    question, answer = generate_proportion(difficulty="hard")
    assert "=" in question
    assert isinstance(answer, float)

def test_time_problem():
    question = generate_time_problem(difficulty="easy")
    assert "Поточний час:" in question

def test_generate_test():
    test = generate_test(num_questions=5, difficulty="medium")
    assert len(test) == 5
    for question, answer in test:
        assert len(question) > 0
        assert isinstance(answer, (int, float, str))
