in_to_ft = lambda x: x/12.
ft_to_yd = lambda x: x/3.
in_to_cm = lambda x: x*2.54
cm_to_m = lambda x: x/100.
m_to_km = lambda x: x/1000.

in_to_m = lambda x: cm_to_m(in_to_cm(x))
in_to_km = lambda x: m_to_km(in_to_m(x))
in_to_yd = lambda x: ft_to_yd(in_to_ft(x))

sample = (36, 72, 360, 480, 1000)
print "sample: ", sample
print "in to km: ", map(lambda x: in_to_km(x), sample)
print "in to m: ", map(lambda x: in_to_km(x), sample)
print "in to ft: ", map(lambda x: in_to_ft(x), sample)
print "in to yd: ", map(lambda x: in_to_yd(x), sample)
