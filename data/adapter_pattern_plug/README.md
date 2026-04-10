# Algorithm name

Adapter Design Pattern (Electricity Plug)

# Author

Victor Manuel Montini (2026-04-10)

# Algorithm description

The Adapter Pattern is a structural design pattern that allows objects with incompatible interfaces to collaborate. It acts as a wrapper that catches calls to one interface and transforms them into a format that the second object expects. This example adapts a US-style plug to a European socket.

# Model used to create the base code

Gemini 3

### Prompt

```
Create an Adapter Design Pattern in Python. Implement a scenario where a `USPlug` (providing 110V) needs to be adapted to work with a `EuropeanSocket` interface. The code should clearly show the wrapping of the adaptee and use descriptive English names.
```

# Obfuscated version

Manually obfuscated by renaming classes to `_U`, `_E`, and `_A` and using f-string concatenation to hide the adaptation logic.
