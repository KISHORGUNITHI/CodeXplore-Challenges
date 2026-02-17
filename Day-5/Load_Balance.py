n=int(input("Enter the total no.of entries that you want to enter:"))
weights=[0]*n

# processed for taking weights
for i in range(n):
    weight=int(input(f"Enter the weight of package "+str(i+1)+" :"))
    weights[i]=weight;

# weights classification 

invalid_entries=[]
overload=[]
heavy_load=[]
normal_load=[]
very_light=[]

for weight in weights:
    if weight<0:
        invalid_entries.append(weight)
    elif weight<=5:
        very_light.append(weight)
    elif weight<=25:
        normal_load.append(weight)
    elif weight<60:
        heavy_load.append(weight)
    else:
        overload.append(weight)

