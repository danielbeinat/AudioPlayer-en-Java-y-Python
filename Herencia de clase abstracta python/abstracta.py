from abc import ABC, abstractmethod 


class Player(ABC):
    def __init__(self,isOpen,isPlaying,volume):
        print("The Player constructor was invoked.")

        self.isOpen = isOpen
        self.isPlaying = isPlaying
        self.volume = volume
        self.setvolume = 10
    
    def __del__(self):
        print("The Player destructor was invoked.")

    def open(filePath): #Metodo abstracto
        pass
    
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

        

    
        


class VLC(Player):
    def __init__(self,isOpen,isPlaying,volume):
        super().__init__(isOpen,isPlaying,volume)
        print("The VLC constructor was invoked.")

        self.pitch = 0
        self.setvolume = 10

    def __del__(self):
        print("The VLC destructor was invoked.")

    def open(self,filePath):
        self.isOpen = True
        print(f"The audiofile: {filePath}  is open")


    def setPitch(self,value):
        self.pitch = value
        print(f"The pitch value is:  {self.pitch}")



class Winamp(Player):
    def __init__(self,isOpen,isPlaying,volume):
        super().__init__(isOpen,isPlaying,volume)
        print("The Winamp constructor was invoked.")

        self.setvolume = 10
        
    def __del__(self):
        print("The Winamp destructor was invoked.")
    
    def open(self,filePath):
        self.isOpen = True
        print(f"The audiofile: {filePath}  is open")

    




vlcPlayer = VLC(None,None,0)
vlcPlayer.open("./resources/orchestral.ogg")
vlcPlayer.play()
vlcPlayer.setVolume(13)


winampPlayer = Winamp(None,None,0)
winampPlayer.open("./resources/orchestral.ogg")
winampPlayer.play()
winampPlayer.setVolume(13)