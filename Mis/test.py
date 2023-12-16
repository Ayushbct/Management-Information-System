winter_period_time = ['10:15', '11:00', '11:45', '12:30', '1:00', '1:45', '2:30', '3:15', '4:00','4:15','5:00']
summer_period_time = ['10:15', '11:05', '11:55', '12:45', '1:35', '2:25', '3:15', '4:05', '4:55','5:45','6:35']

# season=request.data.get('season')
# starting_period_value = int(request.data.get('starting_period'))
# no_of_period_value = int(request.data.get('no_of_period'))
season='summer'
starting_period_value = int(8)
no_of_period_value = int(1)
ending_period_value = starting_period_value + no_of_period_value
if season == 'winter':
    period_time = winter_period_time
elif season == 'summer':
    period_time = summer_period_time
else:
    print("Invalid season.")
    period_time = []
# Create period_mapping dynamically using a loop
period_mapping = {}
for index, time in enumerate(period_time):
    period_mapping[index + 1] = time

# Get the starting time and ending time based on the input value
time_start = period_mapping.get(starting_period_value)
time_end = period_mapping.get(ending_period_value)

# Check if the value is valid and exists in the mapping
if time_start:
    print(f"The starting time for period {starting_period_value} is: {time_start}")
    print(f"The ending time for period {ending_period_value} is: {time_end}")
else:
    print("Invalid starting period value.")
076bct013ayush
MoiOoIJ6yEGSCWrK

mongodb+srv://076bct013ayush:MoiOoIJ6yEGSCWrK@miscluster.zimodif.mongodb.net/?retryWrites=true&w=majority

{
    "teacher": [5],
    "subject": "Distrubuted System",
    "year": "3rd Year",
    "course": "BCT",
    "day": "thu",
    "time_start": "",
    "time_end": "",
    "session_type": "lecture",
    "room_number": "305",
    "season":"winter",
    "starting_period_value":"2",
    "no_of_period_value":"1"
}