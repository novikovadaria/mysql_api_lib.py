# Модуль для работы с базами данных через библиотеку pymysql

## Получение всех данных из mysql по названию таблицы

get_all_data_from_mysql_table(connection, mysql_table_name) 

connection - соединение с бд, mysql_table_name - название таблицы

Возвращает mysql_data - данные из бд из нужной таблицы

## Запрос из MySQL списка последних данных по каждой строчке с уникальным ключом, в т.ч. составным из нескольких столбцов

get_last_mysql_data(connection,  mysql_table_name, time_column_name, key_columns_name_list)

connection - соединение с бд, mysql_table_name - название таблицы, time_column_name - название таблицы со временнем, key_columns_name_list - название столбов, которые надо найти

Возвращает result_dict

## Вставка данных из словаря JSON в mySQL

insert_data_from_json_to_mysql(connection, json_data_to_insert, mysql_table_name, mysql_column_name_list, json_field_name_list)

connection - соединение с бд, mysql_table_name - название таблицы, mysql_column_name_list - название столбов в бд, json_field_name_list -  название столбов в json/словаре

## Обновление данных в mySQL по данным из JSON согласно списку id

update_data_from_json_to_mysql(connection, json_data, id_to_update_list, mysql_table_name, mysql_column_name_names, mysql_column_id_name, json_field_names, json_key_field)

connection - соединение с бд, json_data - json словарь с данными,  mysql_table_name - название таблицы, mysql_column_name_names - название столбов в бд, mysql_column_id_name -  название столбов в бд c id, json_key_field - название ключей в json

## Получение последней даты записи в таблицу mySQL (Возвращает дату)

get_max_date(connection, msql_table_name, time_column_name, max_time_shift)

connection - соединение с бд, mysql_table_name - название таблицы, time_column_name - название столбика со временем в бд, max_time_shift -  кол-во времени.

## Изменение всех текстовых значений из указанного поля в JSON словаре на их id из таблицы-словаря MySQL. Возвращает JSON словарь с измененными данными
replace_data_name_to_data_id(connection, json_data, json_field_name, mysql_table_name, mysql_column_id_name, mysql_column_name_name)

connection - соединение с бд, json_data - json словарь с данными, json_field_name - название столбов в json, mysql_table_name -  название таблицы, mysql_column_id_name - название колонок с id в бд, mysql_column_name_name - название колонок с названиями в бд

## Вносение новых уникальных значений в справочник MySLQ по 2-м столбцам (Например, id и name)
insert_new_data_pairs_into_dictionary(connection, data_to_insert_tuple_list, mysql_table_name, mysql_column_name_tuple)

connection - соединение с бд, data_to_insert_tuple_list - json словарь с данными, к-ые надо внести,  mysql_table_name -  название таблицы, mysql_column_name_tuple - название колонок с названиями в бд

## Получаем информацию по двум условиям
get_data_with_condition(connection, mysql_table_name, condition)

connection - соединение с бд, mysql_table_name -  название таблицы,  condition - любое условие для выборки
