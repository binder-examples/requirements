with open('dependent.txt', 'r') as file:
  if file == '':
    print(":heavy_check_mark: All dependencies up to date :heavy_check_mark:")
  else:
    print("### :x: Outdated/Missing Dependencies List :x:")
    for line in file:
      listings = list(line.split())
      length = len(listings)
    
      for i in range(length):
        if i == length-1:
          print(listings[i], end=" | \n")
        else:
          print(listings[i], end=" | ")

    print("##### Update these dependencies:")
    print("""- Ensure that ALL dependencies in the ***requirements.txt*** file are connected to their version with 
    ***>=*** and not ***==*** (i.e. ***pandas>=1.5.1***)""")
    print("- Run the following command within the folder the ***requirements.txt*** file resides")
    print("  - ***pip install -r requirements.txt -U***")
file.close()
