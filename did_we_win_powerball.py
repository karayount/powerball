"""This script reads a space-delimited text file with the 5 regular ball numbers
followed by the powerball number, ticket purchaser, and ticked id, then sees
if they won the powerball with any of the possible winning combinations"""

all_plays = []

with open("powerball_tickets.txt") as tickets:
    for line in tickets:
        regular_balls = set()
        sheet = 0
        play = line.rstrip().split()
        for ball in range(5):
            regular_balls.add(int(play[ball]))
        power_ball = int(play[5])
        whose = play[6]
        sheet = int(play[7])
        all_plays.append((regular_balls, power_ball, whose, sheet))


winning_power_ball = 13
winning_regular_balls = set([32, 16, 19, 57, 34])
just_3 = 0
just_4 = 0
just_5 = 0
just_power = 0
power_1 = 0
power_2 = 0
power_3 = 0
power_4 = 0
jackpot = 0

for play in range(0, len(all_plays)):
    if all_plays[play][1] == winning_power_ball:
        matches = winning_regular_balls & all_plays[play][0]
        print "The Power Ball and", len(matches), "others match on ticket", all_plays[play][3], "which belongs to", all_plays[play][2]
        if all_plays[play][2] == "us":
            if len(matches) == 0:
                just_power += 1
            elif len(matches) == 1:
                power_1 += 1
            elif len(matches) == 2:
                power_2 += 1
            elif len(matches) == 3:
                power_3 += 1
            elif len(matches) == 4:
                power_4 += 1
            elif len(matches) == 5:
                jackpot += 1
    else:
        matches = winning_regular_balls & all_plays[play][0]
        if len(matches) > 2:
            print len(matches), "non-Power balls match on ticket", all_plays[play][3], "which belongs to", all_plays[play][2]
        if all_plays[play][2] == "us":
            if len(matches) == 3:
                just_3 += 1
            elif len(matches) == 4:
                just_4 += 1
            elif len(matches) == 5:
                just_5 += 1
print "Steffen's wins: "
print "Jackpots:", jackpot
print "Powerball plus 4:", power_4
print "Powerball plus 3:", power_3
print "Powerball plus 2:", power_2
print "Powerball plus 1:", power_1
print "Powerball alone:", just_power
print "5 non-Power balls:", just_5
print "4 non-Power balls:", just_4
print "3 non-Power balls:", just_3
print "Thanks for riding the liquor store lottery ticket line ride!"
