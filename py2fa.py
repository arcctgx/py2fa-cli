#!/usr/bin/env python3

import os
import pyotp
import sys
from time import time

secret = os.getenv('MY_SECRET')
if secret is None:
    print("Failed to get MY_SECRET!")
    sys.exit(1)

totp = pyotp.TOTP(secret)
validFor = 30 - time()%30

print("One-time password: %s (valid for %.1f seconds)" % (totp.now(), validFor))
