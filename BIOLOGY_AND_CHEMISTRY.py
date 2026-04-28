"""BIOLOGY_AND_CHEMISTRY_LISTS:
1. chem functions
2. bioq functions
3. general funtions
"""

from elements_DICTS import *
from aminoacids_and_nucleotides_DICTS import *

import numpy as np
import gemmi
import pandas as pd

class CapitalInsensitiveDict(dict):
    # standard dict use
    def __getitem__(self, key):
        return dict.__getitem__(self, key.upper())
    # when using .get()
    def get(self, key, default=None):
        return dict.get(self, key.upper(), default)
    # when checking if a KEY is present
    def __contains__(self, key):
        return dict.__contains__(self, key.upper())
    # when saving a key => KEY
    def __setitem__(self, key, value):
        dict.__setitem__(self, key.upper(), value)
#

""" 
ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ
Ξ 1. CHEMISTRY Ξ
ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ
"""
def hasselbalch_charge(pKa, pH=7.4):
    ratio = 10 ** (pH - pKa)
    f_protonated = 1 / (1 + ratio)
    f_deprotonated = ratio / (1 + ratio)
    return f_protonated - f_deprotonated 

def dihedral_angle(P1, P2, P3, P4):
    # ω CA-C-N-CA => 180 or 0 rarely        
    # φ C-N-CA-C
    # ψ N-CA-C-N
    P1, P2, P3, P4 = map(np.array, [P1, P2, P3, P4])

    b1 = P2 - P1
    b2 = P3 - P2 
    b3 = P4 - P3

    n1 = np.cross(b1, b2)
    n2 = np.cross(b2, b3) 

    cos_angle = np.dot(n1, n2) / (np.linalg.norm(n1) * np.linalg.norm(n2))
    return np.degrees(np.arccos(cos_angle))

def angle(P1, P2, P3, degrees_radians="degrees"):
    P1, P2, P3 = map(np.array, [P1, P2, P3])
    vec1 = P1 - P2
    vec2 = P3 - P2
    cos_angle = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    if degrees_radians == "degrees":
        angle = np.degrees(np.arccos(cos_angle))
    if degrees_radians == "radians":
        angle = np.arccos(cos_angle)
    return angle
""" 
ΞΞΞΞΞΞΞΞΞΞΞΞΞΞ
Ξ 2. BIOLOGY Ξ
ΞΞΞΞΞΞΞΞΞΞΞΞΞΞ
"""
#
def search_AAsequence_in_prot(reference, search_sequence):
    pad = len(search_sequence) - 1
    padded_reference = "-" * pad + reference + "-" * pad

    st = 0
    end = len(search_sequence)
    scores = []
    for i in range(len(padded_reference) - len(search_sequence)):
        score_alignment = 0
        window = padded_reference[st:end]
        for N in range(len(search_sequence)):
            if search_sequence[N] == window[N] and window[N] != "-":
                score_alignment += 1
        scores.append([i - pad, score_alignment])
        st += 1
        end += 1

    best = max(scores, key=lambda x: x[1])
    best_aligned_residues = list(range(best[0], best[0] + len(search_sequence)))
    print(f"Matched: {best[1]}/{len(search_sequence)}, residues in referene: {best_aligned_residues}")
    
    print(f"reference: {reference}")
    shifted_search ='·'*best[0]+f"{search_sequence}"+'·'*(len(reference)-(best[0]+len(search_sequence)))
    print(f"peptide:   {shifted_search}")
    return best_aligned_residues 

""" CIF OPENERS
> stress tests:
# 1JG1 | ATP
# 4F3T | RNA and missing resisues
# 1NKP | DNA
# 1TIG | Hydrogens
# 9KBO | Hydrogens and missing residues
# 9G6Y | farmaco
# 9R30 | farmaco
# 2BNH | acetylation 
# 6ELW | selocysteine Sec (should) 5L71, 5H5Q, 2OBI :(
# 7UGS | cromophore
# 1B9C | cromophore
# 8FIF | cyclic heptapetide
# 7YV1 | cyclic petptide antibody
# 6U74 | cyclic petptide with oddity?
# 2IZQ | alternating D and L
# 5DK3 | ANTIBODY INSERTION CODE (DIE) glycosilayion
# 1IGY | ANTIBODY glycosilayion
# 5TB5 | farnesil, [methyl cysteine], GDP, farnesyl, missing residues
# 9EYE | AAA chain names
"""
# 1. CIF_metadata:
def CIF_metadata(file_path, silenced=False):
    def search(*search_itemS):
        for search_item in search_itemS:
            prefix, field = search_item.rsplit(".", 1)
            for row in cif_block.find(prefix + ".", [field]):
                val = gemmi.cif.as_string(row[0]).strip().strip('"').strip("'").strip() # le clean
                if val in {"", ".", "?"}:
                    continue
                return str(val)
        return None
    file_path = str(file_path)
    doc = gemmi.cif.read_file(file_path)
    cif_block = doc.sole_block()

    organism = search(
        '_entity_src_gen.pdbx_gene_src_scientific_name',
        '_entity_src_nat.pdbx_organism_scientific_name',
        '_entity_src_nat.pdbx_organism_scientific',
        '_pdbx_entity_src_syn.organism_scientific',
        '_entity_src_gen.gene_src_scientific_name',
        '_entity_src_gen.pdbx_gene_src_common_name',
        '_entity_src_gen.gene_src_common_name',
        '_entity_src_nat.common_name',     
        '_entity_src_gen.pdbx_gene_src_strain',
    )
    metadata_cif = {
        "PDB Code":        search('_entry.id'),
        "Method":          search('_exptl.method'),
        "Resolution (Å)":  search('_refine.ls_d_res_high',
                                        '_reflns.d_resolution_high',
                                        '_em_3d_reconstruction.resolution'),
        "Organism":        organism,
        "Oficial Name":    search('_struct.title'),
        "Keywords":        search('_struct_keywords.pdbx_keywords',
                                  '_struct_keywords.text'),
        "R_work":          search('_refine.ls_r_factor_r_work',
                                        '_refine.ls_r_factor_obs'),
        "R_free":          search('_refine.ls_r_factor_r_free'),
        "Deposition Date": search('_pdbx_database_status.recvd_initial_deposition_date'),
        "Citation Title":  search('_citation.title'),
    }

    if not silenced:
        print("Ξ" * 40)
        print(f"PDB Code: {metadata_cif['PDB Code']}")
        print(f"    Method           : {metadata_cif['Method']}")
        print(f"    Resolution (Å)   : {metadata_cif['Resolution (Å)']}")
        print(f"    Organism         : {metadata_cif['Organism']}")
        print(f"    Oficial Name     : {metadata_cif['Oficial Name']}")
        print(f"    Keywords         : {metadata_cif['Keywords']}")
        print(f"    R_work           : {metadata_cif['R_work']}")
        print(f"    R_free           : {metadata_cif['R_free']}")
        print(f"    Deposition Date  : {metadata_cif['Deposition Date']}")
        print(f"    Citation Title   : {metadata_cif['Citation Title']}")

    return metadata_cif

