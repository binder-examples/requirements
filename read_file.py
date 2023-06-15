# Open file with outdated dependencies
with open('dependent.txt', 'r') as depend:

  # If the file is empty, this means all dependencies are up to date
  if depend == '':
    print(":heavy_check_mark: All dependencies up to date :heavy_check_mark:")

  # If the file is not empty, we make a table out of it's content
  else:

    # Header
    print("### :x: Outdated/Missing Dependencies List :x:")

    # Read file line-by-line
    for line in depend:
      listings = list(line.split())
      length = len(listings)

      # Read line word-by-word
      for i in range(length):

        # If it is the last word in the line, advance to next line after printing
        if i == length-1:
          print(listings[i], end=" | \n")

        # All other words will be printed as is with a '|' to make a table
        else:
          print(listings[i], end=" | ")

    # Instructions outlining how to update outdated dependencies
    print("##### How to update these dependencies:")
    print("""- Ensure that ALL dependencies in the ***requirements.txt*** file are connected to their version with 
    '***>=***' and not '***==***' (i.e. ***pandas>=1.5.1***)""")
    print("- Run the following command within the folder the ***requirements.txt*** file resides")
    print("  - ***pip install -r requirements.txt -U***")
    print("- **OR** run the command ***pip install {DEPENDENCY_NAME} -U*** to update a specific dependency")
file.close()

with open('check_major_minor.txt', 'r') as checker:
  if 'Major' in checker:
    print("### MAJOR DEPENDENCY UPDATE(S): Make sure to check the dependency docs before updating")
  if 'Minor' in checker:
    print("### MINOR DEPENDENCY UPDATE(S): Update these dependencies before merging")
    sys.exit("Minor dependency updates available")
