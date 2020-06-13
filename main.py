print("Hi. Today we are going to do steps from Proposal to Payment")
a = input("Are you the employer or the employee:  ")
if a == "employer":
  print("Welcome employer")
  def client_request():
   b = input("Do you have a client request. Yes or No: ")
   if b == "Yes" or b == "y" or b == "yes" or b == "Y":
    def proposal():
      c = input("Have you given the client a proposal. Yes or No:  ")
      if c == "Yes" or c == "yes" or c == "Y" or c == "y":
        print("You can continue.")
        def contract():
          d = input("Do you have a contract:  ")
          if d == "Yes" or d == "Y" or d == "y" or d == "yes":
            def code():
              e = input("Has the employee finnished the code:  ")
              if e == "Yes" or e == "y" or e == "yes" or e == "Y":
                def invoice():
                  f = input("Have you written an invoice to the client. Yes or No:  ")
                  if f == "Yes" or f == "y" or f == "Y" or f == "yes":
                    def payment():
                      g = input("Have you paid the employee:  ")
                      if g == "Yes" or g == "yes" or g == "Y" or g == "y":
                        print("Thankyou for all that you have done.")
                      elif g == "No" or g == "n" or g == "no" or "N":
                        print("Make sure you pay the employee")
                        payment()
                    payment()   
                  elif f == "No" or f == "no" or f == "N" or f == "n":
                    print("You need to write an invoice to the client")
                    invoice()
                invoice()
              elif e == "No" or e == "n" or e == "no" or e == "N":
                print("Call the employee to ask him if he has finnished the work.")
                code()
            code()
          elif d == "No" or d == "n" or d == "Y" or d == "yes":
            print("You are supposed to have a contract to continue.")
            contract()
        contract()
      elif c == "No" or c == "n" or c == "no" or c == "N":
        print("You need to develop a proposal")
        proposal()
    proposal()
   elif b == "No" or b == "n" or b == "no" or b == "N":
     print("Call the client to tell them for Client request")
     client_request()
  client_request()
  
