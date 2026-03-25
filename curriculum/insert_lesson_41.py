import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_41 = (
    '<h2>Underground Wonders</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Carlsbad_Caverns.jpg/800px-Carlsbad_Caverns.jpg" '
    'alt="Massive stalactites and stalagmites inside a limestone cave" loading="lazy">'
    '<p class="image-caption">Stalactites and stalagmites \u2014 stone sculptures built one drop at a time over thousands of years</p>'
    '</div>'

    '<p>William was lying on his stomach, peering under the bed with a flashlight. '
    '\u201cRobert, do you think there\u2019s anything under the ground? Like, way down deep?\u201d</p>'

    '<p>Robert grinned and reached for the brass telescope. '
    '\u201cUnder the ground? There are entire worlds down there \u2014 '
    'cathedrals of stone, rivers that have never seen sunlight, '
    'and creatures that have never seen the sky. Let me show you.\u201d</p>'

    '<p>The telescope\u2019s golden light swept them downward through the bedroom floor, '
    'through soil and clay and rock, deeper and deeper into the Earth until they stood '
    'at the entrance of an enormous underground chamber so vast that their flashlight '
    'couldn\u2019t reach the ceiling.</p>'

    '<h3>How Caves Are Born</h3>'

    '<p>\u201cMost caves form in <strong>limestone</strong>,\u201d Robert said, running his hand '
    'along the damp cave wall. \u201cLimestone is a soft rock made from the shells and skeletons '
    'of ancient sea creatures that lived millions of years ago. Over time, those shells '
    'piled up on the ocean floor and were compressed into rock.\u201d</p>'

    '<p>\u201cBut here\u2019s the key: when rainwater falls through the air and seeps through soil, '
    'it picks up carbon dioxide and becomes a weak acid called <strong>carbonic acid</strong>. '
    'This mildly acidic water trickles into tiny cracks in the limestone '
    'and slowly <strong>dissolves</strong> the rock, atom by atom, grain by grain. '
    'Over hundreds of thousands of years, those tiny cracks become tunnels, '
    'the tunnels become passages, and the passages become enormous chambers.\u201d</p>'

    '<p>\u201cSo this whole cave was carved by rainwater?\u201d William asked, staring up '
    'at the cathedral-sized ceiling.</p>'

    '<p>\u201cJust rainwater and time. Lots and lots of time.\u201d</p>'

    '<h3>Stalactites and Stalagmites \u2014 Stone Icicles</h3>'

    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Tropfsteinh%C3%B6hle.jpg/800px-Tropfsteinh%C3%B6hle.jpg" '
    'alt="Stalactites hanging from a cave ceiling with stalagmites rising from the floor" loading="lazy">'
    '<p class="image-caption">Stalactites hang tight to the ceiling; stalagmites might reach the ceiling someday</p>'
    '</div>'

    '<p>The telescope illuminated the chamber, and William gasped. '
    'Hanging from the ceiling were hundreds of stone icicles, some thin as soda straws, '
    'others thick as tree trunks. Rising from the floor were matching pillars, '
    'reaching upward like fingers. Where the two met, they formed solid stone columns.</p>'

    '<p>\u201c<strong>Stalactites</strong> grow from the ceiling down,\u201d Robert said. '
    '\u201cWater carrying dissolved limestone drips from the ceiling. '
    'When the drop hangs there, some of the water evaporates and leaves behind '
    'a tiny ring of mineral called <strong>calcite</strong>. '
    'Drop after drop, ring after ring, over thousands of years, '
    'a stone icicle grows downward. A stalactite might grow only one inch every hundred years.\u201d</p>'

    '<p>\u201c<strong>Stalagmites</strong> grow from the floor up. '
    'When that same drop of water falls and splashes on the ground, '
    'it deposits more calcite on the floor, building a mound that slowly rises. '
    'Eventually, a stalactite and a stalagmite can meet and fuse into a <strong>column</strong>.\u201d</p>'

    '<p>\u201cHere\u2019s a trick to remember: stala<strong>c</strong>tites have a C for ceiling, '
    'stala<strong>g</strong>mites have a G for ground.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 180" width="700" height="180" xmlns="http://www.w3.org/2000/svg" '
    'aria-label="How stalactites and stalagmites form">'
    '<rect width="700" height="180" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">'
    'How Cave Formations Grow</text>'

    '<rect x="30" y="30" width="640" height="8" rx="2" fill="#5a4a3a"/>'
    '<text x="350" y="27" text-anchor="middle" fill="#b8a88a" font-size="8">Cave Ceiling (limestone)</text>'

    '<rect x="30" y="145" width="640" height="8" rx="2" fill="#5a4a3a"/>'
    '<text x="350" y="168" text-anchor="middle" fill="#b8a88a" font-size="8">Cave Floor</text>'

    '<path d="M150,38 L150,85" stroke="#e8a838" stroke-width="6" stroke-linecap="round"/>'
    '<circle cx="150" cy="92" r="3" fill="#4a90d9" opacity="0.7"/>'
    '<text x="150" y="110" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Stalactite</text>'
    '<text x="150" y="122" text-anchor="middle" fill="#b8a88a" font-size="7">Grows from ceiling DOWN</text>'
    '<text x="150" y="134" text-anchor="middle" fill="#b8a88a" font-size="7">C = Ceiling</text>'

    '<path d="M350,38 L350,75" stroke="#e8a838" stroke-width="6" stroke-linecap="round"/>'
    '<path d="M350,145 L350,105" stroke="#e8a838" stroke-width="8" stroke-linecap="round"/>'
    '<text x="350" y="95" text-anchor="middle" fill="#4a90d9" font-size="7">They meet!</text>'
    '<text x="350" y="168" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Column</text>'

    '<path d="M550,145 L550,110" stroke="#e8a838" stroke-width="7" stroke-linecap="round"/>'
    '<text x="550" y="100" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Stalagmite</text>'
    '<text x="550" y="85" text-anchor="middle" fill="#b8a88a" font-size="7">Grows from floor UP</text>'
    '<text x="550" y="73" text-anchor="middle" fill="#b8a88a" font-size="7">G = Ground</text>'

    '</svg>'
    '</div>'

    '<h3>Mammoth Cave \u2014 The Longest Cave on Earth</h3>'

    '<p>The telescope whisked them to Kentucky, deep into the bowels of '
    '<strong>Mammoth Cave</strong> \u2014 the longest known cave system in the world.</p>'

    '<p>\u201cMammoth Cave has over <strong>420 miles</strong> of explored passages,\u201d Robert said, '
    '\u201cand explorers keep finding more. Scientists estimate there could be another '
    '600 miles still unmapped. It was carved by underground rivers over the last '
    '10 million years.\u201d</p>'

    '<p>\u201cNative Americans explored parts of it over 4,000 years ago \u2014 '
    'archaeologists have found their reed torches and moccasin prints preserved in the cave. '
    'During the War of 1812, miners dug calcium nitrate from the cave to make gunpowder. '
    'And in the 1840s, a doctor even set up a tuberculosis hospital inside, '
    'believing the constant cool air would cure his patients (it didn\u2019t).\u201d</p>'

    '<h3>Crystal Caves \u2014 Nature\u2019s Hidden Jewels</h3>'

    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Cristales_cueva_de_Naica.JPG/800px-Cristales_cueva_de_Naica.JPG" '
    'alt="Giant selenite crystals in the Cave of the Crystals in Naica, Mexico" loading="lazy">'
    '<p class="image-caption">The Cave of the Crystals in Naica, Mexico \u2014 selenite beams up to 39 feet long</p>'
    '</div>'

    '<p>The telescope brought them somewhere that looked like another planet. '
    'Enormous translucent beams of crystal crisscrossed an underground chamber, '
    'some as long as school buses.</p>'

    '<p>\u201cThis is the <strong>Cave of the Crystals</strong> in Naica, Mexico,\u201d Robert whispered. '
    '\u201cThese are <strong>selenite crystals</strong> \u2014 a form of gypsum \u2014 '
    'and some of them are nearly <strong>39 feet long</strong> and weigh over 50 tons. '
    'They\u2019re the largest natural crystals ever found.\u201d</p>'

    '<p>\u201cThey grew so large because the cave was flooded with mineral-rich water '
    'heated to about 136\u00b0F by magma deep below. For half a million years, '
    'the crystals grew at an incredibly slow, steady rate \u2014 '
    'about the width of a human hair per hundred years. '
    'The temperature inside is still so hot and humid that humans can only survive '
    'about ten minutes without special cooling suits.\u201d</p>'

    '<h3>Underground Rivers and Spelunking</h3>'

    '<p>They followed an underground river, its dark water flowing silently '
    'through a passage worn smooth over millennia.</p>'

    '<p>\u201c<strong>Underground rivers</strong> are streams that flow entirely within cave systems,\u201d '
    'Robert said. \u201cSome are enormous. The <strong>Puerto Princesa Underground River</strong> '
    'in the Philippines flows for five miles through a limestone cave directly into the sea. '
    'You can take a boat ride through it.\u201d</p>'

    '<p>\u201cExploring caves is called <strong>spelunking</strong> or <strong>caving</strong>,\u201d '
    'Robert continued. \u201cCavers use helmets with lights, ropes, harnesses, '
    'and waterproof gear. The three rules of caving are: never go alone, '
    'always tell someone where you\u2019re going and when you\u2019ll be back, '
    'and bring at least three sources of light.\u201d</p>'

    '<h3>Cave Life \u2014 Creatures of Eternal Darkness</h3>'

    '<p>William shone his flashlight into a pool of crystal-clear water and jumped back. '
    'Something was swimming in it \u2014 something pale and ghostly, with no eyes at all.</p>'

    '<p>\u201cThose are <strong>troglobites</strong> \u2014 animals that live their entire lives in caves,\u201d '
    'Robert said. \u201cThey\u2019ve adapted to total darkness over millions of years. '
    'Many have lost their eyes and their pigmentation because in complete darkness, '
    'seeing and being colored are useless. Instead, they\u2019ve developed '
    'extraordinary senses of touch, smell, and vibration.\u201d</p>'

    '<p>\u201cThat\u2019s an <strong>olm</strong>, also called the \u2018human fish\u2019 '
    'because of its pinkish skin. It\u2019s a salamander that lives in caves in Slovenia. '
    'It\u2019s completely blind, breathes through gills, '
    'and can survive up to <strong>ten years without eating</strong> by slowing '
    'its metabolism to almost nothing. It can live over 100 years.\u201d</p>'

    '<p>\u201c<strong>Cave fish</strong> around the world have independently evolved blindness \u2014 '
    'species in Mexico, Alabama, China, and Somalia all lost their eyes separately, '
    'because in darkness, the energy cost of building eyes isn\u2019t worth it.\u201d</p>'

    '<h3>Waitomo Glowworm Caves</h3>'

    '<p>The telescope carried them to New Zealand, into a cave that looked like it contained '
    'a galaxy. Thousands of tiny blue-green lights sparkled across the ceiling, '
    'reflected in the still water below.</p>'

    '<p>\u201cThese are <strong>glowworms</strong> \u2014 actually the larvae of a fungus gnat,\u201d '
    'Robert said. \u201cEach one hangs sticky silk threads from the ceiling '
    'and glows with <strong>bioluminescence</strong> to attract insects. '
    'When a flying insect is drawn to the light and gets stuck in the silk, '
    'the glowworm reels it in and eats it \u2014 like a tiny glowing fisherman.\u201d</p>'

    '<p>\u201cThe <strong>Waitomo Glowworm Caves</strong> are home to thousands of these creatures. '
    'Visitors float through the caves on boats in complete silence, '
    'gazing up at a living starscape made entirely by larvae.\u201d</p>'

    '<p>The telescope brought them back to their bedroom. William clicked off his flashlight '
    'and stared at the dark ceiling.</p>'

    '<p>\u201cThere\u2019s a whole world under our feet,\u201d he said, '
    '\u201cand most people walk right over it without knowing.\u201d</p>'

    '<p>\u201cThe best wonders are hidden,\u201d Robert said. '
    '\u201cGoodnight, William.\u201d</p>'

    '<p>\u201cGoodnight, underground.\u201d</p>'
)

