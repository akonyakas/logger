# Logger System

## Description

This project implements a logging system in Python. The system allows logging messages with timestamps, ensuring that each unique message can only be logged once every 10 seconds. The system can be cleaned when not processing messages, and has a maximum capacity of 100 messages.

## Features

- **Logging Messages**: Each unique message can only be logged once every 10 seconds.
- **Cleaning System**: The system can be cleaned at a given timestamp if it's not processing messages.
- **Capacity Management**: The logger holds a maximum of 100 unique messages.

## Usage

### Prerequisites

- Python 3.x

### Installation

Clone the repository:

```sh
git clone https://github.com/akonyakas/logger.git
cd logger
```

### Running the Code

#### Command Line Interface

Run the main application:

```sh
python app.py
```

#### Testing

Run the test script to ensure everything works as expected:

```sh
python test.py
```

## Files

- `logger.py`: Contains the `Logger` class with methods to log messages, clean the system, and get the current logger size.
- `test.py`: Script for testing the `Logger` class.
- `app.py`: Command line interface for interacting with the logger system.

## Logger Class

### Methods

- **`shouldPrintMessage(timestamp: int, message: str) -> bool`**: Checks if a message can be logged at a given timestamp.
- **`clean(timestamp: int) -> bool`**: Cleans the system if no messages are being processed.
- **`loggerSize() -> int`**: Returns the current size of the logger.

## Test

```python
from logger import Logger

logger = Logger()

assert logger.shouldPrintMessage(1, "foo") == True
assert logger.shouldPrintMessage(2, "bar") == True
assert logger.shouldPrintMessage(3, "foo") == False
assert logger.shouldPrintMessage(8, "bar") == False
assert logger.shouldPrintMessage(10, "foo") == False
assert logger.shouldPrintMessage(11, "foo") == True

assert logger.loggerSize() == 2
assert logger.clean(11) == False
assert logger.clean(12) == True
```
