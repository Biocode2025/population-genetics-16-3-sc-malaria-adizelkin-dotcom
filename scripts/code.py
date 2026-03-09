file = open("scripts/csv.Sickle_cell_freq_het", "w")
q = 0.0036 ** 0.5
p = 1 - q
generations = 50
header = "Generation\tp(HbA)\tq(HbS)\n"
file.write(header)
gen = 0

while gen <= generations:

    line = str(gen) + "\t\t\t" + str(p) + "\t" + str(q) + "\n"
    file.write(line)
    q_next = q / (0.98 * p + 2 * q)
    q_next=round(q_next,2)
    p_next = 1 - q_next
    q = q_next
    p = p_next
    gen = gen + 1

file.close()