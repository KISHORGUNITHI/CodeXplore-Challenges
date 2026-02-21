

durations=[]

# here the termination is in user's hand
print("Enter songs as much as you want but ---If nothing left to input then PRESS ENTER:")
while(1):
    duration=input("Enter the song duration:")
    if duration!="":
        durations.append(int(duration))
    else:
        break;

# Invalid Entry handling
isInvalid=False
for dur in durations:
    if dur<=0:
        isInvalid=True
        print("Invalid Playlist")

# Playlist Analysis Rules
if not isInvalid:
    isRept=False
    isBalanced=False
    isIrr=False

    totalDur=sum(durations)
    for dur in durations:
        if durations.count(dur)>1:
            isRept=True
            break

    # Repetitive Playlist
    if totalDur<300:
        category="Too short Playlist"
        recommendation="Add more songs"
    elif totalDur>3600:
        category="Too Long Playlist"
        recommendation="Consider trimming your Playlist"
    elif isRept:
        category="Repetitive Playlist"
        recommendation="Add variety"
    elif 300<=totalDur<=3600:
        category="Balanced Playlist"
        recommendation="Good listening session"
    else:
        category="Irregular Playlist"
        recommendation="Needs better structuring"

    # Output
    print("Total Duration:",totalDur,"seconds")
    print("Songs:",len(durations))
    print("Category:",category)
    print("Recommendation:",recommendation)