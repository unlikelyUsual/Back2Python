# Python 101: A Step-by-Step Learning Journey

This repository contains a structured Python learning path organized by days, with each day covering different Python concepts. It's designed for beginners who want to learn Python programming from scratch.

## Project Structure

The project is organized into days, with each day covering specific Python concepts:

### Day 1: Python Basics

- **hello_world.py**: Introduction to printing, taking user input, and virtual environment setup
- **data_types.py**: Basic data types (int, float, str, bool), composite data types (list, tuple, set, dict), type parsing, string methods, and arithmetic operations
- **operator.py**: Logical operators (and, or, not) and their equivalents in other languages

### Day 2: Functions and Classes

- **def.py**: Function definitions with type hints for parameters and return values
- **class.py**: Class definitions, constructors, methods, string representation, and operator overloading
- **constants.py**: How to define constants in Python using the Final type hint

### Day 3: Control Flow

- **comparision.py**: Conditional statements using if-else

## Prerequisites

- Python 3.x installed on your system
- Basic understanding of programming concepts (helpful but not required)

## Setup Instructions

1. Clone this repository to your local machine
2. Navigate to the project directory

### Setting Up a Virtual Environment (Recommended)

To keep dependencies isolated from your global Python installation:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# .\venv\Scripts\activate

# Install dependencies (if any)
pip install -r requirements.txt
```

### Running the Examples

Navigate to the specific day's directory and run the Python files:

```bash
# Example: Running hello_world.py from Day 1
python day_1/hello_world.py
```

## Managing Dependencies

- To install dependencies from requirements.txt:

  ```bash
  pip install -r requirements.txt
  ```

- To update requirements.txt after installing new packages:
  ```bash
  pip freeze > requirements.txt
  ```

## Learning Path

This repository is designed to be followed in order, starting from Day 1 and progressing through the days as you become more comfortable with the concepts.

Each file contains examples and comments explaining the concepts, making it easy to follow along and learn at your own pace.

Feel free to experiment with the code and modify it to deepen your understanding of Python programming.
