import psycopg2


class TablesManager:
    """
    Класс для создания базы данных и её заполнения.
    """

    def __init__(self, database_name: str, params: dict):
        self.name = database_name
        self.params = params
        self.create_database()
        self.create_table_companies()
        self.create_table_vacancies()

    def create_database(self) -> None:
        """
        Метод для создания базы данных.
        """
        conn = psycopg2.connect(**self.params)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f"DROP DATABASE IF EXISTS {self.name}")
        cur.execute(f"CREATE DATABASE {self.name}")

        conn.close()

        self.params.update({"dbname": self.name})

    def create_table_companies(self) -> None:
        """
        Метод для создания таблицы компаний.
        """
        conn = psycopg2.connect(**self.params)
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE companies (
            company_id_hh integer PRIMARY KEY,
            company_name varchar(150),
            employer_url varchar(150)
        )"""
        )
        conn.commit()

        cur.close()
        conn.close()

    def create_table_vacancies(self) -> None:
        """
        Метод для создания таблицы вакансий.
        """
        conn = psycopg2.connect(**self.params)
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE vacancies (
            vacancy_id_hh integer PRIMARY KEY,
            company_id_hh integer,
            vacancy_name varchar(150),
            data_published date,
            salary_average integer,
            area varchar(150),
            url varchar(150),
            requirement varchar(500),
            experience varchar(150),
            employment varchar(150),
            CONSTRAINT fk_hh_vacancies_vacancies FOREIGN KEY(company_id_hh) 
            REFERENCES companies(company_id_hh)
            )"""
        )
        conn.commit()

        cur.close()
        conn.close()

    def insert_data_company(self, data: dict) -> None:
        """
        Метод для заполнения данными таблицу компаний.
        """
        conn = psycopg2.connect(**self.params)
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO companies VALUES (%s, %s, %s)",
            (
                int(data["employer"]["id"]),
                data["employer"]["name"],
                data["employer"]["alternate_url"],
            ),
        )

        conn.commit()

        cur.close()
        conn.close()

    def insert_data_vacancy(self, vacancies: list) -> None:
        """
        Метод для заполнения данными таблицу вакансий.
        """
        conn = psycopg2.connect(**self.params)
        cur = conn.cursor()
        for vacancy in vacancies:
            cur.execute(
                "INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    vacancy.id,
                    vacancy.employer_id,
                    vacancy.name,
                    vacancy.data_published,
                    vacancy.salary_average,
                    vacancy.area,
                    vacancy.url,
                    vacancy.requirement,
                    vacancy.experience,
                    vacancy.employment,
                ),
            )

        conn.commit()

        cur.close()
        conn.close()
