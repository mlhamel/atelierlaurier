# -*- coding: utf-8 -*-


def triplets(number=10):
    """ Triplet(s) creation where `number` is the maximum value """
    def _build_triplet(item, number):
        if number - item > 1:
            return range(item, item+3)
        elif number - item == 1:
            return range(item, item+2)
        return ()
    return [_build_triplet(x, number) for x in range(1, number, 3)]


if __name__ == "__main__":
    assert triplets(1) == []
    assert triplets(2) == [range(1, 2)]
    assert triplets(32) == [range(1, 3), range(4, 6), range(7, 9),
                           range(10, 12), range(13, 15), range(16, 18),
                           range(19, 21), range(22, 24), range(25, 27),
                           range(28, 30), range(31, 32)]
