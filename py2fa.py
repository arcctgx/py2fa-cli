#!/usr/bin/env python3
"""Calculate one-time passwords for two-factor authentication."""

import os
import sys
from time import time

import pyotp

secret = os.getenv('MY_SECRET')
if secret is None:
    print('Failed to get MY_SECRET!')
    sys.exit(1)

totp = pyotp.TOTP(secret)
valid_for = 30.0 - time() % 30

print(f'One-time password: {totp.now()} (valid for {valid_for:.1f} seconds)')
