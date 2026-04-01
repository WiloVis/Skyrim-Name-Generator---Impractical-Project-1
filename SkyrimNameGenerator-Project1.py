import sys, random

print("Welcome to the Skyrim Name Generator!")

nord_female = (
    "Astrid", "Brynja", "Dagny", "Eir", "Fridrika", "Gerdur", "Hilda", "Ingrid", "Jora", "Katla",
    "Lydia", "Marta", "Nanna", "Olga", "Rikke", "Sigrid", "Tora", "Ulfhild", "Vivienne", "Wulfur",
    "Aela", "Borghild", "Danika", "Elda", "Freydis", "Gisli", "Helga", "Idgrod", "Jordis", "Karla",
    "Lillemor", "Maren", "Nura", "Olfina", "Ragnhild", "Sif", "Thora", "Ulla", "Valga", "Wilhelmina",
    "Aina", "Bera", "Disa", "Erna", "Fjola", "Gunnhild", "Hrefna", "Inga", "Jensine", "Kirsten"
)

nord_male = (
    "Aldar", "Bjorn", "Cnut", "Dagur", "Einar", "Farkas", "Gunnar", "Hakon", "Ivar", "Jarl",
    "Kjeld", "Leif", "Magnus", "Njord", "Olaf", "Ragnar", "Sten", "Torvald", "Ulfric", "Vilkas",
    "Agni", "Baldur", "Calder", "Dengeir", "Eorlund", "Fjori", "Galmar", "Hjalti", "Ingvar", "Jofthor",
    "Kodlak", "Loki", "Mikael", "Njal", "Orm", "Ralof", "Skjor", "Thrym", "Uthgerd", "Valdimar",
    "Alrik", "Borkul", "Dorian", "Erik", "Frothar", "Gorm", "Hroar", "Idolaf", "Joric", "Kjotve"
)

nord_unisex = (
    "Ari", "Bjarni", "Delling", "Eirik", "Fenrir", "Grim", "Haki", "Ingolf", "Jormun", "Kari",
    "Lothar", "Mimir", "Njal", "Odin", "Runa", "Sigrun", "Tyr", "Ulf", "Vidar", "Yngvar",
    "Alvis", "Bodil", "Dag", "Eldrid", "Frode", "Gunn", "Havard", "Inger", "Jorunn", "Knut",
    "Liv", "Magne", "Nott", "Odd", "Ragni", "Saga", "Tor", "Urd", "Vali", "Yrsa",
    "Asger", "Birna", "Dyre", "Edda", "Frida", "Gyda", "Hild", "Idunn", "Jarl", "Kol"
)

nord_last = (
    "Battleborn", "Bearclaw", "Coldstone", "Deepwood", "EagleEye", "Frostbeard", "GrayMane", "HeartHoarder", "Ironhand", "JadeFang",
    "Kingslayer", "Longhammer", "MistWalker", "NorthWind", "OakenShield", "ProudMane", "QuickArrow", "RedBeard", "StoneFist", "ThunderFist",
    "Unbroken", "Viking", "Winterborn", "WolfSister", "Ysmir", "Blackthorne", "CopperHand", "Dragonslayer", "EmberFist", "FrostWind",
    "GoldHilt", "Hammerfall", "IceVein", "Jotun", "KeenEye", "Lionheart", "MoonBlade", "NightSinger", "Oakenshield", "PlainsWalker",
    "Quicksilver", "RavenHair", "SilverBlood", "TrueHeart", "Ulfson", "VoidWalker", "Wulf", "Xar", "Ymir", "Zealot"
)

imperial_female = (
    "Alessia", "Bianca", "Cordelia", "Domitia", "Elena", "Fabia", "Gallia", "Horatia", "Italia", "Julia",
    "Katerina", "Livia", "Marcia", "Nadia", "Octavia", "Portia", "Quintia", "Romana", "Sabina", "Tullia",
    "Valeria", "Vittoria", "Aquila", "Bellona", "Camilla", "Diana", "Flavia", "Gemina", "Helena", "Isabella",
    "Justina", "Lucia", "Minerva", "Nerina", "Olivia", "Paula", "Ravenna", "Silvia", "Teresa", "Ursula",
    "Veronica", "Aelia", "Basilia", "Crispa", "Drusilla", "Emilia", "Fausta", "Gratia", "Honoria", "Iulia"
)

