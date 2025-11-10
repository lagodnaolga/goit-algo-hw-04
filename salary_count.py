from pathlib import Path

def total_salary(path: str) ->tuple[int, float]:
    """
    Функція аналізує файл і повертає загальну та середню суму заробітної плати всіх працівників.
    
    Аргументи:
    path - шлях до текстового файлую

    Повертає:
    
    salary_total - загальна заробітня плата всіх працівників.
    
    salary_average - середня заробітня платаю
    
    FileNotFoundError, якщо файл не знайдено.
    """
    path = Path(path)
    salary_total=0
    count_of_employees=0
    try:

        with open(path, "r", encoding="utf-8") as employees_list:
            for employee in employees_list:
                employee = employee.strip()
                parameters=employee.split(',')
                salary=int(parameters[1])
                salary_total=int(salary_total+salary)
                count_of_employees+=1
        if count_of_employees == 0:
            print("Файл порожній.")
            return (0, 0.0)
        salary_average=float(f"{salary_total / count_of_employees:.2f}")
        return (salary_total, salary_average)
                
    except FileNotFoundError:
        print (f'Файл не знайдено. Спробуйте ще раз.')
        return (0, 0.0)



       
    