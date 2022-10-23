import user_interface as ui
import view_data as vd
import data_interface as di

while True:
    in_string = ui.get_command_str('\n1. Показать все записи\n' 
                                 + '2. Найти сотрудника по имени и фамилии\n'
                                 + '3. Выборка по должности\n'
                                 + '4. Выборка по зарплате\n'
                                 + '5. Удалить сотрудника\n'
                                 + '6. Добавить сотрудника\n'
                                 + '7. Обновить данные сотрудника\n'
                                 + '8. Выход из программы\n'
                                 + 'Введите команду: ')
    print('')
    if in_string == '1':
        ui.view_request()
        vd.print_ok()
    elif in_string == '2':
        param_list = ui.get_param_list('Формат данных: Фамилия,Имя - например:\n'
                                      + 'Введите фамилию и имя: ')
        ui.view_request(second_name = param_list[0], first_name = param_list[1])
        vd.print_ok()
    elif in_string == '3':
        param = ui.get_param('Введите название должности или первые ее буквы: ')
        ui.view_request(position = param)
        vd.print_ok()
    elif in_string == '4':
        param_list = ui.get_param_list('Формат данных: мин.значение, макс.значение - например: 100,1000 \n\n'
                                      + 'Введите параметры поиска: ')
        ui.view_request(salary_min=float(param_list[0]), salary_max=float(param_list[1]))
        vd.print_ok()
    elif in_string == '5':
        param = ui.get_param('Введите фамилию или первые ее буквы: ')
        if ui.del_request(param) == di.OK_RETURN:
            vd.print_ok()
        else:
            vd.print_err()
    elif in_string == '6':
        param_list = ui.get_param_list_all('Формат данных: Фамилия, Имя, Телефон, Должность, Оклад \n\n'
                                        +  'Введите данные сотрудника: ')
        if ui.add_request(param_list)==di.OK_RETURN:
            vd.print_ok()
        else:
            vd.print_err()
    elif in_string == '7':
        param = ui.get_param('Введите фамилию или первые ее буквы: ')
        if ui.edit_request(param) == di.OK_RETURN:
            vd.print_ok()
        else:
            vd.print_err()  
    elif in_string == '8': 
        break