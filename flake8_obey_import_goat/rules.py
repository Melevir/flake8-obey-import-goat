from typing import Tuple

from flake8_obey_import_goat.pathes import convert_filepath_to_importable


def collect_rules_for(filename, all_rules) -> list[Tuple[str, str]]:
    matching_rules = []
    importable = convert_filepath_to_importable(filename)
    for import_rule, rules in all_rules.items():
        if is_rule_matched(importable, import_rule):
            matching_rules += rules
    return sorted(set(matching_rules))


def is_rule_matched(importable: str, rule: str) -> bool:
    if '*' not in rule:
        match_result = importable == rule
    elif rule.startswith('*.'):
        match_result = importable.endswith(rule[1:])
    elif rule.endswith('.*'):
        match_result = importable.startswith(rule[:-1])
    else:
        prefix, suffix = rule.split('*')
        match_result = importable.startswith(prefix) and importable.endswith(suffix)
    return match_result
