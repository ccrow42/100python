dict = {
    "bug": "some form of bug",
    }

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }

programming_dictionary["Loop"] = "The action of doing something over and over again."

print (programming_dictionary)
print (programming_dictionary["Bug"])

empty_dict = {}

for item in programming_dictionary:
    print(item)
    print(programming_dictionary[item])

# Nesting:
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]


# A function to update the travel log with indentation for readibility:
def add_new_country (func_country, func_visits, func_cities):
  travel_log.append(
    {
      "country": func_country, 
      "visits": func_visits, 
      "cities": func_cities
    }
  )
add_new_country ("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
print (travel_log)