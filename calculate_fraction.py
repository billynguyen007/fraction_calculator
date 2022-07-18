from fractions import Fraction


def add(x, y):
    return Fraction(x) + Fraction(y)


def subtract(x, y):
    return Fraction(x) - Fraction(y)


def product(x, y):
    return Fraction(x) * Fraction(y)


def divide(x, y):
    return Fraction(x) / Fraction(y)


def mixed_to_improper_fraction(ip_fraction):
    x = ip_fraction[:ip_fraction.find("_")]
    y = ip_fraction[ip_fraction.find("_") + 1:ip_fraction.find("/")]
    z = ip_fraction[ip_fraction.find("/") + 1:]
    num = int(x) * int(z) + int(y)
    den = int(z)
    return Fraction(num, den)


def improper_fraction_to_mixed(num, den):
    return "{0}_{1}/{2}".format(str(num // den), str(num % den), str(den))


input_fraction = input("Input an equation containing fractions : \n")
input_fraction = input_fraction.replace(" ", "")
operators_list = ["+", "-", "*", "/"]
op = []
for i in range(len(input_fraction)):
    if input_fraction[i] in operators_list:
        op.append(input_fraction[i])

operation = op[1]
first_frac = input_fraction[:input_fraction.find(operation)]
second_frac = input_fraction[input_fraction.find(operation) + 1:]

if operation == "/":
    first_frac = input_fraction[:input_fraction.index("/", input_fraction.find("/") + 1)]
    second_frac = input_fraction[input_fraction.index("/", input_fraction.find("/") + 1) + 1:]

if first_frac.find("_") != -1:
    first_frac = mixed_to_improper_fraction(first_frac)

if second_frac.find("_") != -1:
    second_frac = mixed_to_improper_fraction(second_frac)

if operation == "+":
    result = add(first_frac, second_frac)

elif operation == "*":
    result = (product(first_frac, second_frac))

elif operation == "-":
    result = (subtract(first_frac, second_frac))

else:
    result = (divide(first_frac, second_frac))

if result.numerator > result.denominator:
    print("= " + improper_fraction_to_mixed(int(result.numerator), int(result.denominator)))
else:
    print("= " + str(result))