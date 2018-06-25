import time
import webbrowser
print('Python Google link generator for Windows')
base = "https://www.google.co.uk/search?q="
query = input('What do you want to search?')
print('Okay, here\'s your link:')
print(base,query,sep="")
webbrowser.open(base + query)
time.sleep(10)
