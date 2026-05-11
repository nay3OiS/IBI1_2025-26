# aim：to predict creatinine clearance rate for a person
# a is the age, unit: year
# b is the weight, unit: kg
# c is gender
# d is creatine concentration, Cr, in μmol/l
a=int(input("Please enter your age: "))
b=int(input("Please enter your weight in kg:"))
c=input("Please input your gender (male or female):")
d=int(input("Please enter your Cr in μmol/l:"))
error="Please try it again."
if not (0<a<100):
   error=error+"The age must be between 0 and 100 (excluded 0 and 100)."
if not (20<b<80):
   error=error+"The weight must be between 20 and 80 kg (excluded 20 and 80)."
if c not in ["male","female"]:
   error=error+"The gender must be male or female."
if not (0<d<100):
   error=error+"The Cr must be between 0 ad 100 μmol/l (excluded 0 and 100)."
if error!="Please try it again.":
   print(error)
else:
    if c == "male":
      print("CrCl=", (140-a)*b/(72*d))
    else:
      print("CrCl=", 0.85*(140-a)*b/(72*d))