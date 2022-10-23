import view_data as vd
import json

ERROR_RETURN = -1
OK_RETURN = 1
JSON_TYPE_DATA = 'json'
CSV_TYPE_DATA = 'csv'
SEPARATOR_CHAR_CSV = ','
JSON_PATH = 'database.json'
CSV_PATH = 'database.csv'
ONE_RECORD_SIZE = 6

def load_data(data_path=CSV_PATH, type_data=CSV_TYPE_DATA):
    """
    Загружает БД (id, фамилия, имя, должность, телефон, оклад), отфильтровывая 
    данные заполненные не по правилам 
    :param data_path: название и расположение файла БД
    :param type_data: тип файла JSON или CSV
    :return: list БД/ERROR_RETURN
    """
    try:
        list_out = []
        with open(data_path, 'r', encoding='utf-8') as dp:
            if type_data==CSV_TYPE_DATA:
                read_data = dp.read()
            else:
                temp_list = []
                for line in dp:
                    temp = json.loads(line.strip())
                    temp_list.append(temp)
        if type_data == CSV_TYPE_DATA:
            temp_list = read_data.split('\n')
            temp_list = [i.split(SEPARATOR_CHAR_CSV) for i in temp_list]
        for i in range(len(temp_list)):
            if ONE_RECORD_SIZE == len(temp_list[i]):
                if type_data == CSV_TYPE_DATA:
                    list_out.append(temp_list[i])
                else:
                    list_json = ['','','','','','']
                    list_json[0] = temp_list[i]['id']
                    list_json[1] = temp_list[i]['second_name']
                    list_json[2] = temp_list[i]['first_name']
                    list_json[3] = temp_list[i]['position']
                    list_json[4] = temp_list[i]['phone']
                    list_json[5] = temp_list[i]['salary']
                    list_out.append(list_json)
        return list_out
    except Exception as e:   
        vd.print_message(e)
        return ERROR_RETURN


def save_data(data: list, data_path: str,  type_data: str):
    """
    Сохраняет данные в БД 
    :param data: данные (id, фамилия, имя, должность, телефон, оклад)
    :param data_path: название и расположение файла БД
    :param type_data: тип файла TXT или CSV
    :return: OK_RETURN/ERROR_RETURN
    """
    fields = ['id','second_name','first_name','position','phone','salary']
    try:
        write_string = ''
        for i in range(len(data)):
            if type_data == JSON_TYPE_DATA:
                write_string += json.dumps(dict(zip(fields, data[i])))
            else:
                for j in range(ONE_RECORD_SIZE):
                    if j < ONE_RECORD_SIZE-1:
                        write_string += data[i][j] + SEPARATOR_CHAR_CSV
                    else:
                        write_string += data[i][j]
            write_string += '\n'
        with open(data_path, 'w', encoding='utf-8') as dp:
            dp.writelines(write_string)
        return OK_RETURN
    except Exception as e:
        vd.print_message(e)
        return ERROR_RETURN


def save_all_format(data: list):
    """
    Сохраняет данные в БД  
    в формате JSON и CSV
    :param data: данные (id, фамилия, имя, должность, телефон, оклад)
    :return: OK_RETURN/ERROR_RETURN
    """
    ret1 = save_data(data,JSON_PATH,JSON_TYPE_DATA)
    ret2 = save_data(data,CSV_PATH,CSV_TYPE_DATA)
    if ret1==ret2==OK_RETURN:
        return OK_RETURN
    else:
        return ERROR_RETURN

