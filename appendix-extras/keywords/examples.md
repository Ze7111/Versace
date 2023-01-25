---
description: This is an example use case of all the Keywords in Versace.
---

# Examples

### Public

```csharp
public init() {
    out << "runs when the program starts";
}
public update() {
    out << "runs every cpu cycle";
}
public close() {
    out << "runs when the program closes";
}
func init() {
    out << "runs when this is called, due to public functions being overloaded";
}
```

### Private

```csharp
priv func someFunction() {
    out << "only runs when called through out";
}
priv int func someFunction2() {
    out << "only runs when called through out and returns an int";
    return 0;
}
priv someVariable = "some value can be any type";
```

### If, Else, Else If

```csharp
if (true) {
    out << "runs if true";
} else if (false) {
    out << "runs if false";
} else {
    out << "runs if none of the above are true";
}
```

### While

```csharp
int i = 0;
while (i < 10) {
    out << i;
    let i += 1;
}
```

### Both types of for loops

```csharp
for (int i = 0 | i < 10 | i += 1) {
    out << i;
}
list someList = [1, 2, 3, 4, 5];
for (i in someList) {
    out << i;
}
```

### Structures

```csharp
struct someStruct {
    int someInt;
    str someStr;
}
usize structInstance = someStruct(100, "some string"); // this is how you create a structure instance with a constructor

let someStruct::someInt = 0; // this modifies the original structure
let someStruct::someStr = "some string"; // this modifies the original structure

out << someStruct::someInt << structInstance;
```

### Classes

```csharp
class someClass {
    func repr(self) {
        in a << "name? :";
        let self::name = a;
    }
    func someFunction(self) {
        out << "some function";
        out << self::name;
    }
}
usize classInstance = someClass();
let classInstance::someFunction();
```

### Methods

```csharp
method someMethod(fun, data | arg1) {
    if (data == "yes") {
        fun(~args, ~~kwargs);
    } else {
        fun(arg1);
    }
}

@someMethod("no")
func someFunction(arg1) {
    out << data << arg1;
}
 
@someMethod("yes")
func someFunction2(~args, ~~kwargs) {
    out << args << kwargs;
}
```

### Constants

```csharp
const int someConstant = 100;
```

### Final

```csharp
int someFinal = 100
final someFinal;
```

### Including

```csharp
include "Winui.vh" as winui; 
include "std.v";

public init() {
    str size = f"{get_screen_size()::width - 100}x{get_screen_size()::height - 100}";
    winui::geometry(size);
    button = ttk::Button(winui, text="Click me!", command=winui::quit, width=25); 
    // center the button in the middle of the window both vertically and horizontally
    button::pack(expand=True);
    winui::mainloop();
}
```

### Async

```csharp
async func someFunction() {
    out << "runs async";
}
```

### Await

```csharp
async func someFunction() {
    for (int i = 0 | i < 10 | i += 1) {
        out << i;
        wait(0.3);
    }
}
await someFunction();
```

### Coroutines

```csharp
async func myFunction() {
    for (int i = 0 | i < 10 | i += 1) {
        out << i;
        wait(0.3);
    }
}

async func myFunction2() {
    for (int i = 0 | i < 10 | i += 1) {
        out << i;
        wait(0.3);
    }
}
 
async func myFunction3() {
    for (int i = 0 | i < 10 | i += 1) {
        out << i;
        wait(0.3);
    }
}
// coroutine auto_clear = True;
coroutine myFunction() | myFunction2() | myFunction3(); 
coroutine exec(myFunction() | myFunction2());
coroutine exec();
coroutine delete(myFunction());
coroutine clear();
```

### Try, Except, Finally

```csharp
try {
    out << "runs if no errors";
} except Exception {
    out << "runs if there is an error";
} finally {
    out << "runs no matter what";
}
```

### Throw

```csharp
throw Exception("some error");
```

### With

```csharp
with open("someFile.txt", "r") as file:
    out << file::read();
```

### All Data Types Including Low Level Types

```csharp
class MyClass {
    func repr(self) {
        return NULL;
    }
}
int a = 100;
str b = "some string";
list c = [1, 2, 3, 4, 5];
dict d = {"a": 1, "b": 2, "c": 3};
tuple e = (1, 2, 3, 4, 5);
set f = {1, 2, 3, 4, 5};
bool g = true;
float h = 1.0;
double i = 1.0;
usize j = MyClass();
bytes k = b"some bytes";
char l = "a";
memoryview m = memoryview(b"some bytes");
bytearray n = bytearray(b"some bytes");
range o = range(0 | 10);
// Low level types
u8 p;
u16 q;
u32 r;
u64 s;
i8 t = 127;
i16 u = 32767;
i32 v = 2147483647;
i64 w = 9223372036854775807;
i128 x = 170141183460469231731687303715884105727;
f32 y = 1.0;
f64 z = 1.0;
out << a << b << c << d << e << f << g << h << i << j << k << l << m << n << o << p << q << r << s << t << u << v << w << x << y << z;
```

### Pyc

```csharp
pyc file = "someFile.py";
pyc "print('hello world')";
pyc "for i in range(10):";
pyc "    print(i)";
```
