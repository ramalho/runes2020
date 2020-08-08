import collections
import pytest
import functools

from assign import count_attr

Card = collections.namedtuple('Card', 'rank suit')

sample = [
    [Card('A', 'spades'), # 0
     Card('A', 'hearts'),
     Card('2', 'clubs'),
     Card('2', 'spades'),
     Card('3', 'clubs'),
     Card('4', 'clubs'),],
    [Card('A', 'clubs'),  # 1
     Card('2', 'clubs'),
     Card('2', 'spades'),
     Card('3', 'clubs'),
     Card('4', 'clubs'),],
    [Card('A', 'diamonds'), # 2
     Card('A', 'hearts'),
     Card('A', 'spades'),
     Card('2', 'clubs'),
     Card('2', 'spades'),],
]

@pytest.mark.parametrize('attr_name, attr_value, want', [
    ('rank', '3', 1),
    ('rank', 'A', 2),
    ('suit', 'clubs', 3),
    ('suit', 'leisure', 0),
])
def test_count_attr(attr_name, attr_value, want):
    assert count_attr(sample[0], attr_name, attr_value) == want
    count = functools.partial(count_attr,
        attr_name=attr_name, attr_value=attr_value)
    assert count(sample[0]) == want

@pytest.mark.parametrize('attr_name, attr_value, want', [
    ('rank', '3', [sample[2], sample[0], sample[1]]),
    ('rank', 'A', [sample[1], sample[0], sample[2]]),
    ('suit', 'clubs', [sample[2], sample[0], sample[1]]),
    ('suit', 'leisure', sample),
])
def test_sort(attr_name, attr_value, want):
    count = functools.partial(count_attr,
        attr_name=attr_name, attr_value=attr_value)
    assert sorted(sample, key=count) == want
