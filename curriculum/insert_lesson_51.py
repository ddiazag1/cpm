import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_51 = (
    '<h2>Cities by the River</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Mohenjo-daro_Priesterk%C3%B6nig.jpeg/800px-Mohenjo-daro_Priesterk%C3%B6nig.jpeg" '
    'alt="The Priest-King statue from Mohenjo-daro" loading="lazy">'
    '<p class="image-caption">The Priest-King of Mohenjo-daro \u2014 one of the most famous artifacts from the Indus Valley Civilization</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass dial spun backward, and the brothers landed on a wide, '
    'dusty street flanked by neat brick buildings. Ox carts rumbled past, '
    'and the smell of roasting grain filled the air.</p>'

    '<p>\u201cWhere are we?\u201d Robert asked.</p>'

    '<p>\u201cThe Indus Valley,\u201d William said. \u201cAbout 2500 BC. '
    'Welcome to one of the greatest cities the ancient world ever built.\u201d</p>'

    '<h3>The Indus Valley Civilization</h3>'

    '<p>\u201cWhile Egypt was building pyramids and Mesopotamia was writing on clay tablets, '
    'a third great civilization was thriving here, along the <strong>Indus River</strong> '
    'in what is now Pakistan and northwest India,\u201d William said. '
    '\u201cThe <strong>Indus Valley Civilization</strong> \u2014 also called the <strong>Harappan Civilization</strong> \u2014 '
    'was one of the largest ancient civilizations in the world. '
    'At its peak, it covered an area larger than ancient Egypt and Mesopotamia <em>combined</em>, '
    'with a population of perhaps 5 million people.\u201d</p>'

    '<p>\u201cIts two greatest cities were <strong>Mohenjo-daro</strong> and <strong>Harappa</strong>, '
    'each home to roughly 40,000 people. But there were over 1,000 settlements '
    'spread across the region.\u201d</p>'

    '<h3>The World\u2019s First City Planners</h3>'

    '<p>\u201cLook at these streets,\u201d William pointed. \u201cThey\u2019re laid out in a perfect <strong>grid pattern</strong> \u2014 '
    'straight lines crossing at right angles, like a modern city. '
    'Most ancient cities grew randomly, with winding alleys and crooked lanes. '
    'But the Harappans <em>planned</em> their cities from the start.\u201d</p>'

    '<p>\u201cEvery house was made of <strong>uniform baked bricks</strong> \u2014 all exactly the same size, '
    'in a precise 4:2:1 ratio. That means there were standards and quality control '
    '4,500 years ago. The buildings had multiple stories, interior courtyards, '
    'and \u2014 most remarkably \u2014 <strong>indoor bathrooms</strong> connected to a citywide drainage system.\u201d</p>'

    '<h3>The Great Bath and Sanitation</h3>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Great_Bath%2C_Mohenjo-daro%2C_Larkana_District%2C_Sindh%2C_Pakistan.jpg/800px-Great_Bath%2C_Mohenjo-daro%2C_Larkana_District%2C_Sindh%2C_Pakistan.jpg" '
    'alt="The Great Bath at Mohenjo-daro" loading="lazy">'
    '<p class="image-caption">The Great Bath at Mohenjo-daro \u2014 the world\u2019s earliest known public water tank</p>'
    '</div>'

    '<p>\u201cThis is the <strong>Great Bath</strong>,\u201d William said, pointing to a large rectangular pool '
    'lined with waterproof bricks. \u201cIt\u2019s about 40 feet long, 23 feet wide, and 8 feet deep. '
    'Scholars believe it was used for ritual bathing \u2014 spiritual purification \u2014 '
    'a practice that continues in South Asia today.\u201d</p>'

    '<p>\u201cBut the real engineering marvel was underground. Every house had a toilet or bathing platform '
    'that drained into <strong>covered brick sewers</strong> running beneath the streets. '
    'These sewers had inspection holes so workers could clean them. '
    'This was the most advanced sanitation system in the ancient world \u2014 '
    'Europe wouldn\u2019t match it for another 4,000 years.\u201d</p>'

    '<h3>Trade and Writing</h3>'

    '<p>\u201cThe Harappans were great traders,\u201d William continued. '
    '\u201cArchaeologists have found Indus Valley seals in Mesopotamia '
    'and Mesopotamian goods in Harappan cities. They traded cotton textiles, '
    'beads, ivory, and precious stones across vast distances \u2014 '
    'by land and by sea along the coast of the Arabian Sea.\u201d</p>'

    '<p>\u201cThey had their own <strong>writing system</strong> \u2014 short inscriptions carved on small stone seals, '
    'usually alongside images of animals like bulls, elephants, and a mysterious unicorn-like creature. '
    'But here\u2019s the frustrating part: <strong>no one has been able to read it</strong>. '
    'The Indus script remains undeciphered \u2014 one of the greatest unsolved puzzles in archaeology.\u201d</p>'

    '<h3>The Mystery of the Collapse</h3>'

    '<p>\u201cAround 1900 BC, the Indus Valley cities began to decline,\u201d William said. '
    '\u201cPeople abandoned the great cities and moved to smaller villages. '
    'Why? We\u2019re not sure. The leading theory is that the <strong>rivers shifted course</strong> \u2014 '
    'the Ghaggar-Hakra River, which many settlements depended on, may have dried up '
    'due to tectonic shifts or climate change. Without reliable water, '
    'the cities couldn\u2019t sustain their populations.\u201d</p>'

    '<p>\u201cUnlike Egypt and Mesopotamia, there\u2019s no evidence of a great war or invasion. '
    'The civilization seems to have slowly dispersed, its people migrating east '
    'into the Ganges River plain, where new cultures and kingdoms would eventually arise.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Indus Valley Civilization">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Indus Valley Civilization at a Glance</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">When</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">~3300\u20131300 BC</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Peak: 2600\u20131900 BC</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Where</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Indus River (Pakistan/India)</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">1,000+ settlements</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Key Innovation</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Grid-planned cities</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Sewer systems + indoor plumbing</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Unsolved Mystery</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Script never deciphered</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">~400 symbols, no Rosetta Stone</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">No evidence of armies, kings, or palaces \u2014 possibly the most peaceful ancient civilization</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">Standardized weights &amp; measures suggest a highly organized society</text>'
    '</svg>'
    '</div>'

    '<p>The telescope pulled them home. Robert was still thinking about the underground sewers.</p>'

    '<p>\u201cThey had better plumbing than most of medieval Europe,\u201d he said.</p>'

    '<p>\u201cAnd we can\u2019t even read their writing,\u201d William said. '
    '\u201cImagine what we\u2019d learn if we could. Goodnight, river cities.\u201d</p>'

    '<p>\u201cGoodnight, unsolved puzzles.\u201d</p>'
)

