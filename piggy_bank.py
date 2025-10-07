"""
ENCAPSULATION — the friendliest intro 🌱

Day-to-day story:
You have a PIGGY BANK. You put money in. You take money out.
Rules:
- Money cannot be negative.
- You cannot take out more than you have.

We’ll start very simple, see the problem, then fix it bit by bit.
"""

from datetime import datetime

LINE = "-" * 60

# ------------------------------------------------------------
# 1) JUST A NUMBER (no protection at all)
# ------------------------------------------------------------
print(LINE)
print("1) JUST A NUMBER (no rules)")

coins = 100  # I have 100 coins
print("I have:", coins, "coins")

# Oops, anyone can set it to nonsense:
coins = -999
print("Someone set coins to:", coins, "👎 (this makes no real-life sense)")

# Lesson:
# If anyone can change the value to anything, we can get bad or silly states.


# ------------------------------------------------------------
# 2) A SIMPLE BOX (a class) — still PUBLIC (not safe yet)
# ------------------------------------------------------------
print(LINE)
print("2) A SIMPLE BOX (public, still not safe)")

class PiggyBoxPublic:
    # This is just a box that holds coins, but the door is always open.
    def __init__(self, coins: int = 0):
        self.coins = coins  # public: anyone can change this freely

boxA = PiggyBoxPublic(100)
print("BoxA started with:", boxA.coins)

# Anyone can break the rules:
boxA.coins = -500  # direct write… no checks
print("BoxA after naughty change:", boxA.coins, "👎")


# ------------------------------------------------------------
# 3) ENCAPSULATION IDEA: hide inside + only safe doors (methods)
#    We make the coins "internal" and offer safe actions.
# ------------------------------------------------------------
print(LINE)
print("3) PIGGY BANK with simple ENCAPSULATION (safe doors)")

class PiggyBank:
    """
    Think of this bank like a box with a lid.
    The coins live inside as _coins (underscore means 'please don't touch directly').
    We use methods (put_in, take_out, how_much) as the only doors to change or read.
    """
    def __init__(self, opening_coins: int = 0):
        # Keep the real amount 'inside' the box
        self._coins = 0
        self.put_in(opening_coins)  # use our own door so rules apply

    def put_in(self, amount: int) -> None:
        # Only positive amounts make sense
        if amount <= 0:
            raise ValueError("You can only put in a positive number of coins.")
        self._coins += amount

    def take_out(self, amount: int) -> None:
        # Only positive and not more than we have
        if amount <= 0:
            raise ValueError("You must take out a positive number of coins.")
        if amount > self._coins:
            raise ValueError("You cannot take more coins than you have.")
        self._coins -= amount

    def how_much(self) -> int:
        # Read-only peek at how many coins are inside
        return self._coins

# Try it!
bank = PiggyBank(50)         # start by putting in 50 safely
print("Start:", bank.how_much(), "coins")
bank.put_in(30)              # now 80
print("After put_in(30):", bank.how_much(), "coins")
bank.take_out(20)            # now 60
print("After take_out(20):", bank.how_much(), "coins")

# Try to break rules:
try:
    bank.take_out(999)       # more than we have
except ValueError as e:
    print("Blocked silly action:", e)


# ------------------------------------------------------------
# 4) MAKE THE RULES A BIT STRONGER — capacity and receipt
#    - Add a maximum capacity (the box is small!)
#    - Add a receipt line to show what happened and when
# ------------------------------------------------------------
print(LINE)
print("4) ENCAPSULATION + extra RULES (capacity) and a receipt")

class PiggyBankPlus:
    """
    Same piggy bank, but:
    - has a maximum capacity (like a small tin)
    - prints a friendly receipt when asked
    """
    def __init__(self, opening_coins: int = 0, max_capacity: int = 200):
        self._coins = 0
        self._max_capacity = int(max_capacity)
        if self._max_capacity <= 0:
            raise ValueError("Capacity must be positive.")
        if opening_coins < 0:
            raise ValueError("Opening coins cannot be negative.")
        if opening_coins > self._max_capacity:
            raise ValueError("Opening coins exceed capacity.")
        self._coins = opening_coins

    def put_in(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Put-in must be positive.")
        if self._coins + amount > self._max_capacity:
            raise ValueError("Too many coins! The box will overflow.")
        self._coins += amount

    def take_out(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Take-out must be positive.")
        if amount > self._coins:
            raise ValueError("Cannot take more than you have.")
        self._coins -= amount

    def how_much(self) -> int:
        return self._coins

    def receipt(self, title: str = "Piggy Receipt") -> str:
        # One tidy line to show state + time (very common in real systems)
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{title} | coins={self._coins} | capacity={self._max_capacity} | time={ts}"

big = PiggyBankPlus(opening_coins=100, max_capacity=150)
print("Big start:", big.how_much(), "coins (cap 150)")
big.put_in(40)
print("After put_in(40):", big.how_much(), "coins")
try:
    big.put_in(20)  # would overflow (100+40+20=160 > 150)
except ValueError as e:
    print("Blocked overflow:", e)
print(big.receipt("End of Day"))


# ------------------------------------------------------------
# 5) WHY NOT JUST TOUCH THE _coins DIRECTLY?
#    Because then we can put nonsense again. That breaks the rules.
# ------------------------------------------------------------
print(LINE)
print("5) WHAT IF we poke _coins directly? (Don't do this)")

sneaky = PiggyBankPlus(10, max_capacity=50)
print("Sneaky start:", sneaky.how_much())

# You *could* try to cheat (underscore is only a warning sign).
# In real life, teammates agree not to do this. It's a social + code rule.
sneaky._coins = -12345  # 😈 bypassed the door (BAD PRACTICE)
print("Sneaky after direct poke:", sneaky.how_much(), "(nonsense)")

# Lesson:
# Encapsulation says: "Please, always use the doors (methods)."
# In languages like Java/C#, the doors are more strictly enforced.
# In Python, we rely on good habits + clear method design.


# ------------------------------------------------------------
# 6) “PRIVATE-ISH” with name-mangling (__coins) — optional peek
#    This makes accidents harder (but still NOT bulletproof security).
# ------------------------------------------------------------
print(LINE)
print("6) PRIVATE-ish (name-mangling) — fewer accidents")

class SaferPiggy:
    def __init__(self, opening: int = 0):
        self.__coins = 0     # double underscore
        if opening < 0:
            raise ValueError("Opening cannot be negative.")
        self.__coins = opening

    def put_in(self, amount: int):
        if amount <= 0:
            raise ValueError("Must be positive.")
        self.__coins += amount

    def take_out(self, amount: int):
        if amount <= 0:
            raise ValueError("Must be positive.")
        if amount > self.__coins:
            raise ValueError("Not enough coins.")
        self.__coins -= amount

    def how_much(self) -> int:
        return self.__coins

safe = SaferPiggy(20)
safe.put_in(10)
print("SaferPiggy has:", safe.how_much())

# The name is mangled, so this breaks:
try:
    print(safe.__coins)  # AttributeError
except AttributeError as e:
    print("Direct access blocked:", e)

# But Python stores it under a special name internally:
print("Mangled name seen in dir():", [n for n in dir(safe) if "coins" in n])

print(LINE)
print("Done! You just saw:")
print("• Why raw public data can go wrong")
print("• How 'doors' (methods) protect your data")
print("• How extra rules (like capacity) prevent silly states")
print("• Why Python uses naming + good habits to encourage encapsulation")
