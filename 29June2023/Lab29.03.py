# Has A Relationship Example

class Engine:

    def boot_engine(self):
        print("Booted!")


class Vehicle:

    def start_engine(self):
        Engine().boot_engine()
        print("Start Engine")


v = Vehicle()
v.start_engine()