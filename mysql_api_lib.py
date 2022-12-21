from datetime import datetime, timedelta


# Получение всех данных из mysql по названию таблицы
def get_all_data_from_mysql_table(connection, mysql_table_name):
    try:
        error_message = ''
        step = 1
        with connection.cursor() as cursor:
            request = f"SELECT * FROM `{mysql_table_name}`"
            cursor.execute(request)
            mysql_data = cursor.fetchall()
        return mysql_data, error_message
    except Exception as err:
        error_message = f'ошибка в get_all_data_from_mysql_table на шаге {step}: ' + str(err).replace("'", "")
        return 1, error_message
    

# Запрос из MySQL списка последних данных по каждой строчке с уникальным ключом, в т.ч. составным из нескольких столбцов
def get_last_mysql_data(connection,  mysql_table_name, time_column_name, key_columns_name_list):
    try:
        step = 1
        error_message = ''
        order_condition = ''
        for el in key_columns_name_list:
            step = 2
            order_condition += f', {el}'
        order_condition += f', {time_column_name}'
        order_condition = order_condition[2:]
        step = 3
        with connection.cursor() as cursor:
            request = f"SELECT * FROM `{mysql_table_name}` ORDER BY {order_condition}"
            step = 4
            cursor.execute(request)
            mysql_data_dict = cursor.fetchall()
            step = 5
        result_dict = []
        if len(mysql_data_dict) > 0:
            cur_key_value = mysql_data_dict[0]
            for i in range(len(mysql_data_dict)):
                new_flag = False
                for key_column in key_columns_name_list:
                    if mysql_data_dict[i][key_column] != cur_key_value[key_column]:
                        new_flag = True
                if new_flag == True:
                    result_dict.append(cur_key_value)
                    cur_key_value = mysql_data_dict[i]
                else:
                    cur_key_value = mysql_data_dict[i]
                if i == len(mysql_data_dict)-1:
                    result_dict.append(mysql_data_dict[i])
        return result_dict, error_message
    except Exception as err:
        error_message = f'ошибка в get_last_mysql_data на шаге {step}: ' + str(err).replace("'", "")
        return 1, error_message


