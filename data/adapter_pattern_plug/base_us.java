// Target interface
interface MediaPlayer {
    void play(String fileName);
}

// Adaptee (existing class with different interface)
class AdvancedAudioPlayer {
    void playVlc(String file) {
        System.out.println("Playing vlc file: " + file);
    }
}

// Adapter class
class AudioAdapter implements MediaPlayer {
    private AdvancedAudioPlayer advancedPlayer;

    public AudioAdapter() {
        this.advancedPlayer = new AdvancedAudioPlayer();
    }

    @Override
    public void play(String fileName) {
        // Adapts the play call to playVlc
        advancedPlayer.playVlc(fileName);
    }
}

// Client
public class base_us {
    public static void main(String[] args) {
        MediaPlayer player = new AudioAdapter();
        player.play("video_clip.vlc");
    }
}