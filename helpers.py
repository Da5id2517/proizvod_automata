def represent(automat, output_file):
    try:
        output_file = open(output_file, "w")
    except IOError:
        print("I see no point in this its gonna create one either fucking way.")
    output = "\documentclass{scrartcl}\n"
    output += "\usepackage{tikz}\n"
    output += "\usetikzlibrary{arrows,automata}\n"
    output += "\n\\begin{document}\n"
    output += "\\begin{tikzpicture} [>=stealth',shorten >=1pt,auto,node distance=3.2cm]\n"

    k = automat.get_initial()
    output += "\\node[initial, "
    if k.get_final():
        output += r"accepting, "
    output += "state] (_"
    output += str(k)
    output += ") {$_"
    output += str(k)
    output += "$}; \n"

    for v in automat.get_vertices():
        if v == k:
            tmp = k
            continue
        output += "\\node[state"
        if v.get_final():
            output += ", accepting"
        output += "] (_"
        output += str(v)
        output += ") [right of=_"
        output += str(tmp)
        output += "] {$_"
        output += str(v)
        output += "$}; \n"
        tmp = v
    output += "\\path[->]"
    for e in automat.get_edges():
        if e.get_start() == e.get_end():
            output += "(_" + str(e.get_start()) + ")"
            output += "edge [loop above] node {" + e.get_letter() + "}"
            output += "(_" + str(e.get_start()) + ")\n"
            continue
        output += "(_" + str(e.get_start()) + ")"
        output += "edge [bend right] node {" + e.get_letter() + "}"
        output += "(_" + str(e.get_end()) + ")\n"
    output += ";\n"
    output += "\end{tikzpicture}\n"
    output += "\end{document}\n"
    output_file.write(output)
    output_file.close()
