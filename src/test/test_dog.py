from dog import Dog
from person import Person

def test_init_dog_with_name():
    """
    Should be able to initialize a dog with a name.
    """
    dog = Dog('Fido')
    assert dog.name == 'Fido'

def test_can_change_dog_name():
    """
    Should be able to change a dog's name after it 
    is initialized.
    """
    dog = Dog('Fido')
    dog.name = 'Rex'
    assert dog.name == 'Rex'

def test_dog_get_name():
    """
    get_name() should return the name of the dog.
    """
    dog = Dog('Fido')
    assert dog.get_name() == 'Fido'

def test_dog_get_owner():
    """
    get_owner() should return the Person instance 
    associated with the dog
    """
    person = Person('Joe')
    dog = Dog('Fido')
    dog.owner = person
    assert dog.get_owner() == person
