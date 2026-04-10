# Algorithm name

Singleton Design Pattern (Database Connection)

# Author

Victor Manuel Montini (2026-04-10)

# Algorithm description

The Singleton Pattern is a creational design pattern that ensures a class has only one instance while providing a global access point to that instance. This implementation uses the `__new__` method in Python to control object creation and prevent multiple instantiations of a database connection simulator.

# Model used to create the base code

Gemini 3.

### Prompt

```
Implement a Singleton Design Pattern in Python using the `__new__` method. The example should simulate a `DatabaseConnection` class that ensures only one instance is created throughout the execution. Include a simple method to retrieve data and use English for all identifiers.
```

# Obfuscated version

Manually obfuscated by shortening class and instance attributes to single characters (`_D`, `_i`) and minifying the logic flow.

Folder: adapter_pattern_plug (Python)

File: README.md
Markdown

# Algorithm name

Adapter Design Pattern (Electricity Plug)

# Author

Gemini (2026-04-10)

# Algorithm description

The Adapter Pattern is a structural design pattern that allows objects with incompatible interfaces to collaborate. It acts as a wrapper that catches calls to one interface and transforms them into a format that the second object expects. This example adapts a US-style plug to a European socket.

# Model used to create the base code

Manually crafted.

### Prompt

Create an Adapter Design Pattern in Python. Implement a scenario where a USPlug (providing 110V) needs to be adapted to work with a EuropeanSocket interface. The code should clearly show the wrapping of the adaptee and use descriptive English names.

# Obfuscated version

Manually obfuscated by renaming classes to `_U`, `_E`, and `_A` and using f-string concatenation to hide the adaptation logic.

Folder: observer_pattern_news (Python)

File: README.md
Markdown

# Algorithm name

Observer Design Pattern (News Agency)

# Author

Gemini (2026-04-10)

# Algorithm description

The Observer Pattern is a behavioral design pattern that defines a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing. In this case, a news agency notifies its registered subscribers whenever a new message is broadcasted.

# Model used to create the base code

Manually crafted.

### Prompt

Write a Python implementation of the Observer Design Pattern. Create a NewsAgency (Subject) that maintains a list of NewsSubscriber objects (Observers). When the agency notifies subscribers, they should update their state. All code and comments must be in English.

# Obfuscated version

Manually obfuscated by replacing the list and method names with non-descriptive tokens (`_Ag`, `_s`, `_n`) and removing all internal strings.

Folder: adapter_pattern_media (Java)

File: README.md
Markdown

# Algorithm name

Adapter Design Pattern (Media Player)

# Author

Gemini (2026-04-10)

# Algorithm description

This structural pattern allows the integration of an existing class (`AdvancedAudioPlayer`) into a new interface (`MediaPlayer`) that it originally did not support. The `AudioAdapter` class bridges the gap by implementing the target interface and delegating the work to the adaptee.

# Model used to create the base code

Manually crafted.

### Prompt

Implement the Adapter Design Pattern in Java. Create a MediaPlayer interface and an AdvancedAudioPlayer class that plays VLC files. Write an AudioAdapter class that implements the MediaPlayer interface to make the advanced player compatible. Use standard Java naming conventions and English.

# Obfuscated version

Manually obfuscated by stripping descriptive Java class names and using single-letter identifiers for interfaces and methods.

Folder: state_pattern_traffic_light (Java)

File: README.md
Markdown

# Algorithm name

State Design Pattern (Traffic Light)

# Author

Gemini (2026-04-10)

# Algorithm description

The State Pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class. Here, a `TrafficLight` changes its response to a `request()` call based on whether its current state object is `RedLight` or `GreenLight`.

# Model used to create the base code

Manually crafted.

### Prompt

Write a Java implementation of the State Design Pattern. Use a traffic light system as an example where a TrafficLight context changes its behavior based on its current state (RedLight, GreenLight). Each state should be able to transition the context to the next state. All identifiers must be in English.

# Obfuscated version

Manually obfuscated by abstracting the state-machine logic into unreadable class names (`_R`, `_G`, `_C`) and minimizing method signatures.

Folder: decorator_pattern_coffee (JavaScript)

File: README.md
Markdown

# Algorithm name

Decorator Design Pattern (Coffee Shop)

# Author

Gemini (2026-04-10)

# Algorithm description

A structural pattern that allows behavior to be added to an individual object, dynamically, without affecting the behavior of other objects from the same class. This implementation uses functional wrappers to extend the `getCost` and `getDescription` methods of a base coffee object.

# Model used to create the base code

Manually crafted.

### Prompt

Implement the Decorator Design Pattern in JavaScript. Create a SimpleCoffee class and use functional decorators like withMilk and withSugar to dynamically add costs and descriptions to the coffee object. Ensure the code is clean and uses descriptive English names.

# Obfuscated version

Manually obfuscated by using arrow functions, removing white space, and using single-character variables for the original cost and description values.

Folder: proxy_pattern_access (JavaScript)

File: README.md
Markdown

# Algorithm name

Proxy Design Pattern (Data Access)

# Author

Gemini (2026-04-10)

# Algorithm description

The Proxy Pattern provides a surrogate or placeholder for another object to control access to it. Using JavaScript's native `Proxy` object, this implementation intercepts property access to a sensitive object, enforcing security rules and logging activity.

# Model used to create the base code

Manually crafted.

### Prompt

Create a Proxy Design Pattern in JavaScript using the native Proxy object. The implementation should protect a sensitiveData object, logging every access attempt and specifically denying access to a dbPassword property. Use English for all keys and variables.

# Obfuscated version

Manually obfuscated by minifying the handler logic and shortening the target object's keys to obscure the nature of the protected data.
