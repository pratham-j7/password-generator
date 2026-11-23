"""Password generator logic: a custom error and the PasswordGenerator class."""

import secrets
import string


class InvalidPasswordSettingsError(Exception):
    """Raised when the settings can't produce a valid password."""


class PasswordGenerator:
    MIN_LENGTH = 4
    MAX_LENGTH = 128

    def __init__(self, length=12, use_upper=True, use_digits=True, use_symbols=True):
        self.length = length
        self.use_upper = use_upper
        self.use_digits = use_digits
        self.use_symbols = use_symbols

    def _build_groups(self):
        """Return a list of character groups the password must draw from."""
        groups = [string.ascii_lowercase]
        if self.use_upper:
            groups.append(string.ascii_uppercase)
        if self.use_digits:
            groups.append(string.digits)
        if self.use_symbols:
            groups.append(string.punctuation)
        return groups

    def generate(self):
        """Generate one password using the current settings."""
        if not isinstance(self.length, int):
            raise InvalidPasswordSettingsError("Length must be a whole number.")
        if self.length < self.MIN_LENGTH or self.length > self.MAX_LENGTH:
            raise InvalidPasswordSettingsError(
                f"Length must be between {self.MIN_LENGTH} and {self.MAX_LENGTH}."
            )

        groups = self._build_groups()

        # Guarantee at least one character from every selected group
        password = [secrets.choice(group) for group in groups]

        # Fill the rest from the combined pool
        pool = "".join(groups)
        remaining = self.length - len(password)
        password += [secrets.choice(pool) for _ in range(remaining)]

        # Shuffle so the guaranteed characters aren't always at the start
        secrets.SystemRandom().shuffle(password)
        return "".join(password)
