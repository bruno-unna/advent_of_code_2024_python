from functools import cmp_to_key
from operator import contains


class Rule:
    """
    Represents a forceful order between two different page numbers.
    """
    tuple: tuple[int, int]

    def __init__(self, left: int, right: int):
        self.tuple = left, right

    def left(self):
        return self.tuple[0]

    def right(self):
        return self.tuple[1]


class Update:
    """
    Contains a list of page numbers.

    A correct update is one where, for any pair of its elements, there is a rule.
    """
    pages: list[int]

    def __init__(self, p: list[int]):
        self.pages = p

    def __len__(self):
        return len(self.pages)

    def even_length(self):
        return len(self.pages) % 2 == 0

    def mid_element(self) -> int:
        if self.even_length():
            return 0
        else:
            return self.pages[len(self.pages) >> 1]

    def explode_update(self) -> list[Rule]:
        """
        Expands an update (list of page numbers) to all the rules (pairs) of its elements,
        respecting their order.

        :return: A list with all the rules generated from the given update.
        """
        rules: list[Rule] = []
        for left in range(0, len(self.pages) - 1):
            for right in range(left + 1, len(self.pages)):
                rules.append(Rule(self.pages[left], self.pages[right]))
        return rules

    def is_supported_by_rules(self, rules: list[Rule]) -> bool:
        update_tuples: list[tuple[int, int]] = list(map(lambda r: r.tuple, self.explode_update()))
        rule_tuples: list[tuple[int, int]] = list(map(lambda r: r.tuple, rules))

        return all(map(lambda t: contains(rule_tuples, t), update_tuples))

    def is_valid(self, rules: list[Rule]) -> bool:
        if self.even_length():  # this doesn't work for updates with even number of elements
            return False
        return self.is_supported_by_rules(rules)


def triage_updates(rules: list[Rule], updates: list[Update]) -> tuple[list[Update], list[Update]]:
    """
    Partitions a list of updates into valid and invalid based on a set of rules.

    This function iterates through the provided updates and applies the 'is_valid' check
    against the given rules. It returns two distinct lists: one containing all valid updates
    and another containing all invalid ones.

    :param rules: A list of Rule objects that define the validation criteria.
                  Each rule is a tuple of two integers.
    :param updates: A list of Update objects to be triaged.
                    Each update is a list of integers.
    :return: A tuple containing two lists:
             - The first list contains all updates that passed the validation.
             - The second list contains all updates that failed the validation.
     """
    valid_updates = []
    invalid_updates = []
    for u in updates:
        if u.is_valid(rules):
            valid_updates.append(u)
        else:
            invalid_updates.append(u)
    return valid_updates, invalid_updates


def fix(rules: list[Rule], bad_updates: list[Update]) -> list[Update]:
    def fix_update(bad_update: Update) -> Update:
        rules_tuples: list[tuple[int, int]] = list(map(lambda r: r.tuple, rules))

        def rule_based_comparator(a, b):
            if (a, b) in rules_tuples:
                return -1
            else:
                return 1

        comparing_key = cmp_to_key(rule_based_comparator)

        fixed_pages = sorted(bad_update.pages, key=comparing_key)

        return Update(fixed_pages)

    fixed_updates = []
    for bu in bad_updates:
        fixed_updates.append(fix_update(bu))
    return fixed_updates


def report_totals(rules: list[Rule], updates: list[Update]) -> tuple[int, int]:
    """
    Entry point of the module. It generates a report with sums of mid-elements for the given updates.

    There are two sums in the report:
    - The first is the sum of the mid-elements of the *valid* updates.
    - The second is the sum of mid-elements of the *invalid* updates **after fixing them**.

    :param rules: List of the rules to be used for the classification and fix.
    :param updates: List of the updates to be triaged and processed.
    :return: Tuple with the two described sums.
    """

    def sum_mid_elements(us: list[Update]) -> int:
        acc = 0
        for u in us:
            acc += u.mid_element()
        return acc

    valid, invalid = triage_updates(rules, updates)
    fixed = fix(rules, invalid)
    n_valid, n_fixed = map(sum_mid_elements, (valid, fixed))
    return n_valid, n_fixed
