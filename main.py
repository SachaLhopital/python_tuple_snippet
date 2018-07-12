from constants import Constants
from model.room import Room
from model.zone import Zone
from dcop_engine.constraint_manager import ConstraintManager

import itertools


if __name__ == "__main__":

    DIMs = [0, 241]

    z1 = Zone(1)
    z2 = Zone(2)

    a = Room(1)
    b = Room(2)
    c = Room(3)
    d = Room(4)

    cons = ConstraintManager()

    z1.rooms = [a, b]
    z2.rooms = [c, d]

    # --- Util prop

    all_list = []
    for r in z1.rooms:

        temp = list(itertools.product(str(r.id), DIMs))
        r_list = []

        for t in temp:
            r_list.append(t + tuple([cons.get_cost_of_private_constraints_for_value(r, t[1])]))

        all_list.append(r_list)

    temp1 = all_list[0]
    for i in range(1, len(all_list)):
        temp1 = list(itertools.product(temp1, all_list[i]))

    print(temp1)

    all_list = []
    for r in z2.rooms:

        temp = list(itertools.product(str(r.id), DIMs))
        r_list = []

        for t in temp:
            r_list.append(t + tuple([cons.get_cost_of_private_constraints_for_value(r, t[1])]))

        all_list.append(r_list)

    temp2 = all_list[0]
    for i in range(1, len(all_list)):
        temp2 = list(itertools.product(temp2, all_list[i]))

    print(temp2)

    # --- Combine

    R = list(itertools.product(temp1, temp2))
    print(R)

    # --- Value prop

    best_index = 0
    best_value = Constants.INFINITY + 1

    value_prop_result = [('1', 0), ('2', 241)]

    for parent_element, my_element in R:

        if parent_element[0][0:2] in set(value_prop_result) \
                and parent_element[1][0:2] in set(value_prop_result):

            cost = my_element[0][2] + my_element[1][2]
            if cost <= best_value:
                best_value = cost
                best_index = my_element

    print("Value chosen : ", best_index)


