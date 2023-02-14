import time

intro = "💖💖💖...Welcome to Kelvin's Valentines Heart warmer😊🥰💖...\n...Celebrate your valentines in style😘🎉🥳\n"
for i in range(len(intro)):
    print(intro[i],sep='',end='',flush=True);time.sleep(0.05)
    
def get_name():
    name = input("Please enter your name😊: ")
    comment = "\nHello " + name + " every year on 14th of February we celebrate valentines day🎉\nHope this year You are celebrating it too😁😊\n"
    for i in range(len(comment)):
        print(comment[i],sep='',end='',flush=True);time.sleep(0.05)
    return name

def val(name):
    wish = "Hey there "+ name + "\nRoses are Red🌹,\n\tviolets are blue💙,\n\t\tSugar is sweet🍬,\n\t\t\tand so you are🥰"
    for i in range(len(wish)):
	    print(wish[i],sep='',end='',flush=True);time.sleep(0.05)
     
    
def get_gender():
    sex = "\nWe would like to know your gender\n"
    for i in range(len(sex)):
        print(sex[i],sep='',end='',flush=True);time.sleep(0.05)
    gender = input("Are you a male or a female👨👩: ")
    while gender == 'male' or gender == 'female':
        return gender
    else:
        gender = input("OOPS😔! Enter a valid choice...You can either be a male or a female!!")
        return gender
    
    
def get_status(name):
	statement = "\nHey "+ name +" please select your status✨"
	for i in range(len(statement)):
		print(statement[i],sep='',end='',flush=True);time.sleep(0.05)
	status = input("\n\tAre you single, searching, complicated, dating or married😍🥰: ")
	while status == 'single' or status =='searching' or status == 'dating' or status=='complicated' or status =='married':
		return status
	else:
		status = input("\t\tHey "+ name+" Make up your mind and give a valid choice:🙂 ")
		return status

        
   

def advise():
    name = get_name()
    gender = get_gender()
    state = get_status(name)
    if state == 'single' or state == 'searching' or state == 'dating' or state=='maried' or 'complicated':
        if state == 'single' and gender == 'male':
            football = input("\nHey bro do you love football [y/n]: ")
            if football == 'y':
                advice = "\t😁💪🤛You deserve to be happy we gat you covered\n\t\t champions league is back @"+name
                for i in range(len(advice)):
                    print(advice[i],sep='',end='',flush=True);time.sleep(0.05)
            else:
                advice = "Hey "+ name+" Mens Conference is on😂🤣"
                for i in range(len(advice)):
                    print(advice[i],sep='',end='',flush=True);time.sleep(0.05)
        elif state == 'single' and gender == 'female':
            advice = "Hey "+ name + " love is sweet please try and find a soulmate😊💖"
            for i in range(len(advice)):
                    print(advice[i],sep='',end='',flush=True);time.sleep(0.05)
        elif state == 'searching' and (gender == 'male' or gender =='female'):
            advice = "\t\t\tHello "+name+" we wish you the best as you search for a soulmate😊💖"
            for i in range(len(advice)):
                    print(advice[i],sep='',end='',flush=True);time.sleep(0.05)
            
        elif state == 'dating' and gender == 'female':
            advice = "\nKelvin wishes you a happy valentines as you celebrate with your boyfriend🥳🥰💖"
            for i in range(len(advice)):
                    print(advice[i],sep='',end='',flush=True);time.sleep(0.05)
                    val(name)
        elif state == 'dating' and gender == 'male':
            advice = "\nKelvin wishes you a happy valentines as you celebrate with your girlfriend🥳🥰💖"
            for i in range(len(advice)):
                    print(advice[i],sep='',end='',flush=True);time.sleep(0.05)
                    val(name)
        elif state == 'complicated':
            advice = "\nOOPS😔!! We are sorry for you , hope all goes well for you😢😔\n"
            for i in range(len(advice)):
                    print(advice[i],sep='',end='',flush=True);time.sleep(0.05)
            val(name)
        elif state == 'married'and (gender == 'male' or gender =='female'):
            choice = input("Congrats "+ name + " Can we get to know your partner's name [y/n]😊🥰: ")
            if choice == 'y' and gender == 'female':
                spouse = input("Whats his name🥰: ")
                advice = "Happy valentines day "+ name + " and " + spouse+ " 💖💖"
                for i in range(len(advice)):
                    print(advice[i],sep='',end='',flush=True);time.sleep(0.05)
                
            elif choice == 'y' and gender =='male':
                spouse = input("Whats her name🥰: ")
                advice = "Happy valentines day "+ name + " and " + spouse+ " 💖💖"
                for i in range(len(advice)):
                    print(advice[i],sep='',end='',flush=True);time.sleep(0.05)
               
            else:
                advice = "We wish you a happy valentines " + name + " and your spouse"+ " 💖💖"
                for i in range(len(advice)):
                    print(advice[i],sep='',end='',flush=True);time.sleep(0.05)
        print("\n!!!Thank You for visiting us have a nice day👍😊🥰")
                
    else:
        advice = "Thanks for visiting us👍😊🥰"
        for i in range(len(advice)):
                    print(advice[i],sep='',end='',flush=True);time.sleep(0.05)
       

advise()

    