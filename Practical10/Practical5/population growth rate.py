table={"UK":[66.7,69.2],"China":[1426,1410],"Italy":[59.4,58.9],"Brazil":[208.6,212.0],"USA":[331.6,2240.1]}
percentchange={}
for country in table:
    percentchange[country]=((table[country][1]-table[country][0])/table[country][0])*100
print(percentchange.reverse())
print("Population with the highest growth rate:",max(percentchange, key=percentchange.get),"Population with the lowest growth rate:",min(percentchange, key=percentchange.get))
import matplotlib.pyplot as plt
plt.bar(percentchange.keys(),percentchange.values())
plt.xlabel("Countries")
plt.ylabel("Population Growth Rate (%)")
plt.title("Population Growth Rate by Country")
plt.show()