disc_41 = [
    "A stalactite grows about one inch every hundred years. What does that teach us about what patience and slow, steady work can accomplish?",
    "Cave animals like the olm lost their eyes because they didn\u2019t need them in the dark. If humans lived in caves for millions of years, what changes do you think our bodies might develop?",
    "The Cave of the Crystals in Naica is so hot that humans can barely survive ten minutes inside. Should scientists risk their health to explore dangerous places, or should we send robots instead?"
]

quiz_41 = [
    {
        "q": "What type of rock are most caves formed in?",
        "options": ["Granite", "Limestone", "Sandstone", "Marble"],
        "correct": 1
    },
    {
        "q": "What is the longest known cave system in the world?",
        "options": ["Waitomo Caves", "Cave of the Crystals", "Mammoth Cave", "Carlsbad Caverns"],
        "correct": 2
    },
    {
        "q": "Why have many cave animals lost their eyes over millions of years?",
        "options": [
            "The water in caves dissolves their eyes",
            "Cave predators target animals with eyes",
            "In total darkness, eyes are useless and cost energy to build",
            "The minerals in caves block eye development"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 41:
        lessons[i] = {
            "id": 41,
            "type": "science",
            "topic": "Earth Science",
            "title": "Underground Wonders",
            "readingTime": "10 min",
            "story": story_41,
            "discussion": disc_41,
            "quiz": quiz_41
        }
        print("Updated lesson 41: Underground Wonders")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
