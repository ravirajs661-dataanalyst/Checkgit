class store_managment:
    def __init__(self,product_id,product_name,category,price,quantity):
        self.product_id=product_id
        self.product_name=product_name
        self.category=category
        self.price=price
        self.quantity=quantity
        self.total_price=price * quantity

Store=[]
while True:
    print(f"\n_______Grocery Sotre Managment System_______")
    print("1. Add Product")
    print("2. Show All Product")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Sell Product")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == 1:
        product_id=input("Enter Product Id : ")
        product_name=input("Enter Product Name: ")
        category=input("Enter Product Category: ")
        price= int(input("Enter Product Price: "))
        quantity=int(input("Enter Product Quantity: "))

        store_details=Store(product_id, product_name, category, price, quantity)
        Store.append(store_details)
        print("Product Details Added Successfully!")

    elif choice == 2:
        if not Store:
            print("Not Data!")
        else:
            print("\n_____All Product_____")
            for product in Store:
                print(f"Product Id: {product.product_id}")
                print(f"Product Name: {product.product_name}")
                print(f"Product Category: {product.category}")
                print(f"Product Price: {product.price}")
                print(f"Product Quantity: {product.quantity}")
                print(f"Total Amount: {product.total_price}")

    elif choice == 3:
        product_id = input("Enter Product Id: ")
        found=False
        for product in Store:
            if product.product_id == product_id:
                found=True
                print("\n_____All Product_____")
                print(f"Product Id: {product.product_id}")
                print(f"Product Name: {product.product_name}")
                print(f"Product Category: {product.category}")
                print(f"Product Price: {product.price}")
                print(f"Product Quantity: {product.quantity}")
                print(f"Total Amount: {product.total_price}")
                break

            if found==False:
                print("Product Not Found!")

    elif choice == 4:
        product_id= input("Enter Product Id: ")
        found= False
        for product in Store:
            if product.product_id == product_id:
                found= True
                print("1. Update Price")
                print("2. Update Quantity")
                print("3. Update Category")

                Update_Choice= input("Enter Your Choice: ")

                if Update_Choice ==1:
                    Store.price=int(input("Enter Product Price: "))
                    print("Updated Successfully!")
                elif Update_Choice == 2:
                    Store.quantity=int(input("Enter Product Quantity: "))
                    Store.total_amount= Store.price * Store.quantity
                    print("Updated Successfully!")
                elif Update_Choice == 3:
                    Store.category=input("Enter Product Category: ")
                    print("Updated Successfully!")

    elif choice == 5:
        product_id= input("Enter Product Id: ")
        found= False
        for product in Store:
            if product.product_id ==product_id:
                found=True
                Store.remove(product)
                print("Delete Product!")
                break
        if not found:
            print("Invalid Product Id!")





