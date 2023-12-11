from bottle import route, run, template, request

cookies = (
    "If two wrongs don't make a right, try three.",
    "If at first you don't succeed, give up. No use being a fool.",
    "The two hardest things in computer science are cache expiry, naming things, and off-by-one errors.",
    "Why is it called a driveway if you <i>park</i> in it?",
    "Those who think they know it all really annoy those of us who actually do know it all.",
    "Hide under your bed.",
    "Be of good cheer. It annoys the right people.",
    "Does a dog have Buddha-nature?",
    "Wake me when the UFOs land.",
    "A child of five could understand this!  Fetch me a child of five.",
    "A kid'll eat the middle of an Oreo, eventually.",
    "Catproof is an oxymoron, childproof nearly so.",
    "It's never too late to have a happy childhood.",
    "According to the latest official figures, 43% of all statistics are totally worthless.",
    "All science is either physics or stamp collecting.",
    "Always try to do things in chronological order; it's less confusing that way.",
    "Always think of something new; this helps you forget your last rotten idea.",
    "Entropy isn't what it used to be.",
    "Everything should be made as simple as possible, but not simpler.",
    "Experience varies directly with equipment ruined.",
    "Facts are stubborn, but statistics are more pliable."
    "I have a theory that it's impossible to prove anything, but I can't prove it."

)

movies = (
("Metropolis ","1927"),
("Rashomon ","1950"),
("Ikiru ","1952"),
("Sansho The Bailiff ","1954"),
("The Seven Samurai ","1954"),
("The Pather Panchali Trilogy ","1955-1958"),
("Bakumatsu Taiyo-Den ","1957"),
("Touch Of Evil ","1958"),
("Yojimbo/Sanjuro ","1961/1962"),
("The Man Who Shot Liberty Valance ","1962"),
("Harakiri ","1962"),
("Kwaidan ","1964"),
("Au Hasard Balthazar ","1966"),
("The Good, The Bad, And The Ugly ","1966"),
("Le Samouraï ","1967"),
("2001: A Space Odyssey ","1968"),
("Eros + Massacre ","1969"),
("Yellow Submarine ","1969"),
("Funeral Parade Of Roses ","1969"),
("El Topo ","1970"),
("Get Carter ","1971"),
("A Touch Of Zen ","1971"),
("The Harder They Come ","1972"),
("Belladonna Of Sadness ","1973"),
("Scenes From A Marriage ","1975"),
("Xala ","1975"),
("Jeanne Dielman, 23 quai du commerce, 1080 Bruxelles ","1975"),
("Monty Python And The Holy Grail ","1975"),
("In The Realm Of The Senses ","1976"),
("Eraserhead ","1977"),
("Star Wars ","1977"),
("Taxi Driver ","1977"),
("Sorcerer ","1977"),
("Suspiria ","1977"),
("Alien ","1979"),
("The Man Who Stole The Sun ","1979"),
("The Mad Max Saga ","1979-"),
("Berlin Alexanderplatz ","1980"),
("The Taisho Trilogy ","1980-"),
("Apocalypse Now ","1981"),
("Out Of The Blue ","1981"),
("Son Of The White Mare ","1981"),
("Diva ","1981"),
("My Dinner With Andre ","1981"),
("Blade Runner ","1982"),
("Blade Runner 2049","2017"),
("Koyaanisqatsi ","1982"),
("TRON ","1982"),
("Fanny and Alexander ","1982"),
("Angst ","1983"),
("Videodrome ","1983"),
("Paris, Texas ","1984"),
("Repo Man ","1984"),
("The Terminator ","1984"),
("RAN ","1985"),
("Legend ","1985"),
("The Official Story ","1985"),
("Shoah ","1985"),
("Mishima ","1985"),
("Kiss Of The Spider Woman ","1985"),
("To Live And Die In L.A. ","1985"),
("A Time To Live And A Time To Die ","1985"),
("Royal Space Force Honneamise ","1987"),
("AKIRA ","1988"),
("My Neighbor Totoro ","1988"),
("Tetsuo: The Iron Man ","1989"),
("Violent Cop ","1989"),
("Why Has Bodhi-dharma Left For The East? ","1989"),
("GoodFellas ","1990"),
("Rebels Of The Neon God ","1992"),
("Hard Boiled ","1992"),
("Unforgiven ","1992"),
("Naked ","1993"),
("Fear Of A Black Hat ","1993"),
("Ghost In The Shell ","1995"),
("SE7EN ","1995"),
("Come And See ","1995"),
("Strange Days ","1995"),
("Spring & Chaos ","1996"),
("Princess Mononoke ","1997"),
("Perfect Blue ","1997"),
("Jin-roh: The Wolf Brigade ","1999"),
("The Matrix ","1999"),
("The Fast & Furious Series ","2000-"),
("In The Mood For Love ","2000"),
("Sexy Beast ","2000"),
("Gohatto ","2000"),
("Kao [Face] ","2000"),
("Requiem For A Dream ","2000"),
("Gojoe-reisenki ","2000"),
("Avalon [Mamoru Oshii] ","2001"),
("Irreversible ","2002"),
("Oldboy ","2003"),
("Izo ","2004"),
("MIND GAME ","2004"),
("Casino Royale ","2006"),
("REDLINE ","2009"),
("Shutter Island ","2010"),
("Silence ","2016"),
("Parasite ","2020"),
("The Green Knight ","2021"),

)

from random import choice, randint

@route("/")
def index():
    return """
<p><a href="/cookies">Fortune cookies</a>
<p><a href="/movies">Infinite scroll movie list</a>
<p><a href="/search">Search box example</a>
"""
@route("/cookies")
def root():
    return template("01_cookie.html")

@route("/cookie", method="POST")
def cookie():
    return f"{randint(1,1000)}: {choice(cookies)}"

@route("/movies")
def movie_main():
    return template("02_movies.html")

@route("/api/movies")
def movie_list():
    page = int(request.query.get("page",0))
    movie_list = []
    for n in range(50):
        movie_list.append(choice(movies))
    return template("02_scroll.html", movies=movie_list, page=page)

@route("/search")
def search():
    return template("03_search.html")

@route("/api/movie-search", method="POST")
def search_results():
    search_request = request.forms.get("search")
    if not search_request:
        return
    results = [m for m in movies if search_request in m[0]]
    return template("03_results.html", results=results)

import webbrowser
webbrowser.open("http://localhost:8080")

run()