######################################
#
# Movie archival project
# Version: 0.0.0
# Limitations: User's inputs are not checked for this project version.
#
######################################
import json

movies = []


def menu():
    menu = '''
    - Enter l to view all movies in collection 
    - Enter a to add a new movie to collection 
    - Enter f to look up a movie by name
    - or q to quit: 
    '''
    user_input = input(menu)
    while user_input != 'q':
        if (user_input == 'l'):
            show_movies(movies)
        elif (user_input == 'a'):
            add_movie()
        elif (user_input == 'f'):
            find_movie()
        elif (user_input == 'q'):
            print('Thank you for using the app ... Bye for now!')
        else:
            print('Invalid input.  Please try again')
        user_input = input(menu)


def add_movie():
    name = input('Please enter movie name: ');
    director = input('Please enter director name: ');
    year = input('Please enter year release: ');
    movie = {'name': name,
             'director': director,
             'year': year
             }
    movies.append(movie)


def show_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f'Movie: {json.dumps(movie, indent=4, sort_keys=True)}')


def find_movie():
    find_by = input("What property of the movie are you looking for? ")
    looking_for = input("What are you searching for? ")
    found_movies = find_by_attribute(looking_for, lambda x: x[find_by])
    show_movies(found_movies)

def find_by_attribute(expected, finder):
    found = []
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)
    return found


menu();

#     print(movie)
#     if user_input == 'a':
#         add_movie()
#     elif user_input == 'l':
#         show_movies()
#     elif user_input == 'f':
#         find_movie()
#     elif user_input == 'q':
#         print("Stopping program ...")
#     else:
#         print("Invalid input ...")
#
# def show_movies(movies):
#     for movie in movies:
#         print(movie)
#
# def lookup_movies_by_name(movies, name):
#     for movie in movies:
#         if movie['name'] == name:
#             print(movie)
#
# def find_movie(movies, name):
#     for movie in movies:
#         if movie['name'] == name:
#             print(movie)
#
#
# def lookup_movies_by_year(movies, year):
#     for movie in movies:
#         if movie['year'] == year:
#             print(movie)
#
#
# def lookup_movies_by_director(movies, director):
#     for movie in movies:
#         if movie['director'] == director:
#             print(movie)
#
# isDone = False;
# while not isDone:
#     user_input = def_menu();
#     if (user_input == 'l'):
#         print()
#         show_movies(movies)
#     elif (user_input == 'a'):
#         print()
#         add_movie(movies)
#     elif (user_input == 'n'):
#         print()
#         name = input('Enter movie\s name please:')
#         lookup_movies_by_name(movies, name)
#     elif (user_input == 'y'):
#         print()
#         year = input('Enter release year please:')
#         lookup_movies_by_year(movies, year)
#     elif (user_input == 'd'):
#         print()
#         director = input('Enter director name please:')
#         lookup_movies_by_director(movies, director)
#     elif (user_input == 'q'):
#         print()
#         isDone = True;
#         print('Thank you for using the app ... Bye for now!')
#     else:
#         print()
#         print('Invalid input.  Please try again')
# # Do nothing. Keep on looping
