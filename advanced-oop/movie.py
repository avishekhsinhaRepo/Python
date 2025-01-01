MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    return add_movie_to_list(title, director, year)


# Create other functions for:
#   - listing movies
def add_movie_to_list(title, director, year):
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def print_movie(movie):
    print(f"Title: {movie['title']}", f"Director: {movie['director']}", f"Release year: {movie['year']}")


def list_movies():
    for movie in movies:
        print_movie(movie)


#   - finding movies
def find_movie_by_title():
    title = input("Enter the movie title: ")
    for movie in movies:
        if movie['title'] == title:
            print_movie(movie)


user_operations = {
    'a': add_movie,
    'l': list_movies,
    'f': find_movie_by_title
}


# And another function here for the user menu
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_operations:
            user_operations[selection]()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()
