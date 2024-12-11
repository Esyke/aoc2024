import random
import re

rule_list = list()
proposed_update_list = list()
valid_update_list = list()
invalid_update_list = list()
fixed_invalid_update_list = list()


rule_regex = r"(?P<num1>\d{2})\|(?P<num2>\d{2})"
proposal_regex = r"\d{2}"

def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)
    print("######################################")
    print("\n")


def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            if re.match(rule_regex, next_line):
                match = re.search(rule_regex, next_line)
                rule_list.append((int(match.group("num1")), int(match.group("num2"))))
            else:
                if re.match(proposal_regex, next_line):
                    matches = re.findall(proposal_regex, next_line)
                    my_proposal = list()
                    for m in matches:
                        my_proposal.append(int(m))
                    proposed_update_list.append(my_proposal)

def filter_to_valid_updates(input_list, valid_output_list, invalid_output_list):
    for proposed_update in proposed_update_list:
        rules_for_current_proposal = get_rules_for_current_proposal(proposed_update)
        if validate_against_rules(proposed_update, rules_for_current_proposal):
            valid_output_list.append(proposed_update)
        else:
            invalid_output_list.append(proposed_update)
    return
def get_rules_for_current_proposal(my_proposal):
    current_rules = list()
    for rule in rule_list:
        if all(e in my_proposal for e in rule):  # all elements of rule are also elements of my_proposal
            current_rules.append(rule)
    return current_rules

def validate_against_rules(my_proposal, my_rules):
    for rule in my_rules:
        if not my_proposal.index(rule[0]) < my_proposal.index(rule[1]):
            return False
    return True

def sum_of_middle_number_in_list(my_list):
    counter = 0
    for proposal in my_list:
        counter += proposal[int((len(proposal)-1)/2)]
    return counter

def fix_invalid_updates():
    for proposal in invalid_update_list:
        rules_for_current_proposal = get_rules_for_current_proposal(proposal)
        new_proposal = make_proposal_valid(proposal, rules_for_current_proposal)
        print(new_proposal)
        fixed_invalid_update_list.append(new_proposal)
    # for proposal in invalid_update_list:
    #     proposed_update = proposal.copy()
    #     rules_for_current_proposal = get_rules_for_current_proposal(proposed_update)
    #     while not validate_against_rules(proposed_update, rules_for_current_proposal):
    #         random.shuffle(proposed_update)
    #     print(proposed_update)
    #     fixed_invalid_update_list.append(proposed_update)

def make_proposal_valid(input_proposal, my_rules):
    output_proposal = list()
    #count how big shit is with a dict
    proposal_scores_dict = dict()
    for number in input_proposal:
        proposal_scores_dict[number] = get_score(number, my_rules)
    # display_list(proposal_scores_dict.keys())
    # display_list(proposal_scores_dict.values())
    for i in sorted(proposal_scores_dict.values()):
        for x in proposal_scores_dict.keys():
            if proposal_scores_dict.get(x) == i:
                output_proposal.append(x)
                continue
    return  output_proposal

def get_score(my_number, my_rules):
    score = 0
    for rule in my_rules:
        if rule[0] == my_number:
            score -=1
        if rule[1] == my_number:
            score += 1
    return score

def day5_part1():
    read_file("day5.txt")
    # read_file("day5small.txt")
    # display_list(rule_list)
    # display_list(proposed_update_list)
    filter_to_valid_updates(proposed_update_list, valid_update_list, invalid_update_list)
    # display_list(valid_update_list)
    final_sum_1 = sum_of_middle_number_in_list(valid_update_list)
    fix_invalid_updates()
    final_sum_2 = sum_of_middle_number_in_list(fixed_invalid_update_list)
    print("-----")
    print(final_sum_1)
    print("-----")
    print(final_sum_2)


if __name__ == "__main__":
    day5_part1()