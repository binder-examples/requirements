with open('dependent.txt', 'r') as file:
  # first_line = file.readline().strip("\n")
  
  for line in file:
    listings = list(line.split())
    length = len(listings)
    
    for i in range(length):
      if i == length-1:
        print(listings[i], end=" | \n")
      else:
        print(listings[i], end=" | ")

    # if line == first_line:
      