# 2. CIF_entities:
def CIF_entities(file_path, silenced = False):
    ### FUTURE REMINDER WORK detect ACE, FOR STE, MYR and non-amino acid modifications,
    # add that to the warning and tell CIF_dataframe to 
    # move sequence + 1 and remove that from the chain ptm_dict?.
    
    # Some non protein petide like lements get classfied as protein dont want that
    # current metric, ignore peptides smaller than 20
    # ignore sequences with more than 15% nonstandard amino acids
    strange_barrier = 0.15
    small_barrier = 20
    
    def clean(string):
        val = gemmi.cif.as_string(string).strip().strip('"').strip("'").strip()
        return val if val not in {'', '.', '?'} else None

    _POLY_TYPE = {
        'polypeptide(l)':                                    'protein',
        'polypeptide(d)':                                    'protein-D',
        'polydeoxyribonucleotide':                           'DNA',
        'polyribonucleotide':                                'RNA',
        'polydeoxyribonucleotide/polyribonucleotide hybrid': 'DNA/RNA hybrid',
        'polysaccharide(d)':                                 'polysaccharide',
        'polysaccharide(l)':                                 'polysaccharide',
        'cyclic-pseudo-peptide':                             'cyclic-peptide',
    }
    file_path = str(file_path)
    doc   = gemmi.cif.read(file_path)
    block = doc.sole_block()

    entry_id = clean(block.find_value('_entry.id')) or block.name  # fallback to block name

    # --- 1. Base entities ---
    seq_dict = {}
    for row in block.find('_entity.', ['id', 'type', 'pdbx_description']):
        eid = row.str(0)
        seq_dict[eid] = {
            'type':            clean(row[1]),
            'poly_type':       None,
            'description':     clean(row[2]),
            'chain':           [],
            'chem_components': {},
            'sequence':        [],
            'sequence_num':    [],
            'sequence_auth':   [],
            'insertion_codes': [],
        }


    # --- 2. Chains for ALL entities via _struct_asym ---
    for row in block.find('_struct_asym.', ['id', 'entity_id']):
        chain_id, eid = row.str(0), row.str(1)
        if eid in seq_dict:
            seq_dict[eid]['chain'].append(chain_id)

    # --- 2.5 Polymer subtype ---
    for row in block.find('_entity_poly.', ['entity_id', 'type']):
        eid, raw_type = row.str(0), clean(row[1])
        if eid in seq_dict and raw_type:
            seq_dict[eid]['poly_type'] = _POLY_TYPE.get(raw_type.lower(), raw_type)

    # --- 3. Sequence + auth numbering + insertion codes ---
    seen = set()
    for row in block.find('_pdbx_poly_seq_scheme.', 
                        ['entity_id', 'seq_id', 'mon_id', 'auth_seq_num', 'pdb_ins_code']):
        eid    = row.str(0)
        seq_id = int(row.str(1))
        key    = (eid, seq_id)
        if eid in seq_dict and key not in seen:
            seen.add(key)
            seq_dict[eid]['sequence'].append(row.str(2))
            seq_dict[eid]['sequence_num'].append(seq_id)
            seq_dict[eid]['sequence_auth'].append(clean(row[3])) 
            seq_dict[eid]['insertion_codes'].append(clean(row[4]))
    # --- 4. Chem component lookup ---
    chem_comp = {row.str(0): clean(row[1]) for row in block.find('_chem_comp.', ['id', 'name'])}
    
    # --- 5. Assign chem components per entity ---
    for eid, entity in seq_dict.items():
        entity['chem_components'] = {
            mon_id: chem_comp[mon_id]
            for mon_id in entity['sequence']
            if mon_id in chem_comp
        }

    for row in block.find('_pdbx_nonpoly_scheme.', ['entity_id', 'mon_id']):
        eid, mon_id = row.str(0), row.str(1)
        if eid in seq_dict and mon_id in chem_comp:
            seq_dict[eid]['chem_components'][mon_id] = chem_comp[mon_id]
    
    ### REVISIONS ###     
    warning_to_CIF_dataframe = []  
    for ENTRY in seq_dict:
        if seq_dict[ENTRY]['poly_type'] == 'protein':
            C_classfication = 'protein'
            C_seq = seq_dict[ENTRY]['sequence']
            C_chain = seq_dict[ENTRY]['chain']
            nonstandardAA = 0 
            for AA in C_seq:
                result = aminoacid_DICT.get(AA, 'X') 
                if result == 'X': 
                    nonstandardAA += 1
            if len(C_seq) > 0 and (nonstandardAA / len(C_seq)) > strange_barrier:
                C_classfication = "strange" + " " + C_classfication
            if len(C_seq) < small_barrier:
                C_classfication = "small" + " " + C_classfication
            seq_dict[ENTRY]['poly_type'] = C_classfication
            if C_classfication != 'protein':
                warning_to_CIF_dataframe.append([C_chain, C_classfication])     
    
    if not silenced:
        print(f"Entry: {entry_id}\n")
        for eid, entity in seq_dict.items():
            visible_items = {k: v for k, v in entity.items() if v}
            if not visible_items:
                continue

            print(f"[{eid}]")
            padding = max(len(str(k)) for k in visible_items.keys())
            
            for K, V in visible_items.items():
                print(f"    {K:<{padding}} : {V}")

    return entry_id, seq_dict, warning_to_CIF_dataframe

