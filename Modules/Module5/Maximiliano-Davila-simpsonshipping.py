print("Welcome to Simpsons'shipping")
weight:float = float(input("what is the weight of your package"))

#groud shipping

if(weight == 2 or weight < 2):

    costground = weight * 1.75 + 20

    print("Ground shipping: $", float(costground))
elif(weight > 2  or weight <= 6  ):

    costground = weight * 3.40 + 20

    print("Ground shpping:$", float(costground))

elif(weight > 6 or weight <= 10):

    costground = weight * 4.50 + 20

    print("Ground shipping: $", float(costground))

else:
    print("weight > 10")
    
    costground = weight * 5.25 + 20

    print("Ground shipping: $", float(costground))


#Courier shpping

if(weight == 2 or weight < 2):
    
    courierground = weight * 3.50 + 5

    print("Courier shipping: $", float(courierground))
elif(weight > 2  or weight <= 6  ):

    courierground = weight * 7.00 + 8.00

    print("Courier shpping:$", float(courierground))

elif(weight > 6 or weight >= 10):

    courierground = weight * 9.00 + 12.00

    print("Courier shipping: $", float(courierground))

else:
    print("weight > 10")
    
    courierground = weight * 10.50 + 15.00

    print("Courier shipping: $", float(courierground))

#Drone shpping

if(weight == 2 or weight < 2):
    
    droneground = weight * 5.25 + 0.00

    print("Drone shipping: $", float(droneground))
elif(weight > 2  or weight <= 6  ):

    droneground = weight * 10.50 + 0.00

    print("Drone shpping:$", float(droneground))

elif(weight > 6 or weight >= 10):

    droneground = weight * 13.50 + 0.00

    print("Drone shipping: $", float(droneground))

else:
    
    droneground = weight * 15.75 + 0.00

    print("Drone shipping: $", float(droneground))

print("Ground Shipping Premium charge $150")