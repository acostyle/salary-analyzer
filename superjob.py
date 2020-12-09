import requests

from main_functions import predict_rub_salary


def get_vacancies_from_sj(token, popular_languages):
    sj_url = 'https://api.superjob.ru/2.33/vacancies'
    sj_headers = {'X-Api-App-Id': token}
    sj_params = {'period': '7', 'town': 'Москва',
                 'catalogues': '48', 'count': '100'}

    vacancies_by_language = {language: [] for language in popular_languages}

    for language in popular_languages:
        sj_params['keyword'] = language

        page = 0
        pages_number = 1

        while page < pages_number:
            sj_params['page'] = page

            response = requests.get(
                sj_url, headers=sj_headers, params=sj_params)
            response.raise_for_status()

            vacancies = response.json()
            vacancies_by_language[language] += vacancies['objects']

            page += 1
            pages_number = vacancies['more']

    return vacancies_by_language


def predict_rub_salary_sj(vacancy):
    if vacancy['currency'] != 'rub':
        return None
    return predict_rub_salary(vacancy['payment_from'], vacancy['payment_to'])
