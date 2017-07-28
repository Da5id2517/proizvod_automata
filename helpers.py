from Vertex import initial


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

    k = automat.fetch(initial)
    output += "\\node[initial, "
    if k.final:
        output += r"accepting, "
    output += "state] (_"
    output += str(k)
    output += ") {$_"
    output += str(k)
    output += "$}; \n"

    for v in automat.vertices:
        if v == k:
            tmp = k
            continue
        output += "\\node[state"
        if v.final:
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
    for e in automat.edges:
        if e.start == e.end:
            output += "(_" + str(e.start) + ")"
            output += "edge [loop above] node {" + e.letter + "}"
            output += "(_" + str(e.start) + ")\n"
            continue
        output += "(_" + str(e.start) + ")"
        output += "edge [bend right] node {" + e.letter + "}"
        output += "(_" + str(e.end) + ")\n"
    output += ";\n"
    output += "\end{tikzpicture}\n"
    output += "\end{document}\n"
    output_file.write(output)
    output_file.close()
