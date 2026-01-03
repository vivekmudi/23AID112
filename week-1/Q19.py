grades=[85,92,78,65,88,91,73,89,55,94]
A=0 ; B=0; C=0 ;D=0
for i in range(0,10):
  if grades[i]>=90:
       A+=1
  elif grades[i]>=80:
       B+=1
  elif grades[i]>=70:
       C+=1
  else:
       D+=1
print(f"{A} got A-grade(>=90)")
print(f"{B} got B-grade(80-89)")
print(f"{C} got C-grade(70-79)")
print(f"{D} got below 70")