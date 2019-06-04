import random
def get_list_random(elements: list, count):
    if len(elements) <= count:
        return elements
    list_choices = []
    while count != 0:
        temp = random.choice(elements)
        elements.remove(temp)
        list_choices.append(temp)
        count -= 1
    return list_choices
