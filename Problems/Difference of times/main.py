a_hours = int(input())
a_minutes = int(input())
a_seconds = int(input())
b_hours = int(input())
b_minutes = int(input())
b_seconds = int(input())

diff_in_seconds = -((a_hours * 3600 + a_minutes * 60 + a_seconds) - (b_hours * 3600 + b_minutes * 60 + b_seconds))

print(diff_in_seconds)