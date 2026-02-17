n=int(input("Enter the total no.of entries that you want to enter:"))
weights=[0]*n

# processed for taking weights
for i in range(n):
    weight=int(input(f"Enter the weight of package "+str(i+1)+" :"))
    weights[i]=weight;

# Weights Classification 

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
    elif weight<=60:
        heavy_load.append(weight)
    else:
        overload.append(weight)

# Applying PLI
My_Name="KISHORGUNITHI"
L=len(My_Name)
PLI=L%3;

final_plan = []
# removes very_light only
for weight in weights:
    if weight>5:        
        final_plan.append(weight)


# counting Total valid weights
valid_count=n-len(invalid_entries)
print("\nNo.of Valid_Entries are:",valid_count)
# Counting affected items due to PLI
affected=len(very_light)
print("\nNo.of affected entries due to PLI are:",affected)

# Display L and PLI
print(f"\nL={L} and PLI={PLI}")

print("\nVery Light List:",very_light)
print("Normal Load List:",normal_load)
print("Heavy Load List:",heavy_load)
print("Over Load List:",overload)
print("Invalid-Entries List:",invalid_entries)

# Display Final Plan
print("\nFinal Plan List:",final_plan)