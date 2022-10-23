import data_request as dr
import data_interface as di
import view_data as vd
import random

COMMAND_SIZE = 5
PARAM_SIZE = 2

def get_command_str(message) -> str:
    while True:
        in_string = input(message)
        if not in_string in ('1','2','3','4','5','6','7','8'):
            vd.print_inp_err()
        else:
            return in_string

def get_param_list(message) -> list:
    while True:
        in_string = input(message)
        in_list = in_string.split(',')
        if len(in_list) != PARAM_SIZE:
            vd.print_inp_err()
        else:
            return in_list

def get_param_list_all(message) -> list:
    while True:
        in_string = input(message)
        in_list = in_string.split(',')
        if len(in_list) != PARAM_SIZE+3:
            vd.print_inp_err()
        else:
            return in_list

def get_param(message) -> str:
    in_string = input(message)
    return in_string

def view_request(second_name = dr.NO_VALUE, first_name = dr.NO_VALUE, phone = dr.NO_VALUE, position=dr.NO_VALUE, salary_min=dr.NO_VALUE_SALARY, salary_max=dr.NO_VALUE_SALARY):
    request_list = dr.request_list(di.load_data(),second_name, first_name, phone, position, salary_min, salary_max)
    if len(request_list):
        vd.print_message('НИЧЕГО НЕ НАЙДЕНО')
    else:
        vd.print_data(request_list)

def del_request(value: str):
    request_list = dr.request_list(di.load_data(),second_name=value)
    if len(request_list) == 0:
        vd.print_message('НИЧЕГО НЕ НАЙДЕНО')
        return di.OK_RETURN
    else:
        vd.print_data(request_list)
    while True:
        del_number = int(input('Введите номер записи которую нужно удалить: '))
        if 1<=del_number<=len(request_list):
            return dr.del_data(di.load_data(),request_list[del_number-1])
        else:
            vd.print_inp_err()

def add_request(value: list):
    return dr.add_data(di.load_data(),value)

def edit_request(value: str):
    request_list = dr.request_list(di.load_data(),second_name=value)
    if len(request_list) == 0:
        vd.print_message('НИЧЕГО НЕ НАЙДЕНО')
        return di.OK_RETURN
    else:
        vd.print_data(request_list)
    while True:
        edit_number = int(input('Введите номер записи которую нужно отредактировать: '))
        if 1<=edit_number<=len(request_list):
            param_list = get_param_list_all('\nФормат данных: Фамилия,Имя,Должность,Телефон,Оклад - например:\n'
                                      + 'Введите новые значения записи: ')
            return dr.edit_data(di.load_data(),request_list[edit_number-1],param_list)
        else:
            vd.print_inp_err()
    