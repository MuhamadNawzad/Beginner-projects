polls = ["a", "a", "b", "b", "b", "b", "c", "a", "c", "c", "c"]

candidates = []
votes = []
for member in polls:
    if member not in candidates:
        candidates.append(member)
        votes.append(1)
    else:
        votes[candidates.index(member)] += 1
max_candidate = []
max_vote = 0
for i in range(len(votes)):
    if votes[i] > max_vote:
        max_vote = votes[i]
        max_candidate = [candidates[i]]
    elif votes[i] == max_vote:
        max_candidate.append(candidates[i])
print("The highest vote goes to:")
print(*max_candidate, sep="\n")
print("Each person has " + str(max_vote) + " votes.")