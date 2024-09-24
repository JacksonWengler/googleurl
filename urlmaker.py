import webbrowser

#get the input from the user
search= input('What do you want to search for?')
#turn spaces into google spaces %20
search= search.replace(' ', '%20')
google=('google.com/search?q=')
url=(google+search)
webbrowser.open_new(url)
