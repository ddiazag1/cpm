import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_59 = (
    '<h2>Sailors of the North</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Gokstad_viking_ship_-_IMG_9303.jpg/800px-Gokstad_viking_ship_-_IMG_9303.jpg" '
    'alt="The Gokstad Viking ship in a museum" loading="lazy">'
    '<p class="image-caption">The Gokstad ship \u2014 a 9th-century Viking longship discovered in a burial mound in Norway</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass dial turned, and the brothers appeared on a rocky coastline '
    'where gray waves crashed against granite cliffs. A long, narrow ship with a carved dragon head '
    'was being pushed into the freezing surf by men in wool and leather.</p>'

    '<p>\u201cWelcome to Scandinavia,\u201d William said. \u201cAbout 800 AD. '
    'The age of the <strong>Vikings</strong> is beginning.\u201d</p>'

    '<h3>Who Were the Vikings?</h3>'

    '<p>\u201cThe Vikings came from <strong>Scandinavia</strong> \u2014 '
    'modern-day <strong>Norway, Sweden, and Denmark</strong>,\u201d William said. '
    '\u201cThe word \u2018Viking\u2019 probably comes from an Old Norse word meaning '
    '\u2018pirate raid\u2019 or \u2018overseas adventure.\u2019 '
    'But most Vikings weren\u2019t actually raiders. They were farmers, traders, craftspeople, '
    'and storytellers. Only a fraction went on raids \u2014 '
    'but those raids changed the map of Europe.\u201d</p>'

    '<p>\u201cWhy did they leave home? Scandinavia was cold, mountainous, '
    'and had limited farmland. As populations grew, younger sons who wouldn\u2019t inherit land '
    'looked overseas for opportunity. Some went to raid. Some went to trade. '
    'Some went to find new homes.\u201d</p>'

    '<h3>The Longship \u2014 Greatest Vessel of the Age</h3>'

    '<p>\u201cThe secret to Viking success was this,\u201d William pointed to the ship gliding into the waves. '
    '\u201cThe <strong>longship</strong>. It was a masterpiece of engineering \u2014 '
    'light enough to carry overland between rivers, shallow enough to sail up rivers and land on beaches, '
    'yet strong enough to cross the open Atlantic Ocean.\u201d</p>'

    '<p>\u201cLongships were built from overlapping oak planks (<strong>clinker-built</strong>), '
    'held together with iron rivets. They could be powered by sails or oars, '
    'meaning they could keep moving even when the wind died. '
    'A typical longship was about 75 feet long and could carry 60\u201380 warriors. '
    'The shallow draft \u2014 only 3 feet of water \u2014 meant Vikings could sail '
    'far up rivers that no other ships could navigate.\u201d</p>'

    '<h3>Raiders, Traders, and Explorers</h3>'

    '<p>\u201cIn 793 AD, Vikings attacked the monastery at <strong>Lindisfarne</strong> '
    'on the coast of England,\u201d William said. \u201cIt shocked all of Europe. '
    'From that moment, Viking raids terrorized coastlines from Ireland to Constantinople. '
    'They raided monasteries (which were rich and undefended), '
    'captured people to sell as slaves, and demanded silver as ransom.\u201d</p>'

    '<p>\u201cBut Vikings were also extraordinary <strong>traders</strong>. '
    'Swedish Vikings \u2014 called the <strong>Rus</strong> \u2014 traveled east along Russian rivers '
    'all the way to Constantinople (modern Istanbul) and Baghdad. '
    'They traded furs, amber, and walrus ivory for silver, silk, and spices. '
    'The word \u2018Russia\u2019 comes from the Rus Vikings who settled there.\u201d</p>'

    '<p>\u201cAnd they were the greatest <strong>explorers</strong> of their age. '
    'Norwegian Vikings settled <strong>Iceland</strong> around 870, '
    '<strong>Greenland</strong> around 985 (led by <strong>Erik the Red</strong>), '
    'and reached <strong>North America</strong> around 1000 AD \u2014 '
    'nearly 500 years before Columbus. <strong>Leif Erikson</strong>, Erik\u2019s son, '
    'established a settlement at <strong>L\u2019Anse aux Meadows</strong> in Newfoundland, Canada. '
    'The ruins were discovered in 1960, proving the Vikings beat Columbus to America by five centuries.\u201d</p>'

    '<h3>Viking Culture</h3>'

    '<p>\u201cVikings worshipped gods like <strong>Odin</strong> (god of wisdom and war), '
    '<strong>Thor</strong> (god of thunder), and <strong>Freya</strong> (goddess of love),\u201d William said. '
    '\u201cOur days of the week come from Viking gods: Tuesday (Tyr), Wednesday (Woden/Odin), '
    'Thursday (Thor), Friday (Freya).\u201d</p>'

    '<p>\u201cThey passed down their history through oral poems called <strong>sagas</strong> \u2014 '
    'epic stories of heroes, gods, and voyages that were eventually written down in Iceland. '
    'They wrote in a runic alphabet called <strong>futhark</strong>, carving messages on stones, '
    'weapons, and jewelry.\u201d</p>'

    '<p>\u201cViking women had more rights than most European women of the time. '
    'They could own property, request a divorce, and manage the household economy. '
    'When men were away on voyages, women ran the farms and businesses.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Viking Age">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Viking Age (793\u20131066 AD)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Raiders</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Lindisfarne (793 AD)</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Terrorized European coasts</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Traders</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Rivers to Constantinople</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Furs, amber \u2194 silver, silk</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Explorers</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Iceland \u2192 Greenland \u2192 America</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">500 years before Columbus</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Settlers</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Normandy, England, Russia</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Shaped modern Europe</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Tuesday, Wednesday, Thursday, Friday \u2014 all named after Viking gods</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">\u201cRussia\u201d comes from the Rus Vikings who settled along its rivers</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. The dragon ship was gone, '
    'but Robert could still feel the salt spray on his face.</p>'

    '<p>\u201cThey reached America 500 years before Columbus,\u201d Robert said. '
    '\u201cWhy doesn\u2019t everyone know that?\u201d</p>'

    '<p>\u201cHistory remembers the people who stayed, not always the ones who arrived first,\u201d '
    'William said. \u201cGoodnight, sailors of the north.\u201d</p>'

    '<p>\u201cGoodnight, dragon ships.\u201d</p>'
)

