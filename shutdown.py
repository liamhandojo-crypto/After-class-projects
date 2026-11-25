def shutdown():
    a=input("Do you want to shutdown the system?  ")
    if a=='Yes' or a=='yes':
        print("Shutting down...")
    elif a=='No' or a=='no':
        print("Aborting shutdown...")
    else:
        print("Sorry")


shutdown()


