import os

from dotenv import load_dotenv
from headhunter import get_vacancies_from_hh, predict_rub_salary_hh
from superjob import get_vacancies_from_sj, predict_rub_salary_sj
from main_functions import get_statistics_by_language, print_statistics


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
