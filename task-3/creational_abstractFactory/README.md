##  🏭 مفهوم Abstract Factory Pattern:
- It is a design pattern used to create families of related objects without specifying their concrete classes directly. In other words, it separates object creation from object usage

## 🧠 Main Idea: Car factoring 

1. We have two types of cars:

 - Economic Car

 - Luxury Car

2. Each type includes two components:

 - Engine

 - Tire

For each type, the engine and tires are different.


## 🧩 Steps:

1. Create the abstract products: Engine, Tire.

2. Create the concrete products for each car type.

3. Create the abstract factory: CarFactory.

4. Create the concrete factories: EconomicCarFactory, LuxuryCarFactory.


