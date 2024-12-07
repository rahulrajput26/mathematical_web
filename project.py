import streamlit as st

# Helper functions
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(num):
    factors = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1
    return factors

def primes_below(n):
    return [i for i in range(2, n) if is_prime(i)]

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return [root]
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return [root1, root2]

def solve_linear(a, b):
    if a == 0:
        return "No solution" if b != 0 else "Infinite solutions"
    return -b / a

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def permutation(n, r):
    return factorial(n) // factorial(n - r)

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def binary_to_decimal(binary):
    decimal = 0
    for index, bit in enumerate(reversed(str(binary))):
        decimal += int(bit) * (2 ** index)
    return decimal

# Streamlit app
st.title("Mathematical Operations")

option = st.sidebar.selectbox(
    "Choose an operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Prime Factors",
        "Primes Below a Number",
        "Check Prime Number",
        "Solve Quadratic Equation",
        "Solve Linear Equation",
        "Permutation",
        "Combination",
        "Binary to Decimal",
    ],
)

if option == "Addition":
    a = st.number_input("Enter first number")
    b = st.number_input("Enter second number")
    st.write(f"Result: {a + b}")

elif option == "Subtraction":
    a = st.number_input("Enter first number")
    b = st.number_input("Enter second number")
    st.write(f"Result: {a - b}")

elif option == "Multiplication":
    a = st.number_input("Enter first number")
    b = st.number_input("Enter second number")
    st.write(f"Result: {a * b}")

elif option == "Division":
    a = st.number_input("Enter numerator")
    b = st.number_input("Enter denominator")
    st.write(f"Result: {a / b if b != 0 else 'Division by zero is not allowed'}")

elif option == "Prime Factors":
    n = st.number_input("Enter a number", min_value=1, step=1)
    st.write(f"Prime factors: {prime_factors(int(n))}")

elif option == "Primes Below a Number":
    n = st.number_input("Enter a number", min_value=2, step=1)
    st.write(f"Primes below {n}: {primes_below(int(n))}")

elif option == "Check Prime Number":
    n = st.number_input("Enter a number", min_value=0, step=1)
    st.write(f"{n} is {'a prime number' if is_prime(int(n)) else 'not a prime number'}")

elif option == "Solve Quadratic Equation":
    st.write("Enter coefficients for ax² + bx + c = 0")
    a = st.number_input("a",value=1.0,step=0.5)
    b = st.number_input("b",step=0.5)
    c = st.number_input("c",step=0.5)
    if a==0 :
        st.error("--'a' can not be equal to 0")
    else:
        st.write(f"Solutions: {solve_quadratic(a, b, c)}")

elif option == "Solve Linear Equation":
    st.write("Enter coefficients for ax + b = 0")
    a = st.number_input("a")
    b = st.number_input("b")
    st.write(f"Solution: {solve_linear(a, b)}")

elif option == "Permutation":
    n = st.number_input("Enter n", min_value=0, step=1)
    r = st.number_input("Enter r", min_value=0, step=1)
    st.write(f"P({n}, {r}) = {permutation(int(n), int(r))}")

elif option == "Combination":
    n = st.number_input("Enter n", min_value=0, step=1)
    r = st.number_input("Enter r", min_value=0, step=1)
    st.write(f"C({n}, {r}) = {combination(int(n), int(r))}")

elif option == "Binary to Decimal":
    binary = st.text_input("Enter a binary number")
    if binary.isdigit() and all(c in '01' for c in binary):
        st.write(f"Decimal: {binary_to_decimal(binary)}")
    else:
        st.write("Please enter a valid binary number")