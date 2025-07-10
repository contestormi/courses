x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 6, 8, 10]

w = 0
b = 0
learning_rate = 0.01
epochs = 1000

n = len(x_data)

for epoch in range(epochs):
    y_pred = [w * x + b for x in x_data]
    error = [y_p - y_t for y_p, y_t in zip(y_pred, y_data)]

    dw = sum(e * x for e, x in zip(error, x_data)) / n
    db = sum(error) / n

    w -= learning_rate * dw
    b -= learning_rate * db

    if epoch % 100 == 0:
        loss = sum(e**2 for e in error) / n
        print(f"Epoch {epoch}: w = {w:.4f}, b = {b:.4f}, loss = {loss:.4f}")

print(f"\nИтоговая модель: y = {w:.4f} * x + {b:.4f}")
