package data.state_pattern_traffic_light;

// State Interface
interface LightState {
    void handle(TrafficLight context);
}

// Concrete State: Red
class RedLight implements LightState {
    public void handle(TrafficLight context) {
        System.out.println("Red Light: Stopping");
        context.setState(new GreenLight());
    }
}

// Concrete State: Green
class GreenLight implements LightState {
    public void handle(TrafficLight context) {
        System.out.println("Green Light: Going");
        context.setState(new RedLight());
    }
}

// Context
class TrafficLight {
    private LightState current;

    public TrafficLight() {
        this.current = new RedLight();
    }

    public void setState(LightState state) {
        this.current = state;
    }

    public void request() {
        current.handle(this);
    }
}

public class base_us {
    public static void main(String[] args) {
        TrafficLight light = new TrafficLight();
        light.request(); // Red to Green
        light.request(); // Green to Red
    }
}