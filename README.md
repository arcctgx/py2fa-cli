# py2fa

Calculates one-time passwords for two-factor authentication:

```sh
./py2fa.py pypi.org
One-time password: 123456 (valid for 13.7 seconds)
```

## Installation

Just copy `py2fa.py` somewhere to your `PATH`.

## Dependencies

* `pyotp`
* `pyxdg`

## Configuration

Secrets are stored in user's XDG configuration directory as `py2fa/secrets.json`.
The file must not be world-accessible (readable, writable or executable): in
such case `py2fa` will refuse to load it.

The secrets file contains a simple dictionary, e.g.:

```json
{
    "pypi.org": "MYPYPITOTPSECRET",
    "test.pypi.org": "MYTESTPYPITOTPSECRET"
}
```
