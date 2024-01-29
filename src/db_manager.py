from pprint import pprint

import psycopg2


class DBManager:
    """
    Класс предназначен для управления базой данных.
    """

    def __init__(self, database_name: str, params: dict):
        self.params = params
        self.database_name = database_name

    def get_companies_and_vacancies_count(self) -> None:
        """
        Метод получает список всех компаний и количество
        вакансий у каждой компании.
        """
        conn = psycopg2.connect(**self.params)
        cur = conn.cursor()
        cur.execute(
            """SELECT company_name, COUNT(*)
        FROM vacancies
        JOIN companies USING (company_id_hh)
        GROUP BY company_name"""
        )
        pprint(cur.fetchall())
        cur.close()
        conn.close()

    def get_all_vacancies(self) -> None:
        """
        Метод получает список всех вакансий с указанием названия
        компании, названия вакансии и зарплаты и ссылки на вакансию.
        """
        conn = psycopg2.connect(**self.params)
        cur = conn.cursor()
        cur.execute(
            """SELECT company_name, vacancy_name, salary_average, url
        FROM vacancies
        JOIN companies USING (company_id_hh)"""
        )
        pprint(cur.fetchall())
        cur.close()
        conn.close()

    def get_avg_salary(self) -> None:
        """
        Метод получает среднюю зарплату по вакансиям.
        """
        conn = psycopg2.connect(**self.params)
        cur = conn.cursor()
        cur.execute(
            """SELECT AVG(salary_average)
        FROM vacancies
        WHERE salary_average > 0"""
        )
        pprint(cur.fetchall())
        cur.close()
        conn.close()

    def get_vacancies_with_higher_salary(self) -> None:
        """
        Метод получает список всех вакансий, у которых
        зарплата выше средней по всем вакансиям.
        """
        conn = psycopg2.connect(**self.params)
        cur = conn.cursor()
        cur.execute(
            """SELECT company_name, vacancy_name, salary_average, url
        FROM vacancies
        JOIN companies USING (company_id_hh)
        WHERE salary_average > (SELECT AVG(salary_average)
        FROM vacancies
        WHERE salary_average > 0)
        ORDER BY salary_average DESC"""
        )
        pprint(cur.fetchall())
        cur.close()
        conn.close()

    def get_vacancies_with_keyword(self, word: str) -> None:
        """
        Метод получает список всех вакансий, в названии которых
        содержатся переданные в метод слова.
        """
        conn = psycopg2.connect(**self.params)
        cur = conn.cursor()
        cur.execute(
            f"""SELECT company_name, vacancy_name, salary_average, url
        FROM vacancies
        JOIN companies USING (company_id_hh)
        WHERE vacancy_name LIKE '%{word.lower()}%' OR vacancy_name LIKE '%{word.title()}%' 
        OR vacancy_name LIKE '%{word.upper()}%';"""
        )
        pprint(cur.fetchall())
        cur.close()
        conn.close()