# 3. CIF_dataframe:
def CIF_dataframe(file_path, model_index = 0, silenced= False, warning_to_CIF_dataframe=None) -> pd.DataFrame:

    def _comp_type(entity: gemmi.Entity) -> str:
            """Collapse gemmi entity/polymer types into a single readable label."""
            if entity.entity_type == gemmi.EntityType.Water:       
                return "water"
            elif entity.entity_type == gemmi.EntityType.NonPolymer:  
                return "ligand"
            elif entity.entity_type == gemmi.EntityType.Branched: # wwPDB Carbohydrate Remediation Documentation
                return "saccharide"
            elif entity.entity_type == gemmi.EntityType.Polymer:
                if entity.polymer_type == gemmi.PolymerType.PeptideL:
                    return "protein"
                if entity.polymer_type == gemmi.PolymerType.PeptideD:
                    return "protein-D"
                elif entity.polymer_type == gemmi.PolymerType.Dna:
                    return "DNA"
                elif entity.polymer_type == gemmi.PolymerType.Rna:
                    return "RNA"
                elif entity.polymer_type == gemmi.PolymerType.DnaRnaHybrid:
                    return "DNA/RNA hybrid"
                elif entity.polymer_type in (gemmi.PolymerType.SaccharideD, gemmi.PolymerType.SaccharideL):
                    return "saccharide"
                else:
                    return "polymer"
            else:
                return "unknown"
    file_path = str(file_path)
    structure = gemmi.read_structure(file_path)
    structure.setup_entities()
    structure.assign_subchains()
    structure.remove_hydrogens()
    # NMR, errors
    if model_index >= len(structure):
        raise IndexError(
            f"model_index {model_index} out of range "
            f"(structure has {len(structure)} models)."
        )

    subchain_comp_type: dict[str, str] = {
        sub: _comp_type(entity)
        for entity in structure.entities
        for sub in entity.subchains
    }
    # _entry.id   2QXI 
    origin = file_path.split("\\")[-1].split(".")[0]
    model  = structure[model_index]

    rows = [
        {
            "name":           origin,
            "chain":          residue.subchain,       
            "auth_chain":     chain.name,  
            "residue":        residue.name,
            "residue_seqid":  residue.label_seq,
            "auth_seq_id":    residue.seqid.num,       
            "auth_icode":     residue.seqid.icode,    
            "atom_name":      atom.name,
            "element":        atom.element.name,
            "x":              atom.pos.x,
            "y":              atom.pos.y,
            "z":              atom.pos.z,
            "altloc":         atom.altloc,
            "occupancy":      atom.occ,
            "b_iso":          atom.b_iso,
            "component_type": subchain_comp_type.get(residue.subchain, "unknown"),
        }
        for chain in model
        for residue in chain
        for atom in residue
    ]
    
    if not silenced:
        print("Ξ" * 30)
        print(f"Acquired data frame: {origin}")
    CIF_df = pd.DataFrame(rows, columns=[
        "name", "chain", "auth_chain", "residue",
        "residue_seqid","auth_seq_id", "auth_icode",                             
        "atom_name", "element", "x", "y", "z", "altloc",
        "occupancy", "b_iso", "component_type",
    ])
    # Remove H
    CIF_df = CIF_df[CIF_df['element'] != "H"]
    # resolve dulicates due to non 1 occupancy
    CIF_df['residue_seqid'] = pd.to_numeric(CIF_df['residue_seqid'], errors='coerce').astype('Int64')
    CIF_df = CIF_df[
        CIF_df["occupancy"] == CIF_df.groupby(
            ["chain", "residue_seqid", "atom_name"],
            dropna=False          # <-- critical for ligands/waters
        )["occupancy"].transform("max")
    ].reset_index(drop=True)
    # integers seqid
    CIF_df['residue_seqid'] = pd.to_numeric(CIF_df['residue_seqid'], errors='coerce').astype('Int64') # non polymer give a nanone so the int conversions need to be done carefully
    # RESOLVE protein like petides: strange or too small
    if warning_to_CIF_dataframe is not None:
        for warning in warning_to_CIF_dataframe:
            chains_to_change = warning[0]
            new_name = warning[1]
            for chain in chains_to_change:
                mask = (CIF_df['chain'] == chain) & (CIF_df['component_type'] == 'protein')
                CIF_df.loc[mask, 'component_type'] = new_name

    return CIF_df

# 4. CIF_opener:

def CIF_opener(pathcif):
    metadata = CIF_metadata(pathcif, silenced=True)
    entry_id, seq_dict, warning_to_CIF_dataframe = CIF_entities(pathcif, silenced=True)
    CIF_df = CIF_dataframe(pathcif, warning_to_CIF_dataframe=warning_to_CIF_dataframe, silenced=True)
    return entry_id, metadata, seq_dict, CIF_df,  warning_to_CIF_dataframe

""" MUTATORS
"""
def protein_mutator(sequence, what_mutate="everything", probability=0.3, 
                    do_not_mutate="", do_not_mutate_to=None,
                    sulphur=True, aromatic=True, positive=True, 
                    negative=True, hydrofilic=True, hydrophobic=True, 
                    chain_disruptor=True, silenced=False):
    
    if len(what_mutate) == 0:
        print("SELECTED 0 AAs to MUTATE")
        return sequence
        
    if do_not_mutate_to is None: 
        do_not_mutate_to = []
    AA = list("GAVLIFYWHKRDENQSTCMP")
    what_exclude = list(do_not_mutate_to).copy() 
    if not sulphur:         what_exclude += ["M", "C"]
    if not aromatic:        what_exclude += ["F", "Y", "W"]
    if not positive:        what_exclude += ["K", "R"]
    if not negative:        what_exclude += ["D", "E"]
    if not hydrofilic:      what_exclude += ["K", "R", "D", "E", "N", "Q", "S", "T"]
    if not hydrophobic:     what_exclude += ["A", "V", "L", "I", "F", "W"]
    if not chain_disruptor: what_exclude += ["G", "P"]
    what_exclude = np.unique(what_exclude)
    
    mutable_to = [aa for aa in AA if aa not in what_exclude]
    AA_to_mutate = np.random.rand(len(sequence)) < probability
    random_AA = np.random.randint(0, len(mutable_to), size=len(sequence))
    
    if not (isinstance(what_mutate, str) and what_mutate == "everything"):
        mask = np.zeros(len(sequence), dtype=bool)
        indices = np.array(what_mutate) - 1
        mask[indices] = True
        AA_to_mutate = np.where(mask, AA_to_mutate, False)

    if do_not_mutate:
        protected = np.array([aa in do_not_mutate for aa in sequence])
        AA_to_mutate = np.where(protected, False, AA_to_mutate)
    
    mutated_sequence = []
    for n, amino_acid in enumerate(sequence):
        if AA_to_mutate[n]:
            mutated_sequence.append(mutable_to[random_AA[n]])
        else:
            mutated_sequence.append(amino_acid)
    mutated_sequence = "".join(mutated_sequence)

    MAX_ATTEMPTS = 30
    if mutated_sequence == sequence:
        for attempt in range(MAX_ATTEMPTS):
            mutated = protein_mutator(sequence, silenced=True)
            if mutated != sequence:
                print(f"Mutation achieved after {attempt + 1} attempt(s)")
                print(f"Original: {sequence}")
                print(f"Mutated:  {mutated}")
                print(f"Mutated {sum(a != b for a, b in zip(sequence, mutated))} amino acids out of {len(sequence)}")
                break
        else:
            print(f"No mutation achieved after {MAX_ATTEMPTS} attempts with {probability} used")
            mutated = sequence

    if not silenced:
        print(f"-"*30)
        print(f"Original sequence: {sequence}")
        print(f"Mutated sequence:  {mutated_sequence}")
        print(f"Mutated {AA_to_mutate.sum()} amino acids, out of {len(sequence)}")
        print(f"-"*30)
    return mutated_sequence

""" PROTEIN STATS
"""
def net_charge_protein(seq, pH=None):
    if pH is None:
        charge = 0
        for aa in seq:
            if aa in ('D', 'E'):
                charge -= 1
            elif aa in ('K', 'R'):
                charge += 1
        return charge

    charge = 0.0
    for aa in seq:
        pKa_data = aminoacid_pKa_DICT.get(aa)
        if pKa_data is None:
            continue

        pKaR = pKa_data['pKaR']
        if pKaR is None:
            continue

        ratio = 10 ** (pH - pKaR)

        #  ACIDS
        if aa in ('D', 'E', 'C', 'Y'):
            fraction_deprotonated = ratio / (1 + ratio)
            charge -= fraction_deprotonated

        #  BASES    
        elif aa in ('K', 'R', 'H'):
            fraction_protonated = 1 / (1 + ratio)
            charge += fraction_protonated

    return round(charge, 3)
    

