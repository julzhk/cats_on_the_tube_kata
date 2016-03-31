Cats run away from their houses all the time and that's really inconvenient for their owners.

Determine how likely is that an owner will find their cat:
- Run a simulation placing random owners and cats all around the tube map
- check how long it takes them to find each other.

- You should create N owners and N cats, where N is specified by command-line.
- The initial position of the owner and the cat must be random and different to each other.
- Any number of owners and cats can start in the same station.
- Because cats are not very intelligent, at each turn they will move randomly to one of the stations
  connected to their current station.
- Owners are more intelligent: they will move to a station connected to their current station, 
  but (if at all possible) not use a station they have visited before.

- Every time an owner finds their cat, the amount of love released is SO big
that TFL needs to close the station to clean the love from the walls.

- When a station is closed, owners and cats at the station will leave it as usual, 
but nobody can visit this station again.

- It is possible that owners or cats can get trapped at a station because there are 
no available routes to leave -- that's ok, we don't care - that's life.

- Create a program that reads in the tube map, 
- creates N owners and cats and unleashes them. 

- The program should run until all the owners have found their cats, 
- or each owner and cat has moved 100,000 times.

- When an owner finds their cat the output should be of the form:
  Owner 14 found cat 14 - Picadilly Circus is now closed.

- Once the program has finished, it should print out something like:

Total number of cats: 200
Number of cats found: 25
Average number of movements required to find a cat: 34

- Calculate other metrics: eg: the most visited station or the owner with least luck... 
- feel free to include these in the final output too.

Review notes:
 - We are not looking for speed, we are looking for a readable elegant solution.
 - It is ok to make assumptions as far as you write them in a comment.
 - Feel free to write tests (If you wish)