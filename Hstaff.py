import pyautogui as pg
import webbrowser as wb
import time as t



"""
food = pg.prompt("What is your favorite food?")

if food == "turkey chili":
        pg.alert("I eat mine with habanero cheese.")
        wb.open("www.google.com/search?tbm=isch&source=hp&biw=1366&bih=651&ei=LcjZW-fWHeT25gLLsIegAw&q=turkey+chili&oq=turkey+chili&gs_l=img.3..0l10.2814.4629..5461...0.0..0.280.1327.7j4j1......0....1..gws-wiz-img.1qdYgXSKCNo#imgrc=CA2INlczapy8lM:")

elif food == "pizza":
        pg.alert("I'm not the kind of person that likes big pizza companies. I only like local or homemade pizza.")
        wb.open("https://www.google.com/search?biw=681&bih=616&tbm=isch&sa=1&ei=ecvZW-yYMOLp_QaPzqyQBQ&q=homemade+pizza&oq=homemade+pizza&gs_l=img.3..0i67j0l9.18557.21310..21898...3.0..0.86.759.12......0....1..gws-wiz-img.......0i10j0i7i30.vL3y-VuAkx4#imgrc=93JYJ1YdiBRwXM:")
        
elif food == "ravioli":
        pg.alert("I like mine with alfredo sauce with mushrooms. It's called ravioli tartufati and it's soo good!")
        wb.open("https://www.google.com/search?q=ravioli+tartufati&rlz=1C1GCEA_enUS751US751&tbm=isch&tbo=u&source=univ&sa=X&ved=2ahUKEwiMztargbHeAhVwTd8KHWIKC4AQsAR6BAgGEAE&biw=681&bih=616#imgrc=pTDDF1aHNTIEkM:")
        
elif food == "ice cream":
        pg.alert("I like that too, but I'm trying to eat less of it because it's really bad for you.")
        wb.open("https://www.google.com/search?tbm=isch&source=hp&biw=681&bih=568&ei=Bc3ZW_H9Lc6b_QbDiJn4CA&q=ice+cream&oq=ice+cream&gs_l=img.3..0l10.9770.11280..11510...1.0..0.65.599.10......0....1..gws-wiz-img.......0i10.ejnHXbnMH1I#imgrc=tpNwMjb5ymI7OM:")
        
elif food == "candy":
        pg.alert("I have not had candy in a while. My favorite is Twix. It's unhealthy, but it tastes soo good!")
        wb.open("https://www.google.com/search?biw=681&bih=616&tbm=isch&sa=1&ei=Pc3ZW8atAeSFggeC-6LoAg&q=twix&oq=twix&gs_l=img.3..0i67l3j0l7.13247.13940..14104...0.0..0.64.242.4......0....1..gws-wiz-img.AiFDUMPlJmo#imgrc=n-4k3m7lgXlVrM:")
elif food == "chocolate":
        chocolate = pg.prompt("Really? Do you like dark, milk, or white?")

        if chocolate == "dark":
                pg.alert("I like that too, but not plain. It's not sweet enough to eat plain for me.")
                wb.open("https://www.google.com/search?q=dark+chocolate&rlz=1C1GCEA_enUS751US751&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi5jefSgrHeAhXPnOAKHXlrBKwQ_AUIDygC&biw=681&bih=616#imgrc=bzivnPNVKfgbCM:")
        elif chocolate == "milk":
                pg.alert("I love milk chocolate. It's great for literally any dessert!")
                wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS751US751&biw=681&bih=616&tbm=isch&sa=1&ei=qs3ZW_iRFarv_QbntrjICA&q=milk+chocolate&oq=milk+chocolate&gs_l=img.3..0i67l3j0l3j0i67j0l3.34795.36460..36702...0.0..0.77.553.8......0....1..gws-wiz-img.......0i10i67j0i10j0i7i30.Pwf43pEhOh0#imgrc=xUHXDxYtn9OasM:")
        elif chocolate == "white":
                pg.alert("White chocolate is a little too sweet for me, but it's great for gingerbread houses.")
                wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS751US751&biw=681&bih=616&tbm=isch&sa=1&ei=0M3ZW4DMCaeJggeV5pr4Bw&q=white+chocolate&oq=white+chocolate&gs_l=img.3..0i67j0l2j0i67j0j0i67j0j0i67j0l2.33249.35805..36431...4.0..0.88.927.13......0....1..gws-wiz-img.......0i7i30.i7YdvV0CK0Q#imgrc=lCVKhCALhmF5yM:")
        else:
                pg.alert("That's cool. I like milk chocolate.")
elif food == "steak":
        steak = pg.prompt("What kind of steak do you like?")

        if steak == "filet mingon":
                pg.alert("My favorite!")
                wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS751US751&biw=681&bih=616&tbm=isch&sa=1&ei=9c3ZW9KOJKWV_Qa6hZ7QCA&q=filet+mignon&oq=filet+mignon&gs_l=img.3..0l10.40709.42973..43221...0.0..0.84.785.12......0....1..gws-wiz-img.......0i67.KMvywqjlyvc#imgrc=VYuN3p8mK1BtIM:")
        elif steak == "T-bone":
                pg.alert("I hear that the steak closest to the middle in a T-bone is the most flavorful.")
                wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS751US751&biw=681&bih=616&tbm=isch&sa=1&ei=Ic7ZW5y0LOyJgge6loX4Cw&q=t-bone&oq=t-bone&gs_l=img.3..0j0i67j0l8.37046.38526..38706...0.0..0.66.374.6......0....1..gws-wiz-img.XiQUz0w40u0#imgrc=amODxdugOhUJEM:")
        elif steak == "rib eye":
                pg.alert("My dad loves rib eye!")
                wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS751US751&biw=681&bih=616&tbm=isch&sa=1&ei=Sc7ZW_PZE5C6ggfW8psw&q=rib+eye&oq=rib+eye&gs_l=img.3..0l2j0i67l3j0l5.17885.18743..18853...0.0..0.73.461.7......0....1..gws-wiz-img.kpKfSaXdpV4#imgrc=eBOiBuzZT7R4eM:")
        elif steak == "beef tenderloin":
                pg.alert("My mom is kind of a fan of that one.")
                wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS751US751&biw=681&bih=616&tbm=isch&sa=1&ei=Xc7ZW53JDs-xgger-KzYBQ&q=beef+tenderloin&oq=beef+tenderloin&gs_l=img.3..0l10.33637.36151..39683...0.0..0.72.947.15......0....1..gws-wiz-img.......0i67.0uA-zck53-U#imgrc=YQCwLGfMF1CgsM:")
        elif steak == "tenderloin":
                pg.alert("My mom is kind of a fan of that one.")
                wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS751US751&biw=681&bih=616&tbm=isch&sa=1&ei=Xc7ZW53JDs-xgger-KzYBQ&q=beef+tenderloin&oq=beef+tenderloin&gs_l=img.3..0l10.33637.36151..39683...0.0..0.72.947.15......0....1..gws-wiz-img.......0i67.0uA-zck53-U#imgrc=YQCwLGfMF1CgsM:")
        else:
                pg.alert("I don't love " + steak + " as much as filet mingon.")


elif food == "chicken parmesean":
        chickenparm = pg.prompt("You have such great taste in food. Do you like to add extra cheese to it?")
        wb.open("https://www.afamilyfeast.com/wp-content/uploads/2018/01/chicken-parmesan-3.jpg")
        if chickenparm == "yes":
                pg.alert("I like to do that too.")

        elif chickenparm == "no":
                pg.alert("Really? I do.")

        else:
            pg.alert("Okay.")
                
elif food == "chicken parm":
        chickenparm = pg.prompt("You have such great taste in food. Do you like to add extra cheese to it?")
        wb.open("https://www.afamilyfeast.com/wp-content/uploads/2018/01/chicken-parmesan-3.jpg")
        if chickenparm == "yes":
                pg.alert("I like to do that too.")

        elif chickenparm == "no":
                pg.alert("Really? I do.")

        else:
            pg.alert("Okay.")
else:
        pg.prompt("Really? What do you like about " + str(food) + "?")
        pg.alert("Okay.")
"""
