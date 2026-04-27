""" 
ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ
Ξ aminoacids_DICTS Ξ
ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ
"""

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

# aminoacid strings
aminoacid_ONEL  = list('GAVLIFYWHKRDENQSTCMP')
aminoacid_THREEL = ['GLY','ALA','VAL','LEU','ILE','PHE','TYR','TRP','HIS','LYS','ARG','ASP','GLU','ASN','GLN','SER','THR','CYS','MET','PRO']
aminoacid_NAMES = ['GLYCINE','ALANINE','VALINE','LEUCINE','ISOLEUCINE','PHENYALANINE','TYROSINE','TRYPTOPHAN','HISTIDINE','LYSINE','ARGININE','ASPARTATE','GLUTAMATE','ASPARAGINE','GLUTAMINE','SERINE','THREONINE','CYSTEINE','METHIONINE','PROLINE']

# aminoacid_DICT.get("A", "X")
#"".join([bioq.aminoacid_DICT.get(AA,"X") for AA in seq])
aminoacid_DICT = CapitalInsensitiveDict(
{
'G': 'G',  'GLY': 'G',  'GLYCINE':       'G',      
'A': 'A',  'ALA': 'A',  'ALANINE':       'A',      
'V': 'V',  'VAL': 'V',  'VALINE':        'V',       
'L': 'L',  'LEU': 'L',  'LEUCINE':       'L',      
'I': 'I',  'ILE': 'I',  'ISOLEUCINE':    'I',   
'F': 'F',  'PHE': 'F',  'PHENYLALANINE': 'F',
'Y': 'Y',  'TYR': 'Y',  'TYROSINE':      'Y',    
'W': 'W',  'TRP': 'W',  'TRYPTOPHAN':    'W',   
'H': 'H',  'HIS': 'H',  'HISTIDINE':     'H',    
'K': 'K',  'LYS': 'K',  'LYSINE':        'K',       
'R': 'R',  'ARG': 'R',  'ARGININE':      'R',     
'D': 'D',  'ASP': 'D',  'ASPARTATE':     'D',    
'E': 'E',  'GLU': 'E',  'GLUTAMATE':     'E',    
'N': 'N',  'ASN': 'N',  'ASPARAGINE':    'N',   
'Q': 'Q',  'GLN': 'Q',  'GLUTAMINE':     'Q',    
'S': 'S',  'SER': 'S',  'SERINE':        'S',       
'T': 'T',  'THR': 'T',  'THREONINE':     'T',    
'C': 'C',  'CYS': 'C',  'CYSTEINE':      'C',     
'M': 'M',  'MET': 'M',  'METHIONINE':    'M',   
'P': 'P',  'PRO': 'P',  'PROLINE':       'P',})
# dictionary of amino acid inputs AA => n => aminoacid strings
aminoacid_NUM_DICT = CapitalInsensitiveDict(
{'G': 0, 'GLY': 0,'GLYCINE':       0,
 'A': 1, 'ALA': 1,'ALANINE':       1,
 'V': 2, 'VAL': 2,'VALINE':        2,
 'L': 3, 'LEU': 3,'LEUCINE':       3,
 'I': 4, 'ILE': 4,'ISOLEUCINE':    4,
 'F': 5, 'PHE': 5,'PHENYLALANINE': 5,
 'Y': 6, 'TYR': 6,'TYROSINE':      6,
 'W': 7, 'TRP': 7,'TRYPTOPHAN':    7,
 'H': 8, 'HIS': 8,'HISTIDINE':     8,
 'K': 9, 'LYS': 9,'LYSINE':        9,
 'R': 10,'ARG': 10,'ARGININE':    10,
 'D': 11,'ASP': 11,'ASPARTATE':   11,
 'E': 12,'GLU': 12,'GLUTAMATE':   12,
 'N': 13,'ASN': 13,'ASPARAGINE':  13,
 'Q': 14,'GLN': 14,'GLUTAMINE':   14,
 'S': 15,'SER': 15,'SERINE':      15,
 'T': 16,'THR': 16,'THREONINE':   16,
 'C': 17,'CYS': 17,'CYSTEINE':    17,
 'M': 18,'MET': 18,'METHIONINE':  18,
 'P': 19,'PRO': 19,'PROLINE':     19,})

