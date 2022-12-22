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

_______________________________________________________________________________________________________________________________
# A module for working with databases via the pymysql library

## Getting all data from mysql by table name

get_all_data_from_mysql_table(connection, mysql_table_name)

connection - db connection, mysql_table_name - table name

Returns mysql_data - data from the database from the desired table

## Request from MySQL a list of the latest data for each row with a unique key, including a composite of several columns

get_last_mysql_data(connection, mysql_table_name, time_column_name, key_columns_name_list)

connection - connection to the database, mysql_table_name - the name of the table, time_column_name - the name of the table with the time, key_columns_name_list - the name of the columns to be found

Returns result_dict

## Inserting data from a JSON dictionary into MySQL

insert_data_from_json_to_mysql(connection, json_data_to_insert, mysql_table_name, mysql_column_name_list, json_field_name_list)

connection - db connection, mysql_table_name - table name, mysql_column_name_list - name of columns in the database, json_field_name_list - name of columns in the json/dictionary

## Updating data in MySQL based on data from JSON according to the id list

update_data_from_json_to_mysql(connection, json_data, id_to_update_list, mysql_table_name, mysql_column_name_names, mysql_column_id_name, json_field_names, json_key_field)

connection - database connection, json_data - json dictionary with data, mysql_table_name - table name, mysql_column_name_names - name of columns in the database, mysql_column_id_name - name of columns in the database with id, json_key_field - name of keys in json

## Getting the last record date in the MySQL table (Returns the date)

get_max_date(connection, msql_table_name, time_column_name, max_time_shift)

connection - connection to the database, mysql_table_name - the name of the table, time_column_name - the name of the column with the time in the database, max_time_shift - the number of times.

## Changing all text values from the specified field in the JSON dictionary to their id from the MySQL dictionary table. Returns a JSON dictionary with modified data
replace_data_name_to_data_id(connection, json_data, json_field_name, mysql_table_name, mysql_column_id_name, mysql_column_name_name)

connection - database connection, json_data - json dictionary with data, json_field_name - name of columns in json, mysql_table_name - table name, mysql_column_id_name - name of columns with id in db, mysql_column_name_name - name of columns with names in db

## Adding new unique values to the myslq directory by 2 columns (for example, id and name)
insert_new_data_pairs_into_dictionary(connection, data_to_insert_tuple_list, mysql_table_name, mysql_column_name_tuple)

connection - connection to the database, data_to_insert_tuple_list - json dictionary with data to be entered, mysql_table_name - table name, mysql_column_name_tuple - name of columns with names in the database

## We get information on two conditions
get_data_with_condition(connection, mysql_table_name, condition)

connection - db connection, mysql_table_name - table name, condition - any condition for selection
