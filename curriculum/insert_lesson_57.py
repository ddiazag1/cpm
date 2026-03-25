import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_57 = (
    '<h2>Empire in the Mountains</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Machu_Picchu%2C_Peru.jpg/800px-Machu_Picchu%2C_Peru.jpg" '
    'alt="Machu Picchu, the famous Inca citadel in the Andes Mountains of Peru" loading="lazy">'
    '<p class="image-caption">Machu Picchu \u2014 the Inca citadel perched nearly 8,000 feet above sea level in the Andes Mountains</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass dial spun backward, and suddenly the brothers '
    'were standing on a narrow stone path carved into the side of a mountain. '
    'The air was thin and cold. Below them, clouds filled the valleys like white rivers, '
    'and above, snow-capped peaks scraped the sky in every direction.</p>'

    '<p>\u201cI can barely breathe,\u201d Robert gasped, clutching the stone wall beside him.</p>'

    '<p>\u201cWe\u2019re in the <strong>Andes Mountains</strong> of South America,\u201d William said. '
    '\u201cAbout 13,000 feet above sea level. Welcome to the empire of the <strong>Inca</strong> \u2014 '
    'the largest civilization ever built in the Americas.\u201d</p>'

    '<h3>Tawantinsuyu \u2014 The Four Quarters</h3>'

    '<p>\u201cThe Inca called their empire <strong>Tawantinsuyu</strong>, which means '
    '\u201cThe Four Quarters of the World,\u201d\u201d William said. '
    '\u201cAt its peak around 1500 AD, just before the Spanish arrived, '
    'it stretched 2,500 miles along the western coast of South America \u2014 '
    'from modern Colombia in the north to Chile in the south. '
    'That\u2019s roughly the distance from New York to Los Angeles. '
    'It ruled over <strong>12 million people</strong> speaking more than 100 different languages.\u201d</p>'

    '<p>\u201cThe amazing part is how fast they built it. The Inca Empire really only lasted '
    'about 100 years \u2014 from around 1438, when the great ruler <strong>Pachacuti</strong> '
    'began his conquests, to 1533, when the Spanish arrived. In just a century, '
    'they went from a small kingdom around one city to the largest empire '
    'in the Western Hemisphere.\u201d</p>'

    '<h3>Cusco \u2014 The Navel of the World</h3>'

    '<p>\u201cEvery empire needs a capital,\u201d William continued, '
    '\u201cand the Inca capital was <strong>Cusco</strong>, a city nestled 11,200 feet up in the Andes. '
    'The Inca called it the \u201cnavel of the world.\u201d '
    'At its center stood the <strong>Coricancha</strong> \u2014 the Temple of the Sun \u2014 '
    'whose walls were lined with sheets of solid gold. When the morning sun hit those walls, '
    'the entire temple blazed like fire.\u201d</p>'

    '<p>\u201cGold?\u201d Robert said, eyes wide.</p>'

    '<p>\u201cThe Inca called gold the \u201csweat of the sun\u201d and silver the \u201ctears of the moon.\u201d '
    'But here\u2019s what\u2019s fascinating \u2014 they didn\u2019t use gold or silver as money. '
    'They had <strong>no currency at all</strong>. No markets, no merchants, no buying or selling. '
    'Instead, the empire ran on a system called <strong>mit\u2019a</strong> \u2014 a labor tax. '
    'Every citizen owed the state a certain amount of work each year, '
    'and in return, the state provided food, clothing, and shelter for everyone.\u201d</p>'

    '<h3>Machu Picchu \u2014 The Lost City</h3>'

    '<p>\u201cThis is the place everyone knows,\u201d William said as they rounded a bend in the trail '
    'and a breathtaking sight appeared: stone buildings cascading down a steep green ridge, '
    'with a sharp peak towering behind them. '
    '\u201c<strong>Machu Picchu</strong> was built around 1450 AD, probably as a royal estate '
    'for the emperor Pachacuti. It sits on a ridge nearly 8,000 feet above sea level, '
    'between two mountain peaks.\u201d</p>'

    '<p>\u201cAbout 750 people lived here. The builders cut enormous stone blocks '
    'and fitted them together so precisely that you can\u2019t slide a piece of paper '
    'between the joints \u2014 and they did it <em>without mortar</em>. '
    'The stones hold together by their own weight and the perfection of their cuts. '
    'Many of these walls have survived 500 years of earthquakes.\u201d</p>'

    '<p>\u201cThe Spanish never found Machu Picchu. It was hidden in the mountains, '
    'overgrown by jungle, until the American explorer <strong>Hiram Bingham</strong> '
    'was led there by local farmers in 1911. The rest of the world had '
    'no idea it existed for nearly 400 years.\u201d</p>'

    '<h3>The Road System</h3>'

    '<p>\u201cTo hold their empire together, the Inca built an incredible network of roads,\u201d '
    'William said. \u201cThe <strong>Qhapaq \u00d1an</strong> \u2014 the Royal Road system \u2014 '
    'covered more than <strong>25,000 miles</strong>. That\u2019s enough road to circle the entire Earth. '
    'The roads ran through deserts, along coastal cliffs, across mountain passes '
    'over 16,000 feet high, and through dense tropical jungle.\u201d</p>'

    '<p>\u201cWhere rivers blocked the way, they built <strong>suspension bridges</strong> '
    'woven from braided grass ropes as thick as a man\u2019s body. '
    'Some of these bridges spanned gaps of over 150 feet. '
    'Local communities were responsible for rebuilding each bridge every year or two, '
    'weaving new ropes and replacing the old ones. '
    'One of these bridges, the <strong>Q\u2019eswachaka</strong>, is still rebuilt every June '
    'using the same ancient techniques \u2014 it has been maintained continuously '
    'for over 500 years.\u201d</p>'

    '<p>\u201cAlong the roads, the Inca placed relay runners called <strong>chasquis</strong>. '
    'These runners waited in small stations about a mile and a half apart. '
    'When a message arrived, the chasqui would sprint to the next station and pass it on. '
    'Working in relays, they could carry a message 150 miles in a single day \u2014 '
    'faster than the Spanish could carry mail on horseback centuries later.\u201d</p>'

    '<h3>Quipu \u2014 Writing Without Words</h3>'

    '<p>\u201cHere\u2019s one of the biggest mysteries,\u201d William said, holding up a bundle '
    'of colored strings with knots tied at different points. '
    '\u201cThe Inca had <strong>no written language</strong>. No alphabet, no symbols, no script. '
    'Instead, they recorded information using these \u2014 <strong>quipus</strong>. '
    'A quipu is a set of knotted strings, sometimes just a few, sometimes thousands, '
    'hanging from a main cord.\u201d</p>'

    '<p>\u201cThe position, color, and type of each knot encoded numbers and possibly words. '
    'The Inca used quipus to record census data, tax records, troop counts, '
    'harvest yields, and even stories. Specially trained officials called '
    '<strong>quipucamayocs</strong> spent their entire lives learning to read and create them.\u201d</p>'

    '<p>\u201cSo it was like a secret code?\u201d Robert asked.</p>'

    '<p>\u201cMore like a language made of knots instead of letters,\u201d William said. '
    '\u201cScholars today can read the number portions, but the rest remains undeciphered. '
    'About 600 quipus survive in museums around the world.\u201d</p>'

    '<h3>Terraced Farming and Freeze-Dried Food</h3>'

    '<p>\u201cFarming on a steep mountainside seems impossible,\u201d Robert said, '
    'looking at the nearly vertical slopes.</p>'

    '<p>\u201cIt is \u2014 unless you reshape the mountain,\u201d William said. '
    '\u201cThe Inca carved <strong>terraces</strong> into the hillsides \u2014 '
    'giant steps of flat land held in place by stone walls. '
    'Each terrace had its own soil and irrigation channel. '
    'They grew over <strong>70 different crops</strong>, including 3,000 varieties of potato \u2014 '
    'yes, the potato comes from Peru \u2014 plus corn, quinoa, peppers, and tomatoes.\u201d</p>'

    '<p>\u201cThey also invented <strong>freeze-drying</strong>, thousands of years '
    'before modern science figured it out. At high altitudes, they would leave potatoes out '
    'during freezing nights and then stomp out the moisture during warm days, '
    'repeating the process until the potatoes turned into a lightweight, dried food called '
    '<strong>chu\u00f1o</strong>. Chu\u00f1o could last for <em>years</em> without spoiling \u2014 '
    'perfect for feeding armies on the march or surviving lean harvests.\u201d</p>'

    '<h3>Incredible Engineers Without the Wheel</h3>'

    '<p>\u201cHere\u2019s what amazes me most,\u201d William said. '
    '\u201cThe Inca built all of this \u2014 25,000 miles of roads, cities on mountaintops, '
    'suspension bridges, terraced farms \u2014 without three things that Europeans considered '
    'essential: the <strong>wheel</strong>, <strong>iron tools</strong>, and <strong>written language</strong>.\u201d</p>'

    '<p>\u201cNo wheels?\u201d Robert said. \u201cHow did they move those giant stones?\u201d</p>'

    '<p>\u201cHuman muscle, wooden rollers, ramps, and levers \u2014 organized by a state '
    'that could coordinate the labor of millions. Some of the stones at the fortress '
    'of <strong>Sacsayhuam\u00e1n</strong> near Cusco weigh over <strong>100 tons</strong> \u2014 '
    'heavier than a loaded freight train car \u2014 and they\u2019re fitted together '
    'with the same impossible precision as Machu Picchu, no mortar, no gaps.\u201d</p>'

    '<h3>The Sapa Inca</h3>'

    '<p>\u201cThe emperor was called the <strong>Sapa Inca</strong>, which means '
    '\u201cSole Ruler,\u201d\u201d William said. \u201cHe was considered the son of '
    '<strong>Inti</strong>, the sun god, and his word was absolute law. '
    'He ate from gold dishes, wore clothes only once before they were burned, '
    'and traveled on a golden litter carried by specially chosen bearers. '
    'When the Sapa Inca died, his body was mummified and kept in his palace, '
    'which continued to be maintained as if he were still alive. '
    'Servants brought food to his mummy and changed its clothing.\u201d</p>'

    '<p>\u201cThat\u2019s a little creepy,\u201d Robert said.</p>'

    '<p>\u201cDifferent culture, different beliefs,\u201d William replied. '
    '\u201cThe Inca believed their dead rulers could still influence the world of the living. '
    'On important occasions, the mummies of past emperors were brought out '
    'and paraded through the streets of Cusco.\u201d</p>'

    '<h3>The Spanish Conquest</h3>'

    '<p>\u201cIn 1532, a Spanish conquistador named <strong>Francisco Pizarro</strong> '
    'arrived in Peru with just <strong>168 soldiers</strong>,\u201d William said quietly. '
    '\u201cThe Inca Empire had millions of people and hundreds of thousands of warriors. '
    'It should have been no contest.\u201d</p>'

    '<p>\u201cBut the empire was already weakened. A devastating <strong>smallpox epidemic</strong> \u2014 '
    'brought to the Americas by earlier Spanish expeditions \u2014 had swept through the empire, '
    'killing the Sapa Inca <strong>Huayna Capac</strong> and millions of his subjects. '
    'A brutal <strong>civil war</strong> between his two sons, <strong>Atahualpa</strong> and <strong>Huascar</strong>, '
    'had torn the empire apart.\u201d</p>'

    '<p>\u201cPizarro captured Atahualpa through treachery at the city of <strong>Cajamarca</strong>. '
    'The Inca filled an entire room with gold and two rooms with silver '
    'as ransom \u2014 an estimated <strong>24 tons of precious metal</strong>. '
    'Pizarro took the treasure and executed Atahualpa anyway. '
    'Within a few years, the greatest empire in the Americas was gone.\u201d</p>'

    '<h3>The Legacy</h3>'

    '<p>\u201cBut the Inca people didn\u2019t disappear,\u201d William said. '
    '\u201cToday, millions of their descendants live in Peru, Bolivia, Ecuador, and beyond. '
    'The <strong>Quechua language</strong>, the language of the Inca, '
    'is still spoken by roughly <strong>8 million people</strong>. '
    'Terraced farms still cover the Andean hillsides. '
    'The Q\u2019eswachaka bridge is still rebuilt every year. '
    'And Machu Picchu draws over a million visitors annually, '
    'standing as proof that human beings can build wonders '
    'even in the most impossible places.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Inca Empire at a Glance">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Inca Empire \u2014 Tawantinsuyu</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Empire (1438\u20131533)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">2,500 miles, 12 million people</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">No wheel, no iron, no writing</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Engineering</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">25,000 miles of roads</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Machu Picchu, 100-ton stones</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Innovation</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Quipu (knotted string records)</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Freeze-dried food, 3,000 potato types</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Legacy</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">8 million Quechua speakers</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Q\u2019eswachaka rebuilt every year</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Built the largest empire in the Americas on mountaintops \u2014 without wheels, iron, or a written alphabet</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">Conquered by 168 Spanish soldiers after smallpox and civil war shattered the empire</text>'
    '</svg>'
    '</div>'

    '<p>The telescope pulled them home. Robert stood by the window, '
    'looking out at the flat neighborhood streets.</p>'

    '<p>\u201cThey built cities on top of mountains without even having wheels,\u201d he said quietly. '
    '\u201cWe can\u2019t even fix our driveway.\u201d</p>'

    '<p>William laughed. \u201cDifferent priorities. Goodnight, empire in the mountains.\u201d</p>'

    '<p>\u201cGoodnight, knotted strings.\u201d</p>'
)