imperial_male = (
    "Aurelius", "Brutus", "Cassius", "Decimus", "Emilian", "Fabius", "Gaius", "Horatius", "Ignatius", "Julius",
    "Krassus", "Lucius", "Marcus", "Nero", "Octavius", "Paulus", "Quintus", "Roman", "Septimus", "Tiberius",
    "Valerius", "Victor", "Aelius", "Benedict", "Caius", "Davian", "Ettore", "Flavian", "Germanicus", "Hadrian",
    "Iacobus", "Justus", "Lorenzo", "Marius", "Nicolas", "Ovid", "Petronius", "Rufus", "Servius", "Titus",
    "Ulpius", "Vibius", "Antonius", "Bassus", "Cato", "Drusus", "Eugenius", "Faustus", "Gratian", "Horatio"
)

imperial_unisex = (
    "Aurel", "Blaise", "Cael", "Domi", "Eli", "Flo", "Gale", "Hilary", "Ivo", "Jovi",
    "Kai", "Lux", "Milo", "Nova", "Ori", "Pax", "Quinn", "Remy", "Sage", "Tavi",
    "Unity", "Vale", "Wren", "Xen", "Yuri", "Zeno", "Aura", "Bell", "Cris", "Drew",
    "Echo", "Finn", "Grey", "Haven", "Indigo", "Jade", "Kael", "Len", "Mica", "Nico",
    "Onyx", "Piero", "Rae", "Sol", "Tess", "Ula", "Vero", "Wynn", "Xanthe", "Zia"
)

imperial_last = (
    "Aquilae", "Brutus", "Capitolinus", "Draconis", "Eagle", "Felix", "Gloriosus", "Honoratus", "Imperialis", "Justus",
    "Kaiser", "Laurentius", "Maximus", "Nobilis", "Octavian", "Patrician", "Quintillus", "Romulus", "Severus", "Trajan",
    "Urbanus", "Valerius", "Aquila", "Bellator", "Caesar", "Dominus", "Equitus", "Ferox", "Gratian", "Hadrianus",
    "Invictus", "Julianus", "Kryptos", "Legatus", "Magnus", "Nero", "Optimus", "Pius", "Quirinus", "Rex",
    "Scipio", "Titanus", "Ulpius", "Venator", "Warden", "Xenon", "Yulius", "Zephyr", "Aetius", "Florentius"
)

breton_female = (
    "Adelais", "Beatrice", "Celeste", "Delphine", "Elise", "Florence", "Genevieve", "Helene", "Isabeau", "Josephine",
    "Katherine", "Liliane", "Marguerite", "Nicole", "Odette", "Pascale", "Rosalind", "Simone", "Therese", "Vivienne",
    "Annette", "Brigitte", "Claire", "Danielle", "Elodie", "Fleur", "Gabrielle", "Honorine", "Isobel", "Juliette",
    "Lorraine", "Madeleine", "Noelle", "Odile", "Pauline", "Renee", "Sabine", "Teresa", "Valentine", "Yvette",
    "Aveline", "Blanche", "Colette", "Denise", "Estelle", "Felicity", "Giselle", "Heloise", "Irene", "Jacqueline"
)

breton_male = (
    "Alain", "Benoit", "Claude", "Denis", "Etienne", "Francois", "Gilles", "Henri", "Isidore", "Jacques",
    "Laurent", "Michel", "Nicolas", "Olivier", "Philippe", "Quentin", "Rene", "Sebastien", "Thierry", "Urbain",
    "Andre", "Bernard", "Charles", "Daniel", "Edmond", "Felix", "Gaston", "Hugo", "Ives", "Julien",
    "Luc", "Marcel", "Noel", "Oscar", "Pascal", "Raoul", "Simon", "Tristan", "Vincent", "Yves",
    "Armand", "Bertrand", "Clement", "Didier", "Emile", "Fabien", "Guy", "Honore", "Jean", "Lucien"
)

breton_unisex = (
    "Angel", "Blair", "Camille", "Dominic", "Eden", "Francis", "Gabriel", "Haven", "Ives", "Jules",
    "Kendall", "Laurel", "Morgan", "Noel", "Oriel", "Peyton", "Quinn", "Rene", "Sage", "Tristan",
    "Urie", "Valentine", "Wynn", "Xavier", "Yves", "Zion", "Adrien", "Briar", "Corey", "Dana",
    "Emmett", "Florian", "Grey", "Harper", "Indigo", "Jean", "Kael", "Linden", "Milan", "Nova",
    "Ollie", "Pierce", "Remy", "Sterling", "Tate", "Unique", "Vivian", "Winter", "Xen", "Yael"
)

