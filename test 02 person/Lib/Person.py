import datetime


class Person:
    def allowed_to_buy_alcohol(self, birthday, alcohol_percentage):
        # age 16-18: < 16.5%
        # age 18 and over: > 16.5%
        age = self.calculate_age(birthday)
        return age >= 18 and alcohol_percentage > 16.5

    def allowed_to_buy_tobacco(self, birthday):
        # age 18 and over
        age = self.calculate_age(birthday)
        return age >= 18

    def calculate_age(self, birthday):
        today = datetime.date.today()
        birthdate = datetime.datetime.strptime(birthday, '%Y-%m-%d').date()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age