aminoacid_ATOMLABELS_DICT = CapitalInsensitiveDict({
 'G': ['N', 'CA', 'C', 'O'],
 'A': ['N', 'CA', 'C', 'O', 'CB'],
 'V': ['N', 'CA', 'C', 'O', 'CB', 'CG1', 'CG2'],
 'L': ['N', 'CA', 'C', 'O', 'CB', 'CG',  'CD1', 'CD2'],
 'I': ['N', 'CA', 'C', 'O', 'CB', 'CG1', 'CG2', 'CD1'],
 'F': ['N', 'CA', 'C', 'O', 'CB', 'CG',  'CD1', 'CD2', 'CE1', 'CE2', 'CZ'],
 'Y': ['N', 'CA', 'C', 'O', 'CB', 'CG',  'CD1', 'CD2', 'CE1', 'CE2', 'CZ', 'OH'],
 'W': ['N', 'CA', 'C', 'O', 'CB', 'CG',  'CD1', 'CD2', 'NE1', 'CE2', 'CE3','CZ2','CZ3','CH2'],
 'H': ['N', 'CA', 'C', 'O', 'CB', 'CG',  'ND1', 'CD2', 'CE1', 'NE2'],
 'K': ['N', 'CA', 'C', 'O', 'CB', 'CG',  'CD',  'CE',  'NZ'],
 'R': ['N', 'CA', 'C', 'O', 'CB', 'CG',  'CD',  'NE',  'CZ',  'NH1', 'NH2'],
 'D': ['N', 'CA', 'C', 'O', 'CB', 'CG',  'OD1', 'OD2'],
 'E': ['N', 'CA', 'C', 'O', 'CB', 'CG',  'CD',  'OE1', 'OE2'],
 'N': ['N', 'CA', 'C', 'O', 'CB', 'CG',  'OD1', 'ND2'],
 'Q': ['N', 'CA', 'C', 'O', 'CB', 'CG',  'CD',  'OE1', 'NE2'],
 'T': ['N', 'CA', 'C', 'O', 'CB', 'OG1', 'CG2'],
 'S': ['N', 'CA', 'C', 'O', 'CB', 'OG'],
 'C': ['N', 'CA', 'C', 'O', 'CB', 'SG'],
 'M': ['N', 'CA', 'C', 'O', 'CB', 'CG',  'SD',  'CE'],
 'P': ['N', 'CA', 'C', 'O', 'CB', 'CG',  'CD']})
# Exeptions, N terminal
aminoacid_HDONORS_DICT = CapitalInsensitiveDict({
 'G': ['N'],
 'A': ['N'],
 'V': ['N'],
 'L': ['N'],
 'I': ['N'],
 'F': ['N'],
 'Y': ['N', 'OH'],
 'W': ['N', 'NE1'],
 'H': ['N','ND1','NE2'],
 'K': ['N','NZ'],
 'R': ['N','NE', 'NH1', 'NH2'],
 'D': ['N'],
 'E': ['N'],
 'N': ['N', 'ND2'],
 'Q': ['N', 'NE2'],
 'T': ['N', 'OG1'],
 'S': ['N', 'OG'],
 'C': ['N'],
 'M': ['N'],
 'P': [   ],}) # except terminal N
aminoacid_HACCEPTORS_DICT = CapitalInsensitiveDict({
 'G': ['O'],
 'A': ['O'],
 'V': ['O'],
 'L': ['O'],
 'I': ['O'],
 'F': ['O'],
 'Y': ['O', 'OH'],
 'W': ['O'],
 'H': ['O', 'ND1', 'NE2'],
 'K': ['O'],
 'R': ['O'],
 'D': ['O', 'OD1', 'OD2'],
 'E': ['O', 'OE1', 'OE2'],
 'N': ['O', 'OD1'],
 'Q': ['O', 'OE1'],
 'T': ['O', 'OG1'],
 'S': ['O', 'OG'],
 'C': ['O'],
 'M': ['O'],
 'P': ['O'],})
