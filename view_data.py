import data_request as dr


def print_data(value: list):
    """
    Выводит данные списка на консоль
    :param value: (фамилия, имя, должность, телефон, оклад)
    """
    result_str = ''
    for i in range(len(value)):
        result_str += f'{i+1}. {value[i][dr.SECOND_NAME]} {value[i][dr.FIRST_NAME]}   tel: {value[i][dr.PHONE]}   position: {value[i][dr.POSITION]}   salary: {value[i][dr.SALARY]}\n'
    print(result_str)

def print_err():
    """
    Выводит сообщение об ошибке на консоль
    """
    print('Произошла ошибка выполнения программы')

def print_ok():
    """
    Выводит на консоль, что программа выполнена успешно
    """
    print('Команда выполнена успешно')

def print_inp_err():
    """
    Выводит сообщение об ошибке ввода на консоль
    """
    print('Произошла ошибка ввода данных')

def print_message(message: str):
    """
    Выводит любое сообщение на консоль
    :param message: сообщение
    """
    print(message)