breton_last = (
    "Beaumont", "Champion", "Delacroix", "Ermine", "Forest", "Guildford", "Hastings", "Ironside", "Jourdain", "Kingswell",
    "Lafayette", "Mornay", "Northwood", "Orleans", "Pendragon", "Rochefort", "Saintclair", "Tremaine", "Vallois", "Windsor",
    "Artois", "Bellerose", "Champagne", "Dumont", "Everard", "Fitzwilliam", "Grayson", "Harcourt", "Inglewood", "Jasper",
    "Kensington", "Langley", "Montclair", "Nightingale", "Oakley", "Pembroke", "Rutherford", "Sutherland", "Thatcher", "Vane",
    "Westbrook", "Ainsworth", "Bradford", "Cavendish", "Davenport", "Ellsworth", "Falkner", "Grenville", "Hawthorne", "Iver"
)

redguard_female = (
    "Ahlam", "Bashira", "Cyrelle", "Deera", "Elhayam", "Fadila", "Gamila", "Hasana", "Iman", "Jasmina",
    "Kamilah", "Layla", "Mariam", "Nadia", "Omani", "Pasha", "Qadira", "Rashida", "Samira", "Tahira",
    "Umm", "Vashara", "Wafiya", "Xenya", "Yasmin", "Zahra", "Aaliyah", "Badiya", "Chandra", "Dalila",
    "Eshana", "Fatima", "Ghaliya", "Halima", "Ibtisam", "Jamila", "Karima", "Latifa", "Malika", "Nailah",
    "Oria", "Pari", "Qamar", "Ranya", "Safiya", "Tala", "Umaima", "Vida", "Warda", "Yara"
)

redguard_male = (
    "Ahmad", "Basir", "Cyrus", "Dari", "Ebrahim", "Fahim", "Ghalib", "Hakim", "Idris", "Jabir",
    "Karim", "Latif", "Malik", "Nadir", "Omar", "Pasha", "Qasim", "Rashid", "Salim", "Tariq",
    "Umar", "Vikar", "Walid", "Xerxes", "Yusuf", "Zayd", "Aziz", "Bashir", "Camil", "Dawud",
    "Emir", "Farid", "Ghazi", "Hussein", "Iskandar", "Jafar", "Khalid", "Lutfi", "Mansur", "Nawaf",
    "Osman", "Qadir", "Rafiq", "Sultan", "Tahir", "Usman", "Wafiq", "Yasin", "Zahir", "Azhar"
)

redguard_unisex = (
    "Akil", "Bilal", "Cairo", "Dunya", "Essa", "Faris", "Gaza", "Hadi", "Iman", "Jali",
    "Kamil", "Lami", "Mazin", "Nuri", "Omani", "Puri", "Qays", "Rami", "Sami", "Tali",
    "Umni", "Veda", "Wasi", "Xian", "Yara", "Zaki", "Adil", "Bahir", "Chase", "Dali",
    "Eli", "Fida", "Gia", "Hana", "Idan", "Jana", "Kali", "Lian", "Mika", "Nima",
    "Ora", "Paz", "Rana", "Saba", "Tala", "Uma", "Vanya", "Wafi", "Yani", "Zia"
)

redguard_last = (
    "Alikr", "Bentus", "Crescent", "Desertwind", "Eclipse", "Falcon", "Golden", "Hawk", "Iron", "Jewel",
    "Knight", "Lion", "Mirage", "Noble", "Oasis", "Proud", "Quicksand", "Rider", "Sandstorm", "Thunder",
    "Uprising", "Viper", "Warrior", "Xen", "Yamani", "Zeal", "Ashanti", "Bakr", "Crimson", "Dune",
    "Elite", "Fierce", "Guild", "Hassan", "Ibn", "Jazira", "Khalil", "Lotus", "Mamluk", "Nadir",
    "Osiris", "Pharaoh", "Qadir", "Rashid", "Sahara", "Taj", "Umar", "Valiant", "Windwalker", "Zahir"
)

darkelf_female = (
    "Alma", "Barenziah", "Cindiri", "Darvame", "Elanwe", "Faryon", "Galdra", "Hlaren", "Ildari", "Jenassa",
    "Karliah", "Lleril", "Mephala", "Naryu", "Oreyn", "Palla", "Ravani", "Seryn", "Teldryn", "Uvani",
    "Veya", "Witchie", "Xelha", "Yagaz", "Zana", "Alandro", "Baeli", "Cerul", "Dalasi", "Elvi",
    "Farena", "Gilyn", "Helviane", "Ilwen", "Julan", "Kireth", "Llarel", "Mithri", "Nelsi", "Olava",
    "Phelan", "Relyn", "Sildra", "Thava", "Ulven", "Veral", "Wendir", "Xilma", "Yvara", "Zalena"
)

