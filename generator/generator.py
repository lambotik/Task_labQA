from faker import Faker

from data.data import Person
from pathlib import Path

RANDOM_FILE = Path(__file__).parent


faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()


# Генерирует произвольные фейковые данные
def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )