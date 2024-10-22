class IncorrectVinNumber(Exception):
    def __init__(self, message="Некорректный VIN номер"):
        self.message = message
        super().__init__(self.message)

class IncorrectCarNumbers(Exception):
    def __init__(self, message="Неверный номер автомобиля"):
        self.message = message
        super().__init__(self.message)

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = self.__is_valid_vin(vin)
        self.__numbers = self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("VIN номер должен быть целым числом")
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber("VIN номер должен быть в диапазоне от 1000000 до 9999999")
        return vin_number

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Номер должен быть строкой")
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера, переданная строка должна состоять ровно из 6 символов")
        return numbers


try:
    car = Car("Toyota", 1234567, "ABC123")
    print(f"Модель: {car.model}, VIN: {car._Car__vin}, Номер: {car._Car__numbers}")
except (IncorrectVinNumber, IncorrectCarNumbers) as e:
    print(e.message)


test_cases = [
    (123456, "ABC123"),
    (12345678, "ABC123"),
    (1234567, 123456),
    (1234567, "AB12")
]

for vin, numbers in test_cases:
    try:
        car = Car("Honda", vin, numbers)
    except (IncorrectVinNumber, IncorrectCarNumbers) as e:
        print(e.message)