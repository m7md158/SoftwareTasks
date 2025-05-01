# Payment Processing System


## ما تخليش الكود الرئيسي بتاعك مربوط مباشرة بالتفاصيل (زي كلاس معين)،
##  بل اربطه بـ interface 
## أو abstract class، 
## وساعتها التفاصيل (الكلاسات اللي بتنفذ فعلاً) تعتمد عليه.


The flow of control will still follow the same path. However, now both our objects will depend on the abstraction level of the interface. Thus, ClassB inverts its dependency on ClassA. We can also create a class diagram to show how both classes now depended on abstraction:

Abstraction Class Diagram

- high level = it's appear to user
 - abs
   - low level = app