darkelf_male = (
    "Adril", "Baren", "Cyrus", "Dren", "Eno", "Favel", "Gavros", "Helseth", "Idras", "Jagar",
    "Kurik", "Llovar", "Morrow", "Neloth", "Ondres", "Pellus", "Reldyn", "Savos", "Tandil", "Ulen",
    "Varen", "Wulff", "Xander", "Yash", "Zainab", "Aren", "Bolu", "Codus", "Dath", "Eris",
    "Falyn", "Gothren", "Hlaren", "Ilnor", "Jorik", "Kodyn", "Llarar", "Malyn", "Nalyn", "Othren",
    "Palon", "Ralas", "Sedryn", "Torik", "Ulyn", "Velan", "Welyn", "Xenon", "Yakin", "Zaroth"
)

darkelf_unisex = (
    "Aren", "Bael", "Cael", "Dres", "Eris", "Faryn", "Galen", "Hlan", "Ilen", "Julan",
    "Kael", "Llan", "Maren", "Nael", "Oryn", "Pael", "Rael", "Sera", "Tel", "Ulen",
    "Vael", "Wren", "Xel", "Yan", "Zal", "Ara", "Bera", "Ceryn", "Dara", "Elyn",
    "Fera", "Gera", "Hera", "Ira", "Jara", "Kera", "Lira", "Mera", "Nera", "Ora",
    "Pera", "Rael", "Sera", "Tera", "Ura", "Vera", "Wera", "Xera", "Yera", "Zera"
)

darkelf_last = (
    "Andrano", "Berne", "Cantus", "Dagoth", "Elder", "Falos", "Gratian", "Hlaalu", "Indoril", "Julianos",
    "Kinsman", "Llarar", "Morrowind", "Nerevar", "Othren", "Pell", "Quarra", "Redoran", "Sarethi", "Telvanni",
    "Uvirith", "Veloth", "Worm", "Xil", "Yng", "Zainab", "Ahemmusa", "Bael", "Cul", "Dres",
    "Erabenimsun", "Fyr", "Gorak", "Helseth", "Ieneth", "Jor", "Kaushad", "Llor", "Molag", "Nay",
    "Othrelas", "Pensalis", "Quarn", "Rels", "Sul", "Tharn", "Ur", "Vvarden", "Wasten", "Zain"
)

highelf_female = (
    "Alara", "Brianna", "Celedriel", "Delyna", "Elara", "Faelivrin", "Gloriel", "Heliana", "Ithilwen", "Jade",
    "Kalara", "Laraliel", "Meriath", "Nimriel", "Orianna", "Paloma", "Quenya", "Riel", "Siliana", "Talara",
    "Ulmira", "Vaelia", "Wynne", "Xandra", "Yavanna", "Zariel", "Aelindra", "Belara", "Caelia", "Delara",
    "Eleniel", "Faelara", "Galara", "Halara", "Ileara", "Jalara", "Kaliel", "Lara", "Malara", "Nalara",
    "Orelia", "Pelara", "Qaela", "Raela", "Saelia", "Telara", "Urelia", "Velara", "Welara", "Yelara"
)

highelf_male = (
    "Aelar", "Belthas", "Calendil", "Daran", "Eltar", "Falor", "Gildor", "Halendir", "Ithil", "Jorund",
    "Kalendor", "Lorias", "Malorn", "Neldor", "Orophin", "Pelandor", "Quildor", "Rumil", "Sildor", "Talendir",
    "Uldor", "Valandil", "Weland", "Xendor", "Yavon", "Zelindor", "Aran", "Belendor", "Caran", "Dolion",
    "Eldar", "Fingon", "Galion", "Haldor", "Inglor", "Jelendor", "Kelendor", "Lorien", "Malon", "Nandor",
    "Orodreth", "Pelendur", "Quen", "Roland", "Sindar", "Telion", "Umbriel", "Vanyar", "Wendel", "Yavion"
)

highelf_unisex = (
    "Ael", "Bel", "Cal", "Dal", "El", "Fel", "Gal", "Hal", "Il", "Jal",
    "Kal", "Lal", "Mal", "Nal", "Ol", "Pal", "Qel", "Ral", "Sal", "Tal",
    "Ull", "Val", "Wal", "Xal", "Yal", "Zal", "Ari", "Bri", "Cael", "Dael",
    "Eri", "Fael", "Gael", "Hael", "Iri", "Jael", "Kael", "Lael", "Mael", "Nael",
    "Oriel", "Pael", "Quel", "Rael", "Sael", "Tael", "Uriel", "Vael", "Wael", "Yael"
)

