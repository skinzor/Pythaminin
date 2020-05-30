import collections
import concurrent.futures
import time
from pprint import pprint
from os import getpid as process_id

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel'
])

scientist = (
    Scientist(name='Ada Lovelance', field='Math', born=1815, nobel=False),
    Scientist(name='Emmy Noethere', field='Math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='Physics', born=1867, nobel=True),
    Scientist(name='To Youyou', field='Chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='Chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='Astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='Physics', born=1951, nobel=False),
)


def transform(x):
    print(f'Process ID: {process_id()} | Processing record "{x.name}"')
    time.sleep(1)
    result = {'name': x.name, 'age': 2019 - x.born}
    print(f'Process ID: {process_id()} | Done processing "{x.name}"')
    return result


def run():
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as E:
        result = E.map(transform, scientist)
        
    #with concurrent.futures.ProcessPoolExecutor() as E:
    #    result = E.map(transform, scientist)

    end_time = time.time()

    print(f'\nTime to complete: {end_time - start_time:.2f}s\n')
    pprint(tuple(result))


if __name__ == '__main__':
    run()
