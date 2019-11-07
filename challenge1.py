#!/usr/bin/env python3
import random

"""File name: challenge.py

How It Works:
    0. this applaction depend on Path (every recomend has it's path and also new recommends)
    1. The user will enter three inputs: age, gender and type of recommendation
    2. The program  sort the user based on their age into 3 categories
    :less than 16 years old, from 16 years old to 40 and above 40 years old
    3. The program sort the user based on their gender to either female or male
    4. The program provide 3 types of categories: a gift, a film or a restaurant
    5. The program provide different suggestions based on different inputs
    6. The user can enter new suggestions from the terminal/shell
    7.  general_recommends : a list stores untitled added recommendation
    to keep the applaction strong and smart
Extra:
    1. The program can filter user suggestion with  with not specific gender or age or type
    And  store them at general_recommends
    2. The Program filter words like gun
    3. Try adding a movie called Top Gun, or blood, or etc. to recommends for kids section,
    To check the app ability to protect kids section from spam!

"""

#Fake DataBase
#I used global variables to be able to check the new added suggestion from users
gift_a_female = ["Toy", "Barbie", "Puzzle", "Ipad", "Teddy Bear"]
gift_b_female = ["Perfume", "dress", "Hot Air Brush", "Flowers", "Makeup Set"]  # gifts for > 16 female and < 40
gift_c_female = ["Necklace", "Ring", "Programmable Pressure Cooker", "printed cup"] # female > 40

rest_a_female = ["Super Kid Restaurant", "Zengo", "Mcdonalds", "Margherita", "Wavebreaker", "Chuck E. Cheese's"]
rest_b_female = ["Izakaya", "Zengo", "Armani/Hashi", "Revo Cafe", "Sardina Seafood Restaurant", "Rockfish", "Market24", "Sansation", " The Hamptons Cafe" ]
rest_c_female = ["Margherita", "Bombay Brasserie","Al Dawaar Revolving Restaurant", "Sardina Seafood Restaurant", "Rockfish", "Market24", "Sansation", " The Hamptons Cafe" ]

film_a_female = ["Lego DC Super Hero Girls", "Frozen1", "Frozen2", "Lady and the Tramp", "Trolls Holiday", "Aladdin" ]
film_b_female = ["he Empire Strikes Back", "The Big Sick", "An Affair to Remember", "The Notebook", "The Apartment", "A Knight's Tale" ]
film_c_female = ["Manhattan", "Pretty Woman", "The Fly", "The Big Sick.", "Wings of Desire ", "Gone with the Wind" ]

gift_a_male = ["PlayStaion", "Football", "Computer", "Mobile", "WowWee Robot"] # males < 16
gift_b_male = ["Headphone", "Men Wallet", "Laptop", "Whey protein"] # males > 16 and < 40
gift_c_male = ["Perfume", "Wrist watch", "Suit", "Sun glasses", "Car"] # males > 40

rest_a_male = ["Super Kid Restaurant", "Margherita", "mcdonalds", "subway", "burger king", "Wavebreaker" ]
rest_b_male = ["Wavebreaker", "Reform Social & Grill", " Margherita", "Bombay Brasserie", "Sardina Seafood Restaurant", "Rockfish" ]
rest_c_male = ["Benihana", "Solo Dubai", "Margherita", "Bombay Brasserie", "Al Dawaar Revolving Restaurant", "Rockfish" ]

film_a_male = ["Toy Story", "Wonder Park", "The Lion Kin", "Aladdin", "the boss baby", "Small Foot", "Avengers" ]
film_b_male = ["Joker", "Aladdin", "The Dead Don't Die", "Zombieland", "in the Tall Grass", "Top Gun 2" ]
film_c_male = ["Angry Men", "Citizen Kane", "Casablanca", "Apocalypse Now", "A Space Odyssey", "Psycho" ]

general_recommends = [] # for undefined recmoends

close_msg = "Thanks For Using ASK ME Bot Applaction"


