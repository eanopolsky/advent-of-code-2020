#!/usr/bin/python3

import loader

raw_survey_groups = loader.blank_line_delimited("input_day6")

intersection_groups = []
for raw_survey_group in raw_survey_groups:
    intersection_group = set(raw_survey_group[0])
    for survey_response in raw_survey_group[1:]:
        intersection_group = intersection_group.intersection(set(survey_response))
    intersection_groups.append(intersection_group)

print(sum([len(group) for group in intersection_groups]))
