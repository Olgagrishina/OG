
print ("Perevod v secundi, minuti, i chasov")
ch = int (intut("Vvvedite chislo"))

print ( "1) Secundi v minutax i chasi; 2)Minuti v secundi i chasi;  3) Chasi v minuti i secundi;)
choice = int (input ("Vo chto xotite perevesti?" ))
if choice == 1:
    minuti = ch / 60
    print (ch, "cekund = ", minyt, "minut")
    chas = minuti / 60
    print (ch, "cekund = ", chas, "chas")
elif choise == 2:
    sec = ch * 60
    print (ch, "minut = ", sec, "chas")
    chas = ch / 60
    print (ch, "minut = ", chas, "chas")
elif choice == 3:
    minut = ch * 60
    print (ch, "chas = ", minut, "minut")
    sec = (ch * 60) * 60
    print (ch, "cekund = ", sec, "cekund")
else:
    print ("Oshibka! Vvedite vibor ot 1 do 3")
    exit (0)