import collections

Scientists = collections.namedtuple('Scientist', [
    'name',
    'field',
    'birth',
    'nobel'
])

ada = Scientists(name="Ada Lovelace", field="Mathematics", birth=1815, nobel=False)
marie = Scientists(name="Marie Curie", field="Mathematics", birth=1882, nobel=False)

print(f"{ada.name} was born in {ada.birth}. [{ada.field}]")
