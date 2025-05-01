# Abstract Products
class Engine:
    def design(self):
        pass

class Tire:
    def produce(self):
        pass

# Concrete Products for Economic Car
class EconomicEngine(Engine):
    def design(self):
        print("Designing economic engine")

class EconomicTire(Tire):
    def produce(self):
        print("Producing economic tires")

# Concrete Products for Luxury Car
class LuxuryEngine(Engine):
    def design(self):
        print("Designing luxury engine")

class LuxuryTire(Tire):
    def produce(self):
        print("Producing luxury tires")

# Abstract Factory
class CarFactory:
    def create_engine(self) -> Engine:
        pass

    def create_tire(self) -> Tire:
        pass

# Concrete Factory for Economic Cars
class EconomicCarFactory(CarFactory):
    def create_engine(self):
        return EconomicEngine()

    def create_tire(self):
        return EconomicTire()

# Concrete Factory for Luxury Cars
class LuxuryCarFactory(CarFactory):
    def create_engine(self):
        return LuxuryEngine()

    def create_tire(self):
        return LuxuryTire()

# Client code
def build_car(factory: CarFactory):
    engine = factory.create_engine()
    tire = factory.create_tire()

    engine.design()
    tire.produce()

# Test
print("Economic Car:")
build_car(EconomicCarFactory())

print("\nLuxury Car:")
build_car(LuxuryCarFactory())
