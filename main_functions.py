from terminaltables import DoubleTable


def predict_rub_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    if salary_from and not salary_to:
        return salary_from * 1.2
    if not salary_from and salary_to:
        return salary_to * 0.8


def predict_rub_salary_hh(vacancy):
    salary = vacancy['salary']
    if salary is None or salary['currency'] != 'RUR':
        return None
    return predict_rub_salary(salary['from'], salary['to'])


def predict_rub_salary_sj(vacancy):
    if vacancy['currency'] != 'rub':
        return None
    return predict_rub_salary(vacancy['payment_from'], vacancy['payment_to'])


def get_statistics_by_language(vacancies, predict_salary, popular_languages):
    statistics_by_lang = {language: {} for language in popular_languages}

    for language in popular_languages:
        salaries_by_language = []
        number_of_jobs = len(vacancies[language])
        statistics_by_lang[language]['vacancies_found'] = number_of_jobs

        for vacancy in vacancies[language]:
            predicted_rub_salary = predict_salary(vacancy)
            if predicted_rub_salary is not None:
                salaries_by_language.append(predicted_rub_salary)

        amount_of_salaries_to_calc_avg = len(salaries_by_language)

        try:
            statistics_by_lang[language]['average_salary'] = int(
                sum(salaries_by_language) / amount_of_salaries_to_calc_avg)
        except ZeroDivisionError:
            statistics_by_lang[language]['average_salary'] = 0
        statistics_by_lang[language]['vacancies_processed'] = amount_of_salaries_to_calc_avg

    return statistics_by_lang


def print_statistics(statistics, title):
    table_data = list((('Programming language', 'Vacancies found',
                        'Vacancies processed', 'Average salary (RUB)'),))
    for language in statistics:
        table_data.append(
            (
                f"{language}",
                f"{statistics[language]['vacancies_found']}",
                f"{statistics[language]['vacancies_processed']}",
                f"{statistics[language]['average_salary']}",
            )
        )
    table_instance = DoubleTable(table_data, title)
    table_instance.justify_columns[0] = 'left'
    table_instance.justify_columns[1] = 'left'
    table_instance.justify_columns[2] = 'left'
    table_instance.justify_columns[3] = 'left'
    print(table_instance.table)
    print()
