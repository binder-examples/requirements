# Open file with outdated dependencies
with open('dependent.txt', 'r') as depend:

  # If the file is empty, this means all dependencies are up to date
  if depend == '':
    print("## :heavy_check_mark: All dependencies up to date :heavy_check_mark:")

  # If the file is not empty, we make a table out of it's content
  else:

    # Header
    print("## :small_red_triangle_down: Outdated/Missing Dependencies List :small_red_triangle_down:")

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
    print("##")
    print("### Updating **SPECIFIC** Dependencies:")
    print("""- Ensure that ALL dependencies in the ***requirements.txt*** file are connected to their version with 
    '***>=***' and not '***==***' (i.e. ***pandas>=1.5.1***)""")
    print("- Go inside the folder with the ***requirements.txt*** file from your CLI")
    print("- Run the following command in your CLI to update the dependency:")
    print("  - ***pip install {DEPENDENCY_NAME} -U --force-reinstall***")

    print("### Updating **ALL** Dependencies **(not recommended, will update dependencies with major updates)**:")
    print("""- Ensure that ALL dependencies in the ***requirements.txt*** file are connected to their version with 
    '***>=***' and not '***==***' (i.e. ***pandas>=1.5.1***)""")
    print("- Go inside the folder with the ***requirements.txt*** file from your CLI")
    print("- Run the following command in your CLI to update all dependencies:")
    print("  - ***pip install -r requirements.txt -U --force-reinstall***")
depend.close()

with open('check_major_minor.txt', 'r') as checker:
  content = checker.read()

  print("##")
  
  if 'Major' in content:
    print("#### :warning: MAJOR DEPENDENCY UPDATE(S): Make sure to check the dependency docs before updating :warning:")
    
  if 'Minor' in content:
    print("#### :x: MINOR DEPENDENCY UPDATE(S): Update these dependencies, otherwise the check will keep failing :x:")
    exit("Cannot merge: Minor dependency updates available")
