from debugger import PyDebugger

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

def main():
    debugger = PyDebugger()
    # Set a breakpoint at the factorial calculation
    debugger.set_breakpoint(__file__, 11)
    
    try:
        # Start debugging
        debugger.set_trace()
        result = calculate_factorial(5)
        print(f"Factorial of 5 is: {result}")
        
        # This will raise an error
        result = calculate_factorial(-1)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()