disc_51 = [
    "The Indus Valley Civilization had grid-planned cities with indoor plumbing 4,500 years ago, but Europe didn\u2019t match their sanitation until the 1800s. What does this tell you about the idea that history always moves \u2018forward\u2019?",
    "The Indus script has never been deciphered. If you could ask the Harappans one question about their civilization, what would it be?",
    "There\u2019s no evidence of armies, weapons, or kings in the Indus Valley. Do you think a large civilization can thrive without warfare? Why or why not?"
]

quiz_51 = [
    {
        "q": "What were the two largest cities of the Indus Valley Civilization?",
        "options": ["Memphis and Thebes", "Ur and Babylon", "Mohenjo-daro and Harappa", "Athens and Sparta"],
        "correct": 2
    },
    {
        "q": "What is remarkable about the Indus Valley writing system?",
        "options": [
            "It was written on papyrus",
            "It has never been deciphered",
            "It used an alphabet like ours",
            "It was identical to Egyptian hieroglyphics"
        ],
        "correct": 1
    },
    {
        "q": "What engineering achievement made Indus Valley cities unique in the ancient world?",
        "options": [
            "Pyramids taller than Egypt\u2019s",
            "Aqueducts that carried water uphill",
            "Covered brick sewers and indoor plumbing",
            "Bridges spanning the Indus River"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 51:
        lessons[i] = {
            "id": 51,
            "type": "history",
            "topic": "Ancient India",
            "title": "Cities by the River",
            "readingTime": "10 min",
            "story": story_51,
            "discussion": disc_51,
            "quiz": quiz_51
        }
        print("Updated lesson 51: Cities by the River")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
