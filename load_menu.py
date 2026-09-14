from Inventory.models import Product


menu = [

    # =========================
    # INDIAN
    # =========================

    ("Masala Dosa", "Indian", "Vegetarian", "i1.jpg"),
    ("Plain Dosa", "Indian", "Vegetarian", "i2.jpg"),
    ("Rava Dosa", "Indian", "Vegetarian", "i3.jpg"),
    ("Onion Dosa", "Indian", "Vegetarian", "i4.jpg"),
    ("Mysore Masala Dosa", "Indian", "Vegetarian", "i5.jpg"),
    ("Set Dosa", "Indian", "Vegetarian", "i6.jpg"),
    ("Idli", "Indian", "Vegetarian", "i7.jpg"),
    ("Medu Vada", "Indian", "Vegetarian", "i8.jpg"),
    ("Pongal", "Indian", "Vegetarian", "i9.jpg"),
    ("Uttapam", "Indian", "Vegetarian", "i10.jpg"),
    ("Appam & Vegetable Stew", "Indian", "Vegetarian", "i11.jpg"),
    ("Puttu & Kadala Curry", "Indian", "Vegetarian", "i12.jpg"),
    ("Poori Masala", "Indian", "Vegetarian", "i13.jpg"),
    ("Parotta", "Indian", "Vegetarian", "i14.jpg"),
    ("Kothu Parotta", "Indian", "Vegetarian", "i15.jpg"),
    ("Lemon Rice", "Indian", "Vegetarian", "i16.jpg"),
    ("Tomato Rice", "Indian", "Vegetarian", "i17.jpg"),
    ("Curd Rice", "Indian", "Vegetarian", "i18.jpg"),
    ("Sambar Rice", "Indian", "Vegetarian", "i19.jpg"),
    ("Bisibele Bath", "Indian", "Vegetarian", "i20.jpg"),
    ("Vegetable Biryani", "Indian", "Vegetarian", "i21.jpg"),
    ("Chicken Biryani", "Indian", "Non-Vegetarian", "i22.jpg"),
    ("Mutton Biryani", "Indian", "Non-Vegetarian", "i23.jpg"),
    ("Egg Biryani", "Indian", "Non-Vegetarian", "i24.jpg"),
    ("Ambur Chicken Biryani", "Indian", "Non-Vegetarian", "i25.jpg"),
    ("Chicken 65", "Indian", "Non-Vegetarian", "i26.jpg"),
    ("Chicken Chettinad", "Indian", "Non-Vegetarian", "i27.jpg"),
    ("Pepper Chicken", "Indian", "Non-Vegetarian", "i28.jpg"),
    ("Butter Chicken", "Indian", "Non-Vegetarian", "i29.jpg"),
    ("Chicken Tikka", "Indian", "Non-Vegetarian", "i30.jpg"),
    ("Tandoori Chicken", "Indian", "Non-Vegetarian", "i31.jpg"),
    ("Chicken Kebab", "Indian", "Non-Vegetarian", "i32.jpg"),
    ("Mutton Rogan Josh", "Indian", "Non-Vegetarian", "i33.jpg"),
    ("Mutton Kebab", "Indian", "Non-Vegetarian", "i34.jpg"),
    ("Fish Fry", "Indian", "Non-Vegetarian", "i35.jpg"),
    ("Fish Curry", "Indian", "Non-Vegetarian", "i36.jpg"),
    ("Prawn Masala", "Indian", "Non-Vegetarian", "i37.jpg"),
    ("Egg Curry", "Indian", "Non-Vegetarian", "i38.jpg"),
    ("Paneer Butter Masala", "Indian", "Vegetarian", "i39.jpg"),
    ("Palak Paneer", "Indian", "Vegetarian", "i40.jpg"),
    ("Shahi Paneer", "Indian", "Vegetarian", "i41.jpg"),
    ("Chana Masala", "Indian", "Vegetarian", "i42.jpg"),
    ("Rajma Masala", "Indian", "Vegetarian", "i43.jpg"),
    ("Dal Tadka", "Indian", "Vegetarian", "i44.jpg"),
    ("Dal Makhani", "Indian", "Vegetarian", "i45.jpg"),
    ("Aloo Gobi", "Indian", "Vegetarian", "i46.jpg"),
    ("Vegetable Korma", "Indian", "Vegetarian", "i47.jpg"),
    ("Malai Kofta", "Indian", "Vegetarian", "i48.jpg"),
    ("Baingan Bharta", "Indian", "Vegetarian", "i49.jpg"),
    ("Naan", "Indian", "Vegetarian", "i50.jpg"),
    ("Butter Naan", "Indian", "Vegetarian", "i51.jpg"),
    ("Garlic Naan", "Indian", "Vegetarian", "i52.jpg"),
    ("Tandoori Roti", "Indian", "Vegetarian", "i53.jpg"),
    ("Butter Roti", "Indian", "Vegetarian", "i54.jpg"),
    ("Chapati", "Indian", "Vegetarian", "i55.jpg"),
    ("Samosa", "Indian", "Vegetarian", "i56.jpg"),
    ("Onion Pakora", "Indian", "Vegetarian", "i57.jpg"),
    ("Paneer Tikka", "Indian", "Vegetarian", "i58.jpg"),
    ("Aloo Tikki", "Indian", "Vegetarian", "i59.jpg"),
    ("Vada Pav", "Indian", "Vegetarian", "i60.jpg"),
    ("Pav Bhaji", "Indian", "Vegetarian", "i61.jpg"),
    ("Pani Puri", "Indian", "Vegetarian", "i62.jpg"),
    ("Bhel Puri", "Indian", "Vegetarian", "i63.jpg"),
    ("Dahi Puri", "Indian", "Vegetarian", "i64.jpg"),
    ("Gulab Jamun", "Indian", "Vegetarian", "i65.jpg"),
    ("Rasmalai", "Indian", "Vegetarian", "i66.jpg"),
    ("Jalebi", "Indian", "Vegetarian", "i67.jpg"),
    ("Kheer", "Indian", "Vegetarian", "i68.jpg"),
    ("Gajar Ka Halwa", "Indian", "Vegetarian", "i69.jpg"),
    ("Mysore Pak", "Indian", "Vegetarian", "i70.jpg"),

    # =========================
    # CHINESE
    # =========================

    ("Vegetable Fried Rice", "Chinese", "Vegetarian", "i71.jpg"),
    ("Chicken Fried Rice", "Chinese", "Non-Vegetarian", "i72.jpg"),
    ("Egg Fried Rice", "Chinese", "Non-Vegetarian", "i73.jpg"),
    ("Vegetable Hakka Noodles", "Chinese", "Vegetarian", "i74.jpg"),
    ("Chicken Hakka Noodles", "Chinese", "Non-Vegetarian", "i75.jpg"),
    ("Schezwan Fried Rice", "Chinese", "Vegetarian", "i76.jpg"),
    ("Chilli Paneer", "Chinese", "Vegetarian", "i77.jpg"),
    ("Chilli Chicken", "Chinese", "Non-Vegetarian", "i78.jpg"),
    ("Dragon Chicken", "Chinese", "Non-Vegetarian", "i79.jpg"),
    ("Manchurian", "Chinese", "Vegetarian", "i80.jpg"),
    ("Vegetable Spring Rolls", "Chinese", "Vegetarian", "i81.jpg"),
    ("Hot & Sour Soup", "Chinese", "Vegetarian", "i82.jpg"),
    ("Chicken Momos", "Chinese", "Non-Vegetarian", "i83.jpg"),

    # =========================
    # ITALIAN
    # =========================

    ("Margherita Pizza", "Italian", "Vegetarian", "i84.jpg"),
    ("Chicken Pepper Pizza", "Italian", "Non-Vegetarian", "i85.jpg"),
    ("Four Cheese Pizza", "Italian", "Vegetarian", "i86.jpg"),
    ("Vegetable Pizza", "Italian", "Vegetarian", "i87.jpg"),
    ("Chicken Pizza", "Italian", "Non-Vegetarian", "i88.jpg"),
    ("Spaghetti Aglio e Olio", "Italian", "Vegetarian", "i89.jpg"),
    ("Spaghetti Carbonara", "Italian", "Non-Vegetarian", "i90.jpg"),
    ("Penne Arrabbiata", "Italian", "Vegetarian", "i91.jpg"),
    ("Penne Alfredo", "Italian", "Vegetarian", "i92.jpg"),
    ("Lasagna", "Italian", "Vegetarian", "i93.jpg"),
    ("Ravioli", "Italian", "Vegetarian", "i94.jpg"),
    ("Fettuccine Alfredo", "Italian", "Vegetarian", "i95.jpg"),
    ("Pesto Pasta", "Italian", "Vegetarian", "i96.jpg"),
    ("Bruschetta", "Italian", "Vegetarian", "i97.jpg"),
    ("Garlic Bread", "Italian", "Vegetarian", "i98.jpg"),

    # =========================
    # JAPANESE
    # =========================

    ("Vegetable Sushi", "Japanese", "Vegetarian", "i99.jpg"),
    ("California Roll", "Japanese", "Non-Vegetarian", "i100.jpg"),
    ("Chicken Teriyaki", "Japanese", "Non-Vegetarian", "i101.jpg"),
    ("Chicken Ramen", "Japanese", "Non-Vegetarian", "i102.jpg"),
    ("Gyoza", "Japanese", "Vegetarian", "i103.jpg"),

    # =========================
    # MEXICAN
    # =========================

    ("Chicken Tacos", "Mexican", "Non-Vegetarian", "i104.jpg"),
    ("Chicken Burrito", "Mexican", "Non-Vegetarian", "i105.jpg"),
    ("Chicken Quesadilla", "Mexican", "Non-Vegetarian", "i106.jpg"),
    ("Nachos with Cheese", "Mexican", "Vegetarian", "i107.jpg"),

    # =========================
    # FRENCH
    # =========================

    ("French Onion Soup", "French", "Vegetarian", "i108.jpg"),
    ("Ratatouille", "French", "Vegetarian", "i109.jpg"),
    ("Potato Gratin", "French", "Vegetarian", "i110.jpg"),
    ("Vegetable Quiche", "French", "Vegetarian", "i111.jpg"),
    ("Spinach Quiche", "French", "Vegetarian", "i112.jpg"),
    ("Coq au Vin", "French", "Non-Vegetarian", "i113.jpg"),
    ("Chicken Fricassee", "French", "Non-Vegetarian", "i114.jpg"),
    ("Crêpes", "French", "Vegetarian", "i115.jpg"),
    ("Crème Brûlée", "French", "Vegetarian", "i116.jpg"),
    ("Soufflé", "French", "Vegetarian", "i117.jpg"),

    # =========================
    # WESTERN
    # =========================

    ("Classic Cheeseburger", "Western", "Vegetarian", "i118.jpg"),
    ("Chicken Burger", "Western", "Non-Vegetarian", "i119.jpg"),
    ("Veggie Burger", "Western", "Vegetarian", "i120.jpg"),
    ("Grilled Chicken Sandwich", "Western", "Non-Vegetarian", "i121.jpg"),
    ("Club Sandwich", "Western", "Non-Vegetarian", "i122.jpg"),
    ("French Fries", "Western", "Vegetarian", "i123.jpg"),
    ("Loaded Fries", "Western", "Vegetarian", "i124.jpg"),
    ("Grilled Chicken Steak", "Western", "Non-Vegetarian", "i125.jpg"),
    ("Fish & Chips", "Western", "Non-Vegetarian", "i126.jpg"),
    ("Chicken Wings", "Western", "Non-Vegetarian", "i127.jpg"),
    ("Caesar Salad", "Western", "Vegetarian", "i128.jpg"),
    ("Greek Salad", "Western", "Vegetarian", "i129.jpg"),
    ("Pancakes", "Western", "Vegetarian", "i130.jpg"),

    # =========================
    # BEVERAGES & DESSERTS
    # =========================

    ("Coca-Cola", "Beverages & Desserts", "Vegetarian", "i131.jpg"),
    ("Pepsi", "Beverages & Desserts", "Vegetarian", "i132.jpg"),
    ("Sprite", "Beverages & Desserts", "Vegetarian", "i133.jpg"),
    ("Fresh Lime Soda", "Beverages & Desserts", "Vegetarian", "i134.jpg"),
    ("Lemonade", "Beverages & Desserts", "Vegetarian", "i135.jpg"),
    ("Iced Tea", "Beverages & Desserts", "Vegetarian", "i136.jpg"),
    ("Espresso", "Beverages & Desserts", "Vegetarian", "i137.jpg"),
    ("Cappuccino", "Beverages & Desserts", "Vegetarian", "i138.jpg"),
    ("Café Latte", "Beverages & Desserts", "Vegetarian", "i139.jpg"),
    ("Masala Chai", "Beverages & Desserts", "Vegetarian", "i140.jpg"),
    ("Hot Chocolate", "Beverages & Desserts", "Vegetarian", "i141.jpg"),
    ("Mango Milkshake", "Beverages & Desserts", "Vegetarian", "i142.jpg"),
    ("Chocolate Milkshake", "Beverages & Desserts", "Vegetarian", "i143.jpg"),
    ("Strawberry Milkshake", "Beverages & Desserts", "Vegetarian", "i144.jpg"),
    ("Vanilla Milkshake", "Beverages & Desserts", "Vegetarian", "i145.jpg"),
    ("Chocolate Mousse Cake", "Beverages & Desserts", "Vegetarian", "i146.jpg"),
    ("Milk Cake", "Beverages & Desserts", "Vegetarian", "i147.jpg"),
    ("Chocolate Brownie", "Beverages & Desserts", "Vegetarian", "i148.jpg"),
    ("Vanilla Ice Cream", "Beverages & Desserts", "Vegetarian", "i149.jpg"),
    ("Chocolate Ice Cream", "Beverages & Desserts", "Vegetarian", "i150.jpg"),
]


print("Loading menu...")


for name, style, food_type, image in menu:

    product, created = Product.objects.update_or_create(
        product_name=name,
        defaults={
            "product_code": image.replace(".jpg", ""),
            "food_style": style,
            "food_type": food_type,
            "menu_image": image,
        }
    )

    if created:
        print("Created:", name)
    else:
        print("Updated:", name)


print()
print("================================")
print("MENU LOADING COMPLETE")
print("Total dishes:", Product.objects.count())
print("================================")