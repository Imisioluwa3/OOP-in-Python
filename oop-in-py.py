class Superhero:
    def __init__(self, name, nickname, phrase):
        self.name = name
        self.phrase = phrase
        self.nickname = nickname
        
    def details(self):
        print(f"Previous on {self.nickname}\n")
        print(f"My name is {self.name}, {self.phrase}")
        
# intro = Superhero("Barry Allen", "The Flash", " and I am the fastest man alive")
intro = Superhero("Bruce Wayne", "Batman", "I am the Batman")
intro.details()

# Create a readme.md for this file
