#Chore Class
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)   # inheriting name from Person
        self.school = school

class Boy(Student):
    def __init__(self, name, school, favourite_song):
        super().__init__(name, school)
        self.favourite_song = favourite_song

class Girl(Student):
    def __init__(self, name, school, favourite_song_taste):
        super().__init__(name, school)
        self.favourite_song_taste = favourite_song_taste

    def write_letter(self, address):
        print(f"{self.name} writes a love letter addressed to '{address}'.")

    def choose_boy(self, boy1, boy2):
        print("\nNow she must choose between the two boys based on her music taste...")
        if boy1.favourite_song in self.favourite_song_taste:
            print(f"{self.name} chooses {boy1.name} because she loves his favourite song '{boy1.favourite_song}'.")
        elif boy2.favourite_song in self.favourite_song_taste:
            print(f"{self.name} chooses {boy2.name} because she loves his favourite song '{boy2.favourite_song}'.")
        else:
            print(f"{self.name} cannot decide — neither boy's song matches her taste.")

# Story Simulation
def story():
    # The two schools
    school_real = "Namiryango College"
    school_wrong = "Namiryango Secondary School"

    # The two boys
    boy1 = Boy("Elias", school_real, "Moonlight Lullaby")
    boy2 = Boy("Michael", school_wrong, "Summer Serenade")

    # The girl
    girl = Girl("Dora", "St. Mary's Girls", ["Summer Serenade", "River Whisper"])

    # The mix-up
    print(f"Dora wants to write to {boy1.name} at {boy1.school}, but she mishears and writes the address '{school_wrong}' instead.\n")
    girl.write_letter(school_wrong)

    print(f"\nThe letter goes to {boy2.name} at {boy2.school}, who starts replying instead of Elias.")
    print(f"{boy2.name} is charming and romantic, and Aisha falls for him — thinking he's Elias.\n")

    print("Later, she discovers the truth: she has been talking to the wrong boy!")

    # She now chooses based on favourite songs
    girl.choose_boy(boy1, boy2)

# Runing the story
if __name__ == "__main__":
    story()