# charge spread out over E:2, D:2, H:2, K:1, R:3, Y:1, C:1, terminal-O:2, terminal-N:1
# C-terminal also have a negative charge; O, OXT, OT1, OT2
aminoacid_NEGATIVEC_DICT = CapitalInsensitiveDict({
 'G': [],'A': [],'V': [],'L': [],'I': [],'F': [],'Y': ['OH'],'W': [],'H': [],'K': [],'R': [],
 'D': ['OD1', 'OD2'],
 'E': ['OE1', 'OE2'],
 'N': [],'Q': [],'T': [],'S': [],'C': ['SG'],'M': [],'P': []})
# N-terminal ~always has potive charge
aminoacid_POSITIVEC_DICT = CapitalInsensitiveDict({
 'G': [],'A': [],'V': [],'L': [],'I': [],'F': [],'Y': [],'W': [],
 'H': ['ND1', 'NE2'],
 'K': ['NZ'],
 'R': ['NE', 'NH1', 'NH2'],
 'D': [],'E': [],'N': [],'Q': [],'T': [],'S': [],'C': [],'M': [],'P': []})
aminoacid_SP2_DICT = CapitalInsensitiveDict({
 'G': ['N','C','O'],
 'A': ['N','C','O'],
 'V': ['N','C','O'],
 'L': ['N','C','O'],
 'I': ['N','C','O'],
 'F': ['N','C','O','CG','CD1','CD2','CE1','CE2','CZ'],
 'Y': ['N','C','O','CG','CD1','CD2','CE1','CE2','CZ'],
 'W': ['N','C','O','CG','CD1','CD2','NE1','CE2','CE3','CZ2','CZ3','CH2'],
 'H': ['N','C','O','CG','ND1','CD2','CE1','NE2'],
 'K': ['N','C','O'],
 'R': ['N','C','O','NE','CZ','NH1','NH2'],
 'D': ['N','C','O','CG','OD1','OD2'],
 'E': ['N','C','O','CD','OE1','OE2'],
 'N': ['N','C','O','CG','OD1','ND2'],
 'Q': ['N','C','O','CD','OE1','NE2'],
 'T': ['N','C','O'],
 'S': ['N','C','O'],
 'C': ['N','C','O'],
 'M': ['N','C','O'],
 'P': ['N','C','O'],})
