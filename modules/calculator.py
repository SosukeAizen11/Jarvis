class Calculator:
    def calculate(self, expression):
        try:
            answer = eval(expression)
            print(f"Answer: {answer}")
        except:
            print("Invalid Expression")