duration = int(input())
food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())

required_sum = duration * food_cost + flight_cost * 2 + (duration - 1) * hotel_cost

print(required_sum)