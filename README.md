# RECON v1

RECON is a simple command line interface (CLI) application built in Python. It provides a variety of commands for users to interact with the file system and execute tasks in a colorful and engaging manner.

## Features

- Greet the user
- Clear the screen
- Print the current working directory
- List files in the current directory
- Change directories
- Create and remove directories
- Display the contents of files
- Custom command support

## Installation

To install and run RECON, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/cashsoftworks/recon-cli
   cd recon
   ```

2. **Install the required dependencies:**

   Make sure you have Python installed on your system. You can install the required libraries using pip:

   ```bash
   pip install pystyle
   ```

3. **Run the application:**

   ```bash
   python recon.py
   ```

   You should see a colorful prompt ready for commands.

## Adding Custom Commands

You can easily extend the functionality of RECON by adding your own custom commands. Here's how to do it:

1. Open the `recon.py` file in your preferred text editor.

2. Define your custom command method inside the `MyCLI` class. For example:

   ```python
   def do_custom_command(self, line):
       "Description of what the command does"
       # Your command logic here
       print(Colorate.Horizontal(Colors.green_to_white, f"You executed: {line}"))
   ```

3. Add a help description for your command in the `do_help` method:

   ```python
   def do_help(self, line):
       "Display help for commands"
       help_text = """
       Available commands:
       ...
       - custom_command [arg]: Description of custom command
       """
       print(Colorate.Horizontal(Colors.cyan_to_blue, help_text))
   ```

4. Save the file and run the application again to see your new command in action!

## Usage

Once you have RECON running, you can use the following commands:

- `greet [name]`: Greet the user
- `exit`: Exit the command line interface
- `echo [text]`: Echo back the input
- `clear`: Clear the screen
- `pwd`: Print the current working directory
- `ls`: List files in the current directory
- `cd [path]`: Change the current directory
- `mkdir [dirname]`: Create a new directory
- `rmdir [dirname]`: Remove a directory
- `cat [filename]`: Display the content of a file
- `help`: Display this help message

## Contributing

Contributions are welcome! If you would like to contribute to RECON, please fork the repository and submit a pull request.

## License

This project is open-sourced under the MIT License. See the [LICENSE](LICENSE) file for details.
