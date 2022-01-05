from typing import Tuple


def collect_rules_for(filename, all_rules) -> list[Tuple[str, str]]:
    return []


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
