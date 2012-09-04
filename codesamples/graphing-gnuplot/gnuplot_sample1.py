# Import the gnuplot packages
import Gnuplot, Gnuplot.funcutils
plot = Gnuplot.Gnuplot()
plot('set terminal eps')
plot("set output 'programm.eps'")
plot("plot 'programm.dat' title 'Data'")
plot('quit')