#
aminoacid_pKa_DICT = CapitalInsensitiveDict({
    'G': {'pKa1': 2.34, 'pKa2': 9.60,  'pKaR':  None},
    'A': {'pKa1': 2.34, 'pKa2': 9.69,  'pKaR':  None},
    'V': {'pKa1': 2.32, 'pKa2': 9.62,  'pKaR':  None},
    'L': {'pKa1': 2.36, 'pKa2': 9.60,  'pKaR':  None},
    'I': {'pKa1': 2.36, 'pKa2': 9.68,  'pKaR':  None},
    'F': {'pKa1': 1.83, 'pKa2': 9.13,  'pKaR':  None},
    'Y': {'pKa1': 2.20, 'pKa2': 9.11,  'pKaR': 10.07},
    'W': {'pKa1': 2.38, 'pKa2': 9.39,  'pKaR':  None},
    'H': {'pKa1': 1.82, 'pKa2': 9.17,  'pKaR':  6.00},
    'K': {'pKa1': 2.18, 'pKa2': 8.95,  'pKaR': 10.53},
    'R': {'pKa1': 2.17, 'pKa2': 9.04,  'pKaR': 12.48},
    'D': {'pKa1': 2.11, 'pKa2': 9.62,  'pKaR':  3.65},
    'E': {'pKa1': 2.19, 'pKa2': 9.67,  'pKaR':  4.25},  
    'N': {'pKa1': 2.02, 'pKa2': 8.80,  'pKaR':  None},
    'Q': {'pKa1': 2.17, 'pKa2': 9.13,  'pKaR':  None},
    'S': {'pKa1': 2.21, 'pKa2': 9.15,  'pKaR':  None},
    'T': {'pKa1': 2.11, 'pKa2': 9.62,  'pKaR':  None},
    'C': {'pKa1': 1.96, 'pKa2': 10.28, 'pKaR':  8.18},
    'M': {'pKa1': 2.28, 'pKa2': 9.21,  'pKaR':  None},
    'P': {'pKa1': 1.99, 'pKa2': 10.96, 'pKaR':  None},
})
# AA_bonds:
G_bonds = [
    #N   CA    C    O
    [ 0,  1,   0,   0],   # N
    [ 1,  0,   1,   0],   # CA
    [ 0,  1,   0,   1],   # C
    [ 0,  0,   1,   0],   # O
]
A_bonds = [
    #N   CA    C    O   CB
    [ 0,  1,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1],   # CA
    [ 0,  1,   0,   1,   0],   # C
    [ 0,  0,   1,   0,   0],   # O
    [ 0,  1,   0,   0,   0],   # CB
]
V_bonds = [
    #N   CA    C    O   CB  CG1  CG2
    [ 0,  1,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   1],   # CB
    [ 0,  0,   0,   0,   1,   0,   0],   # CG1
    [ 0,  0,   0,   0,   1,   0,   0],   # CG2
]
L_bonds = [
    #N   CA    C    O   CB   CG  CD1  CD2
    [ 0,  1,   0,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   0,   0],   # CB
    [ 0,  0,   0,   0,   1,   0,   1,   1],   # CG
    [ 0,  0,   0,   0,   0,   1,   0,   0],   # CD1
    [ 0,  0,   0,   0,   0,   1,   0,   0],   # CD2
]
I_bonds = [
    #N   CA    C    O   CB  CG1  CG2  CD1
    [ 0,  1,   0,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   1,   0],   # CB
    [ 0,  0,   0,   0,   1,   0,   0,   1],   # CG1
    [ 0,  0,   0,   0,   1,   0,   0,   0],   # CG2
    [ 0,  0,   0,   0,   0,   1,   0,   0],   # CD1
]
F_bonds = [
    #N   CA    C    O   CB   CG  CD1  CD2  CE1  CE2   CZ
    [ 0,  1,   0,   0,   0,   0,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0,   0,   0,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0,   0,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   0,   0,   0,   0,   0],   # CB
    [ 0,  0,   0,   0,   1,   0,   1,   1,   0,   0,   0],   # CG
    [ 0,  0,   0,   0,   0,   1,   0,   0,   1,   0,   0],   # CD1
    [ 0,  0,   0,   0,   0,   1,   0,   0,   0,   1,   0],   # CD2
    [ 0,  0,   0,   0,   0,   0,   1,   0,   0,   0,   1],   # CE1
    [ 0,  0,   0,   0,   0,   0,   0,   1,   0,   0,   1],   # CE2
    [ 0,  0,   0,   0,   0,   0,   0,   0,   1,   1,   0],   # CZ
]
Y_bonds = [
    #N   CA    C    O   CB   CG  CD1  CD2  CE1  CE2   CZ   OH
    [ 0,  1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0,   0,   0,   0,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0],   # CB
    [ 0,  0,   0,   0,   1,   0,   1,   1,   0,   0,   0,   0],   # CG
    [ 0,  0,   0,   0,   0,   1,   0,   0,   1,   0,   0,   0],   # CD1
    [ 0,  0,   0,   0,   0,   1,   0,   0,   0,   1,   0,   0],   # CD2
    [ 0,  0,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],   # CE1
    [ 0,  0,   0,   0,   0,   0,   0,   1,   0,   0,   1,   0],   # CE2
    [ 0,  0,   0,   0,   0,   0,   0,   0,   1,   1,   0,   1],   # CZ
    [ 0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0],   # OH
]
W_bonds = [
    #N   CA    C    O   CB   CG  CD1  CD2  NE1  CE2  CE3  CZ2  CZ3  CH2
    [ 0,  1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0],   # CB
    [ 0,  0,   0,   0,   1,   0,   1,   1,   0,   0,   0,   0,   0,   0],   # CG
    [ 0,  0,   0,   0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   0],   # CD1
    [ 0,  0,   0,   0,   0,   1,   0,   0,   0,   1,   1,   0,   0,   0],   # CD2
    [ 0,  0,   0,   0,   0,   0,   1,   0,   0,   1,   0,   0,   0,   0],   # NE1
    [ 0,  0,   0,   0,   0,   0,   0,   1,   1,   0,   0,   1,   0,   0],   # CE2
    [ 0,  0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0],   # CE3
    [ 0,  0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   1],   # CZ2
    [ 0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   1],   # CZ3
    [ 0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   1,   0],   # CH2
]
H_bonds = [
    #N   CA    C    O   CB   CG  ND1  CD2  CE1  NE2
    [ 0,  1,   0,   0,   0,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0,   0,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   0,   0,   0,   0],   # CB
    [ 0,  0,   0,   0,   1,   0,   1,   1,   0,   0],   # CG
    [ 0,  0,   0,   0,   0,   1,   0,   0,   1,   0],   # ND1
    [ 0,  0,   0,   0,   0,   1,   0,   0,   0,   1],   # CD2
    [ 0,  0,   0,   0,   0,   0,   1,   0,   0,   1],   # CE1
    [ 0,  0,   0,   0,   0,   0,   0,   1,   1,   0],   # NE2
]
K_bonds = [
    #N   CA    C    O   CB   CG   CD   CE   NZ
    [ 0,  1,   0,   0,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   0,   0,   0],   # CB
    [ 0,  0,   0,   0,   1,   0,   1,   0,   0],   # CG
    [ 0,  0,   0,   0,   0,   1,   0,   1,   0],   # CD
    [ 0,  0,   0,   0,   0,   0,   1,   0,   1],   # CE
    [ 0,  0,   0,   0,   0,   0,   0,   1,   0],   # NZ
]
R_bonds = [
    #N   CA    C    O   CB   CG   CD   NE   CZ  NH1  NH2
    [ 0,  1,   0,   0,   0,   0,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0,   0,   0,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0,   0,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   0,   0,   0,   0,   0],   # CB
    [ 0,  0,   0,   0,   1,   0,   1,   0,   0,   0,   0],   # CG
    [ 0,  0,   0,   0,   0,   1,   0,   1,   0,   0,   0],   # CD
    [ 0,  0,   0,   0,   0,   0,   1,   0,   1,   0,   0],   # NE
    [ 0,  0,   0,   0,   0,   0,   0,   1,   0,   1,   1],   # CZ
    [ 0,  0,   0,   0,   0,   0,   0,   0,   1,   0,   0],   # NH1
    [ 0,  0,   0,   0,   0,   0,   0,   0,   1,   0,   0],   # NH2
]
D_bonds = [
    #N   CA    C    O   CB   CG  OD1  OD2
    [ 0,  1,   0,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   0,   0],   # CB
    [ 0,  0,   0,   0,   1,   0,   1,   1],   # CG
    [ 0,  0,   0,   0,   0,   1,   0,   0],   # OD1
    [ 0,  0,   0,   0,   0,   1,   0,   0],   # OD2
]
E_bonds = [
    #N   CA    C    O   CB   CG   CD  OE1  OE2
    [ 0,  1,   0,   0,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   0,   0,   0],   # CB
    [ 0,  0,   0,   0,   1,   0,   1,   0,   0],   # CG
    [ 0,  0,   0,   0,   0,   1,   0,   1,   1],   # CD
    [ 0,  0,   0,   0,   0,   0,   1,   0,   0],   # OE1
    [ 0,  0,   0,   0,   0,   0,   1,   0,   0],   # OE2
]
N_bonds = [
    #N   CA    C    O   CB   CG  OD1  ND2
    [ 0,  1,   0,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   0,   0],   # CB
    [ 0,  0,   0,   0,   1,   0,   1,   1],   # CG
    [ 0,  0,   0,   0,   0,   1,   0,   0],   # OD1
    [ 0,  0,   0,   0,   0,   1,   0,   0],   # ND2
]
Q_bonds = [
    #N   CA    C    O   CB   CG   CD  OE1  NE2
    [ 0,  1,   0,   0,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   0,   0,   0],   # CB
    [ 0,  0,   0,   0,   1,   0,   1,   0,   0],   # CG
    [ 0,  0,   0,   0,   0,   1,   0,   1,   1],   # CD
    [ 0,  0,   0,   0,   0,   0,   1,   0,   0],   # OE1
    [ 0,  0,   0,   0,   0,   0,   1,   0,   0],   # NE2
]
T_bonds = [
    #N   CA    C    O   CB  OG1  CG2
    [ 0,  1,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   1],   # CB
    [ 0,  0,   0,   0,   1,   0,   0],   # OG1
    [ 0,  0,   0,   0,   1,   0,   0],   # CG2
]
S_bonds = [
    #N   CA    C    O   CB   OG
    [ 0,  1,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0],   # CA
    [ 0,  1,   0,   1,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1],   # CB
    [ 0,  0,   0,   0,   1,   0],   # OG
]
C_bonds = [
    #N   CA    C    O   CB   SG
    [ 0,  1,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0],   # CA
    [ 0,  1,   0,   1,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1],   # CB
    [ 0,  0,   0,   0,   1,   0],   # SG
]
M_bonds = [
    #N   CA    C    O   CB   CG   SD   CE
    [ 0,  1,   0,   0,   0,   0,   0,   0],   # N
    [ 1,  0,   1,   0,   1,   0,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   0,   0],   # CB
    [ 0,  0,   0,   0,   1,   0,   1,   0],   # CG
    [ 0,  0,   0,   0,   0,   1,   0,   1],   # SD
    [ 0,  0,   0,   0,   0,   0,   1,   0],   # CE
]
P_bonds = [
    #N   CA    C    O   CB   CG   CD
    [ 0,  1,   0,   0,   0,   0,   1],   # N 
    [ 1,  0,   1,   0,   1,   0,   0],   # CA
    [ 0,  1,   0,   1,   0,   0,   0],   # C
    [ 0,  0,   1,   0,   0,   0,   0],   # O
    [ 0,  1,   0,   0,   0,   1,   0],   # CB
    [ 0,  0,   0,   0,   1,   0,   1],   # CG
    [ 1,  0,   0,   0,   0,   1,   0],   # CD
]