highelf_last = (
    "Alinor", "Bright", "Crystal", "Dawn", "Elden", "Firstborn", "Golden", "High", "Iliac", "Jewel",
    "Kings", "Luminance", "Mer", "Noble", "Oracle", "Prism", "Queen", "Radiance", "Sun", "Thalmor",
    "Uplands", "Valor", "White", "Xan", "Yew", "Zephyr", "Aether", "Beryl", "Crown", "Divine",
    "Evergreen", "Falmer", "Grace", "Heaven", "Iris", "Justice", "Kindle", "Light", "Moon", "North",
    "Opal", "Pearl", "Quell", "Rose", "Star", "Tempest", "Unity", "Virtue", "Willow", "Xenon"
)

woodelf_female = (
    "Aeriel", "Briar", "Cedar", "Dew", "Elara", "Fern", "Glimmer", "Hazel", "Ivy", "Juniper",
    "Kestrel", "Lark", "Moss", "Nettle", "Olive", "Petal", "Quill", "Raven", "Sage", "Thistle",
    "Ula", "Vine", "Willow", "Xara", "Yarrow", "Zinnia", "Acorn", "Berry", "Clover", "Daisy",
    "Ember", "Fauna", "Grove", "Holly", "Iris", "Jasmine", "Katniss", "Laurel", "Maple", "Nut",
    "Orchid", "Primrose", "Quince", "Rose", "Sorrel", "Tansy", "Ursa", "Violet", "Wren", "Yew"
)

woodelf_male = (
    "Alder", "Birch", "Cypress", "Drake", "Elder", "Falcon", "Garth", "Hawthorn", "Ilex", "Jasper",
    "Kael", "Linden", "Marl", "Nash", "Oak", "Pine", "Quill", "Rook", "Spruce", "Thorn",
    "Ulf", "Valen", "Wolf", "Xen", "Yew", "Zephyr", "Ash", "Bracken", "Cedar", "Dune",
    "Elm", "Fen", "Glen", "Heath", "Ivor", "Jarrah", "Kade", "Larch", "Moss", "Niall",
    "Oren", "Peregrine", "Ridge", "Sylvan", "Talon", "Umber", "Vale", "Wren", "Yarrow", "Zale"
)

woodelf_unisex = (
    "Aspen", "Briar", "Cedar", "Dale", "Eld", "Fern", "Gale", "Hawke", "Ilex", "Jade",
    "Kestrel", "Lynx", "Moss", "Nettle", "Osprey", "Pine", "Quail", "Raven", "Sparrow", "Thorn",
    "Umber", "Vale", "Wren", "Xen", "Yarrow", "Zephyr", "Alder", "Birch", "Cypress", "Drift",
    "Ember", "Flint", "Grove", "Heath", "Ivy", "Juniper", "Kelp", "Lark", "Mist", "Nova",
    "Orion", "Petal", "Quill", "Ridge", "Sage", "Tern", "Ula", "Vine", "Willow", "Yew"
)

woodelf_last = (
    "Blackbriar", "Creek", "Deepforest", "Evergreen", "Fallow", "Greenwood", "Hawthorn", "Ivy", "Juniper", "Kestrel",
    "Leaffall", "Moss", "Nightshade", "Oakenshield", "Pine", "Quickwood", "Root", "Shadowglen", "Thornwood", "Underleaf",
    "Vine", "Willow", "Xylos", "Yew", "Zenith", "Ashwood", "Birchwood", "Cedarwood", "Dawnwood", "Elmwood",
    "Fernwood", "Glenwood", "Hazelwood", "Ironwood", "Jasperwood", "Kingswood", "Lindenwood", "Maplewood", "Northwood", "Oakwood",
    "Pinewood", "Quailwood", "Redwood", "Sprucewood", "Thistlewood", "Upland", "Valewood", "Wrenwood", "Xenwood", "Yarrowwood"
)

orc_female = (
    "Agronak", "Borgakh", "Cael", "Dular", "Ebra", "Falla", "Ghorza", "Horna", "Ilsa", "Jorla",
    "Kashya", "Lash", "Mazoga", "Nagrub", "Olur", "Pogash", "Qora", "Rugdumph", "Shuftharz", "Tog",
    "Ugor", "Vong", "Wog", "Xar", "Yag", "Zag", "Arob", "Bar", "Corg", "Durz",
    "Erg", "Fur", "Gar", "Hor", "Irb", "Jurg", "Kor", "Lur", "Mor", "Nur",
    "Orbul", "Porg", "Qur", "Rar", "Sor", "Tur", "Urak", "Var", "Wur", "Yor"
)

