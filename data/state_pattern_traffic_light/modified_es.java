package data.state_pattern_traffic_light;

// Interfaz de Estado
interface EstadoLuz {
    void manejar(LuzDeTrafico contexto);
}

// Estado Concreto: Rojo
class LuzRoja implements EstadoLuz {
    public void manejar(LuzDeTrafico contexto) {
        System.out.println("Red Light: Stopping");
        contexto.asignarEstado(new LuzVerde());
    }
}

// Estado Concreto: Verde
class LuzVerde implements EstadoLuz {
    public void manejar(LuzDeTrafico contexto) {
        System.out.println("Luz Verde: yendo");
        contexto.asignarEstado(new LuzRoja());
    }
}

// contexto
class LuzDeTrafico {
    private EstadoLuz actual;

    public LuzDeTrafico() {
        this.actual = new LuzRoja();
    }

    public void asignarEstado(EstadoLuz estado) {
        this.actual = estado;
    }

    public void solicitar() {
        actual.manejar(this);
    }
}
