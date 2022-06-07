#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    m_of_2 = []

    for i in my_list:
        m_of_2.append(True) if i % 2 == 0 else m_of_2.append(False)

    return m_of_2
