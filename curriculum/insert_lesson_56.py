import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_56 = (
    '<h2>The Island City</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Murales_Rivera_-_Markt_in_Tlatelolco_3.jpg/800px-Murales_Rivera_-_Markt_in_Tlatelolco_3.jpg" '
    'alt="Diego Rivera mural depicting the great market of Tlatelolco in the Aztec capital" loading="lazy">'
    '<p class="image-caption">Diego Rivera\u2019s mural of the great market at Tlatelolco \u2014 showing daily life in the Aztec capital</p>'
    '</div>'

    '<p>Jason ran his fingers over the brass clasp of The Living World. '
    'The tiny hourglass symbol pulsed with green light. '
    '\u201cTonight,\u201d he said, \u201cwe\u2019re visiting a city that was built in the middle of a lake.\u201d</p>'

    '<p>Evelyn pulled her blanket up to her chin. \u201cA city? In a lake? How does it not sink?\u201d</p>'

    '<p>\u201cThat\u2019s what makes it one of the most incredible places ever built.\u201d '
    'Jason opened the book and green light swallowed the room. When it faded, '
    'they were standing on a wide stone road that stretched across shimmering blue water. '
    'Ahead of them rose an enormous city \u2014 white temples, bustling markets, '
    'and thousands of canoes gliding through canals. It was bigger than anything Evelyn had ever imagined.</p>'

    '<h3>An Island in the Lake</h3>'

    '<p>\u201cThis is <strong>Tenochtitlan</strong>,\u201d Jason said, pronouncing it slowly: '
    '<em>teh-notch-TEET-lan</em>. '
    '\u201cIt was the capital of the <strong>Aztec Empire</strong>, and it was built on an island '
    'in the middle of <strong>Lake Texcoco</strong>, high in the Valley of Mexico. '
    'The Aztecs \u2014 who called themselves the <strong>Mexica</strong> \u2014 founded this city in <strong>1325</strong>.\u201d</p>'

    '<p>\u201cWhy would anyone build a city on an island in a lake?\u201d Evelyn asked.</p>'

    '<p>\u201cBecause of a legend,\u201d Jason said. '
    '\u201cThe Mexica had wandered for over a hundred years, looking for a sign from their god '
    '<strong>Huitzilopochtli</strong> \u2014 an eagle perched on a cactus, eating a snake. '
    'They finally saw it on a small, swampy island in Lake Texcoco. '
    'So they built their city right there. That image is still on the '
    '<strong>flag of Mexico</strong> today.\u201d</p>'

    '<p>Evelyn looked down at the road they stood on. It was wide enough for ten people to walk side by side, '
    'and it ran straight across the lake toward the city center.</p>'

    '<h3>Causeways and Canals</h3>'

    '<p>\u201cThis road is called a <strong>causeway</strong>,\u201d Jason explained. '
    '\u201cThe Aztecs built three enormous causeways connecting the island to the mainland. '
    'Each one had removable bridges, so the Aztecs could pull them up to stop enemies from getting in. '
    'The causeways also had gaps that let canoes pass through underneath.\u201d</p>'

    '<p>Evelyn watched a parade of people walking in both directions \u2014 '
    'merchants carrying bundles on their backs, warriors with feathered shields, '
    'women balancing baskets of fruit on their heads.</p>'

    '<p>\u201cThe city also had a system of canals, almost like streets made of water,\u201d Jason said. '
    '\u201cPeople traveled by canoe the way we use cars. At its peak, around <strong>1500</strong>, '
    'Tenochtitlan had between <strong>200,000 and 300,000 people</strong> \u2014 '
    'making it one of the largest cities in the entire world. '
    'It was bigger than London, bigger than Paris, bigger than almost any European city at the time.\u201d</p>'

    '<p>\u201cAll on an island?\u201d Evelyn whispered.</p>'

    '<p>\u201cThey expanded it. The Aztecs piled up mud, rocks, and reeds to make the island larger and larger, '
    'year after year. They were extraordinary engineers.\u201d</p>'

    '<h3>Floating Gardens</h3>'

    '<p>Their canoe drifted past rows of long, rectangular gardens that seemed to float on the water. '
    'Bright green plants grew in neat rows, and farmers knelt among them, tending crops.</p>'

    '<p>\u201cThese are called <strong>chinampas</strong>,\u201d Jason said, '
    '\u201cand people sometimes call them \u2018floating gardens,\u2019 '
    'even though they\u2019re actually anchored to the lake bottom. '
    'The Aztecs wove reeds and branches into a mat, piled rich mud on top, '
    'and planted willow trees at the corners whose roots grew down and held everything in place. '
    'The mud from the lake bottom was incredibly fertile.\u201d</p>'

    '<p>\u201cWhat did they grow?\u201d Evelyn asked.</p>'

    '<p>\u201c<strong>Maize</strong> \u2014 that\u2019s corn \u2014 was the most important crop. '
    'They also grew <strong>beans, squash, tomatoes, chili peppers, and amaranth</strong>. '
    'The chinampas could produce up to <strong>seven harvests per year</strong>, '
    'which is how they fed so many people on an island.\u201d</p>'

    '<h3>The Aztec Empire and Tribute</h3>'

    '<p>They stepped off the canoe and into the heart of the city. A massive open square was filled '
    'with merchants and customers \u2014 the great marketplace of <strong>Tlatelolco</strong>. '
    'Thousands of goods were spread on mats: jade jewelry, jaguar skins, '
    'feathered cloaks, obsidian knives, rubber balls, and live birds in wicker cages.</p>'

    '<p>\u201cThe Aztec Empire wasn\u2019t like most empires,\u201d Jason said. '
    '\u201cThey didn\u2019t send governors to rule conquered cities. Instead, they demanded <strong>tribute</strong> \u2014 '
    'regular payments of goods. Conquered peoples had to send gold, feathers, cacao beans, cotton, '
    'rubber, and even warriors to Tenochtitlan. '
    'The Aztecs controlled over <strong>500 city-states</strong> through this tribute system.\u201d</p>'

    '<p>\u201cSo they just collected things from everyone?\u201d Evelyn said.</p>'

    '<p>\u201cYes, and if a city refused to pay, the Aztec army would come. '
    'The <strong>Jaguar Warriors</strong> and <strong>Eagle Warriors</strong> were the most feared soldiers '
    'in Mesoamerica. They wore elaborate costumes shaped like their animal namesakes '
    'and carried weapons edged with <strong>obsidian</strong> \u2014 volcanic glass sharper than steel.\u201d</p>'

    '<h3>Montezuma and the Great Temple</h3>'

    '<p>They walked toward the center of the city, where a towering pyramid rose above everything else. '
    'It had two steep staircases climbing to twin temples at the top, painted in brilliant red and blue.</p>'

    '<p>\u201cThis is the <strong>Templo Mayor</strong> \u2014 the Great Temple,\u201d Jason said. '
    '\u201cIt stood about <strong>150 feet tall</strong> and was the most sacred place in the empire. '
    'The twin temples on top were dedicated to two gods: '
    '<strong>Huitzilopochtli</strong>, the god of war and the sun, '
    'and <strong>Tlaloc</strong>, the god of rain and agriculture.\u201d</p>'

    '<p>\u201cWho was in charge of all this?\u201d Evelyn asked.</p>'

    '<p>\u201cThe ruler was called the <strong>tlatoani</strong>, which means \u2018he who speaks.\u2019 '
    'The most famous tlatoani was <strong>Montezuma II</strong>, who ruled from 1502 to 1520. '
    'He lived in a palace with hundreds of rooms, a private zoo with jaguars and eagles, '
    'and botanical gardens filled with plants from across the empire. '
    'Montezuma ate his meals behind a golden screen, '
    'and no one was allowed to look him directly in the eyes.\u201d</p>'

    '<h3>Gods and Sacrifice</h3>'

    '<p>Evelyn noticed people climbing the steps of the Great Temple, carrying flowers and bundles of incense.</p>'

    '<p>\u201cThe Aztecs believed the gods had sacrificed themselves to create the world,\u201d Jason said carefully. '
    '\u201cThey thought humans owed the gods a debt, and that the sun would stop moving '
    'if they didn\u2019t repay it. So they made offerings \u2014 food, precious objects, and sometimes '
    'the most serious offering of all: <strong>human life</strong>.\u201d</p>'

    '<p>Evelyn looked uneasy. \u201cThat\u2019s scary.\u201d</p>'

    '<p>\u201cIt is,\u201d Jason agreed. \u201cIt\u2019s one of the most difficult things to understand '
    'about the Aztecs. They were brilliant builders, artists, and engineers \u2014 '
    'but their religion included practices that we find deeply wrong today. '
    'History is like that sometimes. Great civilizations can do terrible things, '
    'and understanding that honestly is part of learning.\u201d</p>'

    '<h3>The Calendar Stone and Knowledge</h3>'

    '<p>Near the base of the temple, Jason pointed to an enormous carved disc leaning against a wall.</p>'

    '<p>\u201cThis is the <strong>Sun Stone</strong>, sometimes called the Aztec Calendar Stone. '
    'It weighs about <strong>24 tons</strong> and is nearly <strong>12 feet across</strong>. '
    'The face in the center represents the sun god <strong>Tonatiuh</strong>. '
    'The rings around it show the four previous worlds the Aztecs believed had existed '
    'and been destroyed before the current one.\u201d</p>'

    '<p>\u201cThe Aztecs used <strong>two calendars</strong> at the same time,\u201d Jason continued. '
    '\u201cA <strong>365-day solar calendar</strong> for farming and daily life, '
    'and a <strong>260-day ritual calendar</strong> for religious ceremonies. '
    'Every 52 years, the two calendars lined up again, and the Aztecs held a huge ceremony '
    'called the <strong>New Fire Ceremony</strong>, where every fire in the empire was put out '
    'and then relit from a single new flame.\u201d</p>'

    '<h3>Xocolatl \u2014 The Drink of the Gods</h3>'

    '<p>A servant walked by carrying a golden cup filled with a dark, foamy liquid. '
    'The rich smell of chocolate drifted through the air.</p>'

    '<p>\u201cIs that hot chocolate?\u201d Evelyn asked eagerly.</p>'

    '<p>\u201cAlmost,\u201d Jason laughed. \u201cThe Aztecs made a drink called <strong>xocolatl</strong> '
    '(sho-KO-latl) from <strong>cacao beans</strong>. '
    'But it was nothing like the sweet cocoa we drink today. '
    'It was bitter, spicy, and sometimes mixed with chili peppers, vanilla, or cornmeal. '
    'They drank it cold and frothy.\u201d</p>'

    '<p>\u201cCacao beans were so valuable that the Aztecs used them as <strong>money</strong>,\u201d '
    'he added. \u201cA turkey cost about 100 cacao beans. A tomato cost one bean. '
    'Montezuma reportedly drank <strong>50 cups of xocolatl every day</strong> '
    'from golden goblets.\u201d</p>'

    '<p>\u201cFifty cups?!\u201d Evelyn giggled. \u201cThat\u2019s a lot of chocolate.\u201d</p>'

    '<h3>Strangers from the Sea</h3>'

    '<p>The sky darkened. On the eastern horizon, Evelyn saw the silhouettes of strange ships '
    'with billowing white sails \u2014 unlike any vessel on Lake Texcoco.</p>'

    '<p>\u201cIn <strong>1519</strong>, a Spanish conquistador named <strong>Hern\u00e1n Cort\u00e9s</strong> '
    'arrived on the coast of Mexico with about <strong>600 soldiers</strong>, '
    'a few cannons, and 16 horses. The Aztecs had never seen horses before '
    'and thought the riders were strange, god-like creatures.\u201d</p>'

    '<p>\u201cMontezuma wasn\u2019t sure what to do,\u201d Jason said. '
    '\u201cSome legends spoke of the god <strong>Quetzalcoatl</strong> returning from the east. '
    'Montezuma sent messengers with gold and gifts, hoping the strangers would take them and leave. '
    'Instead, the gold made Cort\u00e9s more determined to reach Tenochtitlan.\u201d</p>'

    '<h3>The Fall of the Empire</h3>'

    '<p>\u201cCort\u00e9s marched to Tenochtitlan and was welcomed into the city in November 1519. '
    'At first, the Spanish were amazed. The soldier <strong>Bernal D\u00edaz del Castillo</strong> wrote '
    'that the city was like an \u201cenchanted vision\u201d and that nothing in Europe could compare.\u201d</p>'

    '<p>\u201cBut everything fell apart,\u201d Jason continued. '
    '\u201cThe Spanish took Montezuma hostage. Violence broke out. '
    'The Aztecs drove the Spanish from the city on the <strong>Noche Triste</strong> \u2014 '
    'the \u201cSad Night\u201d \u2014 in June 1520, killing many of Cort\u00e9s\u2019s men.\u201d</p>'

    '<p>\u201cBut Cort\u00e9s came back. He allied with Aztec enemies like the <strong>Tlaxcalans</strong>, '
    'who hated paying tribute. Together, they laid siege to Tenochtitlan for <strong>75 days</strong>. '
    'The worst weapon wasn\u2019t swords or cannons \u2014 it was <strong>smallpox</strong>. '
    'The disease, brought by the Europeans, killed millions of indigenous people '
    'who had no immunity to it. Montezuma was already dead, and the new leader, '
    '<strong>Cuauht\u00e9moc</strong>, fought bravely but was captured on <strong>August 13, 1521</strong>.\u201d</p>'

    '<p>\u201cThe Spanish tore Tenochtitlan down and built a new city on top of it \u2014 '
    '<strong>Mexico City</strong>, which is still the capital of Mexico today. '
    'When workers dig beneath the streets, they still find Aztec temples, '
    'sculptures, and artifacts buried below.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 150" width="700" height="150" xmlns="http://www.w3.org/2000/svg" aria-label="Timeline of the Aztec Empire">'
    '<rect width="700" height="150" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Rise and Fall of the Aztec Empire</text>'

    '<rect x="15" y="30" width="130" height="55" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="80" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Founding (1325)</text>'
    '<text x="80" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Eagle on cactus vision</text>'
    '<text x="80" y="76" text-anchor="middle" fill="#b8a88a" font-size="7">Island in Lake Texcoco</text>'

    '<rect x="155" y="30" width="130" height="55" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="220" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Growth (1400s)</text>'
    '<text x="220" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Chinampas feed the city</text>'
    '<text x="220" y="76" text-anchor="middle" fill="#b8a88a" font-size="7">Triple Alliance formed</text>'

    '<rect x="295" y="30" width="130" height="55" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="360" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Peak (1500)</text>'
    '<text x="360" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">200,000\u2013300,000 people</text>'
    '<text x="360" y="76" text-anchor="middle" fill="#b8a88a" font-size="7">500+ tribute city-states</text>'

    '<rect x="435" y="30" width="130" height="55" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="500" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Spanish Arrive (1519)</text>'
    '<text x="500" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Cort\u00e9s lands with 600 men</text>'
    '<text x="500" y="76" text-anchor="middle" fill="#b8a88a" font-size="7">Montezuma sends gold gifts</text>'

    '<rect x="575" y="30" width="110" height="55" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="630" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Fall (1521)</text>'
    '<text x="630" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">75-day siege + smallpox</text>'
    '<text x="630" y="76" text-anchor="middle" fill="#b8a88a" font-size="7">Becomes Mexico City</text>'

    '<text x="350" y="110" text-anchor="middle" fill="#b8a88a" font-size="9">Tenochtitlan was larger than London or Paris \u2014 one of the greatest cities of the 15th century</text>'
    '<text x="350" y="126" text-anchor="middle" fill="#b8a88a" font-size="9">The Aztec flag symbol (eagle on cactus) still appears on Mexico\u2019s flag and coat of arms today</text>'
    '<text x="350" y="142" text-anchor="middle" fill="#e8a838" font-size="8">Cacao beans = money | Xocolatl = chocolate | Chinampas = floating gardens</text>'
    '</svg>'
    '</div>'

    '<p>The green light of The Living World wrapped around them, and the great city on the lake '
    'shimmered and faded away. They were back in the bedroom.</p>'

    '<p>Evelyn was quiet for a long moment. '
    '\u201cThey built the most amazing city in the world on a tiny island,\u201d she said. '
    '\u201cAnd then someone knocked it all down.\u201d</p>'

    '<p>\u201cBut it\u2019s still there, buried under Mexico City,\u201d Jason said. '
    '\u201cEvery time they dig a new subway tunnel, they find another piece of it. '
    'The Aztecs are still being discovered.\u201d</p>'

    '<p>\u201cGoodnight, Tenochtitlan,\u201d Evelyn whispered.</p>'

    '<p>\u201cGoodnight, island city.\u201d</p>'
)

