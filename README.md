# practice-relationships-pets

# Deliverables:
## Initializers, Readers, Writers
Dog
- `Dog __init__(self, name)`
    - `Dog` is initialized with a name (string)
    - name *can* be changed after the dog is initialized
- `Dog get_name()`
    - returns the dog's name

Person
- `Person __init__(self, name)`
     - `Person` is initialized with a name (string)
- `Person get_name()`
    - returns the person's name

## Object Relationship Methods
Dog
- `Dog get_owner()`
    - returns the `Person` instance associated with the `Dog` instance.

Person
- `Person get_pets()`
    returns a list of `Dog` instances associated with the `Person` instance.