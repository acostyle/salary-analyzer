import os
import requests

from dotenv import load_dotenv
from main_functions import get_statistics_by_language, print_statistics, predict_rub_salary_hh, predict_rub_salary_sj


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

            if page == vacancies['pages'] or page == 19:
                break

    return hh_languages_result


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

            if page == 5:
                break

    return vacancies_by_language


def main():
    popular_languages = ['JavaScript', 'Python', 'Java',
                         'TypeScript', 'C#', 'PHP', 'C++', 'C', 'Shell', 'Ruby']

    load_dotenv()

    sj_token = os.getenv('SUPERJOB_TOKEN')

    hh_vacancies = get_vacancies_from_hh(popular_languages)
    sj_vacancies = get_vacancies_from_sj(sj_token, popular_languages)

    hh_statistics = get_statistics_by_language(
        hh_vacancies, predict_rub_salary_hh, popular_languages)
    sj_statistics = get_statistics_by_language(
        sj_vacancies, predict_rub_salary_sj, popular_languages)

    print_statistics(hh_statistics, '| HeadHunter Moscow |')
    print_statistics(sj_statistics, '| SuperJob Moscow |')


if __name__ == '__main__':
    main()
