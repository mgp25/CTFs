## El ninja contrareloj

We are given a binary `secadmin.so`. Our mission is to obtain the correct flag.

When you look at the assembly, you will notice that it compares two bytearrays (`s` and `j`), if both are equal, then the input flag is correct, otherwise you will need to try harder.

The input string will be transformed doing substitutions using different operations like XORs, and putting the result of it to `j`.

There is a hint we can use to check wether our code is doing fine or not, and it is the fact that the flag is starting like this: `secadmin{` which will be `0x91, 0x87, 0xEE, 0xEC, 0x2C, 0x25, 0x21, 0x0E, 0x1B` after all the transformations. Guest what? Matches with the first 9 bytes from `s` byte array.

This can be easily reproduced but we need to obtain first the timer values. Notice that easch function is being run in a separate thread, and one of these functions uses a counter value (time) to perform some operations. All the timer values are: 

```python
t_values = bytearray([0x74, 0x74, 0x1b, 0x1b, 0xde, 0xde, 0xde, 0xf6, 0xf6, 0x67, 0x67, 0x67, 0x8b, 0x8b, 0x5a, 0x5a, 0x5a, 0x67, 0x67, 0x34, 0x34, 0x34])
```

From `s` bytearray we can also know the flag length, which in this case is 22.
 