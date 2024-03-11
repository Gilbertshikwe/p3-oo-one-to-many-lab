class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all_pets() if isinstance(pet.owner, Owner) and pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type. Must be an instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        owner_pets = self.pets()
        return sorted(owner_pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets_list = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type. Must be one of: dog, cat, rodent, bird, reptile, exotic.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.__class__.all_pets_list.append(self)

    @classmethod
    def all_pets(cls):
        return cls.all_pets_list

owner1 = Owner("John")
owner2 = Owner("Jane")

pet1 = Pet("Buddy", "dog", owner1)
pet2 = Pet("Whiskers", "cat", owner1)
pet3 = Pet("Tweety", "bird", owner2)


owner1.add_pet(pet1)
owner1.add_pet(pet2)
owner2.add_pet(pet3)

sorted_pets = owner1.get_sorted_pets()

# Print results
print("Owner 1's Pets:", [pet.name for pet in sorted_pets])
