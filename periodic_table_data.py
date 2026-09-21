# Colors
nonMetal = (247, 229, 208)
halfMetal = (248, 255, 0)
metal = (0, 151, 255)
undefined = (255, 255, 255)

# Text colors
gas = (255, 0, 0)
liquid = (0, 0, 255)
solid = (0, 0, 0)

"""
    {"name": "", 
     "symbol": "", 
     "atomic_number": , 
     "atomic_weight": , 
     "category": "", 
     "state": "", 
     "isotopes": [],
     "isotope_names": [],
     "pos": (0, ), 
     "description": ",
     "button_color": , 
     "text_color": ,
     "image": "images//.png",  # Image for normal atom
     "isotope_images": []
    },  # List of isotope images

     {"name": "Test",
     "symbol": "T",
     "atomic_number": 0,
     "atomic_weight": 0,
     "category": "Null",
     "state": "Null",
     "isotopes": [],
     "isotope_names": [],
     "pos": (15, 2),
     "description": "",
     "button_color": nonMetal,
     "text_color": solid,
     "image": "",  # Image for normal atom
     "isotope_images": []
    },  # List of isotope images¨
    
    """

elements = [
    {"name": "Hydrogen", 
     "symbol": "H", 
     "atomic_number": 1, 
     "atomic_weight": 1.008, 
     "category": "Non-metal", 
     "state": "Gas", 
     "isotopes": ['H-1', 'H-2', 'H-3'],
     "isotope_names": ['Protium', 'Deuterium', 'Tritium'],
     "pos": (0, 0), 
     "description": "Hydrogen is the lightest, most abundant element, existing as a colorless, flammable gas. It powers stars, forms water, and is vital in fuel cells, clean energy, and various industries.",
     "button_color": nonMetal, 
     "text_color": gas,
     "image": "images/H/H.png",  # Image for normal atom
     "isotope_images": ["images/H/H-1.png", "images/H/H-2.png", "images/H/H-3.png"]
    },  # List of isotope images
        
    {"name": "Helium", 
     "symbol": "He", 
     "atomic_number": 2, 
     "atomic_weight": 4.003, 
     "category": "Non-Metal", 
     "state": "Gas", 
     "isotopes": ['He-3', 'He-4'],
     "isotope_names": ['Helium-3', 'Helium-4'],
     "pos": (17, 0), 
     "description": "Helium is a light, colorless, and non-flammable gas. It’s the second most abundant element, found in stars and used in balloons, cooling systems, and scientific research due to its low boiling point and stability.",
     "button_color": nonMetal, 
     "text_color": gas,
     "image": "images/He/He.png",  # Image for normal atom
     "isotope_images": ["images/He/He-3.png", "images/He/He-4.png"]
    },  # List of isotope images
    
    {"name": "Lithium", 
     "symbol": "Li", 
     "atomic_number": 3, 
     "atomic_weight": 6.941, 
     "category": "Metal", 
     "state": "Solid", 
     "isotopes": ['Li-6', 'Li-7'],
     "isotope_names": ['Lithium-6', 'Lithium-7'],
     "pos": (0, 1), 
     "description": "Lithium is a soft, silvery-white metal and the lightest metal on the periodic table. Highly reactive and flammable, it is mainly used in rechargeable batteries, ceramics, and pharmaceuticals, playing a vital role in modern technology and mental health treatments.",
     "button_color": metal, 
     "text_color": solid,
     "image": "images/Li/Li.png",  # Image for normal atom
     "isotope_images": ['images/Li/Li-6.png', 'images/Li/Li-7.png']
    },  # List of isotope images

    {"name": "Beryllium", 
     "symbol": "Be", 
     "atomic_number": 4, 
     "atomic_weight": 9.012, 
     "category": "Metal", 
     "state": "Solid", 
     "isotopes": ['Be-9'],
     "isotope_names": ['Beryllium-9'],
     "pos": (1, 1), 
     "description": "Beryllium is a lightweight, strong metal with a grayish color. It’s used in aerospace, electronics, and nuclear reactors due to its stiffness, heat resistance, and ability to slow neutrons. Beryllium is toxic when inhaled.",
     "button_color": metal, 
     "text_color": solid,
     "image": "images/Be/Be.png",  # Image for normal atom
     "isotope_images": ["images/Be/Be-9.png"]
    },  # List of isotope images

    {
        "name": "Boron",
        "symbol": "B",
        "atomic_number": 5,
        "atomic_weight": 10.811,
        "category": "Half-Metal",
        "state": "Solid",
        "isotopes": ['B-10', 'B-11'],
        "isotope_names": ['Boron-10', 'Boron-11'],
        "pos": (12, 1),
        "description": "Boron is a hard, black metalloid used in glassmaking, detergents, and semiconductors. It’s essential in plant growth and has high strength and heat resistance, making it valuable in various industries.",
        "button_color": halfMetal,
        "text_color": solid,
        "image": "images/B/B.png",  # Image for normal atom
        "isotope_images": ["images/B/B-10.png", "images/B/B-11.png"]
    },

    {
        "name": "Carbon",
        "symbol": "C",
        "atomic_number": 6,
        "atomic_weight": 12.011,
        "category": "Non-Metal",
        "state": "Solid",
        "isotopes": ['C-12', 'C-13', 'C-14'],
        "isotope_names": ['Carbon-12', 'Carbon-13', 'Carbon-14'],
        "pos": (13, 1),
        "description": "Carbon is a versatile, nonmetal element that forms the backbone of life on Earth, found in all organic molecules. It exists in various forms, from soft graphite to hard diamond, and is vital in fuels, plastics, and materials like steel.",
        "button_color": nonMetal,
        "text_color": solid,
        "image": "images/C/C.png",  # Image for normal atom
        "isotope_images": ["images/C/C-12.png", "images/C/C-13.png", "images/C/C-14.png"]
    },

    {
        "name": "Nitrogen",
        "symbol": "N",
        "atomic_number": 7,
        "atomic_weight": 14.007,
        "category": "Non-Metal",
        "state": "Gas",
        "isotopes": ['N-14', 'N-15'],
        "isotope_names": ["Nitrogen-14", "Nitrogen-15"],
        "pos": (14, 1),
        "description": "Nitrogen is a colorless, odorless gas that makes up 78% of Earth's atmosphere. Essential for life, it’s found in proteins, DNA, and fertilizers, and its inertness makes it crucial for preserving food and creating controlled environments.",
        "button_color": nonMetal,
        "text_color": gas,
        "image": "images/N/N.png",  # Image for normal atom
        "isotope_images": ["images/N/N-14.png", "images/N/N-15.png"]
    },

    {
        "name": "Oxygen",
        "symbol": "O",
        "atomic_number": 8,
        "atomic_weight": 15.999,
        "category": "Non-Metal",
        "state": "Gas",
        "isotopes": ['O-16', 'O-17', 'O-18'],
        "isotope_names": ['Oxygen-16', 'Oxygen-17', 'Oxygen-18'],
        "pos": (15, 1),
        "description": "Oxygen is a colorless, odorless gas that makes up 21% of Earth's atmosphere. It is essential for life, playing a critical role in respiration and energy production in most organisms.",
        "button_color": nonMetal,
        "text_color": gas,
        "image": "images/O/O.png",  # Image for normal atom
        "isotope_images": ["images/O/O-16.png", "images/O/O-17.png", "images/O/O-18.png"]
    },

    {
        "name": "Fluorine",
        "symbol": "F",
        "atomic_number": 9,
        "atomic_weight": 18.998403163,
        "category": "Non-Metal",
        "state": "Gas",
        "isotopes": ['F-19'],
        "isotope_names": ['Fluorine-19'],
        "pos": (16, 1),
        "description": "",
        "button_color": nonMetal,
        "text_color": gas,
        "image": "images/F/F.png",  # Image for normal atom
        "isotope_images": ["images/F/F-19.png"]
    },

    {
        "name": "Neon",
        "symbol": "Ne",
        "atomic_number": 10,
        "atomic_weight": 20.180,
        "category": "Non-Metal",
        "state": "Gas",
        "isotopes": [],
        "isotope_names": [],
        "pos": (17, 1),
        "description": "",
        "button_color": nonMetal,
        "text_color": gas,
        "image": "",  # Image for normal atom
        "isotope_images": [""]
    },

    {"name": "Sodium", 
     "symbol": "Na", 
     "atomic_number": 11, 
     "atomic_weight": 22.990, 
     "category": "Metal", 
     "state": "Solid", 
     "isotopes": [],
     "isotope_names": [],
     "pos": (0, 2), 
     "description": "",
     "button_color": metal, 
     "text_color": solid,
     "image": "",  # Image for normal atom
     "isotope_images": []
    },  # List of isotope images

    {"name": "Magnesium",
     "symbol": "Mg",
     "atomic_number": 12,
     "atomic_weight": 24.305,
     "category": "Metal",
     "state": "Solid",
     "isotopes": [],
     "isotope_names": [],
     "pos": (1, 2),
     "description": "",
     "button_color": metal,
     "text_color": solid,
     "image": "",  # Image for normal atom
     "isotope_images": []
    },  # List of isotope images
    
    {"name": "Aluminum",
     "symbol": "Al",
     "atomic_number": 13,
     "atomic_weight": 26.982,
     "category": "Metal",
     "state": "Solid",
     "isotopes": [],
     "isotope_names": [],
     "pos": (12, 2),
     "description": "",
     "button_color": metal,
     "text_color": solid,
     "image": "",  # Image for normal atom
     "isotope_images": []
    },  # List of isotope images

    {"name": "Silicon",
     "symbol": "Si",
     "atomic_number": 14,
     "atomic_weight": 28.085,
     "category": "Half-Metal",
     "state": "Solid",
     "isotopes": [],
     "isotope_names": [],
     "pos": (13, 2),
     "description": "",
     "button_color": halfMetal,
     "text_color": solid,
     "image": "",  # Image for normal atom
     "isotope_images": []
    },  # List of isotope images

    {"name": "Phosphorus",
     "symbol": "P",
     "atomic_number": 15,
     "atomic_weight": 30.974,
     "category": "Non-Metal",
     "state": "Solid",
     "isotopes": [],
     "isotope_names": [],
     "pos": (14, 2),
     "description": "",
     "button_color": nonMetal,
     "text_color": solid,
     "image": "",  # Image for normal atom
     "isotope_images": []
    },  # List of isotope images¨
]