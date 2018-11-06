

# First to create are data structures

films = {
    "MR73": [18, 5],
    "Millennium" : [18, 5],
    "Hangover" : [15, 7],
    "The Simpsons" : [12, 4],
    "Hangover II" : [15, 6],
    "Shrek" : [12,5],
    "Fast and Furious" : [12,5],
    
    
    }


while True:

    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())
        
        # check user's age
        if age >=films[choice][0]:

            # check enough seats 
            num_seats = films[choice][1]
            
            if num_seats > 0:
                print("Enjoy the film!")
            films[choice][1] = films[choice][1] - 1
        else: print("Sorry, we don't have tickets.")
            
    else: print("You are too young to watch this movie.")
else: print("We don't have this title...") 
