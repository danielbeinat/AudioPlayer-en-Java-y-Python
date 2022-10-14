
class AudioPlayer:
    def __init__(self,isOpen,isPlaying,volume):
        print("The AudioPlayer constructor was invoked.")

        self.isOpen = isOpen
        self.isPlaying = isPlaying
        self.volume = volume
        self.setvolume = 10
    
    def __del__(self):
        print("The AudioPlayer destructor was invoked.")

    def open(self, filePath):
        self.isOpen = True
        print(f"The audiofile: {filePath}  is open")

    def play(self):
        #if self.isOpen: 
        self.isPlaying = True
        print("The audiofile is playing.")
    
    def stop(self):
        # if self.isPlaying: 
        self.isPlaying = False
        print("The audiofile is stopped.")

    def setVolume(self,value):
        self.volume = value
        print(f"The volume value is: {value} ")

        

    
        


class VLC(AudioPlayer):
    def __init__(self,isOpen,isPlaying,volume):
        super().__init__(isOpen,isPlaying,volume)
        print("The VLC constructor was invoked.")

        self.pitch = 0
        self.setvolume = 10

    def __del__(self):
        print("The VLC destructor was invoked.")

    def setPitch(self,value):
        self.pitch = value
        print(f"The pitch value is:  {self.pitch}")








player = AudioPlayer(None,None,10) 
player.open("./resources/orchestral.ogg")
player.play()
player.setVolume(4)

vlcPlayer= VLC(None,None,10)
vlcPlayer.open("./resources/orchestral.ogg")
vlcPlayer.play()
vlcPlayer.setVolume(13)
vlcPlayer.setPitch(0)
