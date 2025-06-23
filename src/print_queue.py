from operator import contains


class Rule:
    tuple: tuple[int, int]

    def __init__(self, left: int, right: int):
        self.tuple = left, right

    def left(self):
        return self.tuple[0]

    def right(self):
        return self.tuple[1]


class Update:
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


def explode_update(update: Update) -> list[Rule]:
    rules: list[Rule] = []
    for left in range(0, len(update) - 1):
        for right in range(left + 1, len(update)):
            rules.append(Rule(update.pages[left], update.pages[right]))
    return rules


def supported_by_rules(update: Update, rules: list[Rule]) -> bool:
    update_tuples: list[tuple[int, int]] = list(map(lambda r: r.tuple, explode_update(update)))
    rule_tuples: list[tuple[int, int]] = list(map(lambda r: r.tuple, rules))

    return all(map(lambda t: contains(rule_tuples, t), update_tuples))


def is_valid(update: Update, rules: list[Rule]) -> bool:
    if update.even_length():  # this doesn't work for updates with even number of elements
        return False
    return supported_by_rules(update, rules)


def triage_updates(rules: list[Rule], updates: list[Update]) -> tuple[list[Update], list[Update]]:
    valid_updates = []
    invalid_updates = []
    for u in updates:
        if is_valid(u, rules):
            valid_updates.append(u)
        else:
            invalid_updates.append(u)
    return valid_updates, invalid_updates


def fix(rules: list[Rule], bad_updates: list[Update]) -> list[Update]:
    def sort_rules(rules: list[Rule]) -> list[Rule]:
        if len(rules) == 0:
            return []
        first_generator = (r for r in rules if all(not k.right() == r.left() for k in rules))
        first = next(first_generator, None)
        index = rules.index(first)
        new_rules = rules[:index] + rules[index + 1:]
        return [first] + sort_rules(new_rules)

    def fix_update(bad_update: Update) -> Update:
        candidate_rules: list[Rule] = list(
            filter(lambda r: r.left() in bad_update and r.right() in bad_update, rules))

        ordered_rules = sort_rules(candidate_rules)
        return Update(list(map(lambda t: t.left(), ordered_rules)))

    fixed_updates = []
    for bu in bad_updates:
        fixed_updates.append(fix_update(bu))
    return fixed_updates


def sum_middle_pages(rules: list[Rule], updates: list[Update]) -> tuple[int, int]:
    def accumulate(us: list[Update]) -> int:
        acc = 0
        for u in us:
            acc += u.mid_element()
        return acc

    valid, invalid = triage_updates(rules, updates)
    # fixed = fix(rules, invalid)
    n_valid, n_fixed = map(accumulate, (valid, valid))
    return n_valid, n_fixed
