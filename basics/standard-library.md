---
description: What is the standard library include
---

# Standard Library

### get\_screen\_size()

Returns the size of the screen as a structure of (width, height) To get a specific value, you can use the following syntax:

```csharp
include "std.v";
usize screen_width = get_screen_size()::width;
usize screen_height = get_screen_size()::height;
out << screen_width << "x" << screen_height << bright_blue;
```

### get\_pass()

Returns the password entered by the user encoded in `UTF 32 LE`

```csharp
include "std.v";
usize password = get_pass("Enter Password: ");
out << "Encoded" << password << bright_red;
out << "Decoded" << password::decode("utf-32-le") << bright_green;
```
