import cmd
import os
from pystyle import Colors, Colorate

os.system("title recon.exe")

class MyCLI(cmd.Cmd):
    intro = Colorate.Horizontal(Colors.red_to_purple, "RECON v1. Type help or ? to list commands.\n")
    prompt = Colorate.Horizontal(Colors.cyan_to_blue, "recon$ ")

    def do_greet(self, line):
        "Greet the user"
        greeting = Colorate.Horizontal(Colors.green_to_white, f"Hello, {line}!")
        print(greeting)

    def do_exit(self, line):
        "Exit the command line interface"
        print(Colorate.Horizontal(Colors.red_to_purple, "Goodbye!"))
        return True

    def do_echo(self, line):
        "Echo back the input"
        echo = Colorate.Horizontal(Colors.yellow_to_red, line)
        print(echo)

    def do_clear(self, line):
        "Clear the screen"
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Horizontal(Colors.cyan_to_blue, "Screen cleared."))

    def do_pwd(self, line):
        "Print the current working directory"
        cwd = os.getcwd()
        print(Colorate.Horizontal(Colors.green_to_white, f"Current working directory: {cwd}"))

    def do_ls(self, line):
        "List files in the current directory"
        files = os.listdir('.')
        files_str = '\n'.join(files)
        print(Colorate.Horizontal(Colors.yellow_to_red, f"Files in current directory:\n{files_str}"))

    def do_cd(self, line):
        "Change the current directory"
        try:
            os.chdir(line)
            print(Colorate.Horizontal(Colors.green_to_white, f"Changed directory to {os.getcwd()}"))
        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_purple, f"Error: {str(e)}"))

    def do_mkdir(self, line):
        "Create a new directory"
        try:
            os.makedirs(line, exist_ok=True)
            print(Colorate.Horizontal(Colors.green_to_white, f"Directory '{line}' created"))
        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_purple, f"Error: {str(e)}"))

    def do_rmdir(self, line):
        "Remove a directory"
        try:
            os.rmdir(line)
            print(Colorate.Horizontal(Colors.green_to_white, f"Directory '{line}' removed"))
        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_purple, f"Error: {str(e)}"))

    def do_cat(self, line):
        "Display the content of a file"
        try:
            with open(line, 'r') as file:
                content = file.read()
            print(Colorate.Horizontal(Colors.yellow_to_red, content))
        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_purple, f"Error: {str(e)}"))

    def do_help(self, line):
        "Display help for commands"
        help_text = """
        Available commands:
        - greet [name]: Greet the user
        - exit: Exit the command line interface
        - echo [text]: Echo back the input
        - clear: Clear the screen
        - pwd: Print the current working directory
        - ls: List files in the current directory
        - cd [path]: Change the current directory
        - mkdir [dirname]: Create a new directory
        - rmdir [dirname]: Remove a directory
        - cat [filename]: Display the content of a file
        - help: Display this help message
        """
        print(Colorate.Horizontal(Colors.cyan_to_blue, help_text))

if __name__ == '__main__':
    cli = MyCLI()
    cli.cmdloop()
