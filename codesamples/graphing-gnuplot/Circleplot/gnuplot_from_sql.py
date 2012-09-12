import Gnuplot

gp = Gnuplot.Gnuplot()
gp('set datafile separator "|"')
gp('set term jpeg size 1000,1000')
gp('set output "correspondence_map.jpeg"')
gp('set yr[0:]')
gp('set xr[0:]')
gp('set xtics rotate')
#'[0:25][0:25]"< sqlite3 PigeonLoft.db <-- add a x0:25  y0:25 limitation to the grid
gp.plot('"< sqlite3 PigeonLoft.db  \'select * from correspondence_map\'"using 3:5:(log($1)):xtic(2):ytic(4) title "Corrospondence plot" with circles,""using 3:5:1 with labels title" ')