# filter function made to store the user recommendation in the right path (category)
# also for filter some bad words to protect kids
def filter():
    index = 0
    kids = []
    adults = []
    adultsM = []    
    rAge = input("Select age Catagroy(Kids/Adults/Old) press enter to skip" + "\n")
    rGender = input("For what gender (m/f)? if you don't want to specify just click on enter" + "\n")
    rType = input("What type of recommendation is it (gift/film/restaurant" + "\n")
    template = input("please Enter Your Recommendation" + "\n")
    # filter methods to filter results for kids
    while index < len(template):
        if template[index:index+6] == 'top gun' and rType == "film":
            if rGender == "m":
                film_b_male.append(template)
                index += 6
                print("Thank You for Your Reccommendation Path(adults/F/m") # path where the file has appended to or in which list (adults/Film/Male)
                break
            else:
                film_b_female.append(template)
                index += 6
                print("Thank You for Your Reccommendation Path(adults/F/f)")
                break
            
            #Important elif statement to filter and protect kids suggestion 

        elif template[index:index+3] == 'gun' and rType == "film": #if User added movie name gun to kids add it to adults male
            film_b_male.append(template)
            index += 3
            print("Thank You for Your Reccommendation Path(adults/F/m)") 
            break
        
        elif template[index:index+3] == 'gun' and rType == "film" and rGender == "f":  #if User added movie name gun to kids add it to adults male
            film_b_female.append(template)
            index += 3
            print("Thank You for Your Reccommendation Path(adults/F/f)")
            break
            
        elif 'top gun' in template and rType == "film" and rGender != 'f': #another filter type direct search
            film_b_male.append(template)
            index += 6
            print("Thank You for Your Reccommendation Path(adults/F/m)")
            break
        elif 'top gun' in template and rType == "film" and rGender == "f":
            film_b_female.append(template)
            index += 6
            print("Thank You for Your Reccommendation Path(adults/F/f)")
            break
        elif 'top gun' in template and rType == "film" and rGender == "" and rAge == "":
            film_b_male.append(template)
            index += 6
            print("Thank You for Your Reccommendation Path(adults/F/m)")
            break
        elif template[index:index+6] == 'horror' and rType == "film" and rGender == "m" and rAge == "kids":
            film_b_male.append(template)
            index += 6
            print("Thank You for Your Reccommendation Path(adults/F/m)")
            break
        elif template[index:index+6] == 'horror' and rType == "film" and rGender == "f" and rAge == "kids":
            film_b_male.append(template)
            index += 6
            print("Thank You for Your Reccommendation Path(adults/F/f)")
            break
        elif template[index:index+3] == 'gun' and rType == "gift" and rGender == "m" and rAge == "kids":
            gift_b_male.append(template)
            index += 3
            print("Thank You for Your Reccommendation Your Path(adults/G/m)")
            break
        elif template[index:index+3] == 'gun' and rType == "gift" and rGender == "f" and rAge == "kids":
            gift_b_female.append(template)
            index += 3
            print("Thank You for Your Reccommendation Your Path(adults/G/f)")
            break
            
                    
        elif template[index:index+3] == 'gun' and rType == "film" and rGender == "kids":
            film_b_male.append(template)
            index += 3
            print("Thank You for Your Reccommendation Path(adults/F/m)")
            break

        elif template[index:index+5] == 'blood' and rType == "film":
            film_b_male.append(template)
            index  += 5
            print("Thank You for Your Reccommendation Path(adults/F/m)")
            break
            
        elif rAge == "kids" and rGender == "m" and rType == "gift":
            gift_a_male.append(template)
            index += 5
            print("Thank You for Your Reccommendation Your Path:(kids/G/m)")
            break
        
        elif rAge == "adults" and rGender == "m" and rType == "gift":
            gift_b_male.append(template)
            index += 5
            print("Thank You for Your Reccommendation Your Path(adults/G/m)")
            break

        elif rAge == "old" and rGender == "m" and rType == "gift":
            gift_b_male.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path:(old/G/m)")
            break
        
        elif rAge == "kids" and rGender == "m" and rType == "film":
            film_a_male.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path:(kids/F/m)")
            break

        elif rAge == "adults" and rGender == "m" and rType == "film":
            film_b_male.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path:(adult/F/m)")
            break

        elif rAge == "old" and rGender == "m" and rType == "film":
            film_c_male.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path:(old/F/m)")
            break
        
        elif rAge == "kids" and rGender == "m" and rType == "restaurant":
            rest_a_male.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path:(kids/R/m)")
            break

        elif rAge == "adults" and rGender == "m" and rType == "restaurant":
            rest_b_male.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your path(adults/R/m)")
            break

        elif rAge == "old" and rGender == "m" and rType == "restaurant":
            rest_c_male.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path:(old/R/m)")
            break

        # Female



        elif rAge == "kids" and rGender == "f" and rType == "gift":
            gift_a_female.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path:(kids/G/f)")
            break
        
        elif rAge == "adults" and rGender == "f" and rType == "gift":
            gift_b_female.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path(adults/G/f)")
            break


        elif rAge == "old" and rGender == "f" and rType == "gift":
            gift_c_female.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path(old/G/f)")
            break



        elif rAge == "kids" and rGender == "f" and rType == "film":
            film_a_female.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path(kids/f/f)")
            break


        elif rAge == "adults" and rGender == "f" and rType == "film":
            film_b_female.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path(adults/f/f)")
            break


        elif rAge == "old" and rGender == "f" and rType == "film":
            film_c_female.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path(old/f/f)")
            break



        elif rAge == "kids" and rGender == "f" and rType == "restaurant":
            rest_a_female.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path(kids/R/f)")
            break


        elif rAge == "adults" and rGender == "f" and rType == "restaurant":
            rest_a_female.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path(adults/R/f)")
            break



        elif rAge == "old" and rGender == "f" and rType == "restaurant":
            rest_a_female.append(template)
            index +=5
            print("Thank You for Your Reccommendation Your Path(old/R/f)")
            break
            
        else:            
                        general_recommends.append(template)
                        index += len(template)
                        print("Thank You for Your Reccommendation your Path(general_recommends)")
                        checkR = input("Wana Check general recommends (Y/N)")
                        if checkR == "Y" or "y":
                            print("general_recommends")
                        else:
                            return "Thanks For Using Ask Me Bot"
                            
                        break
                        
    
                        

