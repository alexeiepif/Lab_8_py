#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Определить, является ли кортеж упорядоченным по возрастанию.
# В случае отрицательного ответа определить номер первого элемента,
# нарушающего такую упорядоченность.

import sys


if __name__ == '__main__':
    print("Введите кортеж целых чисел:")
    A = tuple(map(int, input().split()))
    if len(A) == 0:
        print("Пустой кортеж!", file=sys.stderr)
        exit(1)
    bool = False
    i = 0
    while (not bool) and i < len(A)-1:
        if A[i] > A[i+1]:
            intruder_count = i+1
            bool = True
        i += 1
    if bool:
        print("Элемент, нарушающий упорядоченность по возрастанию имеет индекс = ", intruder_count)
    else:
        print("Кортеж полностью упорядочен по возрастанию")
