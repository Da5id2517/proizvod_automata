def represent_automata(automat):
    output = "\\documentclass{article}\n"
    output += "\\usepackage{tikz}\n"
    output += "\\usetikzlibrary{automata,positioning}\n"
    output += "\\begin{document}\n"
    output += "\\begin{tikzpicture}" \
              "[shorten >=1pt,node distance=2cm,on grid,auto]\n"
    output += automat.represent()
    output += "\\end{tikzpicture}\n"
    output += "\\end{document}\n"
    return output
