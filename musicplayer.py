from playsound import playsound

print("no of available songs\n1.free\n2.raata\n3.tere")
order = input('enter the music which you want to play:')
if "free" in order:
    playsound('C:\\Users\\vishwavijay kumar\Music\\free.mp3')
elif "raata" in order:
    playsound('C:\\Users\\vishwavijay kumar\Music\\raata.mp3')
elif "tere" in order:
    playsound('C:\\Users\\vishwavijay kumar\Music\\tere.mp3')