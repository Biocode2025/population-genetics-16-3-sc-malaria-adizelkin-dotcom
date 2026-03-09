file = open("Sickle_cell_freq_het.csv", "w")
q = 0.0036 ** 0.5
p = 1 - q
generations = 50
header = "Generation,p(HbA),q(HbS)\n"
file.write(header)
gen = 0