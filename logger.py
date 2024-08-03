class Logger:
    def __init__(self):
        # Initialize a dictionary to store messages and their next allowed timestamps
        self.db: dict[str, int] = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.db:
            # Check if the logger has reached its capacity
            if self.loggerSize() >= 100:
                # Attempt to clean the db if capacity is reached
                if self.clean(timestamp):
                    # If cleaning succeeded, add the message with the next allowed timestamp
                    self.db[message] = timestamp + 10
                    return True
                else:
                    # If db is still full, message cannot be added
                    return False
            else:
                # If capacity is not reached, add the message with the next allowed timestamp
                self.db[message] = timestamp + 10
                return True
        elif self.db[message] <= timestamp:
            # If the message is in the db and the current timestamp is allowed, update the timestamp
            self.db[message] = timestamp + 10
            return True
        else:
            # If the message is in the db but the current timestamp is not allowed, return False
            return False

    def clean(self, timestamp: int) -> bool:
        # Remove messages whose next allowed timestamp is less than or equal to the current timestamp
        messages = list(self.db.keys())
        cleaned = False
        for message in messages:
            if self.db[message] <= timestamp:
                cleaned = True
                del self.db[message]
        return cleaned

    def loggerSize(self) -> int:
        # Return the number of messages in the db
        return len(self.db)