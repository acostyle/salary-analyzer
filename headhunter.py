import requests

from main_functions import predict_rub_salary


def get_vacancies_from_hh(popular_languages):
    hh_url = 'https://api.hh.ru/vacancies/'
    hh_params = {'period': '30', 'area': '1', 'per_page': '100', 'page': '0'}
    hh_languages_result = {language: [] for language in popular_languages}

    for language in popular_languages:
        hh_params['text'] = f'Программист {language}'

        page = 0
        pages_number = 1

        while page < pages_number:

            hh_params['page'] = page

            response = requests.get(hh_url, params=hh_params)
            response.raise_for_status()

            vacancies = response.json()

            hh_languages_result[language] += vacancies['items']

            page += 1
            pages_number = vacancies['pages']

            vacancies_limit_page = 19

            # it's not possible to get more than 2000 vacancies
            if page == vacancies['pages'] or page == vacancies_limit_page:
                break

    return hh_languages_result


def predict_rub_salary_hh(vacancy):
    salary = vacancy['salary']
    if salary is None or salary['currency'] != 'RUR':
        return None
    return predict_rub_salary(salary['from'], salary['to'])
