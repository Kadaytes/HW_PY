# Напишите функцию, которая получает на вход 
# директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, 
# а для директорий размер файлов в ней с учётом всех 
# вложенных файлов и директорий. 

import os
import json
import csv
import pickle

# сохранение в формате JSON
def save_json(results, output_file):
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)
# сохранение в формате CSV
def save_csv(results, output_file):
    fieldnames = ['name', 'type', 'size', 'parent_directory'],
    with open(output_file, 'w', newline='') as f:
        writer.writeheader()
        writer.writerows(results)
# сохранение в формате Pickle
def save_pickle(results, output_file):
    with open(output_file, 'wb') as f:
        pickle.dump(results, f)
###
def get_directory_info(path):
    results = [] 
    for root, dirs, files in os.walk(path):
        print(os.walk(path), path,root, dirs, files)
        dirname = os.path.basename(root)
        dirsize = get_directory_size(root)
        results.append({
            'name': dirname,
            'type': 'directory',
            'size': dirsize,
            'parent_directory': os.path.dirname(root),
        })
        #print(os.walk(path), path)
        for file in files:
            filepath = os.path.join(root, file)
            filesize = get_directory_size(filepath)
            results.append({
                'name': file,
                'type': 'file',
                'size': filesize,
                'parent_directory': os.path.dirname(filepath),
            })
    #print(os.walk(path), path,root, dirs, files)
    return results
###
def get_directory_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
    return total_size
            
# получает на вход директорию и рекурсивно обходит её 
# и все вложенные директории. 
def traverse_directory(path):
    results = get_directory_info(path)
    
    pickle_output_file = 'output.pickle'
    save_pickle(results, pickle_output_file)
    print(f'записаны результаты в {pickle_output_file}')

    json_output_file = 'output.json'
    save_json(results, json_output_file)
    print(f'записаны результаты в {json_output_file}')

    csv_output_file = 'output.csv'
    save_csv(results, csv_output_file)
    print(f'записаны результаты в {csv_output_file}')

#print(get_directory_info('/Users/kadaytes/study/python'))
traverse_directory('/Users/kadaytes/study/python')