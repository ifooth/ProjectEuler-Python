# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import collections
import itertools
import math
import operator


def accumulate(iterable, func=operator.add):
    """
    Return running totals
    accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    """

    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total


def combinations(n, k):
    """
    组合数
    C(n, k) = n! / (k! * (n - k)!) k <= n
    """
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


class NotRanked(Exception):
    pass


class Poker(object):
    """扑克牌类, 需要实现比较方法
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
    heart 红桃 spade 黑桃 club 梅花 diamond 方块
    """
    POKERS = '23456789TJQKA'
    RANKS = [
        'high_card',
        'one_pair',
        'two_pairs',
        'three_of_kind',
        'straight',
        'flush',
        'full_house',
        'four_of_kind',
        'straight_flush',
        'royal_flush'
    ]

    def __init__(self, card):
        """
        ['8C', 'TS', 'KC', '9H', '4S']
        """
        self.card = card
        self.counter = sorted(
            collections.Counter([i[0] for i in self.card]).items(),
            key=lambda x: x[1], reverse=True)
        self.rank = ''
        self.rank_score = 0
        self.values = []
        self.values_score = []
        self()

    @property
    def sorted_card(self):
        card = ''.join([i[0] for i in sorted(self.card, cmp=(
            lambda x, y: self.POKERS.index(x[0]) - self.POKERS.index(y[0])))])
        return card

    def royal_flush(self):
        if len(set([i[1] for i in self.card])) != 1:
            raise NotRanked()
        if self.sorted_card != 'TJQKA':
            raise NotRanked()

    def straight_flush(self):
        if len(set([i[1] for i in self.card])) != 1:
            raise NotRanked()
        if self.sorted_card not in self.POKERS:
            raise NotRanked()

    def four_of_kind(self):
        if [i[1] for i in self.counter] != [4, 1]:
            raise NotRanked()

    def full_house(self):
        if [i[1] for i in self.counter] != [3, 2]:
            raise NotRanked()

    def flush(self):
        if len(set([i[1] for i in self.card])) != 1:
            raise NotRanked()

    def straight(self):
        if self.sorted_card not in self.POKERS:
            raise NotRanked()

    def three_of_kind(self):
        if [i[1] for i in self.counter] != [3, 1, 1]:
            raise NotRanked()

    def two_pairs(self):
        if [i[1] for i in self.counter] != [2, 2, 1]:
            raise NotRanked()

    def one_pair(self):
        if [i[1] for i in self.counter] != [2, 1, 1, 1]:
            raise NotRanked()

    def high_card(self):
        pass

    def __str__(self):
        return '<Poker, %s>' % self.rank

    def __repr__(self):
        return '<Poker, %s>' % self.rank

    def __call__(self):
        for rank in self.RANKS[::-1]:
            _ranked = getattr(self, rank)
            try:
                _ranked()
                self.rank = rank
                self.rank_score = self.RANKS.index(rank)
                values = []
                for i in itertools.groupby(self.counter, key=lambda x: x[1]):
                    values.extend(sorted(i[1], cmp=(
                        lambda x, y: self.POKERS.index(y[0]) -
                        self.POKERS.index(x[0]))))
                self.values = values
                self.values_score = [self.POKERS.index(i[0]) for i in values]
                return
            except NotRanked:
                pass

    def __cmp__(self, other):
        """
        小于返回负数
        等于返回0
        大于返回正数
        """
        score = self.rank_score - other.rank_score
        if score != 0:
            return score
        for i in range(len(self.values_score)):
            score = self.values_score[i] - other.values_score[i]
            if score != 0:
                return score
        return 0
