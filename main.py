from logo import gavel
from replit import clear
print(gavel)
bid = {}
def highest_bidder(bid):
  name = ""
  price = 0
  for x,y in bid.items():
    if y > price:
      price = y
      name  = x
  print(f"The highest bidder is {name}, price is {price}.")
  print(f"All the bidders are {bid}")
  

bid_again = True
while bid_again:
  name = input("Enter name : ").lower()
  price  = int(input("Enter the bid $ "))
  bid[name] = price
  bid_continue = input("Bid again ? 'yes' or 'no'").lower()
  if bid_continue == "yes":
    clear()
  elif bid_continue == "no":
    highest_bidder(bid)
    bid_again = False




# highest_bidder_name = ""
# highest_bidder = 0
# def blind_auction(current_name,current_bid):
#   global highest_bidder
#   global highest_bidder_name 
#   bidder = {}
#   bidder[current_name] = current_bid

#   for key,val in bidder.items():
#     if val > highest_bidder:
#       highest_bidder = val
#       highest_bidder_name = key


# finish_bidding = True
# while finish_bidding:
#   name = input("Enter Name : ").lower()
#   bid = int(input("Enter the bid : "))
#   blind_auction(current_name=name,current_bid=bid)
#   check = input("Anybody else to bid more? 'yes' or 'no' :").lower()
#   # clear()
#   if check == "no":
#     finish_bidding = False
#     print(f"Highest bidder is {highest_bidder_name }, bidded {highest_bidder} ")



# travel_log =[ {
#       "country":"Germany",
#       "cities_visited" : ["Berlin","stutgard","Freiburg"],
#       "visited_time" : 3,},
# {       
#         "country":"Italy" ,
#         "cities_visited" : ["Milan","Rome","Parma"],
#         "visited_time" : 5}
# ]

# def add_new_country(country,visited_time,cities_visited):
#   new_country = {}
#   new_country["country"] = country
#   new_country["cities_visited"] = cities_visited
#   new_country["visited_time"] = visited_time

#   travel_log.append(new_country)

# add_new_country(country="Russia",visited_time="4",cities_visited=["Moscow","Sant Petersburg"])
# print(travel_log)





# student_scores = {
#   "Harry":81,
#   "Ron":78,
#   "Hermione":99,
#   "Draco":74,
#   "Neville":62,
# }
# student_grade = {}
# for key,val in student_scores.items():
#   if val > 90:
#     student_grade[key] = "Outstanding"
#   elif  val > 80:
#     student_grade[key] = "Exceeds Expectations"
#   elif  val > 70:
#     student_grade[key] = "Acceptable"
#   else:
#     student_grade[key] = "Fail"
  
# print(student_grade)


