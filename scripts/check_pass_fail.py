with open('check_major_minor.txt', 'r') as checker:
  content = checker.read()
  
  if 'Minor' in content:
    exit("Cannot merge: Minor dependency update(s) available")
