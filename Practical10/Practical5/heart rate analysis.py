heart_rates=[72,60,126,85,90,59,76,131,88,121,64]
patient=0
for i in range(len(heart_rates)):
    if heart_rates[i]>120 or heart_rates[i]<60:
        patient+=1
print("Number of patients with abnormal heart rates:",patient)
print("The average heart rate is:",sum(heart_rates)/len(heart_rates))
low=normal=high=0
for i in range(len(heart_rates)):
    if heart_rates[i]<60:
        low+=1
    elif heart_rates[i]>120:
        high+=1
    else:
        normal+=1
print("Number of patients with low heart rates:",low)
print("Number of patients with normal heart rates:",normal) 
print("Number of patients with high heart rates:",high)
import matplotlib.pyplot as plt
plt.pie([low,normal,high],labels=["Low","Normal","High"],autopct="%1.1f%%",shadow=True)
plt.title("Heart Rate Distribution")
plt.show()

        