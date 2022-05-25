a = 3.0
b = -5.0
c = 1.0

delta = b ** 2 - 4 * a * c

print(delta)

x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 *a)

print(f"SUAS RAÍZES SÃO: {x1:.2f} E {x2:.2f}")
