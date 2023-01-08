people = ['cong','ying','bin']
print(people[0] + " ge qin ni jin wan lai wo jia chi fan")

print(people[1] + " ge qin ni jin wan lai wo jia chi fan")

print(people[2] + " ge qin ni jin wan lai wo jia chi fan")
print(people[0] + " ge bu lai")
people[0] = 'bang'
print(people[0] + " ge qin ni jin wan lai wo jia chi fan")

print(people[1] + " ge qin ni jin wan lai wo jia chi fan")

print(people[2] + " ge qin ni jin wan lai wo jia chi fan")
print("I find a bigger table")
people.insert(0,'sheng')
people.insert(2,'zen')
people.append('bo') 
print(people[0] + " ge qin ni jin wan lai wo jia chi fan")

print(people[1] + " ge qin ni jin wan lai wo jia chi fan")

print(people[2] + " ge qin ni jin wan lai wo jia chi fan")
print(people[3] + " ge qin ni jin wan lai wo jia chi fan")

print(people[4] + " ge qin ni jin wan lai wo jia chi fan")

print(people[5] + " ge qin ni jin wan lai wo jia chi fan")
print("I can only invite two persons")
print(people.pop(-1) + " sorry")
print(people.pop(-1) + " sorry")
print(people.pop(-1) + " sorry")
print(people.pop(-1) + " sorry")
print(people[0] + ",you can ji xu chi fan")
print(people[1] + ",you can ji xu chi fan") 
del people[1]
del people[0]
print(people)
print(len(people))
