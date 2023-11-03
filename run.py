import os, sys
try:
    __import__("Rudal").main()
except Exception as e:
    exit(str(e))
