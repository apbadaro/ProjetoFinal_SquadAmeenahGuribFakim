import random

# Código criado para gerar um telefone (11) aleatório e facilitar a criação do BD


def random_phone_number():
    area_code = "11"
    first_part = "".join(str(random.randint(0, 9)) for _ in range(4))
    second_part = "".join(str(random.randint(0, 9)) for _ in range(4))
    phone_number = f"({area_code}) {first_part}-{second_part}"
    return phone_number


random_number = random_phone_number()
print(random_number)
