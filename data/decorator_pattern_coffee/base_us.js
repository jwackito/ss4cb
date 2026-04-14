// Base Component
class SimpleCoffee {
    getCost() {
        return 5;
    }
    getDescription() {
        return "Simple Coffee";
    }
}

// Decorator: Milk
function withMilk(coffee) {
    const originalCost = coffee.getCost();
    const originalDesc = coffee.getDescription();

    coffee.getCost = () => originalCost + 2;
    coffee.getDescription = () => originalDesc + ", Milk";
    
    return coffee;
}

// Decorator: Sugar
function withSugar(coffee) {
    const originalCost = coffee.getCost();
    const originalDesc = coffee.getDescription();

    coffee.getCost = () => originalCost + 1;
    coffee.getDescription = () => originalDesc + ", Sugar";
    
    return coffee;
}
