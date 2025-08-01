letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))
# index                0   ,  1

print(f"Hey my name is {name} and I am from {country}")

# If you want the flower brackets
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# doesn't do anything since the txt string has no placeholders
print(txt.format())

print(type(f"{2 * 30}"))
print(f"{2*30}")
