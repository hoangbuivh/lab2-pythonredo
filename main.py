def getLetterGrade(scoreGrade):
  scoreGrade = float(input("Enter your CMPSC 131 grade: "))
  letterGrade = ""
  if scoreGrade >= 93.0: 
    letterGrade = "A"
  elif scoreGrade <= 93.0 and scoreGrade >= 90.0: 
    letterGrade = "A-"
  elif scoreGrade <= 90.0 and scoreGrade >= 87.0: 
    letterGrade = "B+"
  elif scoreGrade <= 87.0 and scoreGrade >= 83.0: 
    letterGrade = "B"
  elif scoreGrade <= 83.0 and scoreGrade >= 80.0: 
    letterGrade = "B-"
  elif scoreGrade <= 80.0 and scoreGrade >= 77.0: 
    letterGrade = "C+"
  elif scoreGrade <= 77.0 and scoreGrade >= 70.0: 
    letterGrade = "C"
  elif scoreGrade <= 70.0 and scoreGrade >= 60.0: 
    letterGrade = "D"
  else: 
    letterGrade = "F"
  print(f"Your letter grade for CMPSC 131 is {letterGrade}. ")

  if __name__== "__main__":
    getLetterGrade(scoreGrade)
