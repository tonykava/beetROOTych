import wikipedia

result = wikipedia.summary("Robots")

with open('Robots.txt', 'w', errors='ignore') as f:
    f.write(result)
    
