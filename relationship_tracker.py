"""
ENCAPSULATION STORY 3 ❤️ — “My Relationship Tracker”

Imagine you are a university student in a relationship.

You and your partner have:
  - A "trust level"
  - A "communication score"
  - A "mood" (happy, neutral, upset)

You want to build an app that helps track these,
BUT — people should not just change trust level or mood directly.

You need ENCLOSURE... also known as ENCAPSULATION 💌
"""

from datetime import datetime
LINE = "-" * 65


# ------------------------------------------------------------
# 1) JUST VARIABLES — no boundaries, chaos begins 💥
# ------------------------------------------------------------
print(LINE)
print("1) OPEN RELATIONSHIP DATA (no rules)")

trust = 100
mood = "happy"
print("Start: Trust =", trust, ", Mood =", mood)

# Oops... anyone can change it however they want
trust = -200
mood = "angry forever"
print("Now: Trust =", trust, ", Mood =", mood, "💔 (nonsense!)")

# Lesson:
# Without rules, anyone can mess with relationship data.
# It’s like letting your friends edit your love life directly 😅


# ------------------------------------------------------------
# 2) SIMPLE CLASS — better organized, but still no safety
# ------------------------------------------------------------
print(LINE)
print("2) SIMPLE CLASS (no rules yet)")

class RelationshipPublic:
    """A relationship without boundaries (everything public)."""
    def __init__(self, partner: str):
        self.partner = partner
        self.trust = 100
        self.mood = "happy"

r1 = RelationshipPublic("Peace")
print("Partner:", r1.partner, "| Trust:", r1.trust, "| Mood:", r1.mood)

# Someone from outside edits everything
r1.trust = -999
r1.mood = "blocked"
print("After outside interference:", r1.trust, "|", r1.mood, "💔")


# ------------------------------------------------------------
# 3) ENCAPSULATION — private attributes + safe methods
# ------------------------------------------------------------
print(LINE)
print("3) PRIVATE ATTRIBUTES (rules + safe doors)")

class RelationshipSafe:
    """
    This class hides emotional data behind methods.
    Only the couple can change trust or mood via safe methods.
    """
    def __init__(self, partner: str):
        self.partner = partner
        self._trust = 100
        self._mood = "happy"
        self._communication = 100

    # Setters and Getters (safe access doors)
    def get_trust(self) -> int:
        return self._trust

    def build_trust(self, amount: int) -> None:
        """Increase trust (up to 100)."""
        if amount <= 0:
            raise ValueError("Trust must grow by a positive number.")
        self._trust = min(100, self._trust + amount)

    def break_trust(self, amount: int) -> None:
        """Decrease trust (but not below 0)."""
        if amount <= 0:
            raise ValueError("Damage amount must be positive.")
        self._trust = max(0, self._trust - amount)

    def get_mood(self) -> str:
        return self._mood

    def talk(self, duration_minutes: int) -> None:
        """Talking improves communication and mood."""
        if duration_minutes < 1:
            raise ValueError("You must talk for at least 1 minute.")
        self._communication += duration_minutes
        self._trust = min(100, self._trust + 5)
        self._mood = "happy" if self._trust > 60 else "neutral"

    def ignore_partner(self, days: int) -> None:
        """Ignoring each other damages mood and trust."""
        if days <= 0:
            raise ValueError("Days must be positive.")
        self._trust = max(0, self._trust - days * 5)
        self._mood = "upset" if self._trust < 50 else "neutral"

    def status_report(self) -> str:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return (f"[{ts}] 💑 Relationship with {self.partner}: "
                f"Trust={self._trust} | Mood={self._mood}")


# Try it!
love = RelationshipSafe("Peace")
print(love.status_report())

love.ignore_partner(5)
print("After ignoring for 5 days:")
print(love.status_report())

love.talk(30)
print("After 30 minutes of talking ❤️:")
print(love.status_report())

try:
    love.break_trust(-5)
except ValueError as e:
    print("Blocked nonsense:", e)


# ------------------------------------------------------------
# 4) STRONGER BOUNDARIES — private trust and rules for respect
# ------------------------------------------------------------
print(LINE)
print("4) STRONGER ENCAPSULATION (more realistic rules)")

class RelationshipBounded:
    """
    More rules:
     - trust can't go below 0 or above 100
     - you can't talk forever to fix it instantly
     - private variables (double underscore)
    """
    def __init__(self, partner: str):
        self.__partner = partner
        self.__trust = 100
        self.__mood = "happy"

    def show_status(self):
        print(f"❤️ With {self.__partner} | Trust={self.__trust} | Mood={self.__mood}")

    def hurt_feelings(self, level: int):
        """Decrease trust, never below 0."""
        if level < 0:
            raise ValueError("Level must be positive.")
        self.__trust = max(0, self.__trust - level)
        if self.__trust < 50:
            self.__mood = "sad"
        if self.__trust < 20:
            self.__mood = "heartbroken"

    def say_sorry(self, effort: int):
        """Increase trust, but not instantly perfect."""
        if effort <= 0:
            raise ValueError("Effort must be positive.")
        self.__trust = min(100, self.__trust + effort)
        if self.__trust > 70:
            self.__mood = "happy"
        elif self.__trust >= 40:
            self.__mood = "okay"

    def talk(self, minutes: int):
        """Talking helps repair small issues."""
        if minutes < 1:
            raise ValueError("You must talk for at least 1 minute.")
        boost = min(100 - self.__trust, minutes // 5)
        self.__trust += boost
        self.__mood = "reconnected" if self.__trust > 60 else "neutral"

    def apology_letter(self, sender: str) -> str:
        """Print a small report (shows timestamp and mood)."""
        ts = datetime.now().strftime("%H:%M:%S")
        return f"{sender} wrote at {ts}: 'Trust={self.__trust}, Mood={self.__mood}' 💌"


# Test it out
couple = RelationshipBounded("Peace")
couple.show_status()

couple.hurt_feelings(70)
couple.show_status()

couple.say_sorry(30)
couple.show_status()

print(couple.apology_letter("Josiah"))


# ------------------------------------------------------------
# LESSON 🌹
# ------------------------------------------------------------
"""
Encapsulation in relationships:
- You don’t let everyone directly change your feelings (that’s __trust, __mood).
- You give controlled, safe “doors” like talk(), say_sorry(), hurt_feelings().
- This keeps the relationship in a valid, realistic state.
- Directly editing trust = emotional chaos 😅

In software, same rule:
keep data private, and only allow safe methods to modify it.
"""

print(LINE)
print("❤️ Lesson: Encapsulation protects relationships — and your variables 😅")
