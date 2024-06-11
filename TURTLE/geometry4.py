import turtle

class FibonacciGenerator:
    def __init__(self):
        self.fib_sequence = [0, 1]

    def generate_sequence(self, n):
        while len(self.fib_sequence) < n:
            next_fib = self.fib_sequence[-1] + self.fib_sequence[-2]
            self.fib_sequence.append(next_fib)

    def get_sequence(self):
        return self.fib_sequence

def draw_fibonacci_circles(fibonacci_sequence):
    turtle.speed(200)
    turtle.pensize(2)

    for fib_number in fibonacci_sequence:
        turtle.circle(fib_number * 40
                      ) # Adjust the multiplier for better visualization
        turtle.left(10)

    turtle.done()

# Example: Generate the first 10 Fibonacci numbers and visualize with turtle circles
fibonacci_generator = FibonacciGenerator()
fibonacci_generator.generate_sequence(10)
fibonacci_sequence = fibonacci_generator.get_sequence()

draw_fibonacci_circles(fibonacci_sequence)
