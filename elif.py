time=input("enter the time")
if time>="6:15" and time<="6:59":
    print("morning exercise")
elif time>="7:00" and time<="7:58":
    print("fresh up")
elif time>="8:00" and time<="8:29":
    print("break fast")
elif time>="8:30" and time<="12:28":
    print("1st coding")
elif time>="12:30" and time<="13:59":
    print("lunch break")
elif time>="14:00" and time<="16:59":
    print("2nd coding")
elif time>="17:00" and time<="17:57":
    print("snacks break")
elif time>="18:00" and time<="18:56":
    print("english acticity")
elif time>="19:00" and time<="19:55":
    print("recreation activity")
elif time>="20:00" and time<="20:59":
    print("dinner break")
elif time>="21:00" and time<="21:59":
    print("aptitude class")
else:
   print("nothing")