disc_57 = [
    "The Inca built 25,000 miles of roads, cities on mountaintops, and moved 100-ton stones \u2014 all without the wheel, iron tools, or a written language. Does this change how you think about what technology is \u2018necessary\u2019 for a great civilization?",
    "Pizarro conquered an empire of 12 million people with just 168 soldiers, largely because smallpox and civil war had already weakened the Inca. How much of history comes down to timing and luck rather than strength?",
    "The Inca had no money, no markets, and no merchants \u2014 instead, the state provided everything in exchange for labor. Could a system like that work today? What would be the advantages and disadvantages?"
]

quiz_57 = [
    {
        "q": "What did the Inca use instead of a written language to record information?",
        "options": [
            "Clay tablets with symbols",
            "Quipus \u2014 knotted strings",
            "Paintings on stone walls",
            "Carved wooden boards"
        ],
        "correct": 1
    },
    {
        "q": "How many miles of roads did the Inca road system cover?",
        "options": [
            "About 5,000 miles",
            "About 10,000 miles",
            "About 25,000 miles",
            "About 50,000 miles"
        ],
        "correct": 2
    },
    {
        "q": "Why was the Inca Empire vulnerable when Pizarro arrived?",
        "options": [
            "The empire had just been founded and was still small",
            "Smallpox and a civil war had weakened it",
            "The Inca had no warriors or weapons",
            "A drought had destroyed all their crops"
        ],
        "correct": 1
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 57:
        lessons[i] = {
            "id": 57,
            "type": "history",
            "topic": "Inca",
            "title": "Empire in the Mountains",
            "readingTime": "10 min",
            "story": story_57,
            "discussion": disc_57,
            "quiz": quiz_57
        }
        print("Updated lesson 57: Empire in the Mountains")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
