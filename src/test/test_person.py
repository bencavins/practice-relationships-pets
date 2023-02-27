from person import Person
from dog import Dog


def test_init_person_with_name():
    person = Person('Joe')
    assert person.name == 'Joe'

def test_person_get_name():
    person = Person('Joe')
    assert person.get_name() == 'Joe'
