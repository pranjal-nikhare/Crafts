import webbrowser
import random
import time

edge_path = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

movies = ["The Godfather", "The Shawshank Redemption", "Schindler's List", "Raging Bull", "Casablanca", "Citizen Kane", "Gone with the Wind", "The Wizard of Oz", "One Flew Over the Cuckoo's Nest", "Lawrence of Arabia", "Vertigo", "Psycho", "The Good, the Bad and the Ugly", "The Lord of the Rings: The Return of the King", "Star Wars: Episode V - The Empire Strikes Back", "The Silence of the Lambs", "Se7en", "The Matrix", "The Dark Knight", "Inception", "Fight Club", "Pulp Fiction", "The Prestige", "The Departed", "The Usual Suspects", "Memento", "The Sixth Sense", "Eternal Sunshine of the Spotless Mind", "The Truman Show", "Forrest Gump",
          "Life Is Beautiful",
          "The Green Mile",
          "The Lion King",
          "Spirited Away",
          "Toy Story",
          "Up",
          "Inside Out",
          "Coco",
          "Wall-E",
          "Finding Nemo",
          "The Incredibles",
          "Shrek",
          "Ratatouille",
          "Zootopia",
          "How to Train Your Dragon",
          "The Iron Giant",
          "Lion King",
          "Beauty and the Beast",
          "Aladdin",
          "The Little Mermaid",
          "Moana",
          "Frozen",
          "Tangled",
          "Mulan",
          "Tarzan",
          "Hercules",
          "The Princess and the Frog",
          "Wreck-It Ralph",
          "Big Hero 6",
          "Kung Fu Panda",
          "The Terminator",
          "Terminator 2: Judgment Day",
          "Alien",
          "Aliens",
          "Predator",
          "Jurassic Park",
          "Jaws",
          "E.T. the Extra-Terrestrial",
          "Back to the Future",
          "Indiana Jones and the Raiders of the Lost Ark",
          "The Avengers",
          "Impeccable", "Fluctuate", "Obliterate", "Ponder", "Enigmatic", "Elusive", "Inquisitive", "Venerate",
          "Melancholy", "Eclectic", "Benevolent", "Quandary", "Ethereal", "Insidious", "Nostalgia", "Serendipity",
          "Ravenous", "Inevitable", "Capricious", "Resilience", "Enthrall", "Diligent", "Impulsive", "Vexation",
          "Placid", "Whimsical", "Incessant", "Jubilant", "Tenacity", "Blissful", "Enrapture", "Visceral",
          "Precarious", "Conundrum", "Chasm", "Ineffable", "Discombobulated", "Mellifluous", "Asinine", "Surreptitious",
          "Iron Man",
          "Captain America: The Winter Soldier",
          "Guardians of the Galaxy",
          "Black Panther",
          "Thor: Ragnarok",
          "Spider-Man: Into the Spider-Verse",
          "Deadpool",
          "Logan",
          "The Dark Knight Rises",
          "Wonder Woman",
          "Aquaman"
          ]

keywords = ["youtube", "amazon", "facebook", "wordle", "google", "gmail", "google translate", "walmart", "weather", "yahoo", "home depot", "fox news", "yahoo mail", "instagram", "nba", "nfl", "target", "ebay", "cnn", "twitter", "espn", "amazon prime", "google docs", "zillow", "google maps", "usps tracking", "craigslist", "costco", "lowes", "netflix",
            "best buy",
            "indeed",
            "etsy",
            "roblox",
            "shein",
            "msn",
            "Albert Einstein", "Amelia Earhart", "Barack Obama", "Bill Gates", "Cleopatra", "Dolly Parton", "Elvis Presley", "Frida Kahlo", "George Washington", "Helen Keller", "Jackie Robinson", "John F. Kennedy", "Leonardo da Vinci", "Marie Curie", "Muhammad Ali", "Nelson Mandela", "Oprah Winfrey", "Queen Elizabeth II", "Steve Jobs", "Thomas Edison", "Walt Disney", "Winston Churchill", "Yasmin Mogahed", "Zaha Hadid",
            "google flights",
            "calculator",
            "kahoot",
            "onlyfans",
            "walgreens",
            "hotmail",
            "wells fargo",
            "dominos",
            "macys",
            "dow jones",
            "omegle",
            "linkedin",
            "google classroom",
            "fedex tracking",
            "bank of america",
            "american airlines",
            "spotify",
            "paypal",
            "airbnb",
            "southwest airlines",
            "twitch",
            "cvs",
            "capital one",
            "outlook",
            "ikea",
            "kohls",
            "discord",
            "google drive",
            "old navy",
            "chase",
            "tiktok",
            "aol mail",
            "mcdonalds",
            "mlb",
            "canva",
            "starbucks"
            ]
queries = movies + keywords

print(len(queries))


for i in range(0, 35):
    # select random integer between 0 and 153
    rand1 = random.randint(1, 193)
    rand2 = random.randint(1, 193)
    # select random movie from list
    query1 = queries[rand1]
    query2 = queries[rand2]
    # search each query in Edge
    webbrowser.get('edge').open(
        "https://www.bing.com/search?q=" + query1 + " " + query2 + " " + query1)
    randm = random.randint(1, 3)
    time.sleep(randm)
