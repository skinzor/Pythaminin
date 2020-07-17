# Immutable Data Structures: Tuples #
import collections
from functools import reduce

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])

scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='math', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='physics', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='chemistry', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

name_and_age = tuple(map(
    lambda x: {"name": x.name, 'age': 2020 - x.born},
    scientists
))

total_age = reduce(
    lambda acc, val: acc + val["age"],
    name_and_age,
    0
)
print(total_age)