aminoacid_BONDS = CapitalInsensitiveDict({
    'G': G_bonds, 'A': A_bonds, 'V': V_bonds, 'L': L_bonds,
    'I': I_bonds, 'F': F_bonds, 'Y': Y_bonds, 'W': W_bonds,
    'H': H_bonds, 'K': K_bonds, 'R': R_bonds, 'D': D_bonds,
    'E': E_bonds, 'N': N_bonds, 'Q': Q_bonds, 'T': T_bonds,
    'S': S_bonds, 'C': C_bonds, 'M': M_bonds, 'P': P_bonds,
})

""" 
ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ
Ξ nucleotide_DICTS Ξ
ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ
"""

DNA_bases = ['DA','DG','DT','DC']
RNA_bases = ['A','G','U','C']
nucleotide_DICT = CapitalInsensitiveDict(
{
'DA': 'DA',  'DEOXYADENOSINE': 'DA',   
'A':   'A',  'ADENOSINE':       'A',   
'DG': 'DG',  'DEOXYGUANOSINE': 'DG',   
'G':   'G',  'GUANOSINE':       'G',   
'DT': 'DT',  'DEOXYTHYMIDINE': 'DT',  # 'T': 'DT', 
'U':   'U',  'URACIL':          'U',   
'DC': 'DC',  'DEOXYCYTIDINE':  'DC',   
'C':   'C',  'CYTIDINE':        'C',   

})