""" BIO-GRAPHS:
"""
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# seqs_view = []
# seqs_view.append(["wt", wtGFP, ["#00C8A3"]*len(wtGFP)])
# seqs_view.append(["wt", wtGFP, ["#8FC800"]*len(wtGFP)])

def VISUALIZE_sequences(
    tracks: list[tuple[str, str, list[str]]],
    title,
    cell_w = 0.12*3, # 0.12
    cell_h = 0.18*3, # 0.18
    fontsize = 40,
    name_fontsize = 40,
    save_path = None,):

    n_rows = len(tracks)
    n_cols = max(len(seq) for _, seq, _ in tracks)

    rgba = np.ones((n_rows, n_cols, 4))
    rgba[..., :3] = 0.97

    for r, (_, seq, colors) in enumerate(tracks):
        for c, color in enumerate(colors):
            rgba[r, c] = mcolors.to_rgba(color)

    name_width = max(len(name) for name, _, _ in tracks)
    left_pad = name_width * 0.055  # inches

    fig, ax = plt.subplots(figsize=(n_cols * cell_w + left_pad, n_rows * cell_h))
    fig.patch.set_facecolor("#83a295")

    ax.imshow(rgba, aspect="auto", interpolation="none",
              extent=[-0.5, n_cols - 0.5, n_rows - 0.5, -0.5])

    for r, (name, seq, _) in enumerate(tracks):
        # Row label
        ax.text(-0.6, r, name,
                ha="right", va="center",
                fontsize=name_fontsize,
                fontfamily="DejaVu Sans Mono",
                fontweight="bold",
                color="#f0f6fc",
                transform=ax.transData)
        # Sequence characters
        for c, char in enumerate(seq):
            ax.text(c, r, char,
                    ha="center", va="center",
                    fontsize=fontsize,
                    fontfamily="DejaVu Sans Mono",
                    fontweight="bold",
                    color="#111111")

    ax.set_xlim(-0.5, n_cols - 0.5)
    ax.set_ylim(n_rows - 0.5, -0.5)
    ax.axis("off")

    if title:
        ax.set_title(title, fontsize=8, fontweight="bold",
                     color="#f0f6fc", pad=4,
                     fontfamily="DejaVu Sans Mono")

    plt.tight_layout(pad=0.1)

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight",
                    facecolor=fig.get_facecolor())

    return fig

"""CHIMERAX
"""
def expand_indices(indices):
    if len(indices) == 0:
        return ()
    expanded = []
    for i in indices:
        s = str(i)
        if "-" in s:
            a, b = s.split("-")
            expanded.extend(range(int(a), int(b) + 1))
        else:
            expanded.append(int(i))
    return tuple(expanded)

def make_chimera_indices(indices):
    expanded = []
    for i in indices:
        s = str(i)
        if "-" in s:
            a, b = s.split("-")
            expanded.extend(range(int(a), int(b) + 1))
        else:
            expanded.append(int(i))
    indices = expanded

    ranges = []
    start = end = indices[0]
    for n in indices[1:]:
        if n == end + 1:
            end = n
        else:
            ranges.append(f"{start}-{end}" if start != end else str(start))
            start = end = n
    ranges.append(f"{start}-{end}" if start != end else str(start))
    return ", ".join(ranges)

def make_chimera_file(color_chain_indices, pdb_file, filepath, extra_content="",
                    simplified=False, base_color="#648697", Nname="coloring",
                    just_color=True):
    filepath = Path(filepath)
    pdb_str = str(pdb_file)
    is_pdb_id = len(pdb_str.strip()) == 4 and pdb_str.strip().isalnum()
    wopen = f"open {pdb_file}" if is_pdb_id else f"open {pdb_file}"

    if just_color:
        lines = ["preset cartoon", f"color {base_color}", "hide atom", ""]
    else:
       lines = ["close", wopen,"preset cartoon", f"color {base_color}", "hide atom", ""] 
    color_chain_indices = [entry for entry in color_chain_indices if all(v is not None and v != "" and v != [] and v != {} for v in entry[:2])]
    for color, chain, indices in color_chain_indices:
        if indices:
            idx_str = make_chimera_indices(indices)
            lines.append(f"color /{chain}:{idx_str} {color}")
            if not simplified:
                lines.append(f"show /{chain}:{idx_str}")
                lines.append(f'label /{chain}:{idx_str} text "{{0.chain_id}}:{{0.name}}{{0.number}}"')
        else:
            lines.append(f"color /{chain} {color}")
            lines.append(f"show /{chain}")
    lines += ["", "color byhetero", "hide solvent", "hide H", "lighting simple", "graphics silhouettes true", extra_content]

    content = "\n".join(lines)
    filepath.mkdir(parents=True, exist_ok=True)
    out_file = filepath / f"{Nname}.cxc"
    with open(out_file, "w") as f:
        f.write(content)

    path_str = str(out_file)
    print("To open in ChimeraX, run this in the ChimeraX terminal:")
    print("windows:")
    print(f"  open {path_str.replace('/', chr(92))}")
    print("linux")
    print(f"  open {path_str.replace(chr(92), '/')}")
    

""" YAMLS:
"""
from pathlib import Path
#
def create_yaml(folder_path, name_of_file, mode, sequence1, sequence2=None, ligand_smiles=None):
    """
    1: One sequence
    2: Two sequences
    3: One sequence + One ligand
    4: One sequence + One ligand + Calculate affinity
    """
    yaml_content = f"""version: 1
sequences:
  - protein:
      id: A
      sequence: {sequence1}"""
    if mode == 1:
        pass
    elif mode == 2:
        if not sequence2:
            raise ValueError("Mode 2 requires 'sequence2' to be provided.")
        yaml_content += f"""
  - protein:
      id: B
      sequence: {sequence2}"""

    elif mode == 3:
        if not ligand_smiles:
            raise ValueError("Mode 3 requires 'ligand_smiles' to be provided.")
        yaml_content += f"""
  - ligand:
      id: B
      smiles: '{ligand_smiles}'"""

    elif mode == 4:
        if not ligand_smiles:
            raise ValueError("Mode 4 requires 'ligand_smiles' to be provided.")
        yaml_content += f"""
  - ligand:
      id: B
      smiles: '{ligand_smiles}'
properties:
  - affinity:
      binder: B"""
    else:
        raise ValueError("Invalid mode. Please select 1, 2, 3, or 4.")
    
    folder = Path(folder_path)
    folder.mkdir(parents=True, exist_ok=True)
    name_of_file += ".yaml"
    file_path = folder / name_of_file

    f = open(file_path, "w", encoding="utf-8")
    f.write(yaml_content)
    f.close()
    
    print(f"{name_of_file}"+fr" saved to {file_path}")

