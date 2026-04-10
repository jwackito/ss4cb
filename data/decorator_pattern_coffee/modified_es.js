// Base Component
class CafeSimple {
    obtenerCosto() {
        return 5;
    }
    obtenerDescripcion() {
        return "Cafe Simple";
    }
}

// Decorador: Milk
function conLeche(cafe) {
    const costoOriginal = cafe.obtenerCosto();
    const descripcionOriginal = cafe.obtenerDescripcion();

    cafe.obtenerCosto = () => costoOriginal + 2;
    cafe.obtenerDescripcion = () => descripcionOriginal + ", Milk";
    
    return cafe;
}

// Decorador: azucar
function conAzucar(cafe) {
    const costoOriginal = cafe.obtenerCosto();
    const descripcionOriginal = cafe.obtenerDescripcion();

    cafe.obtenerCosto = () => costoOriginal + 1;
    cafe.obtenerDescripcion = () => descripcionOriginal + ", azucar";
    
    return cafe;
}