orc_male = (
    "Bolar", "Crom", "Durzog", "Eruz", "Fargoth", "Gat", "Hag", "Igor", "Jorund", "Karg",
    "Largash", "Mog", "Narzul", "Olug", "Porg", "Qar", "Rog", "Shag", "Tor", "Urz",
    "Vrag", "Wulf", "Xar", "Yag", "Zarg", "Azog", "Borg", "Crag", "Durg", "Esh",
    "Frag", "Grom", "Horg", "Ish", "Jarg", "Krog", "Lorg", "Morg", "Narg", "Orc",
    "Parg", "Qrog", "Rog", "Skarg", "Thrag", "Urag", "Vorg", "Warg", "Yorg", "Zog"
)

orc_unisex = (
    "Ash", "Bog", "Crag", "Dust", "Ember", "Flint", "Gore", "Horn", "Iron", "Jaw",
    "Krag", "Lug", "Mud", "Nog", "Ore", "Pit", "Quake", "Rock", "Stone", "Tusk",
    "Urn", "Vulcan", "Wreck", "Xen", "Yard", "Zug", "Axe", "Blade", "Claw", "Drill",
    "Edge", "Fang", "Grit", "Hammer", "Ice", "Jolt", "Kill", "Lash", "Mace", "Nail",
    "Oath", "Pike", "Quell", "Rage", "Spike", "Tear", "Ulf", "Venge", "Wrath", "Zeal"
)

orc_last = (
    "Bloodfist", "Crusher", "Darkfang", "Earthrender", "Foehammer", "Goretusk", "Heartripper", "Ironjaw", "Jawbreaker", "Killgore",
    "Limbcrusher", "Marrowdrinker", "Nightblade", "Oathkeeper", "Painbringer", "Quakefist", "Rageclaw", "Skullsplitter", "Thunderfist", "Undertaker",
    "Venomspike", "Warlord", "Xenokiller", "Yell", "Zealot", "Ashrender", "Bonecrusher", "Coldblood", "Doomhammer", "Earthshaker",
    "Firefang", "Grimskull", "Hatebringer", "Ironfist", "Juggernaut", "Kinslayer", "Lifetaker", "Mountaincrusher", "Nightslayer", "Oathbreaker",
    "Painkiller", "Quarry", "Ruin", "Stormfist", "Trollbane", "Ulfgar", "Vengeance", "Winterscar", "Xar", "Ymir"
)

khajiit_female = (
    "Ahjara", "Bisha", "Caska", "Darja", "Eshara", "Fahja", "Gasha", "Hajah", "Ishja", "Jasha",
    "Kashja", "Lashja", "Mashja", "Nashja", "Oshja", "Pashja", "Qashja", "Rashja", "Sashja", "Tashja",
    "Ushja", "Vashja", "Washja", "Xashja", "Yashja", "Zashja", "Ahnja", "Bahnja", "Cahnja", "Dahnja",
    "Ehnja", "Fahnja", "Gahnja", "Hahnja", "Ihnja", "Jahnja", "Kahnja", "Lahnja", "Mahnja", "Nahnja",
    "Ohnja", "Pahnja", "Qahnja", "Rahnja", "Sahnja", "Tahnja", "Uhnja", "Vahnja", "Wahnja", "Xahnja"
)

khajiit_male = (
    "Ahjir", "Bishir", "Caskir", "Darir", "Eshir", "Fahir", "Gashir", "Hajir", "Ishir", "Jashir",
    "Kashir", "Lashir", "Mashir", "Nashir", "Oshir", "Pashir", "Qashir", "Rashir", "Sashir", "Tashir",
    "Ushir", "Vashir", "Washir", "Xashir", "Yashir", "Zashir", "Ahnir", "Bahnir", "Cahnir", "Dahnir",
    "Ehnir", "Fahnir", "Gahnir", "Hahnir", "Ihnir", "Jahnir", "Kahnir", "Lahnir", "Mahnir", "Nahnir",
    "Ohnir", "Pahnir", "Qahnir", "Rahnir", "Sahnir", "Tahnir", "Uhnir", "Vahnir", "Wahnir", "Xahnir"
)

