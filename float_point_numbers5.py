
#How tall is the tree : 5
    #
   ###
  #####
 #######
#########
    #


# use 1 while loop and 3 for loops
# 4 spaces : 1 hash
# 3 spaces : 3 hash
# 2 spaces : 5 hash
# 1 space : 7 hash
# 0 spaces: 9 hash


#NEED TO DO

#1. Decrement spaces by 1 each time through the loop
#2. Increment the hashes by 2 each time through the loop
#3. Save spaces to the stump by calculating tree height - 1
#4. Decrement from tree height until it equals 0
#5. Print spaces and then hashes for each row
#6. Print stump spaces and then 1 hash



# GET THE NUMBER OF ROWS FOR THE TREE

tree_height = int(input("how tall is the tree: ")) # CONVERT IT INTO AN INTEGER

# GET THE STARTING SPACES FOR THE TOP OF THE TREE

spaces = tree_height - 1

# THERE IS ONE HASH TO START THAT WILL BE INCREMENTED

hashes = 1

# SAVE STUMP SPACES TIL LATER

stump_spaces = tree_height - 1

# MAKE SURE THE RIGHT NUMBER OF ROWS ARE PRINTED


while tree_height != 0:

# PRINT THE SPACES
    for i in range(spaces):
        print (' ', end="")  # end="" force new line
# end="" <-- TIP -->

# PRINT the hashes
    for i in range(hashes):
        print ('#', end="")

# NEWLINE AFTER EACH ROW IS PRINTED

    print()


# THAT SPACES IS DECREMENTED BY 1 EACH TIME
    spaces -= 1

# THAT HASHES IS INCREMENTED BY 2 EACH TIME
    hashes += 2


# DECREMENT TREE HEIGHT EACH TIME TO JUMP OUT OF THE LOOP
    tree_height -= 1
# PRINT THE SPACES BEFORE THE STUMP AND THEN THE HASH

for i in range(stump_spaces):
        print(' ', end="")

print("#")

