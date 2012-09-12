''' Notes
https://www.linux.com/news/software/developer/26873-generating-graphs-with-gnuplot-part-3
'''


import Gnuplot
gp = Gnuplot.Gnuplot()
gp('set term jpeg size 600,700')
gp('set output "plot_scattered.jpeg"')


MeredithVar1 = "Meredith"
MeredithVar2 = "\""+MeredithVar1+"\" x,"+" "



gp('set xtics rotate ("'+MeredithVar1+'" 1, "Avery" 2,"Teddy" 3,"Karev" 4,"Bailey" 5, "Burke" 6, "Lexie" 7, "Owen" 8, "Addison" 9, "O\'Malley" 10, "Arizona" 11, "Derek" 12, "April" 13, "Sloan" 14, "Izzie" 15, "Webber" 16, "Christina" 17, "Callie" 18 ) scale 0')
gp('set ytics ( "Meredith" 1, "Avery" 2, "Teddy" 3, "Karev" 4, "Bailey" 5, "Burke" 6, "Lexie" 7, "Owen" 8, "Addison" 9, "O\'Malley" 10, "Arizona" 11, "Derek" 12, "April" 13, "Sloan" 14, "Izzie" 15, "Webber" 16, "Christina" 17, "Callie" 18 ) scale 0')

#3:5:1    1 is the weight   ( 3 and 5 are the "plot on the xy)  which is x and which is y....)
gp.plot('[0:19][0:23] "homerun.txt" using 3:5:1 title "homerun" with circles linecolor rgb "#9ACD32" fill solid noborder')


variable_name1 = "blalblbalblbalbla"
variable_name2 = "blalblbalblbalbla"

String_constructor1 = "\""+variable_name1+"\" x,"+" "
String_constructor2 = "\""+variable_name2+"\" x,"+" "
print String_constructor1


absolute_constructor = String_constructor1 + String_constructor2


print "\'set xtics rotate (" + absolute_constructor + ") scale 0')"