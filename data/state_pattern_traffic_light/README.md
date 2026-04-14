# Algorithm name

State Design Pattern (Traffic Light)

# Author

Victor Manuel Montini(2026-04-10)

# Algorithm description

The State Pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class. Here, a `TrafficLight` changes its response to a `request()` call based on whether its current state object is `RedLight` or `GreenLight`.

# Model used to create the base code

Gemini 3.

### Prompt

```
Write a Java implementation of the State Design Pattern. Use a traffic light system as an example where a `TrafficLight` context changes its behavior based on its current state (`RedLight`, `GreenLight`). Each state should be able to transition the context to the next state. All identifiers must be in English.
```

# Obfuscated version

Manually obfuscated by abstracting the state-machine logic into unreadable class names (`_R`, `_G`, `_C`) and minimizing method signatures.
