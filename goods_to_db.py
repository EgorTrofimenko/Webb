import os
from app import db, Product

folder = r"C:\Users\sebab\PycharmProjects\Webb\product\Nike\description"
files_list = os.listdir(folder)

for name in files_list:
    s = open(folder + "\\" + name)
    r = s.read()
    print(r)

    brand = r[0]
    model = r[1]
    color = r[2]
    material_up = r[3]
    material_down = r[4]
    season = r[5]
    sports = r[6]
    size = r[7]
    text = r[8]
    price = r[9]

    product = Product(brand=brand, model=model, color=color, material_up=material_up, material_down=material_down,
                      season=season, sports=sports,
                      size=size, text=text, price=price)

    #try:
    db.session.add(product)
    db.session.commit()
    #except:
        #print("При добавлении статьи прозошла ошибка")
    print() #::::