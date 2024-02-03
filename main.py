from src.api_hh import HH_API
from src.db_manager import DBManager
from src.tables_manager import TablesManager
from src.utils import config, load_companies
from src.vacancy import Vacancy


def main():
    database_name = "db_vacancies"
    file_companies_ids = "data/companies.json"

    companies = load_companies(file_companies_ids)

    params = config()

    tables = TablesManager(database_name, params)
    db_manager = DBManager(database_name, params)

    print(f"База SQL '{tables.name}' создана.")

    hh_api = HH_API()

    for company in companies:
        vacancies_info = hh_api.get_all_vacancies(company['id'])

        tables.insert_data_company(vacancies_info[0])

        vacancies = []
        for vacancy_info in vacancies_info:
            vacancy = Vacancy.create_vacancy_from_hh(vacancy_info)
            vacancies.append(vacancy)

        tables.insert_data_vacancy(vacancies)

        print(
            f"Компания '{company['name']}' добавлена в базу данных с количеством вакансий {len(vacancies_info)}."
        )
    print("Данные по вакансиям выбранных работодателей добавлены в базу данных SQL.")

    while True:

        print(
            """
Здравствуйте!
Выберите один из пунктов:
1 - получить список всех компаний и количество вакансий у каждой компании;
2 - получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию;
3 - получить среднюю зарплату по вакансиям;
4 - получить список всех вакансий, у которых зарплата выше средней по всем вакансиям;
5 - получить список всех вакансий, в названии которых содержится слово 'разработчик';
0 - выход"""
        )

        user_input = input("Введите номер выбранного пункта: ")
        if user_input == "1":
            db_manager.get_companies_and_vacancies_count()
        elif user_input == "2":
            db_manager.get_all_vacancies()
        elif user_input == "3":
            db_manager.get_avg_salary()
        elif user_input == "4":
            db_manager.get_vacancies_with_higher_salary()
        elif user_input == "5":
            db_manager.get_vacancies_with_keyword("разработчик")
        elif user_input == "0":
            break
        else:
            print("Неверная команда.")


if __name__ == "__main__":
    main()
