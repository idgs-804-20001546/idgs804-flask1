import datetime


def get_questions():
    return [
        {
            "id": 1,
            "question": "¿ Quien fue el autor de la Noche Estrellada ?",
            "responses": [
                (1, "Kenini"),
                (2, "Pablo Piccaso"),
                (3, "The Rock"),
                (4, "Bangod"),
            ],
            "correct": 4,
        },
        {
            "id": 2,
            "question": "¿ Qué país tiene la mayor economia del mundo ?",
            "responses": [
                (1, "México"),
                (2, "Russia"),
                (3, "U.S.A"),
                (4, "China"),
            ],
            "correct": 3,
        },
        {
            "id": 3,
            "question": "¿ Quién es el hombre más rico del mundo ?",
            "responses": [
                (1, "Elon Musk"),
                (2, "Jeff Bezos"),
                (3, "Zac Effron"),
                (4, "Henrry Cavil"),
            ],
            "correct": 1,
        },
        {
            "id": 4,
            "question": "¿ Cuál es el porcentaje de agua potable en el mundo ?",
            "responses": [
                (1, "3 %"),
                (2, "10 %"),
                (3, "0.007 %"),
                (4, "0 %"),
            ],
            "correct": 3,
        },
        {
            "id": 5,
            "question": "¿ Quién fue el protagostista principal masculino en 'Por que el amor manda' ?",
            "responses": [
                (1, "Sebastian Ruly"),
                (2, "Fernando Colunga"),
                (3, "Kendry Lamar"),
                (4, "AMLO BB"),
            ],
            "correct": 2,
        },
    ]


def calculate_age(birthdate):
    today = datetime.date.today()
    age = (
        today.year
        - birthdate.year
        - ((today.month, today.day) < (birthdate.month, birthdate.day))
    )
    return age


def get_zodiac(year, month, day):
    zodiac_table = [
        (120, "Mono"),
        (218, "Gallo"),
        (320, "Perro"),
        (420, "Cerdo"),
        (521, "Rata"),
        (621, "Buey"),
        (722, "Tigre"),
        (823, "Conejo"),
        (923, "Dragón"),
        (1023, "Serpiente"),
        (1122, "Caballo"),
        (1222, "Cabra"),
        (1231, "Mono"),
    ]

    # Calcular el signo zodiacal chino
    birth_date = datetime.datetime(year, month, day)
    zodiac_start = datetime.datetime(year, 1, 1)
    zodiac_offset = (birth_date - zodiac_start).days

    for start, zodiac in zodiac_table:
        if zodiac_offset < start:
            break
    return  zodiac
