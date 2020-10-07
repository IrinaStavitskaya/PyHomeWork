def dates(name, surname, year_of_birth, city_of_residence, email, phone_number):
    return ['name:' + name, 'surname:' + surname,
            'year_of_birth:' + year_of_birth,
            'city_of_residence:' + city_of_residence,
            'email:' + email, 'phone_number:' + phone_number]


your_name = input('Введите имя')
your_surname = input('Введите фамилию')
your_year_of_birth = input('Введите год рождения')
your_city_of_residence = input('Введите город проживания')
your_email = input('Введите email')
your_phone_number = input('Введите номер телефона')
print(dates(name=your_name, surname=your_surname, year_of_birth=your_year_of_birth,
            city_of_residence=your_city_of_residence, email=your_email, phone_number=your_phone_number))
