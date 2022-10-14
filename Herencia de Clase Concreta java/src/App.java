
 class AudioPlayer {
    
    boolean isOpen;
    boolean isPlaying;
    int volumen;
    

    public AudioPlayer(boolean isOpen, boolean isPlaying){


System.out.println("The AudioPlayer constructor was invoked.");
isOpen = false;
isPlaying = false;



    }

    public void Open(String Filepath){
        isOpen=true;
      System.out.println("The audiofile:" + Filepath + " is open.");
    }

    public void play(){

        if(isPlaying) isPlaying = false;
        System.out.println("The audiofile is playing.");
  
  
    }

    public void stop(){
        if(isPlaying) isPlaying = false;
        System.out.println("The audiofile is stopped.");
  
  
    }

    public void setvolume(int volumen){

        System.out.println("The volume value is: " + volumen);
  
  
    }

}
  




class vlc extends AudioPlayer {

     int pitch;
    
      public vlc(boolean isOpen, boolean isPlaying,int pitch){

        super(isOpen,isPlaying);

        this.pitch = pitch;
        System.out.println("The VLC constructor was invoked");


}



public void setpicht(int value){
  pitch= value;

System.out.println("The pitch value is: " + pitch);
}



    }
  


  
  
  class Main {
    public static void main(String[] args) {

      AudioPlayer player = new AudioPlayer(false,false);  
      player.Open("./resources/orchestal.ogg");
      player.play();
      player.setvolume(4);


      vlc myvlc = new vlc(false,false,10);

      myvlc.Open("./resources/orchestral.ogg");
      myvlc.play();
      myvlc.setvolume(13);
      myvlc.setpicht(10);
    }
  }