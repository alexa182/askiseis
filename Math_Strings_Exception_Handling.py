while True: #<- anagazw to input na einai number(int) gia na sunexisei
      try: #<- kanw try giat kserw oti mporei na yparxei periptosi error
        number = int(input("PLS ENTER A NUMBER: "))
        break #<- an valei noumero vgenei apo while loop


      except ValueError: #<-- an yparxei VALUERROR(an afisw mono to except tha katalavei oti enww ola ta errors)
          print("YOU DIDNT ENTER A NUMBER")

      except:
          print("AN UNKNOWN ERROR OCCURRED")

print("THANK YOU FOR ENTERING A NUMBER")