abstract class Player{
protected boolean isOpen;
private boolean isPlaying;
// int setVolume;
private int volume;


public Player(boolean isOpen,boolean isPlaying){
System.out.println("The Player constructor was invoked.");
isOpen = false;
isPlaying = false;
//setvolume = 10;

}

public abstract void open(String filepath);

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
public void setVolume(int value)
{
volume = value;
System.out.println("The volume value is: " + volume);
}

}




class VLC extends Player
{
private float pitch;

public VLC (boolean isOpen,boolean isPlaying){
super(isOpen,isPlaying);


System.out.println("The VLC constructor was invoked.");

}

public void open(String filePath)
{
isOpen = true;
System.out.println("The audiofile: " + filePath + " is open.");
}
void setPitch(float value)
{
pitch = value;
System.out.println("The pitch value is: " + pitch);
}

}



class Winamp extends Player
{

public Winamp(boolean isOpen,boolean isPlaying){
super(isOpen,isPlaying);

System.out.println("The Winamp constructor was invoked.");
}

public void open(String filePath)
{
isOpen = true;
System.out.println("The audiofile: " + filePath + " is open.");
}
}


class Main {
    public static void main(String[] args) {
      VLC vlcPlayer = new VLC(false,false);
      vlcPlayer.open("./resources/orchestral.ogg");
      vlcPlayer.play();
      vlcPlayer.setVolume(13);


      Winamp winampPlayer = new Winamp(false,false);
      winampPlayer.open("./resources/orchestral.ogg");
      winampPlayer.play();
      winampPlayer.setVolume(13);

    }
  }