""" 
ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ
Ξ 3. GENERAL FUNTIONS Ξ
ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ
"""
scripts = CapitalInsensitiveDict({
'GREEK_CAPITAL': "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ",
'GREEK': "αβγδεζηθικλμνξοπρστυφχψω",
'CYPRO_MINOAN': "𒾐𒾑𒾒𒾓𒾔𒾕𒾖𒾗𒾘𒾙𒾚𒾛𒾜𒾝𒾞𒾟𒾠𒾡𒾢𒾣𒾤𒾥𒾦𒾧𒾨𒾩𒾪𒾫𒾬𒾭𒾮𒾯𒾰𒾱𒾲𒾳𒾴𒾵𒾶𒾷𒾸𒾹𒾺𒾻𒾼𒾽𒾾𒾿𒿀𒿁𒿂𒿃𒿄𒿅𒿆𒿇𒿈𒿉𒿊𒿋𒿌𒿍𒿎𒿏𒿐𒿑𒿒𒿓𒿔𒿕𒿖𒿗𒿘𒿙𒿚𒿛𒿜𒿝𒿞𒿟𒿠𒿡𒿢𒿣𒿤𒿥𒿦𒿧𒿨𒿩𒿪𒿫𒿬𒿭𒿮𒿯𒿰𒿱𒿲",
'EGYPTIAN_HIEROGLYPHS': "𓀀𓀁𓀂𓀃𓀄𓀅𓀆𓀇𓀈𓀉𓀊𓀋𓀌𓀍𓀎𓀏𓀐𓀑𓀒𓀓𓀔𓀕𓀖𓀗𓀘𓀙𓀚𓀛𓀜𓀝𓀞𓀟𓀠𓀡𓀢𓀣𓀤𓀥𓀦𓀧𓀨𓀩𓀪𓀫𓀬𓀭𓀮𓀯𓀰𓀱𓀲𓀳𓀴𓀵𓀶𓀷𓀸𓀹𓀺𓀻𓀼𓀽𓀾𓀿𓁀𓁁𓁂𓁃𓁄𓁅𓁆𓁇𓁈𓁉𓁊𓁋𓁌𓁍𓁎𓁏𓁐𓁑𓁒𓁓𓁔𓁕𓁖𓁗𓁘𓁙𓁚𓁛𓁜𓁝𓁞𓁟𓁠𓁡𓁢𓁣𓁤𓁥𓁦𓁧𓁨𓁩𓁪𓁫𓁬𓁭𓁮𓁯𓁰𓁱𓁲𓁳𓁴𓁵𓁶𓁷𓁸𓁹𓁺𓁻𓁼𓁽𓁾𓁿𓂀𓂁𓂂𓂃𓂄𓂅𓂆𓂇𓂈𓂉𓂊𓂋𓂌𓂍𓂎𓂏𓂐𓂑𓂒𓂓𓂔𓂕𓂖𓂗𓂘𓂙𓂚𓂛𓂜𓂝𓂞𓂟𓂠𓂡𓂢𓂣𓂤𓂥𓂦𓂧𓂨𓂩𓂪𓂫𓂬𓂭𓂮𓂯𓂰𓂱𓂲𓂳𓂴𓂵𓂶𓂷𓂸𓂹𓂺𓂻𓂼𓂽𓂾𓂿𓃀𓃁𓃂𓃃𓃄𓃅𓃆𓃇𓃈𓃉𓃊𓃋𓃌𓃍𓃎𓃏𓃐𓃑𓃒𓃓𓃔𓃕𓃖𓃗𓃘𓃙𓃚𓃛𓃜𓃝𓃞𓃟𓃠𓃡𓃢𓃣𓃤𓃥𓃦𓃧𓃨𓃩𓃪𓃫𓃬𓃭𓃮𓃯𓃰𓃱𓃲𓃳𓃴𓃵𓃶𓃷𓃸𓃹𓃺𓃻𓃼𓃽𓃾𓃿𓄀𓄁𓄂𓄃𓄄𓄅𓄆𓄇𓄈𓄉𓄊𓄋𓄌𓄍𓄎𓄏𓄐𓄑𓄒𓄓𓄔𓄕𓄖𓄗𓄘𓄙𓄚𓄛𓄜𓄝𓄞𓄟𓄠𓄡𓄢𓄣𓄤𓄥𓄦𓄧𓄨𓄩𓄪𓄫𓄬𓄭𓄮𓄯𓄰𓄱𓄲𓄳𓄴𓄵𓄶𓄷𓄸𓄹𓄺𓄻𓄼𓄽𓄾𓄿𓅀𓅁𓅂𓅃𓅄𓅅𓅆𓅇𓅈𓅉𓅊𓅋𓅌𓅍𓅎𓅏𓅐𓅑𓅒𓅓𓅔𓅕𓅖𓅗𓅘𓅙𓅚𓅛𓅜𓅝𓅞𓅟𓅠𓅡𓅢𓅣𓅤𓅥𓅦𓅧𓅨𓅩𓅪𓅫𓅬𓅭𓅮𓅯𓅰𓅱𓅲𓅳𓅴𓅵𓅶𓅷𓅸𓅹𓅺𓅻𓅼𓅽𓅾𓅿𓆀𓆁𓆂𓆃𓆄𓆅𓆆𓆇𓆈𓆉𓆊𓆋𓆌𓆍𓆎𓆏𓆐𓆑𓆒𓆓𓆔𓆕𓆖𓆗𓆘𓆙𓆚𓆛𓆜𓆝𓆞𓆟𓆠𓆡𓆢𓆣𓆤𓆥𓆦𓆧𓆨𓆩𓆪𓆫𓆬𓆭𓆮𓆯𓆰𓆱𓆲𓆳𓆴𓆵𓆶𓆷𓆸𓆹𓆺𓆻𓆼𓆽𓆾𓆿𓇀𓇁𓇂𓇃𓇄𓇅𓇆𓇇𓇈𓇉𓇊𓇋𓇌𓇍𓇎𓇏𓇐𓇑𓇒𓇓𓇔𓇕𓇖𓇗𓇘𓇙𓇚𓇛𓇜𓇝𓇞𓇟𓇠𓇡𓇢𓇣𓇤𓇥𓇦𓇧𓇨𓇩𓇪𓇫𓇬𓇭𓇮𓇯𓇰𓇱𓇲𓇳𓇴𓇵𓇶𓇷𓇸𓇹𓇺𓇻𓇼𓇽𓇾𓇿𓈀𓈁𓈂𓈃𓈄𓈅𓈆𓈇𓈈𓈉𓈊𓈋𓈌𓈍𓈎𓈏𓈐𓈑𓈒𓈓𓈔𓈕𓈖𓈗𓈘𓈙𓈚𓈛𓈜𓈝𓈞𓈟𓈠𓈡𓈢𓈣𓈤𓈥𓈦𓈧𓈨𓈩𓈪𓈫𓈬𓈭𓈮𓈯𓈰𓈱𓈲𓈳𓈴𓈵𓈶𓈷𓈸𓈹𓈺𓈻𓈼𓈽𓈾𓈿𓉀𓉁𓉂𓉃𓉄𓉅𓉆𓉇𓉈𓉉𓉊𓉋𓉌𓉍𓉎𓉏𓉐𓉑𓉒𓉓𓉔𓉕𓉖𓉗𓉘𓉙𓉚𓉛𓉜𓉝𓉞𓉟𓉠𓉡𓉢𓉣𓉤𓉥𓉦𓉧𓉨𓉩𓉪𓉫𓉬𓉭𓉮𓉯𓉰𓉱𓉲𓉳𓉴𓉵𓉶𓉷𓉸𓉹𓉺𓉻𓉼𓉽𓉾𓉿𓊀𓊁𓊂𓊃𓊄𓊅𓊆𓊇𓊈𓊉𓊊𓊋𓊌𓊍𓊎𓊏𓊐𓊑𓊒𓊓𓊔𓊕𓊖𓊗𓊘𓊙𓊚𓊛𓊜𓊝𓊞𓊟𓊠𓊡𓊢𓊣𓊤𓊥𓊦𓊧𓊨𓊩𓊪𓊫𓊬𓊭𓊮𓊯𓊰𓊱𓊲𓊳𓊴𓊵𓊶𓊷𓊸𓊹𓊺𓊻𓊼𓊽𓊾𓊿𓋀𓋁𓋂𓋃𓋄𓋅𓋆𓋇𓋈𓋉𓋊𓋋𓋌𓋍𓋎𓋏𓋐𓋑𓋒𓋓𓋔𓋕𓋖𓋗𓋘𓋙𓋚𓋛𓋜𓋝𓋞𓋟𓋠𓋡𓋢𓋣𓋤𓋥𓋦𓋧𓋨𓋩𓋪𓋫𓋬𓋭𓋮𓋯𓋰𓋱𓋲𓋳𓋴𓋵𓋶𓋷𓋸𓋹𓋺𓋻𓋼𓋽𓋾𓋿𓌀𓌁𓌂𓌃𓌄𓌅𓌆𓌇𓌈𓌉𓌊𓌋𓌌𓌍𓌎𓌏𓌐𓌑𓌒𓌓𓌔𓌕𓌖𓌗𓌘𓌙𓌚𓌛𓌜𓌝𓌞𓌟𓌠𓌡𓌢𓌣𓌤𓌥𓌦𓌧𓌨𓌩𓌪𓌫𓌬𓌭𓌮𓌯𓌰𓌱𓌲𓌳𓌴𓌵𓌶𓌷𓌸𓌹𓌺𓌻𓌼𓌽𓌾𓌿𓍀𓍁𓍂𓍃𓍄𓍅𓍆𓍇𓍈𓍉𓍊𓍋𓍌𓍍𓍎𓍏𓍐𓍑𓍒𓍓𓍔𓍕𓍖𓍗𓍘𓍙𓍚𓍛𓍜𓍝𓍞𓍟𓍠𓍡𓍢𓍣𓍤𓍥𓍦𓍧𓍨𓍩𓍪𓍫𓍬𓍭𓍮𓍯𓍰𓍱𓍲𓍳𓍴𓍵𓍶𓍷𓍸𓍹𓍺𓍻𓍼𓍽𓍾𓍿𓎀𓎁𓎂𓎃𓎄𓎅𓎆𓎇𓎈𓎉𓎊𓎋𓎌𓎍𓎎𓎏𓎐𓎑𓎒𓎓𓎔𓎕𓎖𓎗𓎘𓎙𓎚𓎛𓎜𓎝𓎞𓎟𓎠𓎡𓎢𓎣𓎤𓎥𓎦𓎧𓎨𓎩𓎪𓎫𓎬𓎭𓎮𓎯𓎰𓎱𓎲𓎳𓎴𓎵𓎶𓎷𓎸𓎹𓎺𓎻𓎼𓎽𓎾𓎿𓏀𓏁𓏂𓏃𓏄𓏅𓏆𓏇𓏈𓏉𓏊𓏋𓏌𓏍𓏎𓏏𓏐𓏑𓏒𓏓𓏔𓏕𓏖𓏗𓏘𓏙𓏚𓏛𓏜𓏝𓏞𓏟𓏠𓏡𓏢𓏣𓏤𓏥𓏦𓏧𓏨𓏩𓏪𓏫𓏬𓏭𓏮𓏯𓏰𓏱𓏲𓏳𓏴𓏵𓏶𓏷𓏸𓏹𓏺𓏻𓏼𓏽𓏾𓏿𓐀𓐁𓐂𓐃𓐄𓐅𓐆𓐇𓐈𓐉𓐊𓐋𓐌𓐍𓐎𓐏𓐐𓐑𓐒𓐓𓐔𓐕𓐖𓐗𓐘𓐙𓐚𓐛𓐜𓐝𓐞𓐟𓐠𓐡𓐢𓐣𓐤𓐥𓐦𓐧𓐨𓐩𓐪𓐫𓐬𓐭𓐮",
'LINEAR_A': "𐘀𐘁𐘂𐘃𐘄𐘅𐘆𐘇𐘈𐘉𐘊𐘋𐘌𐘍𐘎𐘏𐘐𐘑𐘒𐘓𐘔𐘕𐘖𐘗𐘘𐘙𐘚𐘛𐘜𐘝𐘞𐘟𐘠𐘡𐘢𐘣𐘤𐘥𐘦𐘧𐘨𐘩𐘪𐘫𐘬𐘭𐘮𐘯𐘰𐘱𐘲𐘳𐘴𐘵𐘶𐘷𐘸𐘹𐘺𐘻𐘼𐘽𐘾𐘿𐙀𐙁𐙂𐙃𐙄𐙅𐙆𐙇𐙈𐙉𐙊𐙋𐙌𐙍𐙎𐙏𐙐𐙑𐙒𐙓𐙔𐙕𐙖𐙗𐙘𐙙𐙚𐙛𐙜𐙝𐙞𐙟𐙠𐙡𐙢𐙣𐙤𐙥𐙦𐙧𐙨𐙩𐙪𐙫𐙬𐙭𐙮𐙯𐙰𐙱𐙲𐙳𐙴𐙵𐙶𐙷𐙸𐙹𐙺𐙻𐙼𐙽𐙾𐙿𐚀𐚁𐚂𐚃𐚄𐚅𐚆𐚇𐚈𐚉𐚊𐚋𐚌𐚍𐚎𐚏𐚐𐚑𐚒𐚓𐚔𐚕𐚖𐚗𐚘𐚙𐚚𐚛𐚜𐚝𐚞𐚟𐚠𐚡𐚢𐚣𐚤𐚥𐚦𐚧𐚨𐚩𐚪𐚫𐚬𐚭𐚮𐚯𐚰𐚱𐚲𐚳𐚴𐚵𐚶𐚷𐚸𐚹𐚺𐚻𐚼𐚽𐚾𐚿𐛀𐛁𐛂𐛃𐛄𐛅𐛆𐛇𐛈𐛉𐛊𐛋𐛌𐛍𐛎𐛏𐛐𐛑𐛒𐛓𐛔𐛕𐛖𐛗𐛘𐛙𐛚𐛛𐛜𐛝𐛞𐛟𐛠𐛡𐛢𐛣𐛤𐛥𐛦𐛧𐛨𐛩𐛪𐛫𐛬𐛭𐛮𐛯𐛰𐛱𐛲𐛳𐛴𐛵𐛶𐛷𐛸𐛹𐛺𐛻𐛼𐛽𐛾𐛿𐜀𐜁𐜂𐜃𐜄𐜅𐜆𐜇𐜈𐜉𐜊𐜋𐜌𐜍𐜎𐜏𐜐𐜑𐜒𐜓𐜔𐜕𐜖𐜗𐜘𐜙𐜚𐜛𐜜𐜝𐜞𐜟𐜠𐜡𐜢𐜣𐜤𐜥𐜦𐜧𐜨𐜩𐜪𐜫𐜬𐜭𐜮𐜯𐜰𐜱𐜲𐜳𐜴𐜵𐜶𐝀𐝁𐝂𐝃𐝄𐝅𐝆𐝇𐝈𐝉𐝊𐝋𐝌𐝍𐝎𐝏𐝐𐝑𐝒𐝓𐝔𐝕𐝠𐝡𐝢𐝣𐝤𐝥𐝦𐝧",
'LINEAR_B__SYLLABARY': "𐀀𐀁𐀂𐀃𐀄𐀅𐀆𐀇𐀈𐀉𐀊𐀋𐀌𐀍𐀎𐀏𐀐𐀑𐀒𐀓𐀔𐀕𐀖𐀗𐀘𐀙𐀚𐀛𐀜𐀝𐀞𐀟𐀠𐀡𐀢𐀣𐀤𐀥𐀦𐀧𐀨𐀩𐀪𐀫𐀬𐀭𐀮𐀯𐀰𐀱𐀲𐀳𐀴𐀵𐀶𐀷𐀸𐀹𐀺𐀻𐀼𐀽𐀾𐀿𐁀𐁁𐁂𐁃𐁄𐁅𐁆𐁇𐁈𐁉𐁊𐁋𐁌𐁍𐁎𐁏𐁐𐁑𐁒𐁓𐁔𐁕𐁖𐁗𐁘𐁙𐁚𐁛𐁜𐁝",
'LINEAR_B_IDEOGRAMS': "𐂀𐂁𐂂𐂃𐂄𐂅𐂆𐂇𐂈𐂉𐂊𐂋𐂌𐂍𐂎𐂏𐂐𐂑𐂒𐂓𐂔𐂕𐂖𐂗𐂘𐂙𐂚𐂛𐂜𐂝𐂞𐂟𐂠𐂡𐂢𐂣𐂤𐂥𐂦𐂧𐂨𐂩𐂪𐂫𐂬𐂭𐂮𐂯𐂰𐂱𐂲𐂳𐂴𐂵𐂶𐂷𐂸𐂹𐂺𐂻𐂼𐂽𐂾𐂿𐃀𐃁𐃂𐃃𐃄𐃅𐃆𐃇𐃈𐃉𐃊𐃋𐃌𐃍𐃎𐃏𐃐𐃑𐃒𐃓𐃔𐃕𐃖𐃗𐃘𐃙𐃚𐃛𐃜𐃝𐃞𐃟𐃠𐃡𐃢𐃣𐃤𐃥𐃦𐃧𐃨𐃩𐃪𐃫𐃬𐃭𐃮𐃯𐃰𐃱𐃲𐃳𐃴𐃵𐃶𐃷𐃸𐃹𐃺",
'AEGEAN_NUMBERS': "𐄀𐄁𐄂𐄇𐄈𐄉𐄊𐄋𐄌𐄍𐄎𐄏𐄐𐄑𐄒𐄓𐄔𐄕𐄖𐄗𐄘𐄙𐄚𐄛𐄜𐄝𐄞𐄟𐄠𐄡𐄢𐄣𐄤𐄥𐄦𐄧𐄨𐄩𐄪𐄫𐄬𐄭𐄮𐄯𐄰𐄱𐄲𐄳𐄷𐄸𐄹𐄺𐄻𐄼𐄽𐄾𐄿",
'OLD_PERSIAN': "𐎠𐎡𐎢𐎣𐎤𐎥𐎦𐎧𐎨𐎩𐎪𐎫𐎬𐎭𐎮𐎯𐎰𐎱𐎲𐎳𐎴𐎵𐎶𐎷𐎸𐎹𐎺𐎻𐎼𐎽𐎾𐎿𐏀𐏁𐏂𐏃𐏈𐏉𐏊𐏋𐏌𐏍𐏎𐏏𐏐𐏑𐏒𐏓𐏔𐏕",
'PHOENICIAN': "𐤀𐤁𐤂𐤃𐤄𐤅𐤆𐤇𐤈𐤉𐤊𐤋𐤌𐤍𐤎𐤏𐤐𐤑𐤒𐤓𐤔𐤕𐤖𐤗𐤘𐤙𐤚𐤛𐤟",
'ANATOLIAN_HIEROGLYPHS': "𔐀𔐁𔐂𔐃𔐄𔐅𔐆𔐇𔐈𔐉𔐊𔐋𔐌𔐍𔐎𔐏𔐐𔐑𔐒𔐓𔐔𔐕𔐖𔐗𔐘𔐙𔐚𔐛𔐜𔐝𔐞𔐟𔐠𔐡𔐢𔐣𔐤𔐥𔐦𔐧𔐨𔐩𔐪𔐫𔐬𔐭𔐮𔐯𔐰𔐱𔐲𔐳𔐴𔐵𔐶𔐷𔐸𔐹𔐺𔐻𔐼𔐽𔐾𔐿𔑀𔑁𔑂𔑃𔑄𔑅𔑆𔑇𔑈𔑉𔑊𔑋𔑌𔑍𔑎𔑏𔑐𔑑𔑒𔑓𔑔𔑕𔑖𔑗𔑘𔑙𔑚𔑛𔑜𔑝𔑞𔑟𔑠𔑡𔑢𔑣𔑤𔑥𔑦𔑧𔑨𔑩𔑪𔑫𔑬𔑭𔑮𔑯𔑰𔑱𔑲𔑳𔑴𔑵𔑶𔑷𔑸𔑹𔑺𔑻𔑼𔑽𔑾𔑿𔒀𔒁𔒂𔒃𔒄𔒅𔒆𔒇𔒈𔒉𔒊𔒋𔒌𔒍𔒎𔒏𔒐𔒑𔒒𔒓𔒔𔒕𔒖𔒗𔒘𔒙𔒚𔒛𔒜𔒝𔒞𔒟𔒠𔒡𔒢𔒣𔒤𔒥𔒦𔒧𔒨𔒩𔒪𔒫𔒬𔒭𔒮𔒯𔒰𔒱𔒲𔒳𔒴𔒵𔒶𔒷𔒸𔒹𔒺𔒻𔒼𔒽𔒾𔒿𔓀𔓁𔓂𔓃𔓄𔓅𔓆𔓇𔓈𔓉𔓊𔓋𔓌𔓍𔓎𔓏𔓐𔓑𔓒𔓓𔓔𔓕𔓖𔓗𔓘𔓙𔓚𔓛𔓜𔓝𔓞𔓟𔓠𔓡𔓢𔓣𔓤𔓥𔓦𔓧𔓨𔓩𔓪𔓫𔓬𔓭𔓮𔓯𔓰𔓱𔓲𔓳𔓴𔓵𔓶𔓷𔓸𔓹𔓺𔓻𔓼𔓽𔓾𔓿𔔀𔔁𔔂𔔃𔔄𔔅𔔆𔔇𔔈𔔉𔔊𔔋𔔌𔔍𔔎𔔏𔔐𔔑𔔒𔔓𔔔𔔕𔔖𔔗𔔘𔔙𔔚𔔛𔔜𔔝𔔞𔔟𔔠𔔡𔔢𔔣𔔤𔔥𔔦𔔧𔔨𔔩𔔪𔔫𔔬𔔭𔔮𔔯𔔰𔔱𔔲𔔳𔔴𔔵𔔶𔔷𔔸𔔹𔔺𔔻𔔼𔔽𔔾𔔿𔕀𔕁𔕂𔕃𔕄𔕅𔕆𔕇𔕈𔕉𔕊𔕋𔕌𔕍𔕎𔕏𔕐𔕑𔕒𔕓𔕔𔕕𔕖𔕗𔕘𔕙𔕚𔕛𔕜𔕝𔕞𔕟𔕠𔕡𔕢𔕣𔕤𔕥𔕦𔕧𔕨𔕩𔕪𔕫𔕬𔕭𔕮𔕯𔕰𔕱𔕲𔕳𔕴𔕵𔕶𔕷𔕸𔕹𔕺𔕻𔕼𔕽𔕾𔕿𔖀𔖁𔖂𔖃𔖄𔖅𔖆𔖇𔖈𔖉𔖊𔖋𔖌𔖍𔖎𔖏𔖐𔖑𔖒𔖓𔖔𔖕𔖖𔖗𔖘𔖙𔖚𔖛𔖜𔖝𔖞𔖟𔖠𔖡𔖢𔖣𔖤𔖥𔖦𔖧𔖨𔖩𔖪𔖫𔖬𔖭𔖮𔖯𔖰𔖱𔖲𔖳𔖴𔖵𔖶𔖷𔖸𔖹𔖺𔖻𔖼𔖽𔖾𔖿𔗀𔗁𔗂𔗃𔗄𔗅𔗆𔗇𔗈𔗉𔗊𔗋𔗌𔗍𔗎𔗏𔗐𔗑𔗒𔗓𔗔𔗕𔗖𔗗𔗘𔗙𔗚𔗛𔗜𔗝𔗞𔗟𔗠𔗡𔗢𔗣𔗤𔗥𔗦𔗧𔗨𔗩𔗪𔗫𔗬𔗭𔗮𔗯𔗰𔗱𔗲𔗳𔗴𔗵𔗶𔗷𔗸𔗹𔗺𔗻𔗼𔗽𔗾𔗿𔘀𔘁𔘂𔘃𔘄𔘅𔘆𔘇𔘈𔘉𔘊𔘋𔘌𔘍𔘎𔘏𔘐𔘑𔘒𔘓𔘔𔘕𔘖𔘗𔘘𔘙𔘚𔘛𔘜𔘝𔘞𔘟𔘠𔘡𔘢𔘣𔘤𔘥𔘦𔘧𔘨𔘩𔘪𔘫𔘬𔘭𔘮𔘯𔘰𔘱𔘲𔘳𔘴𔘵𔘶𔘷𔘸𔘹𔘺𔘻𔘼𔘽𔘾𔘿𔙀𔙁𔙂𔙃𔙄𔙅𔙆",
'IMPERIAL_ARAMAIC': "𐡀𐡁𐡂𐡃𐡄𐡅𐡆𐡇𐡈𐡉𐡊𐡋𐡌𐡍𐡎𐡏𐡐𐡑𐡒𐡓𐡔𐡕𐡖𐡗𐡘𐡙𐡚𐡛𐡜𐡝𐡞𐡟",
})
# Symbols
Other_strange = "═║╔╩═╩╗╚═╝╠═╣╩═╬═╦╰─╯╭─╮╱╲╳┏━┓┗━┛┃┌─┐└─┘│├┤┬┴┼██≡="

