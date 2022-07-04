destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
   destination_index = destinations.index(destination)
   return destination_index


def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

attractions = [[] for destination in destinations]

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attraction_for_destination = attractions[destination_index]
  attraction_for_destination.append(attraction)
  return attraction_for_destination

add_attraction("Los Angeles, USA" ,['Venice Beach', ['beach']])

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attraction_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tag = attraction[1]
    for interest in interests:
      if interest in attraction_tag:
        attraction_with_interest.append(possible_attraction[0])
  return attraction_with_interest

las_arts = find_attractions("Los Angeles, USA", ['art'])

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interest = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interest)
  interesting_string = "Hi "
  interesting_string += traveler[0]
  interesting_string += ", we think you'll like these places around " 
  interesting_string += traveler_destination + ": The "
  for item in traveler_attractions:
    interesting_string += item
  
  return interesting_string + "!!!!"
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

print(smills_france)




  


