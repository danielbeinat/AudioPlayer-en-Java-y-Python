class Player:
    def open(filePath):
        pass
    def play(self):
        pass
    def stop(self):
        pass
    def setVolume(value):
        pass


class PlayerPitchable:
    def setPich(pitch):
        pass
    



class VLC(Player,PlayerPitchable):
    def __init__(self):
        print("The VLC constructor was invoked.")
        self.isOspen = False 
        self.isPlaying = False
        self.volume = 0
        self.pitch = 0
        self.setvolume = 10

    def __del__(self):
        print("The VLC destructor was invoked.")

    def open(self,filePath):
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
    
    def setPitch(self,value):
        self.pitch = value
        print(f"The pitch value is:  {self.pitch}")


    



vlcPlayer = VLC()
vlcPlayer.open("./resources/orchestral.ogg")
vlcPlayer.play()
vlcPlayer.setVolume(13)