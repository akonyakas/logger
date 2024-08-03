from logger import Logger

logger = Logger()

assert logger.shouldPrintMessage(1, "foo") == True  # next allowed timestamp for "foo" is 1 + 10 = 11
assert logger.shouldPrintMessage(2, "bar") == True  # next allowed timestamp for "bar" is 2 + 10 = 12

assert logger.shouldPrintMessage(3, "foo") == False  # 3 < 11
assert logger.shouldPrintMessage(8, "bar") == False  # 8 < 12
assert logger.shouldPrintMessage(10, "foo") == False # 10 < 11
assert logger.shouldPrintMessage(11, "foo") == True  # 11 >= 11, next allowed timestamp for "foo" is 11 + 10 = 21

assert logger.loggerSize() == 2  # in logger you have: foo, bar
assert logger.clean(11) == False # message "bar" would be printed in this timestamp
assert logger.clean(12) == True  # in timestamp 12 there is no messages in stream

print("Passed all tests!")