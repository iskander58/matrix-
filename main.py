import time
import random
import sys

symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

try:
    while True:
        print("".join(random.choice(symbols) for _ in range(50)))
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
