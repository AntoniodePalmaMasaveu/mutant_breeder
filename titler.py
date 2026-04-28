import sys

tree = [
"       .        ",
"      .:.       ",
"     .::::.     ",
"    ·::::::·    ",
"_______][_______"]
peptide  = [
"        H      R      H        ",
"   +    |      |      |    -   ",
"    H3N-C-CONH-C-CONH-C-COO    ",
"        |      |      |        ",
"        R      H      R        "]
aminoacid  = [
"         H         ",
"    +    |    -    ",
"     H3N-C-COO     ",
"         |         ",
"         R         "]
sugar = [
"           OH  H   OH  OH  H        ",
"           |   |   |   |   |        ",
"   O = C - C - C - C - C - C - OH   ",
"       |   |   |   |   |   |        ",
"       H   H   OH  H   H   H        "]
DNA = [
"    ├─ C ≡ G ─┤    ",
"    ├─ G = C ─┤    ",
"    ├─ T = A ─┤    ",
"    ├─ C ≡ G ─┤    ",
"    ├─ A = T ─┤    "]
RNA = [
" ┬─┬─┬─┬─┬─┬─┬─┬─  ",
" A U G C A G U U   ",
"                   ",
" ┬─┬─┬─┬─┬─┬─┬─┬─  ",
" G C G U A A A A   ",]

file  = [
"    ___________    ",
"    |110001110|    ",
"    |001100101|    ",
"    |100011010|    ",
"    |110010110|    "]

features = {"tree":tree,
            "peptide":peptide,
            "aminoacid":aminoacid,
            "sugar":sugar,
            "DNA": DNA,
            "RNA": RNA,
            "file":file,}

def titler(main_title, seco_title, terc_title, name_autho, feat):
    center_len = 30
    longest_string = max((len(main_title), len(seco_title), len(terc_title), len(name_autho)))
    if longest_string > center_len:
        center_len = center_len - (center_len - longest_string)
    center_len += 4
    feature_n = 1

    main_title = " "*int(((center_len-len(main_title))/2) + 0.5) + main_title + " "*int(((center_len-len(main_title))/2))
    seco_title = " "*int(((center_len-len(seco_title))/2) + 0.5) + seco_title + " "*int(((center_len-len(seco_title))/2))
    terc_title = " "*int(((center_len-len(terc_title))/2) + 0.5) + terc_title + " "*int(((center_len-len(terc_title))/2))
    name_autho = " "*int(((center_len-len(name_autho))/2) + 0.5) + name_autho + " "*int(((center_len-len(name_autho))/2))
    floor_sect = "_" * center_len

    FEATURE = features[feat]
    print(" "*len(FEATURE[0]) + "_"*center_len + " "*len(FEATURE[0]))
    print(FEATURE[0]*feature_n + main_title + FEATURE[0]*feature_n)
    print(FEATURE[1]*feature_n + seco_title + FEATURE[1]*feature_n)
    print(FEATURE[2]*feature_n + terc_title + FEATURE[2]*feature_n)
    print(FEATURE[3]*feature_n + name_autho + FEATURE[3]*feature_n)
    print(FEATURE[4]*feature_n + floor_sect + FEATURE[4]*feature_n)
    print("\n")

if __name__ == "__main__":
    main_title = sys.argv[1]
    seco_title = sys.argv[2]
    terc_title = sys.argv[3]
    name_autho = sys.argv[4]
    feat       = sys.argv[5]

    titler(main_title, seco_title, terc_title, name_autho, feat)