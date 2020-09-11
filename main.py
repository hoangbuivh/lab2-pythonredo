def getLetterGrade(scoreGrade):
  if scoreGrade >= 93.0: 
    return "A"
  elif scoreGrade <= 93.0 and scoreGrade >= 90.0: 
    return "A-"
  elif scoreGrade <= 90.0 and scoreGrade >= 87.0: 
    return "B+"
  elif scoreGrade <= 87.0 and scoreGrade >= 83.0: 
    return "B"
  elif scoreGrade <= 83.0 and scoreGrade >= 80.0: 
    return "B-"
  elif scoreGrade <= 80.0 and scoreGrade >= 77.0: 
    return "C+"
  elif scoreGrade <= 77.0 and scoreGrade >= 70.0: 
    return "C"
  elif scoreGrade <= 70.0 and scoreGrade >= 60.0: 
    return "D"
  else: 
    return "F"
  
def run(): 
  entrance = input("Enter your CMPSC 131 grade: ")
  print("Your letter grade for CMPSC 131 is ",getLetterGrade(entrance),".")

if __name__== "__main__":
  run()