disc_59 = [
    "Vikings are often remembered as brutal raiders, but they were also traders, explorers, farmers, and poets. Why do you think the violent parts of history are remembered more than the peaceful parts?",
    "Leif Erikson reached North America 500 years before Columbus, but the Viking settlement didn\u2019t last. What makes the difference between discovering a place and truly changing its history?",
    "Our days of the week are named after Viking gods. What other parts of modern life were shaped by cultures most people have forgotten about?"
]

quiz_59 = [
    {
        "q": "Where did Leif Erikson establish a settlement in North America?",
        "options": ["Plymouth Rock", "Jamestown", "L\u2019Anse aux Meadows", "Manhattan"],
        "correct": 2
    },
    {
        "q": "What was the Vikings\u2019 greatest technological advantage?",
        "options": ["Iron weapons", "The longship", "Gunpowder", "Horseback riding"],
        "correct": 1
    },
    {
        "q": "Which modern country\u2019s name comes from the Viking Rus people?",
        "options": ["Finland", "Poland", "Russia", "Iceland"],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 59:
        lessons[i] = {
            "id": 59,
            "type": "history",
            "topic": "Vikings",
            "title": "Sailors of the North",
            "readingTime": "10 min",
            "story": story_59,
            "discussion": disc_59,
            "quiz": quiz_59
        }
        print("Updated lesson 59: Sailors of the North")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