nucleotide_ATOMLABELS_DICT = CapitalInsensitiveDict({
    'A': ["P", "OP1", "OP2", "O5'", "C5'", "C4'", "O4'", "C3'", "O3'", "C2'", "O2'", "C1'",   # P-sugar
           "N9", "C8", "N7", "C5", "C4", "N3", "C2", "N1", "C6", "N6"],                       # adenine base

    'C': ["P", "OP1", "OP2", "O5'", "C5'", "C4'", "O4'", "C3'", "O3'", "C2'", "O2'", "C1'",   # P-sugar
           "N1", "C2", "O2", "N3", "C4", "N4", "C5", "C6"],                                   # cytosine base

    'G': ["P", "OP1", "OP2", "O5'", "C5'", "C4'", "O4'", "C3'", "O3'", "C2'", "O2'", "C1'",   # P-sugar
           "N9", "C8", "N7", "C5", "C4", "N3", "C2", "N2", "N1", "C6", "O6"],                 # guanine base

    'U': ["P", "OP1", "OP2", "O5'", "C5'", "C4'", "O4'", "C3'", "O3'", "C2'", "O2'", "C1'",   # P-sugar
           "N1", "C2", "O2", "N3", "C4", "O4", "C5", "C6"],                                   # uracil base

    'DA': ["P", "OP1", "OP2", "O5'", "C5'", "C4'", "O4'", "C3'", "O3'", "C2'", "C1'",         # P-sugar
           "N9", "C8", "N7", "C5", "C4", "N3", "C2", "N1", "C6", "N6"],                       # adenine base

    'DC': ["P", "OP1", "OP2", "O5'", "C5'", "C4'", "O4'", "C3'", "O3'", "C2'", "C1'",         # P-sugar
           "N1", "C2", "O2", "N3", "C4", "N4", "C5", "C6"],                                   # cytosine base

    'DG': ["P", "OP1", "OP2", "O5'", "C5'", "C4'", "O4'", "C3'", "O3'", "C2'", "C1'",         # P-sugar
           "N9", "C8", "N7", "C5", "C4", "N3", "C2", "N2", "N1", "C6", "O6"],                 # guanine base

    'DT': ["P", "OP1", "OP2", "O5'", "C5'", "C4'", "O4'", "C3'", "O3'", "C2'", "C1'",         # P-sugar
           "N1", "C2", "O2", "N3", "C4", "O4", "C5", "C7", "C6"],                             # thymine base
})