khajiit_unisex = (
    "Ahj", "Bah", "Cah", "Dah", "Esh", "Fah", "Gah", "Haj", "Ish", "Jah",
    "Kah", "Lah", "Mah", "Nah", "Osh", "Pah", "Qah", "Rah", "Sah", "Tah",
    "Ush", "Vah", "Wah", "Xah", "Yah", "Zah", "Ahn", "Bahn", "Cahn", "Dahn",
    "Ehn", "Fahn", "Gahn", "Hahn", "Ihn", "Jahn", "Kahn", "Lahn", "Mahn", "Nahn",
    "Ohn", "Pahn", "Qahn", "Rahn", "Sahn", "Tahn", "Uhn", "Vahn", "Wahn", "Xahn"
)

khajiit_last = (
    "Claw", "Dusk", "Eyes", "Fur", "Grin", "Hiss", "Jade", "Kiss", "Leap", "Moon",
    "Night", "Paw", "Quick", "Razor", "Shadow", "Tail", "Under", "Void", "Whisker", "Xen",
    "Yowl", "Zephyr", "Bright", "Crescent", "Dark", "Ember", "Fang", "Glow", "Howl", "Ice",
    "Jinx", "Keen", "Light", "Mist", "Nest", "Onyx", "Prism", "Quiet", "Rune", "Star",
    "Thief", "Umbra", "Veil", "Wind", "Xar", "Yin", "Zen", "Ash", "Bane", "Cinder"
)

argonian_female = (
    "Aneesei", "Baneesi", "Coneesi", "Daneesi", "Eneesi", "Faneesi", "Ganeesi", "Haneesi", "Ineesi", "Janeesi",
    "Kaneesi", "Laneesi", "Maneesi", "Naneesi", "Oneesi", "Paneesi", "Qaneesi", "Raneesi", "Saneesi", "Taneesi",
    "Uneesi", "Vaneesi", "Waneesi", "Xaneesi", "Yaneesi", "Zaneesi", "Aneesha", "Baneesha", "Coneesha", "Daneesha",
    "Eneesha", "Faneesha", "Ganeesha", "Haneesha", "Ineesha", "Janeesha", "Kaneesha", "Laneesha", "Maneesha", "Naneesha",
    "Oneesha", "Paneesha", "Qaneesha", "Raneesha", "Saneesha", "Taneesha", "Uneesha", "Vaneesha", "Waneesha", "Xaneesha"
)

argonian_male = (
    "Aneese", "Baneese", "Coneese", "Daneese", "Eneese", "Faneese", "Ganeese", "Haneese", "Ineese", "Janeese",
    "Kaneese", "Laneese", "Maneese", "Naneese", "Oneese", "Paneese", "Qaneese", "Raneese", "Saneese", "Taneese",
    "Uneese", "Vaneese", "Waneese", "Xaneese", "Yaneese", "Zaneese", "Aneesh", "Baneesh", "Coneesh", "Daneesh",
    "Eneesh", "Faneesh", "Ganeesh", "Haneesh", "Ineesh", "Janeesh", "Kaneesh", "Laneesh", "Maneesh", "Naneesh",
    "Oneesh", "Paneesh", "Qaneesh", "Raneesh", "Saneesh", "Taneesh", "Uneesh", "Vaneesh", "Waneesh", "Xaneesh"
)

argonian_unisex = (
    "Ane", "Bane", "Cone", "Dane", "Ene", "Fane", "Gane", "Hane", "Ine", "Jane",
    "Kane", "Lane", "Mane", "Nane", "One", "Pane", "Qane", "Rane", "Sane", "Tane",
    "Une", "Vane", "Wane", "Xane", "Yane", "Zane", "Aesh", "Baesh", "Caesh", "Daesh",
    "Eesh", "Faesh", "Gaesh", "Haesh", "Iaesh", "Jaesh", "Kaesh", "Laesh", "Maesh", "Naesh",
    "Oaesh", "Paesh", "Qaesh", "Raesh", "Saesh", "Taesh", "Uaesh", "Vaesh", "Waesh", "Xaesh"
)

argonian_last = (
    "Blackscale", "Deep", "Fins", "Gill", "Hist", "Ichor", "Jaws", "Kiss", "Leviathan", "Marsh",
    "Nest", "Ooze", "Pond", "Quicksilver", "River", "Scale", "Tide", "Under", "Venom", "Wet",
    "Xal", "Yolk", "Zara", "Bog", "Creek", "Dew", "Eel", "Frog", "Gator", "Hatch",
    "Ink", "Jelly", "Kelp", "Lizard", "Mire", "Newt", "Oil", "Puddle", "Quag", "Reed",
    "Sludge", "Toad", "Urchin", "Viper", "Water", "Xebec", "Yabby", "Zander", "Brine", "Coral"
)