#bot is the main function for the app it do almost every thing
#used filter function to add new recommendation                    

def bot():
        # We Will USE Random to get random recomends based on this fake database
        # Define the age categories
        # categories id will be a, b, and c for kids, adults, old
        #example if age < 16 and gender == male and recomend == gift random.choice gift_a_fmale
        kids = int
        adults = int
        old = int
        genders = ['male', 'female']
        categories = [kids, adults, old]
        
         
        # Check if age is int or not
        # I used try and except to solve error if not int (I could also Use age.isdigit())
        print("+------------------------|")
        print("| Hello I'm  Ask Me Bot! |")
        print("+------------------------|")
        print(" ")
        print("----------------------------------------------------------------------+")
        print("About: Used to publish and get suggestions based on a fake database.  |")        
        print("----------------------------------------------------------------------+")
        print(" ")
       
        try:
                age = int(input("How Old Are You Sir? " + "\n"))
                gender = str(input("What is your gender? Enter F for female and M for male " + "\n")) #if x != str mean x == int ask next question
        except:
                print("Warning : Enter Numbers Only or App Will close") # if x != int print age again
                age = int(input("How Old Are You Sir? " + "\n"))
                gender = str(input("What is your gender? Enter F for female and M for male " + "\n"))                
                               
        # check if gender == m or f or something else
        if gender == "m" or gender == "f" or gender == "M" or gender == "F":
                recommend = str(input("What would You Like me to Recommend? A gift, B resturant or C Film? " + "\n")) # if gender == m or f print next input
        else:
                if gender != "m" or gender != "f" or gender != "M" or gender != "F":
                        print("You Must Enter F for female Or M for male only ")  # if gender != m or f tell the user and print gender input again 
                        gender = str(input("What is your gender? Enter F for female and M for male " + "\n"))
                        if gender == "m" or gender == "f" or gender == "M" or gender == "F":
                                recommend = str(input("What would You Like me to Recommend? A gift, B resturant or C Film? " + "\n"))
                        else:
                                if gender != "m" or gender != "f" or gender != "M" or gender != "F":                                        
                                        return "!Bad Inputs 2 Times The App Will Close Now"
                                    
        if recommend == "a" or recommend == "b" or recommend == "c" or recommend == "A" or recommend == "B" or recommend == "C":
                right_inputs = 1
        else:
                if recommend != "a" or recommend != "b" or recommend != "c" or recommend != "A" or recommend != "B" or recommend != "C":
                        print("!please Enter A or B or C only Or App Will Close")
                        recommend = str(input("What would You Like me to Recommend? A gift, B resturant or C Film? " + "\n"))
                        if recommend == "a" or recommend == "b" or recommend == "c" or recommend == "A" or recommend == "B" or recommend == "C":
                                right_inputs = 1
                        else:
                                
                                return "!Wrong Inputs Two Time App Will Close Now ... "  #app closed                                                                  

        # check the user input and proccess it then output the result
        # ask user for new sugesstions if yes use filter function to store the data 
        # #Female 
        if age < 16 and gender == "f" and recommend == "a":
                agift = random.choice(gift_a_female)
                print("How About: " + agift + "?")
                ask = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask == "y":
                    filter() #You Should Check filter function synchronous with bot main function()
                else:
                    print(close_msg)
                    
                
                
        elif age > 16 and age < 40 and gender == "f"  and recommend == "a":
                bgift = random.choice(gift_b_female)
                print("How About: " + bgift + "?")
                ask1 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask1 == "y":
                    filter()
                else:                    
                    print(close_msg)                   
                                
        elif gender == "f"  and age > 40 and recommend == "a":
                cgift = random.choice(gift_c_female)
                print("How About: " + cgift + "?")
                ask2 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask2 == "y":
                    filter()
                else:
                    print(close_msg)                    
                
                                
        elif age < 16 and gender == "f"  and recommend == "b":
                arest = random.choice(rest_a_female)
                print("How About: " + arest + "?")
                ask3 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask3 == "y":
                    filter()
                else:
                    print(close_msg)                  
                
            
        elif age > 16 and age < 40 and gender == "f" and recommend == "b":
                brest = random.choice(rest_b_female)
                print("How About: " + brest + "?")
                ask4 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask4 == "y":
                    filter()
                else:
                    print(close_msg)
                    
                
        elif gender == "f" and age > 40 and recommend == "b":
                crest = random.choice(rest_c_female)
                print("How About: " + crest + "?")
                ask5 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask5 == "y":
                    filter()
                else:
                    if ask5 != "y" and ask5 == "n":
                        print(close_msg)
                        
                                      
                
        
        elif gender == "f" and age < 16 and recommend == "c":
                afilm = random.choice(film_a_female)
                print("Watch: " + afilm + "!")
                ask6 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask6 == "y":
                    filter()
                else:
                    print(close_msg)                    
                
        elif gender == "f" and age > 16 and age < 40 and recommend == "c":
                bfilm = random.choice(film_b_female)
                print("Watch: " + bfilm + "!")
                ask7 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask7 == "y":
                    filter()
                else:
                    print(close_msg)                   
                                
        elif gender == "f" and age > 40 and recommend == "c":
                cfilm = random.choice(film_c_female)
                print("Watch: " + cfilm + "!")
                ask8 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask8 == "y":
                    filter()
                else:
                    print(close_msg)                  
                                
        # #Male
         
        elif age < 16 and gender == "m" and recommend == "a":
                agift = random.choice(gift_a_male)
                print("How About: " + agift + "?")
                ask9 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask9 == "y":
                    filter()
                else:
                    print(close_msg)                    
                                
        elif age > 16 and age < 40 and gender == "m"  and recommend == "a":
                bgift = random.choice(gift_b_male)                
                print("How About: " + bgift + "?")
                ask10 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask10 == "y":
                    filter()
                else:
                    print(close_msg)                     
                                
        elif gender == "m"  and age > 40 and recommend == "a":
                cgift = random.choice(gift_c_male)
                print("How About: " + cgift + "?")
                ask11 = input("Would You Like add More Recommendations? Enter y : other key To skip" + "\n") #new style
                if ask11 == "y":
                    filter()
                else:
                    print(close_msg)
                    
                
        elif age < 16 and gender == "m"  and recommend == "b":
                arest = random.choice(rest_a_male)
                print("How About: " + arest + "?")
                ask12 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask12 == "y":
                    filter()
                else:
                    print(close_msg)                 
                                
        elif age > 16 and age < 40 and gender == "m" and recommend == "b":
                brest = random.choice(rest_b_male)
                print("How About: " + brest + "?")
                ask13 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask13 == "y":
                    filter()
                else:
                    print(close_msg)                    
                                
        elif gender == "m" and age > 40 and recommend == "b":
                crest = random.choice(rest_c_male)
                print("How About: " + crest + "?")
                ask14 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask14 == "y":
                    filter()
                else:
                    print(close_msg)                    
                       
        elif gender == "m" and age < 16 and recommend == "c":
                afilm = random.choice(film_a_male)
                print("Watch: " + afilm + "!")
                ask15 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask15 == "y":
                    filter()
                else:
                    print(close_msg)                   
                               
        elif gender == "m" and age > 16 and age < 40 and recommend == "c":
                bfilm = random.choice(film_b_male)
                print("Watch: " + bfilm + "!")
                ask16 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask16 == "y":
                    filter()
                else:
                    print(close_msg)                
                
        elif gender == "m" and age > 40 and recommend == "c":
                cfilm = random.choice(film_c_male)
                print("Watch: " + cfilm + "!")
                ask17 = input("Would You Like add More Recommendations? Enter y/n" + "\n")
                if ask17 == "y":
                    filter()
                else:
                    print(close_msg)
bot()                
                
