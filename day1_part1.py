#!/usr/bin/python3

import loader

expense_report = loader.integer_list('input_day1')

for expense_1 in expense_report:
    for expense_2 in expense_report:
        if expense_1 != expense_2 and expense_1+expense_2 == 2020:
            print(expense_1*expense_2)
            exit(0)
