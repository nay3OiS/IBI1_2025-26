dic={"TP53":12.4,"EGFR":15.1,"BRCA1":8.2,"PTEN":5.3,"ESR1":10.7}
print(dic)
dic["MYC"]=11.6
import matplotlib.pyplot as plt
plt.bar(dic.keys(),dic.values())
plt.xlabel("Genes")
plt.ylabel("Expression level")
plt.title("Gene expression levels")
plt.show()
a=input("Enter a gene name: ")
if a in dic:
    print("The expression level of",a,"is",dic[a])
else:
    print("Gene not found.")
average=sum(dic.values())/len(dic)
print("The average expression level is",average)