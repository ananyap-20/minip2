import sys
import inspect
import traceback

class PyDebugger:
    def __init__(self):
        self.breakpoints = {}
        self.step_mode = False
        self.current_frame = None

    def set_trace(self):
        """Start the debugger"""
        frame = inspect.currentframe().f_back
        self.current_frame = frame
        self.debug_loop()

    def set_breakpoint(self, filename, lineno):
        """Set a breakpoint at the specified line in the given file"""
        if filename not in self.breakpoints:
            self.breakpoints[filename] = set()
        self.breakpoints[filename].add(lineno)

    def clear_breakpoint(self, filename, lineno):
        """Clear a breakpoint at the specified line in the given file"""
        if filename in self.breakpoints:
            self.breakpoints[filename].discard(lineno)

    def get_variable_info(self):
        """Get information about current variables in scope"""
        if self.current_frame:
            return self.current_frame.f_locals
        return {}

    def get_stack_trace(self):
        """Get the current stack trace"""
        if self.current_frame:
            return traceback.extract_stack(self.current_frame)
        return []

    def debug_loop(self):
        """Main debugging loop"""
        while self.current_frame:
            filename = self.current_frame.f_code.co_filename
            lineno = self.current_frame.f_lineno

            # Check if we hit a breakpoint
            if filename in self.breakpoints and lineno in self.breakpoints[filename]:
                print(f"Breakpoint hit at {filename}:{lineno}")
                self.print_current_line()
                self.handle_command()

            # Step mode
            if self.step_mode:
                self.print_current_line()
                self.handle_command()

            # Execute the next line
            self.current_frame = self.current_frame.f_back

    def print_current_line(self):
        """Print the current line being executed"""
        if self.current_frame:
            filename = self.current_frame.f_code.co_filename
            lineno = self.current_frame.f_lineno
            with open(filename, 'r') as f:
                lines = f.readlines()
                if 0 <= lineno - 1 < len(lines):
                    print(f"Line {lineno}: {lines[lineno-1].strip()}")

    def handle_command(self):
        """Handle debugging commands"""
        while True:
            cmd = input('(Pdb) ').strip().lower()
            if cmd == 'c' or cmd == 'continue':
                self.step_mode = False
                break
            elif cmd == 's' or cmd == 'step':
                self.step_mode = True
                break
            elif cmd == 'q' or cmd == 'quit':
                sys.exit(0)
            elif cmd == 'v' or cmd == 'variables':
                variables = self.get_variable_info()
                for name, value in variables.items():
                    print(f"{name} = {value}")
            elif cmd == 'w' or cmd == 'where':
                stack = self.get_stack_trace()
                for frame in stack:
                    print(f"{frame.filename}:{frame.lineno}")
            else:
                print("Available commands:")
                print("c/continue - Continue execution")
                print("s/step - Step to next line")
                print("v/variables - Show variables")
                print("w/where - Show stack trace")
                print("q/quit - Quit debugger")