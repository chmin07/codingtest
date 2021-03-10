def soulution(a,b):

    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    day=["THU","FRI","SAT","SUN","MON","TUE","WED"]
    c= sum(month[:a-1],b) % 7
   	return(day[c])
   