nucleotide_SP2_DICT = CapitalInsensitiveDict({ 
    'A':  ["N9", "C8", "N7", "C5", "C4", "N3", "C2", "N1", "C6", "N6"],
    'G':  ["N9", "C8", "N7", "C5", "C4", "N3", "C2", "N2", "N1", "C6", "O6"],     
    'U':  ["N1", "C2", "O2", "N3", "C4", "O4", "C5", "C6"],
    'C':  ["N1", "C2", "O2", "N3", "C4", "N4", "C5", "C6"],                  
    'DA': ["N9", "C8", "N7", "C5", "C4", "N3", "C2", "N1", "C6", "N6"],      
    'DG': ["N9", "C8", "N7", "C5", "C4", "N3", "C2", "N2", "N1", "C6", "O6"],
    'DT': ["N1", "C2", "O2", "N3", "C4", "O4", "C5", "C6"], 
    'DC': ["N1", "C2", "O2", "N3", "C4", "N4", "C5", "C6"],                              
})
nucleotide_HDONORS_DICT = CapitalInsensitiveDict({
    'A':  ["O2'","N6"],                 
    'G':  ["O2'","N2", "N1"],      
    'U':  ["O2'","N3"],  
    'C':  ["O2'","N4"],   
    'DA': ["N6"],               
    'DG': ["N2", "N1"],
    'DT': ["N3"],    
    'DC': ["N4"],  
                          
})
nucleotide_HACCEPTORS_DICT = CapitalInsensitiveDict({
    'A': ["OP1", "OP2", "O5'","O4'","O3'","O2'",   
          "N7","N3", "N1"],                 
    'G': ["OP1", "OP2", "O5'","O4'","O3'","O2'",
          "N7","N3","O6"],                                   
    'U': ["OP1", "OP2", "O5'","O4'","O3'","O2'",
          "O2","O4"], 
    'C': ["OP1", "OP2", "O5'","O4'","O3'","O2'",   
          "O2", "N3"],  
    'DA': ["OP1", "OP2", "O5'","O4'","O3'",   
           "N7","N3", "N1"],          
    'DG': ["OP1", "OP2", "O5'","O4'","O3'",
           "N7","N3","O6"],                                          
    'DT': ["OP1", "OP2", "O5'","O4'","O3'",
           "O2","O4"], 
    'DC': ["OP1", "OP2", "O5'","O4'","O3'",   
           "O2", "N3"],                    
})
# O1P, O2P and O3P can have negative charge
nucleotide_NEGATIVEC_DICT = CapitalInsensitiveDict({
    'A':  ["OP1", "OP2", "OP3"],                 
    'G':  ["OP1", "OP2", "OP3"],                                   
    'U':  ["OP1", "OP2", "OP3"],
    'C':  ["OP1", "OP2", "OP3"],  
    'DA': ["OP1", "OP2", "OP3"],         
    'DG': ["OP1", "OP2", "OP3"],                                          
    'DT': ["OP1", "OP2", "OP3"],
    'DC': ["OP1", "OP2", "OP3"],                   
})
""" 
ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ
Ξ miscellaneous Ξ
ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ
"""
codon_OUTUTS = list("GAVLIFYWHKRDENQSTCMP*")
RNA_CODONS_DICT = CapitalInsensitiveDict(
{'UUU': 'F', 'UCU': 'S','UAU': 'Y','UGU': 'C',
 'UUC': 'F', 'UCC': 'S','UAC': 'Y','UGC': 'C',
 'UUA': 'L', 'UCA': 'S','UAA': '*','UGA': '*',
 'UUG': 'L', 'UCG': 'S','UAG': '*','UGG': 'W',
 
 'CUU': 'L', 'CCU': 'P','CAU': 'H','CGU': 'R',
 'CUC': 'L', 'CCC': 'P','CAC': 'H','CGC': 'R',
 'CUA': 'L', 'CCA': 'P','CAA': 'Q','CGA': 'R',
 'CUG': 'L', 'CCG': 'P','CAG': 'Q','CGG': 'R',
 
 'AUU': 'I', 'ACU': 'T','AAU': 'N','AGU': 'S',
 'AUC': 'I', 'ACC': 'T','AAC': 'N','AGC': 'S',
 'AUA': 'I', 'ACA': 'T','AAA': 'K','AGA': 'R',
 'AUG': 'M', 'ACG': 'T','AAG': 'K','AGG': 'R',
 
 'GUU': 'V', 'GCU': 'A','GAU': 'D','GGU': 'G',
 'GUC': 'V', 'GCC': 'A','GAC': 'D','GGC': 'G',
 'GUA': 'V', 'GCA': 'A','GAA': 'E','GGA': 'G',
 'GUG': 'V', 'GCG': 'A','GAG': 'E','GGG': 'G',})
aminoacid_TO_CODONS = CapitalInsensitiveDict({
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'I': ['AUU', 'AUC', 'AUA'],
    'F': ['UUU', 'UUC'],
    'Y': ['UAU', 'UAC'],
    'W': ['UGG'],
    'H': ['CAU', 'CAC'],
    'K': ['AAA', 'AAG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'D': ['GAU', 'GAC'],
    'E': ['GAA', 'GAG'],
    'N': ['AAU', 'AAC'],
    'Q': ['CAA', 'CAG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'C': ['UGU', 'UGC'],
    'M': ['AUG'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    '*': ['UAA', 'UGA', 'UAG']})