# Вставка данных из словаря JSON в mySQL
def insert_data_from_json_to_mysql(connection, json_data_to_insert, mysql_table_name, mysql_column_name_list, json_field_name_list):
    try:
        step = 1
        error_message = ''
        if len(json_data_to_insert) > 0:
            step = 2
            # Составление строки для запроса, содержащей названия всех столбцов
            insert_columns_string = ''
            for i in range(len(mysql_column_name_list)):
                step = 3
                insert_columns_string += '`' + mysql_column_name_list[i] + "`, "
            insert_columns_string = '(' + insert_columns_string[0:-2] + ')'
            step = 4

            # Составление строки для запроса, содержащей перечисление всех значений
            insert_data_string = ''
            insert_counter = 0
            json_data_len = len(json_data_to_insert)
            step = 5
            for i in range(json_data_len):
                insert_data_string += '('
                insert_counter += 1
                step = 6
                for j in range(len(json_field_name_list)):
                    step = 7
                    insert_data_string += f"'{json_data_to_insert[i][json_field_name_list[j]]}', "
                insert_data_string = insert_data_string[0:-2] + '), '
                step = 8
                if insert_counter >= 100 or i >= json_data_len-1:
                    step = 9
                    insert_data_string = insert_data_string[0:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(f"INSERT INTO `{str(connection.db)[2:-1]}`.`{mysql_table_name}` {insert_columns_string} VALUES {insert_data_string};")
                        step = 10
                    connection.commit()
                    insert_data_string = ''
                    insert_counter = 0
        return error_message
    except Exception as err:
        error_message = f'ошибка в insert_data_from_json_to_mysql на шаге {step}: ' + str(err).replace("'", "")
        return error_message


# Обновление данных в mySQL по данным из JSON согласно списку id
def update_data_from_json_to_mysql(connection, json_data, id_to_update_list, mysql_table_name, mysql_column_name_names, mysql_column_id_name, json_field_names, json_key_field):
    try:
        step = 1
        error_message = ''
        # Удаление дубликатов
        id_to_update_list = list(set(id_to_update_list))
        
        if len(id_to_update_list) > 0:
            step = 2
            for i in range(len(json_data)):
                step = 3
                if json_data[i][json_key_field] in id_to_update_list:
                    step = 4
                    request = f'UPDATE {str(connection.db)[2:-1]}.{mysql_table_name} SET '
                    for j in range(len(mysql_column_name_names)):
                        step = 5
                        request += f"{mysql_column_name_names[j]} = '{json_data[i][json_field_names[j]]}', "
                    step = 5
                    request = request[0:-2]
                    request += f" WHERE {mysql_column_id_name} = '{json_data[i][json_key_field]}';"
                    step = 6
                    with connection.cursor() as cursor:
                        cursor.execute(request)
                    step = 7
                    connection.commit()
        return error_message
    except Exception as err:
        error_message = f'ошибка в update_data_from_json_to_mysql на шаге {step}: ' + str(err).replace("'", "")
        return error_message

# Получение последней даты записи в таблицу mySQL (Возвращает дату)
def get_max_date(connection, msql_table_name, time_column_name, max_time_shift):
    try:
        step = 1
        error_message = ''
        request = f"SELECT MAX({time_column_name}) as MaxDate FROM {msql_table_name}"
        step = 2
        with connection.cursor() as cursor:
            step = 3
            cursor.execute(request)
            MaxDate = cursor.fetchall()
            step = 4
        if MaxDate[0]['MaxDate'] == None:
            date = str(datetime.today().date() - timedelta(days=max_time_shift))
            step = 5
        else:
            step = 6
            date = str(MaxDate[0]['MaxDate'].date() - timedelta(days=1))
        return date, error_message
    except Exception as err:
        error_message = f'ошибка в get_max_date на шаге {step}: ' + str(err).replace("'", "")
        return 1, error_message

# Изменение всех текстовых значений из указанного поля в JSON словаре на их id из таблицы-словаря MySQL
# Возвращает JSON словарь с измененными данными
def replace_data_name_to_data_id(connection, json_data, json_field_name, mysql_table_name, mysql_column_id_name, mysql_column_name_name):
    try:
        step = 1
        error_message = ''
        with connection.cursor() as cursor:
            step = 2
            request = f"SELECT * FROM `{str(connection.db)[2:-1]}`.`{mysql_table_name}`"
            cursor.execute(request)
            step = 3
            work_data = cursor.fetchall()
            step = 4
            for i in range(len(work_data)):
                step = 5
                for j in range(len(json_data)):
                    step = 6
                    if json_data[j][json_field_name] == work_data[i][mysql_column_name_name]:
                        step = 7
                        json_data[j][json_field_name] = work_data[i][mysql_column_id_name]
                        step = 8
        return json_data, error_message
    except Exception as err:
        error_message = f'ошибка в replace_data_name_to_data_id на шаге {step}: ' + str(err).replace("'", "")
        return 1, error_message


# Вносение новых уникальных значений в справочник MySLQ без id (в таблице MySQL может быть автоинкремент или нет)
def insert_new_data_into_dictionary_no_id(connection, data_to_insert_list, mysql_table_name, mysql_column_name_name):
    try:
        step = 1
        error_message = ''
        # Удаление дубликатов
        data_to_insert_list = list(set(data_to_insert_list))
        # Поиск отсутствующих в БД значений
        with connection.cursor() as cursor:
            request = f"SELECT `{mysql_column_name_name}` FROM `{mysql_table_name}`"
            cursor.execute(request)
            step = 2
            old_data = cursor.fetchall()
        old_data_list = [x[mysql_column_name_name] for x in old_data]
        step = 3
        missing_new_data = list(set([x for x in data_to_insert_list if x not in old_data_list]))
        step = 4
        # Если есть отсутствующие в БД значения, добавить их
        if len(missing_new_data) > 0:
            insert_values_string = ''
            step = 5
            for el in missing_new_data:
                insert_values_string += f"('{el}'), "
            step = 6
            insert_values_string = insert_values_string[0:-2]
            with connection.cursor() as cursor:
                step = 7
                cursor.execute(
                    f"INSERT INTO `{str(connection.db)[2:-1]}`.`{mysql_table_name}` (`{mysql_column_name_name}`) VALUES {insert_values_string};")
                step = 8
            connection.commit()
        return error_message
    except Exception as err:
        error_message = f'ошибка в insert_new_data_into_dictionary_no_id на шаге {step}: ' + str(err).replace("'", "")
        return  error_message

# Вносение новых уникальных значений в справочник MySLQ по 2-м столбцам (Например, id и name)
def insert_new_data_pairs_into_dictionary(connection, data_to_insert_tuple_list, mysql_table_name, mysql_column_name_tuple):
    try:
        step = 1
        error_message = ''
        # Удаление дубликатов
        data_to_insert_tuple_list = list(set(data_to_insert_tuple_list))
        # Поиск отсутствующих в БД значений
        with connection.cursor() as cursor:
            request = f"SELECT {mysql_column_name_tuple[0]}, {mysql_column_name_tuple[1]}  FROM `{mysql_table_name}`"
            step = 2
            cursor.execute(request)
            old_data = cursor.fetchall()
            step = 3
        old_data_list = [(x[mysql_column_name_tuple[0]], x[mysql_column_name_tuple[1]]) for x in old_data]
        step = 4
        missing_new_data = list(set([x for x in data_to_insert_tuple_list if x not in old_data_list]))
        step = 5

        # Если есть отсутствующие в БД значения, добавить их
        if len(missing_new_data) > 0:
            step = 6
            insert_values_string = ''
            for el in missing_new_data:
                insert_values_string += f"('{el[0]}', '{el[1]}'), "
                step = 7
            insert_values_string = insert_values_string[0:-2]
            with connection.cursor() as cursor:
                step = 8
                cursor.execute(f"INSERT INTO `{str(connection.db)[2:-1]}`.`{mysql_table_name}` (`{mysql_column_name_tuple[0]}`, `{mysql_column_name_tuple[1]}`) VALUES {insert_values_string};")
                step = 9
            connection.commit()
            step = 10
        return error_message
    except Exception as err:
        error_message = f'ошибка в insert_new_data_pairs_into_dictionary на шаге {step}: ' + str(err).replace("'", "")
        return error_message

# Получаем информацию по двум условиям
def get_data_with_condition(connection, mysql_table_name, condition):
    try:
        step = 1
        error_message = ''
        with connection.cursor() as cursor:
            step = 2
            request = f"SELECT * FROM `{str(connection.db)[2:-1]}`.`{mysql_table_name}`" + condition
            cursor.execute(request)
            step = 3
            work_data = cursor.fetchall()
        return work_data, error_message
    except Exception as err:
        error_message = f'ошибка в get_info_by_one_condition_from_db на шаге {step}: ' + str(err).replace("'", "")
        return 1, error_message