disc_56 = [
    "The Aztecs built one of the largest cities in the world on a small island using chinampas, causeways, and canals. What does it tell you about a civilization when they solve such a difficult engineering problem instead of just finding an easier place to build?",
    "The Aztecs were brilliant engineers, artists, and astronomers, but they also practiced human sacrifice. How should we think about civilizations that achieved great things but also did terrible things?",
    "Cort\u00e9s conquered the Aztec Empire with only 600 soldiers by allying with peoples the Aztecs had forced to pay tribute. What does this tell us about how empires that rely on fear and forced tribute can be vulnerable?"
]

quiz_56 = [
    {
        "q": "What was the name of the Aztec capital built on an island in Lake Texcoco?",
        "options": ["Tlaxcala", "Tenochtitlan", "Teotihuacan", "Texcoco"],
        "correct": 1
    },
    {
        "q": "What were chinampas?",
        "options": ["Stone causeways across the lake", "Floating gardens for growing crops", "Aztec warrior costumes", "Canoes used for trade"],
        "correct": 1
    },
    {
        "q": "What was the most devastating weapon the Spanish brought that helped defeat the Aztecs?",
        "options": ["Cannons", "Horses", "Smallpox", "Steel swords"],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 56:
        lessons[i] = {
            "id": 56,
            "type": "history",
            "topic": "Aztecs",
            "title": "The Island City",
            "readingTime": "10 min",
            "story": story_56,
            "discussion": disc_56,
            "quiz": quiz_56
        }
        print("Updated lesson 56: The Island City")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
