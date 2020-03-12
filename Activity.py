class inform:
    pass
user1 = inform()

counter = 0
print('1) Add' +'\n2) Edit' + '\n3) Delete' + '\n4) View' + '\n5) Exit')
choice = 0

item = []

while choice != 5:
    choice = int(input('Choose: '))

    if (choice == 1): # ADD
      user1.item_name = (input('Enter Item Name: '))
      user1.id = (input('Enter ID #: '))
      user1.desc = (input('Enter Description: '))
      user1.price = (input('Enter Price: '))
      print('Successfully added #' + user1.id + ' '+ user1.item_name)
      info = [user1.item_name,user1.id,user1.desc,user1.price]
      item.append(info)
      counter += 1
      print(item)

    elif (choice == 2): # EDIT
        dummy = int(input('Choose item number to Edit: '))
        item.pop(dummy-1)
        user1.item_name = (input('Enter Item Name: '))
        user1.id = (input('Enter ID #: '))
        user1.desc = (input('Enter Description: '))
        user1.price = (input('Enter Price: '))
        print('Successfully Updated #' + user1.id + ' '+ user1.item_name)
        info = [user1.item_name,user1.id,user1.desc,user1.price]
        item.insert(dummy-1,info)


    elif (choice == 3): # DELETE
        dummy = int(input('Choose item number to Delete: '))
        item.pop(dummy-1)

    elif (choice == 4): # VIEW
        mnctr = 0
        for i in item:
            print (mnctr+1, end =" ")
            mnctr += 1
            print(') ', end =" ")
            print(','.join(i[0:1])) #Item name
            print('ID: ', end ="#")
            print(','.join(i[1:2])) #Item ID
            print('Description: ', end =" ")
            print(','.join(i[2:3])) #Item Desc
            print('Price: ', end ="P")
            print(','.join(i[3:4])) #Item Price



    else:
        print('Program Terminated')