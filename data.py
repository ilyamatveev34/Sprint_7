class Data:
    valid_login = 'Ilya1990'
    valid_password = '1234'
    valid_firstname = 'Ilya'
    valid_courier_data = {'login': 'Ilya1990', 'password': '1234', 'firstName': 'Ilya'}
    courier_data_without_name = {'login': 'Ilya1990', 'password': '1234'}
    courier_data_with_wrong_password = {'login': 'Ilya1990', 'password': '123456'}


class OrderData:

    order_data_grey_1 = {
        'firstName': 'Иван',
        'lastName': 'Иванов',
        'address': 'Кошурникова, 7',
        'metroStation': 5,
        'phone': '+77777777777',
        'rentTime': 5,
        'deliveryDate': '2024-08-03',
        'comment': 'быстрее',
        'color': [
            'GREY'
        ]
    }

    order_data_black_2 = {
        'firstName': 'Петр',
        'lastName': 'Петров',
        'address': 'Ленина, 10',
        'metroStation': 6,
        'phone': '+78888888888',
        'rentTime': 4,
        'deliveryDate': '2024-08-03',
        'comment': 'быстрее',
        'color': [
            'BLACK'
        ]
    }

    order_data_two_colors_3 = {
        'firstName': 'Павел',
        'lastName': 'Павлов',
        'address': 'Арбат, 1',
        'metroStation': 3,
        'phone': '+79999999999',
        'rentTime': 9,
        'deliveryDate': '2024-08-03',
        'comment': 'быстрее',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    order_data_no_colors_4 = {
        'firstName': 'Сергей',
        'lastName': 'Сергеев',
        'address': 'Шаболовка, 10',
        'metroStation': 20,
        'phone': '+76666666666',
        'rentTime': 2,
        'deliveryDate': '2024-08-03',
        'comment': 'быстрее',
        'color': []
    }