# ----------------------------
# Base Class
# ----------------------------
class Person:
    def __init__(self, name):
        self.name = name

# ----------------------------
# Derived Class
# ----------------------------
class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

# ----------------------------
# Boys (Inheritance + Polymorphism)
# ----------------------------
class Boy(Student):
    def reply_to_letter(self, girl_name):
        """Base version — will be overridden"""
        print(f"{self.name} replies politely to {girl_name}.")

class ShyBoy(Boy):
    def reply_to_letter(self, girl_name):
        print(f"{self.name}: 'Hi {girl_name}, I'm happy to get your letter. I’m not good with words, but I care about you.'")

class SmoothTalker(Boy):
    def reply_to_letter(self, girl_name):
        print(f"{self.name}: 'Dearest {girl_name}, your words light up my day. I think of you all the time.'")

# ----------------------------
# Girl Class
# ----------------------------
class Girl(Student):
    def write_letter(self, address):
        print(f"{self.name} writes a love letter to '{address}'.")
    
    def choose_boy(self, boy1, boy2):
        print("\nNow she must choose based on who touched her heart the most.")
        boy1_song = "Moonlight Lullaby"
        boy2_song = "Summer Serenade"
        taste = ["Summer Serenade"]

        if boy1_song in taste:
            print(f"{self.name} chooses {boy1.name}.")
        elif boy2_song in taste:
            print(f"{self.name} chooses {boy2.name}.")
        else:
            print(f"{self.name} can't decide — both boys are sweet in their own way!")

# ----------------------------
# Story Simulation
# ----------------------------
def story():
    # The two boys at different schools
    shy_boy = ShyBoy("Elias", "Namiryango College")
    smooth_boy = SmoothTalker("Michael", "Namiryango Secondary School")

    # The girl
    aisha = Girl("Aisha", "St. Mary's Girls")

    # Mix-up in address
    correct_school = "Namiryango College"
    wrong_school = "Namiryango Secondary School"

    print(f"Aisha wants to write to {shy_boy.name} at '{correct_school}',")
    print(f"but she mishears and sends it to '{wrong_school}' instead.\n")

    aisha.write_letter(wrong_school)
    print(f"\nLetter arrives at {smooth_boy.school} — {smooth_boy.name} receives it!")
    smooth_boy.reply_to_letter(aisha.name)

    print(f"\nMeanwhile, {shy_boy.name} never receives any letter...")
    print(f"When Aisha discovers the truth, she meets both boys again.\n")

    # Both reply again (polymorphism in action)
    shy_boy.reply_to_letter(aisha.name)
    smooth_boy.reply_to_letter(aisha.name)

    # Final choice
    aisha.choose_boy(shy_boy, smooth_boy)

# Run the story
if __name__ == "__main__":
    story()


## OUTPUT
Aisha wants to write to Elias at 'Namiryango College',
but she mishears and sends it to 'Namiryango Secondary School' instead.

Aisha writes a love letter to 'Namiryango Secondary School'.

Letter arrives at Namiryango Secondary School — Michael receives it!
Michael: 'Dearest Aisha, your words light up my day. I think of you all the time.'

Meanwhile, Elias never receives any letter...
When Aisha discovers the truth, she meets both boys again.

Elias: 'Hi Aisha, I'm happy to get your letter. I’m not good with words, but I care about you.'
Michael: 'Dearest Aisha, your words light up my day. I think of you all the time.'

Now she must choose based on who touched her heart the most.
Aisha chooses Michael.


