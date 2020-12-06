#!/usr/bin/python3

import loader

raw_survey_groups = loader.blank_line_delimited("input_day6")

union_groups = []
for raw_survey_group in raw_survey_groups:
    union_group = set()
    for survey_response in raw_survey_group:
        union_group = union_group.union(set(survey_response))
    union_groups.append(union_group)

print(sum([len(group) for group in union_groups]))
