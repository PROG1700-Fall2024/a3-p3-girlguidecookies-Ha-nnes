#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #: W0474277     
#Student Name: Hannes Meyer-Rahlfs 

def main():
    num_guides = int(input("How many guides sold cookies? "))# Getting user to input numebr of guides
    guides = {}  # Creating the empty dictionary for the names of the guides

    # For loop to collect the needed data                                                                      
    for i in range(num_guides):                                           
        name = input(f"Enter the name of guide {i+1}: ")
        sales = int(input(f"Enter the number of boxes sold by {name}: "))
        guides[name] = sales   # sending data to dictionary by using name as the key and sales as the variable

    avg_sales = sum(guides.values()) / num_guides # this is to calculate avg number of boxes sold across every guide
    highest_sales = max(guides.values()) # this is to get the highest number of boxes sold

    # Header for the table
    print("\nGuide   Prize won:")
    print("-------------------------------------")

    # This loop looks through the dictionary and determines the prizes to assing the guides based on value of their sales
    for name, sales in guides.items():       
        if sales == highest_sales:         
            prize = "Trip to the Jamboree"
        elif sales > avg_sales:
            prize = "Badge"
        elif sales > 0:
            prize = "Split remaining cookies"
        else:
            prize = "No prize"
        
        print(f"{name:<10} {prize}") 

    print(f"\nAverage sales: {avg_sales:.2f}") #rounded the sales 2 decimal places for visibility 

main()
