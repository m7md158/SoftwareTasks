## The Interface Segregation Principle (ISP) is one of the SOLID principles of object-oriented design. It states:

- "Clients should not be forced to depend on interfaces they do not use."

## Analysis of the Provided Diagram:
 In the current diagram:

 - The Shape interface includes the method area(params): void.

 - The 3DShape interface extends Shape and adds volume(params): void.

 - Cylinder implements 3DShape, thus requiring both area() and volume().

 - Square and Circle implement Shape, requiring only area().

 - This violates ISP because:

 - The 3DShape interface inherits area() from Shape, forcing every 3D shape to implement an area, even when some 3D shapes might not need it or may calculate it differently.

✅ Corrected Diagram Following ISP:
Break the interfaces into smaller, more specific ones:


## ✅ Benefits:
 - Square and Circle only depend on the AreaCalculable interface.

 - Cylinder depends on both AreaCalculable and VolumeCalculable, which it actually uses.

 - This respects the Interface Segregation Principle.




## two ways for solving this task
 - one file
 - seprated file


🔁 بهذا الشكل:

كل كلاس يعتمد فقط على الواجهات التي يحتاجها (no unused methods).

لا يوجد أي كلاس مجبر على تنفيذ دوال لا يحتاجها.