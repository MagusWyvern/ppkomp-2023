'''
PPKomp is an individual contest.
Meaning that a contestant is not allowed to discuss on the problems and solutions with other participants while the contest runs.

A contestant is allowed to refer to their text book, note book or other websites (can google or refer to online tutorial).

Even though it is an individual contest, each participant must be registered in a team.
The 5 best contestants from each team will automatically represent their team to determine for the best team award.
The marks of the 5 participants will be added as their team’s score and the team with the highest score wins.

The judge will use the score obtained on each question to detect cases of copying or discussions among participants.
If there are several participants who have the same score for all six questions, these participants will be suspected of discussing, cheating, or copying, except for participants who have a total score of 0.

The judges will then review the submitted codes of each involved participant and compare their submission.
The answers of participants found to be discussing, cheating, or copying will be invalidated, and they will be given a score of 0.

Given a list of scores obtained by all participants from the same group.
You are to calculate the scores of each participant from that group and identify if there are students suspected of discussing, cheating, or copying.
'''

'''
Sample Input:

8
1 2 3 4 5 6
21 0 0 0 0 0
11 2 3 4 5 6
16 18 11 3 5 6
1 2 3 4 5 6
1 2 3 4 5 6
0 0 0 0 0 0
0 0 0 0 0 0
'''

# Input Format

# The first line contains an integer N, the number of participants in the group.
# The next N lines contain 6 integer each, the score obtained by each participant for the 6 questions.

n = int(input())
scores = []

for i in range(n):
    scores.append(list(map(int, input().split())))

# Check if 2 or more participants have the same score sheet
# Store the list of same scores sheet in list 'same_scores'
# If the participant score is 0, do not replace their score
# Also store the index of the participant with the same score sheet in list 'same_scores_index'

same_scores = []
same_scores_index = []

for i in range(n):
    for j in range(i+1, n):
        if scores[i] == scores[j] and sum(scores[i]) != 0:
            same_scores.append(scores[i])
            same_scores_index.append(i)
            same_scores_index.append(j)

# Check if there are participants with the same_score_sheet
# Add their index to list 'same_scores_index'

if len(same_scores) > 0:
    for i in range(n):
        for j in range(len(same_scores)):
            if scores[i] == same_scores[j]:
                same_scores_index.append(i)

# Calculate the score of each participant
# Store in list 'total_individual_scores'

total_individual_scores = []

for i in range(n):
    total_individual_scores.append(sum(scores[i]))

# Refer to list 'same_scores_index'
# Replace the score of participants with the same score sheet with the string  'Invalid'
# Else, just sum up the score of each participant

for i in range(n):
    for j in range(len(same_scores_index)):
        if i == same_scores_index[j]:
            total_individual_scores[i] = 'suspected to have discussed or cheating or allow cheating'
            break
        else:
            total_individual_scores[i] = sum(scores[i])
        
# Print the list of scores of each participant, each on a new line

for i in range(n):
    print(total_individual_scores[i])









