import Gnuplot

gp = Gnuplot.Gnuplot()
#Set size of the picture generated
gp('set term jpeg size 600,700')

#define output with name
gp('set output "plot_scattered.jpeg"')



#Loop through all instences of the "md5 email names" and map these to the following spots as x/y

#gp(set xtics rotate ( "Meredith" 1, "Avery" 2, "Teddy" 3, "Karev" 4, "Bailey" 5, "Burke" 6, "Lexie" 7, "Owen" 8, "Addison" 9, "O'Malley" 10, "Arizona" 11, "Derek" 12, "April" 13, "Sloan" 14, "Izzie" 15, "Webber" 16, "Christina" 17, "Callie" 18 ) scale 0

#set ytics ( "Meredith" 1, "Avery" 2, "Teddy" 3, "Karev" 4, "Bailey" 5, "Burke" 6, "Lexie" 7, "Owen" 8, "Addison" 9, "O'Malley" 10, "Arizona" 11, "Derek" 12, "April" 13, "Sloan" 14, "Izzie" 15, "Webber" 16, "Christina" 17, "Callie" 18 ) scale 0

gp.plot('plot [0:19][0:23] "homerun.txt" using 3:5:1 title "homerun" with circles linecolor rgb "#9ACD32" fill solid noborder')

