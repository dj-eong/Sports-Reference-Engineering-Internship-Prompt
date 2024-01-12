# Sports Reference 2024 Summer Internship Application

## Engineering Internship Prompt Solution

I initially looked at the json data to see how it could be broken up; essentially, the data is an object consisting of 'teams', where each 'team' is also an object made up of 'opposing teams', and each 'opposing team' has an object, which is the parent team's win-loss record with the opposing team.
```js
{
    "BRO": {
        "BSN": {
            "W": 10,
            "L": 12
        },
        "CHC": {
            "W": 15,
            "L": 7
        }, ...
```
I converted this json data into a Python dictionary:
```python
# read json data and convert to dictionary/map
with open('file.json') as file:
    data = json.load(file)
```
I then created a matrix/2D array and started iterating through the first layer of the data (the parent teams), aiming to fill in the top row and leftmost column with the team names.
```python
def convert_to_matrix(data):
    matrix = [['Tm']]
    i = 1
    for team in data:
        # fill out top row and left column with team
        matrix[0].append(team)
        matrix.append([team])

        # fill in team records
        for opp in data[team]:
            record = data[team][opp]
            # when team faces itself, leave cell empty
            if len(matrix[i]) == i:
                matrix[i].append(None)
            matrix[i].append(record['W'])
        i += 1
    return matrix
```
With every iteration of the outer for loop being a new parent team, I created an inner for loop that would look at said parent team's list of opponents, grabbing their win-loss records against each opponent. 

I also realized that since one team's number of wins against a second team is the same as the second team's number of losses against the first team, I only needed to look at each team's wins to fill out the table. So I took the parent team's number of wins `"W"` for each opponent and added it to its respective row. 

If the cell row and column matched (a.k.a. the cell where the team is facing itself), I filled the cell with the `None` keyword.



The first three iterations of the outer for loop would look like this:
```js
# first iteration
[['Tm', 'BRO'], 
['BRO',  None,    10,    15,    15,    14,    14,    15,    11]]

# second iteration
[['Tm', 'BRO', 'BSN'], 
['BRO',  None,    10,    15,    15,    14,    14,    15,    11], 
['BSN',    12,  None,    13,    13,    13,    14,    12,     9]]

# third iteration
[['Tm', 'BRO', 'BSN', 'CHC'], 
['BRO',  None,    10,    15,    15,    14,    14,    15,    11], 
['BSN',    12,  None,    13,    13,    13,    14,    12,     9], 
['CHC',     7,     9,  None,    12,     7,    16,     8,    10]]

```

The final matrix:
```js
[['Tm', 'BRO', 'BSN', 'CHC', 'CIN', 'NYG', 'PHI', 'PIT', 'STL']
['BRO',  None,    10,    15,    15,    14,    14,    15,    11]
['BSN',    12,  None,    13,    13,    13,    14,    12,     9]
['CHC',     7,     9,  None,    12,     7,    16,     8,    10]
['CIN',     7,     9,    10,  None,    13,    13,    13,     8]
['NYG',     8,     9,    15,     9,  None,    12,    15,    13]
['PHI',     8,     8,     6,     9,    10,  None,    13,     8]
['PIT',     7,    10,    14,     9,     7,     9,  None,     6]
['STL',    11,    13,    12,    14,     9,    14,    16]]
```
