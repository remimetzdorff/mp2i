def make_correction(folder, filename):
    with open(folder+filename) as file:
        content = file.readlines()

    corr = open(folder+"temp.tex", "w")
    corr.write("\\documentclass[10pt,a4paper,fleqn,table]{article}\n")
    corr.write("\\usepackage{rm-pv}\n")
    corr.write("\\usepackage{rm-corr}\n")
    corr.write("\n")
    corr.write("\\begin{document}\n\n")
    for i, line in enumerate(content):
        if line[0] == "%":
            pass
        elif "\\mytitle" in line:
            corr.write("\\begin{correction}"+line[8:12]+"}\n")
        elif "\\begin{exercice}" in line:
            title = line[16:]
            newline = ""
            for l in title:
                if l == "\\":
                    newline += "}"
                    break
                else:
                    newline += l
            corr.write("\\exercice"+newline+"\n")
        elif "\\qa" in line:
            corr.write(line)
            open_bracket = 1
            for j in range(1,len(content)-i):
                line = content[i+j]
                open_bracket += line.count("{") - line.count("}")
                if open_bracket > 0:
                    corr.write(line)
                else:
                    corr.write(line+"\n")
                    break
        elif "\\end{document}" in line:
            corr.write("\\end{correction}\n\n")
        elif "% Appendix for correction" in line:
            for j in range(1, len(content)-i):
                line = content[i+j]
                corr.write(line)

    corr.write("\n\n\\end{document}\n")
    corr.close()
    print("Correction of "+folder+filename+" successfully created: "+corr.name)
    return

#folder = "../dm/"
#filename = "dm1.tex"
#make_correction(folder, filename)