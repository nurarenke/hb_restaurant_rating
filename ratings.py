"""Restaurant rating lister."""


# put your code here
def get_scores_dictionary(file_name):
    """ Reformats scores.txt into a dictionary. """

    ratings_dict = {}

    with open(file_name) as f:
        for line in f:
            ratings_list = line.strip().split(':')
            restaurant = ratings_list[0]
            rating = ratings_list[1]
            ratings_dict[restaurant] = rating
    return ratings_dict


def display_restaurant_ratings(ratings):
    """ Given an argument of ratings, displays
    restaurants and corresponding ratings. """

    sorted_ratings_list = sorted(ratings_dict.items())
    for restaurant, rating in sorted_ratings_list:
        print restaurant + " is rated at " + rating + "."


ratings_dict = get_scores_dictionary("scores.txt")

display_restaurant_ratings(ratings_dict)
