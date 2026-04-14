// interfaz objetivo
interface ReproductorDeMedia {
    void reproductor(String archivoNombre);
}

// Adaptado (clase existente con diferente interafaz)
class ReproductorDeAudioAvanzado {
    void reproductorVlc(String archivo) {
        System.out.println("reproduciendo archivo vlc: " + archivo);
    }
}

// clase Adaptador
class AdaptadorDeAudio implements ReproductorDeMedia {
    private ReproductorDeAudioAvanzado reproductorAvanzado;

    public AdaptadorDeAudio() {
        this.reproductorAvanzado = new ReproductorDeAudioAvanzado();
    }

    @Override
    public void reproductor(String archivoNombre) {
        // Adapta la llamada a reproduccion al reproduccionVlc
        reproductorAvanzado.reproductorVlc(archivoNombre);
    }
}
