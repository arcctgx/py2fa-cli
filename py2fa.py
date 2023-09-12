#!/usr/bin/env python3
"""Calculate one-time passwords for two-factor authentication."""

import json
import os
import sys
from time import time

import pyotp
from xdg import BaseDirectory


def _get_config():
    cfg_path = BaseDirectory.load_first_config('py2fa/config.json')

    with open(cfg_path, encoding='utf-8') as cfg:
        secrets = json.load(cfg)

    return secrets


def main():
    if len(sys.argv) != 2:
        print(f'usage: {os.path.basename(sys.argv[0])} <secret_name>')
        sys.exit(0)

    secrets = _get_config()

    try:
        secret = secrets[sys.argv[1]]
    except KeyError:
        print(f'No secret for {sys.argv[1]} is available!')
        sys.exit(1)

    totp = pyotp.TOTP(secret)
    valid_for = 30.0 - time() % 30

    print(f'One-time password: {totp.now()} (valid for {valid_for:.1f} seconds)')


if __name__ == '__main__':
    main()