while True:
    race = int(input("\nPlease choose a race:\n[1] Nord\n[2] Imperial\n[3] Breton\n[4] Redguard\n[5] Dark Elf\n[6] High Elf\n[7] Wood Elf\n[8] Orc\n[9] Khajit\n[10] Argonian\nEnter one of the numbers: "))
    if race not in (1,2,3,4,5,6,7,8,9,10):
        print("\nThat's not one of the numbers! Please start again")
        continue

    gender = input("\nPlease choose a gender:\n[F] Female\n[M] Male\n[U] Unisex\nEnter one of the letters: ")
    if gender not in ('M','N','U'):
        print("\nThat's either not one of the letters or you wrote it in lowercase! Please start again")
        continue

    if gender == 'F':
        if race == 1:
            firstName = random.choice(nord_female)
            lastName = random.choice(nord_last)
        elif race == 2:
            firstName = random.choice(imperial_female)
            lastName = random.choice(imperial_last)
        elif race == 3:
            firstName = random.choice(breton_female)
            lastName = random.choice(breton_last)
        elif race == 4:
            firstName = random.choice(redguard_female)
            lastName = random.choice(redguard_last)
        elif race == 5:
            firstName = random.choice(darkelf_female)
            lastName = random.choice(darkelf_last)
        elif race == 6:
            firstName = random.choice(highelf_female)
            lastName = random.choice(highelf_last)
        elif race == 7:
            firstName = random.choice(woodelf_female)
            lastName = random.choice(woodelf_last)
        elif race == 8:
            firstName = random.choice(orc_female)
            lastName = random.choice(orc_last)
        elif race == 9:
            firstName = random.choice(khajiit_female)
            lastName = random.choice(khajiit_last)
        elif race == 10:
            firstName = random.choice(argonian_female)
            lastName = random.choice(argonian_last)
        print(f"\nName generated: {firstName} {lastName}")
    elif gender == 'M':
        if race == 1:
            firstName = random.choice(nord_male)
            lastName = random.choice(nord_last)
        elif race == 2:
            firstName = random.choice(imperial_male)
            lastName = random.choice(imperial_last)
        elif race == 3:
            firstName = random.choice(breton_male)
            lastName = random.choice(breton_last)
        elif race == 4:
            firstName = random.choice(redguard_male)
            lastName = random.choice(redguard_last)
        elif race == 5:
            firstName = random.choice(darkelf_male)
            lastName = random.choice(darkelf_last)
        elif race == 6:
            firstName = random.choice(highelf_male)
            lastName = random.choice(highelf_last)
        elif race == 7:
            firstName = random.choice(woodelf_male)
            lastName = random.choice(woodelf_last)
        elif race == 8:
            firstName = random.choice(orc_male)
            lastName = random.choice(orc_last)
        elif race == 9:
            firstName = random.choice(khajiit_male)
            lastName = random.choice(khajiit_last)
        elif race == 10:
            firstName = random.choice(argonian_male)
            lastName = random.choice(argonian_last)
        print(f"\nName generated: {firstName} {lastName}")
    elif gender == 'U':
        if race == 1:
            firstName = random.choice(nord_unisex)
            lastName = random.choice(nord_last)
        elif race == 2:
            firstName = random.choice(imperial_unisex)
            lastName = random.choice(imperial_last)
        elif race == 3:
            firstName = random.choice(breton_unisex)
            lastName = random.choice(breton_last)
        elif race == 4:
            firstName = random.choice(redguard_unisex)
            lastName = random.choice(redguard_last)
        elif race == 5:
            firstName = random.choice(darkelf_unisex)
            lastName = random.choice(darkelf_last)
        elif race == 6:
            firstName = random.choice(highelf_unisex)
            lastName = random.choice(highelf_last)
        elif race == 7:
            firstName = random.choice(woodelf_unisex)
            lastName = random.choice(woodelf_last)
        elif race == 8:
            firstName = random.choice(orc_unisex)
            lastName = random.choice(orc_last)
        elif race == 9:
            firstName = random.choice(khajiit_unisex)
            lastName = random.choice(khajiit_last)
        elif race == 10:
            firstName = random.choice(argonian_unisex)
            lastName = random.choice(argonian_last)
        print(f"\nName generated: {firstName} {lastName}")
    
    cont = input("\nWould you like to try again? (Enter Y to continue) ")

    if cont == 'Y':
        continue
    else:
        print("\nThanks for using the Skyrim Name Generator!")
        break

    



