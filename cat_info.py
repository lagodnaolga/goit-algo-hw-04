from pathlib import Path

def get_cats_info(path: str) -> list[dict]:

    """
    Функція аналізує файл і список словників. Кожен словник містить дані про окремого кота, такі як id, ім'я та вік.
    
    Аргументи:
    path - шлях до текстового файлу

    Повертає:
    cats_info_full_list - список словників cats_info.

    cats_info - словник, який містить дані про окремого кота, такі як id, ім'я (name) та вік (age).
    salary_total - загальна заробітня плата всіх працівників.
    
    
    FileNotFoundError, якщо файл не знайдено.
    
    """
    path=Path(path)
    cats_info_full_list=[]

    try:
        with open(path, "r", encoding="utf-8") as cats_list:
            for cat in cats_list:
                cat = cat.strip()
                cat_info = cat.split(',')
                id_num = cat_info[0]
                name = cat_info[1]
                age = cat_info[2]

                cats_info = {
                        'id': cat_info[0],
                        'name': cat_info[1],
                        'age': cat_info[2]
                    }

                cats_info_full_list.append(cats_info)
        return cats_info_full_list
            
            
    
    except FileNotFoundError:
        print (f'Файл не знайдено. Спробуйте ще раз.')
        return []


