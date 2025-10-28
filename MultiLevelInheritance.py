class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

class Boy(Student):
    def __init__(self, name, school, favourite_song):
        super().__init__(name, school)
        self.favourite_song = favourite_song

class Girl(Student):
    def __init__(self, name, school):
        super().__init__(name, school)

    def write_letter(self, boy, written_school):
        print(f"{self.name} writes a letter to {boy.name}, addressed to '{written_school}'.")

# Story
aisha = Girl("Aisha", "St. Mary's Girls")
elias = Boy("Elias", "Namiryango College", "Moonlight Lullaby")
michael = Boy("Michael", "Namiryango Secondary School", "Summer Serenade")

# Mix-up
aisha.write_letter(elias, "Namiryango Secondary School")

#Output
Aisha writes a letter to Elias, addressed to 'Namiryango Secondary School'.
But the letter ends up with Michael instead!
Michael's favourite song is 'Summer Serenade', and Aisha falls for him.

print(f"But the letter ends up with {michael.name} instead!")

print(f"{michael.name}'s favourite song is '{michael.favourite_song}', and Aisha falls for him.")
