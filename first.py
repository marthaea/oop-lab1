class Phone:
    def __init__(self, brand, number, storage, ringtone):
        self.brand = brand
        self.number = number
        self.storage = storage  # in GB
        self.ringtone = ringtone

    def call(self, target_number):
        print(f"{self.number} is calling {target_number}...")

    def change_ringtone(self, new_ringtone):
        print(f"Changing ringtone from '{self.ringtone}' to '{new_ringtone}'")
        self.ringtone = new_ringtone

    def display_info(self):
        print(f"Phone Info:")
        print(f"  Brand: {self.brand}")
        print(f"  Number: {self.number}")
        print(f"  Storage: {self.storage}GB")
        print(f"  Ringtone: {self.ringtone}")


# Example usage
phone1 = Phone("Samsung", "+256700123456", 128, "Over the Horizon")
phone2 = Phone("iPhone", "+256772987654", 256, "Reflection")

phone1.display_info()
phone1.call(phone2.number)
phone2.change_ringtone("Marimba")
phone2.display_info()