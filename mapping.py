# Define car types and manufacturers for rule-based matching in English
CAR_TYPES_EN = ["crossover", "family", "luxury", "jeep", "small", "minivan",
                "executive", "sport", "pickup", "commercial"]

MANUFACTURERS_EN = ["baw", "eveasy", "ktm", "xpeng", "zeekr",
    "audi", "abarth", "autobianchi", "oldsmobile", "austin", "opel",
    "ora", "aiways", "iveco", "infiniti", "isuzu", "levc", "ltai",
    "alfa romeo", "alpine", "mg", "aston martin", "few", "bmw", "byd",
    "buick", "bentley", "gac", "gmc", "geo", "jiayuan", "jac", "geely",
    "jeep","jeep TAR", "genesis", "great wall", "dacia", "dodge", "dongfeng", "ds",
    "daewoo", "daihatsu", "hummer", "hongqi", "honda", "hino", "wey",
    "voyah", "volvo", "tata", "toyota", "tesla", "jaguar", "hyundai",
    "lada", "lynk & co", "lincoln", "leapmotor", "lixi", "lamborghini",
    "land rover", "lancia", "lexus", "mazda", "man", "maserati", "mini",
    "mitsubishi", "maxus", "mercedes", "nio", "nissan", "nanjing", "saab",
    "sun living", "ssangyong", "sunshine", "subaru", "suzuki", "seat",
    "citroen", "smart", "centro", "skoda", "skywell", "seres", "polestar",
    "volkswagen", "pontiac", "ford", "porsche", "forthing", "piaggio",
    "fiat", "peugeot", "ferrari", "chery", "cadillac", "cupra", "kia",
    "chrysler", "rover", "renault", "chevrolet"
]

CAR_TYPES_MAPPING = {"crossover": 10, "family": 2, "luxury": 8, "jeep": 5, "small": 1, "minivan": 9,
                     "executive": 3, "sport": 4, "pickup": 6, "commercial": 7}

MANUFACTURERS_MAPPING = {"baw":193, "eveasy":323, "ktm":72, "xpeng":290, "zeekr":333,
    "audi":1, "abarth":53, "autobianchi":96, "oldsmobile":76, "austin":102, "opel":2,
    "ora":224, "aiways":288, "iveco":85, "infiniti":3, "isuzu":4, "levc":299, "ltai":77,
    "alfa romeo":5, "alpine":115, "mg":6, "aston martin":54, "few":168, "bmw":7, "byd":141,
    "buick":8, "bentley":55, "gac":99, "gmc":9, "geo":94, "jiayuan":346, "jac":200, "geely":177,
    "jeep":10,"jeep TAR":59, "genesis":93, "great wall":11, "dacia":12, "dodge":13, "dongfeng":88, "ds":14,
    "daewoo":60, "daihatsu":15, "hummer":16, "hongqi":301, "honda":17, "hino":95, "wey":284,
    "voyah":322, "volvo":18, "tata":84, "toyota":19, "tesla":62, "jaguar":20, "hyundai":21,
    "lada":80, "lynk & co":321, "lincoln":23, "leapmotor":320, "lixi":98, "lamborghini":63,
    "land rover":24, "lancia":25, "lexus":26, "mazda":27, "man":86, "maserati":28, "mini":29,
    "mitsubishi":30, "maxus":89, "mercedes":31, "nio":289, "nissan":32, "nanjing":78, "saab":33,
    "sun living":302, "ssangyong":34, "sunshine":56, "subaru":35, "suzuki":36, "seat":37,
    "citroen":38, "smart":39, "centro":97, "skoda":40, "skywell":300, "seres":287, "polestar":231,
    "volkswagen":41, "pontiac":42, "ford":43, "porsche":44, "forthing":334, "piaggio":90,
    "fiat":45, "peugeot":46, "ferrari":57, "chery":147, "cadillac":47, "cupra":92, "kia":48,
    "chrysler":49, "rover":50, "renault":51, "chevrolet":52}
