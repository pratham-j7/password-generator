"""Command-line interface for the password generator."""

from generator import PasswordGenerator, InvalidPasswordSettingsError


def ask_yes_no(question):
    """Keep asking until the user answers y or n."""
    while True:
        answer = input(f"{question} (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type y or n.")


def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Password length: "))
    except ValueError:
        print("Error: please enter a valid whole number.")
        return

    use_upper = ask_yes_no("Include uppercase letters?")
    use_digits = ask_yes_no("Include digits?")
    use_symbols = ask_yes_no("Include symbols?")

    generator = PasswordGenerator(
        length=length,
        use_upper=use_upper,
        use_digits=use_digits,
        use_symbols=use_symbols,
    )

    try:
        password = generator.generate()
    except InvalidPasswordSettingsError as error:
        print(f"Error: {error}")
        return

    print(f"\nYour password: {password}")


if __name__ == "__main__":
    main()
