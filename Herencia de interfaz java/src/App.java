interface Player{

    public void open(String filePath);
    public void play();
    public void stop();
    public void setVolume(float value);

}


interface PlayerPitchable
{

public void setPitch(float pitch);

};


class VLC implements Player, PlayerPitchable {

private boolean isOpen;
private boolean isPlaying;
private float volume;
private float pitch;

VLC()
{
System.out.println("The VLC constructor was invoked.");
isOpen = false;
isPlaying = false;
setVolume(10);
}



public void open(String filePath)
{
isOpen = true;
System.out.println("The audiofile: " + filePath + " is open.");
}



public void play()
{
if(isOpen) isPlaying = true;
System.out.println("The audiofile is playing.");
}



public void stop()
{
if(isPlaying) isPlaying = false;
System.out.println("The audiofile is stopped.");
}



public void setVolume(float value)
{
volume = value;
System.out.println("The volume value is: " + volume);
}


public void setPitch(float value)
{
pitch = value;
System.out.println("The pitch value is: " + pitch);
}




}



class Main {
    public static void main(String[] args) {

        VLC vlcPlayer = new VLC();
        vlcPlayer.open("./resources/orchestral.ogg");
        vlcPlayer.play();
        vlcPlayer.setVolume(13);

    }
  }