"""PRINTING AND PROGRESS
"""
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

# titler("main project","thing does XYZ","","Antonio de Palma Masaveu", feat="peptide")
def titler(main_title,seco_title,terc_title,name_autho, feat):
    center_len = 30
    longest_string = max((len(main_title),len(seco_title),len(terc_title),len(name_autho)))
    if longest_string > center_len:
        center_len = center_len - (center_len - longest_string)
    center_len += 4  
    feature_n = 1
    
    main_title = " "*int(((center_len-len(main_title))/2) + 0.5)+ main_title + " "*int(((center_len-len(main_title))/2))
    seco_title = " "*int(((center_len-len(seco_title))/2) + 0.5)+ seco_title + " "*int(((center_len-len(seco_title))/2))
    terc_title = " "*int(((center_len-len(terc_title))/2) + 0.5)+ terc_title + " "*int(((center_len-len(terc_title))/2))
    name_autho = " "*int(((center_len-len(name_autho))/2) + 0.5)+ name_autho + " "*int(((center_len-len(name_autho))/2))
    floor_sect = "_" * center_len

    FEATURE = features[feat]
    print(" "*len(FEATURE[0])+ "_"*center_len + " "*len(FEATURE[0]))
    print(FEATURE[0]*feature_n + main_title + FEATURE[0]*feature_n)
    print(FEATURE[1]*feature_n + seco_title + FEATURE[1]*feature_n)
    print(FEATURE[2]*feature_n + terc_title + FEATURE[2]*feature_n)
    print(FEATURE[3]*feature_n + name_autho + FEATURE[3]*feature_n)
    print(FEATURE[4]*feature_n + floor_sect + FEATURE[4]*feature_n)
    print("\n")
#  
# progress_update("jejeje", n+1, N, compact_updates=True)
def progress_update(main_title, n, lenloop, compact_updates= False):
    curr_p = int((n / lenloop) * 20)
    prev_p = int(((n - 1) / lenloop) * 20)
    if compact_updates and curr_p == prev_p and n != lenloop:
        return
    n += 0
    center_len = 30
    longest_string = len(main_title)
    if longest_string > center_len:
        center_len = center_len - (center_len - longest_string)
    center_len += 4 
    main_title = " "*int(((center_len-len(main_title))/2) + 0.5)+ main_title + " "*int(((center_len-len(main_title))/2))

    p = int((n/lenloop)*20)
    bar = [
    f"╭────────────────────────╮",
    f"│α·{'#'*p+' '*(20-p)  }·ω│",
    f"╰────────────────────────╯",]
    detail = [
    f"╭{'─'*(len(str(abs(n)))+1+len(str(abs(lenloop))))}╮",
    f"│{n}/{lenloop}│",
    f"╰{'─'*(len(str(abs(n)))+1+len(str(abs(lenloop))))}╯",]

    print(bar[0] + "·"*center_len + detail[0])
    print(bar[1] + main_title + detail[1])
    print(bar[2] + "·"*center_len + detail[2])

