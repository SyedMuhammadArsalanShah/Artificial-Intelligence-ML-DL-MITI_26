import pyshorteners




urlInput=input("Enter Your URL here\n")
s = pyshorteners.Shortener()
print(s.tinyurl.short(urlInput))