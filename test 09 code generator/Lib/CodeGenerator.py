import random
from datetime import date


class CodeGenerator:
    def __init__(self):
        self.country_codes = {
            "united states": "US",
            "canada": "CA",
            "united kingdom": "UK",
            "australia": "AU",
            "germany": "DE"
        }

    # Generate a random code with the given length
    def generate_random_code(self, length=16):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(characters) for _ in range(length))

    # Generate a code from the current date and time
    def generate_code_from_date(self):
        now = date.today()
        code = now.strftime("%y%m%d")
        return code

    # Generate a code with country prefix and current date and time
    def generate_code_with_country_prefix(self, country):
        country_code = self.country_codes.get(country.lower(), '')
        if not country_code:
            raise ValueError("Invalid country")
        code = self.generate_random_code(16)
        date_code = self.generate_code_from_date()
        return f"{country_code}-{code}-{date_code}"