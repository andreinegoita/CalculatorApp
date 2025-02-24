# :book: CalculatorAppPython

# :pushpin: About the Project

This application is a scientific calculator built using Kivy for the graphical interface and Python for processing mathematical expressions.
The calculator supports basic arithmetic operations, trigonometric, logarithmic, factorial functions, memory storage and an activateable scientific mode.


# :hammer_and_wrench: Functionalities
 1 :1234: Arithmetic operations:
          :heavy_check_mark: addition (+)
          :heavy_check_mark: subtraction (-)
          :heavy_check_mark: multiplication (*)
          :heavy_check_mark: division ( / )
 * :bar_chart: Scientific functions:
     `sin`
     `cos`
     `tan`
     `log`
     `ln`
     `exp`
     `abs`
     `factorial`
 * :arrow_up_down: Powers and Roots: Exponential and Radical.
 * Brackets for complex expressions.
 * :floppy_disk: Memory:
    M+ - Saves the current value to memory.
    MR - Recalls the value from memory.
    MC - Clear memory.
 *:bar_chart: Scientific mode: enable/disable advanced features.


# :books: Project Structure 
  * :file_folder: `calculator.kv` - GUI definition using Kivy Language.
  * :file_folder: `CalculatorUi.py` - Implementation of interface logic and button manipulation.
  * :file_folder: `MathProcessor.py` - Processing mathematical expressions, converting them and evaluating them.
  * :file_folder: `MemoryManager.py` - Computer memory management.
  *  :file_folder: `CalculatorApp.py` - Initializes and runs the application.
# :gear: Design and Arhitecture
The project is organized on MVC (Model-View-Controller) principles:
 * Model: MathProcessor.py - handles the processing of mathematical expressions.
 * View: calculator.kv - defines the graphical interface.
 - Controller: CalculatorUi.py - handles user interactions.
# :rocket: Installation and run the project
  1. Make sure you have the version of Python 3.13.2
  2. In the IDE run in the terminal (i used `Pycharm` for this project) run:
     * pip install kivy

# :desktop_computer: Technologies and Libraries used:
1. Python-the main language
2. Kivy-Framework for GUI
3. Re-library for processing the mathematical expressions
4. Math & Cmath- library which support for complex numbers
