# import tkinter as tk

# # Calculator logic
# class Calculator:
#     def _init_(self):
#         self.reset()

#     def reset(self):
#         self.numbers = []
#         self.current_number = ""
#         self.operation = None

#     def load_number(self):
#         if self.current_number:
#             self.numbers.append(int(self.current_number))
#             self.current_number = ""  # Reset current number after loading

#     def add_digit(self, digit):
#         self.current_number += str(digit)

#     def set_operation(self, operation):
#         if self.current_number:  # Load the current number before setting operation
#             self.load_number()
#         self.operation = operation

#     def calculate(self):
#         if not self.current_number:  # Ensure last number is loaded
#             self.load_number()
#         if self.operation == 'ADD':
#             return self.add()
#         elif self.operation == 'SUBS':
#             return self.subs()
#         elif self.operation == 'MULT':
#             return self.mult()
#         elif self.operation == 'DIV':
#             return self.div()
#         else:
#             return "Error: Invalid operation"

#     # Arithmetic operations
#     def add(self):
#         return sum(self.numbers)

#     def subs(self):
#         return self.numbers[0] - sum(self.numbers[1:])

#     def mult(self):
#         result = 1
#         for num in self.numbers:
#             result *= num
#         return result

#     def div(self):
#         try:
#             result = self.numbers[0]
#             for num in self.numbers[1:]:
#                 result /= num
#             return result
#         except ZeroDivisionError:
#             return "Error: Division by zero"

# # GUI
# class CalculatorApp:
#     def _init_(self, root):
#         self.calculator = Calculator()
#         self.root = root
#         self.root.title("Calculator Simulation")

#         # Entry widget to display numbers and operations
#         self.entry = tk.Entry(root, width=40, borderwidth=5)
#         self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#         # Button definitions for operations
#         self.buttons = {
#             'LOAD': (1, 4, self.load),
#             'ADD': (2, 4, lambda: self.set_operation('ADD')),
#             'SUBS': (3, 4, lambda: self.set_operation('SUBS')),
#             'MULT': (4, 4, lambda: self.set_operation('MULT')),
#             'DIV': (5, 4, lambda: self.set_operation('DIV')),
#             'OUT': (6, 4, self.output_result),
#         }

#         # Numeric buttons
#         self.create_numeric_buttons()

#         # Operation buttons
#         for btn_text, (row, col, command) in self.buttons.items():
#             tk.Button(root, text=btn_text, width=10, height=2, command=command).grid(row=row, column=col)

#     def create_numeric_buttons(self):
#         numbers = list(range(9, -1, -1))  # 9 to 0
#         row_base, col_base = 1, 0  # Starting grid position for numeric buttons
#         for i, number in enumerate(numbers):
#             tk.Button(self.root, text=str(number), width=10, height=2, command=lambda n=number: self.add_digit(n)).grid(row=row_base + (i // 3), column=col_base + (i % 3))

#     def add_digit(self, digit):
#         self.calculator.add_digit(digit)
#         self.entry.insert(tk.END, str(digit))

#     def load(self):
#         self.calculator.load_number()
#         self.entry.delete(0, tk.END)

#     def set_operation(self, operation):
#         self.calculator.set_operation(operation)
#         self.entry.delete(0, tk.END)
#         self.entry.insert(0, operation)

#     def output_result(self):
#         result = self.calculator.calculate()
#         self.entry.delete(0, tk.END)
#         self.entry.insert(0, str(result))
#         self.calculator.reset()

# # Main application
# if __name__ == "_main_":
#     root = tk.Tk()
#     app = CalculatorApp(root)
#     root.mainloop()

import tkinter as tk

# Calculator logic
class Calculator:
    def __init__(self):
        self.reset()

    def reset(self):
        self.numbers = []
        self.current_number = ""
        self.operation = None

    def load_number(self):
        if self.current_number:
            self.numbers.append(int(self.current_number))
            self.current_number = ""  # Reset current number after loading

    def add_digit(self, digit):
        self.current_number += str(digit)

    def set_operation(self, operation):
        if self.current_number:  # Load the current number before setting operation
            self.load_number()
        self.operation = operation

    def calculate(self):
        if not self.current_number:  # Ensure last number is loaded
            self.load_number()
        if self.operation == 'ADD':
            return self.add()
        elif self.operation == 'SUBS':
            return self.subs()
        elif self.operation == 'MULT':
            return self.mult()
        elif self.operation == 'DIV':
            return self.div()
        else:
            return "Error: Invalid operation"

    def add(self):
        return sum(self.numbers)

    def subs(self):
        return self.numbers[0] - sum(self.numbers[1:])

    def mult(self):
        result = 1
        for num in self.numbers:
            result *= num
        return result

    def div(self):
        try:
            result = self.numbers[0]
            for num in self.numbers[1:]:
                result /= num
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"

# GUI
class CalculatorApp:
    def __init__(self, root):
        self.calculator = Calculator()
        self.root = root
        self.root.title("Pretty Calculator")

        # Styling
        button_params = {
            'padx': 20,
            'pady': 10,
            'bd': 4,
            'fg': "white",
            'bg': "#333333",
            'font': ('Arial', 12, 'bold')
        }

        # Entry widget to display numbers and operations
        self.entry = tk.Entry(root, font=('Arial', 18), borderwidth=5, relief=tk.RIDGE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

        # Numeric buttons
        self.create_numeric_buttons(button_params)

        # Operation buttons
        self.buttons = {
            'LOAD': (1, 4, self.load, '#FF5733'),
            'ADD': (2, 4, lambda: self.set_operation('ADD'), '#FFC300'),
            'SUBS': (3, 4, lambda: self.set_operation('SUBS'), '#FFC300'),
            'MULT': (4, 4, lambda: self.set_operation('MULT'), '#FFC300'),
            'DIV': (5, 4, lambda: self.set_operation('DIV'), '#FFC300'),
            'OUT': (6, 4, self.output_result, '#DAF7A6'),
        }

        # Creating operation buttons with style
        for btn_text, (row, col, command, color) in self.buttons.items():
            tk.Button(root, text=btn_text, width=10, height=2, command=command, bg=color, fg="white", font=('Arial', 10, 'bold')).grid(row=row, column=col, pady=5, padx=5)

        root.grid_columnconfigure((0, 1, 2, 3), weight=1)

    def create_numeric_buttons(self, params):
        numbers = list(range(9, -1, -1))  # 9 to 0
        row_base, col_base = 1, 0  # Starting grid position for numeric buttons
        for i, number in enumerate(numbers):
            button = tk.Button(self.root, text=str(number), width=5, height=2, command=lambda n=number: self.add_digit(n), **params)
            button.grid(row=row_base + (i // 3), column=col_base + (i % 3), sticky="nsew", padx=5, pady=5)

    def add_digit(self, digit):
        self.calculator.add_digit(digit)
        self.entry.insert(tk.END, str(digit))

    def load(self):
        self.calculator.load_number()
        self.entry.delete(0, tk.END)

    def set_operation(self, operation):
        self.calculator.set_operation(operation)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, operation)

    def output_result(self):
        result = self.calculator.calculate()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(result))
        self.calculator.reset()

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
