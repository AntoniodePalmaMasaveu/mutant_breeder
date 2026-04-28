""" 
ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ
Ξ PRINTING FUNTIONS Ξ
ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ
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