import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_67 = (
    '<h2>Vasco da Gama and New Sea Routes</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Vasco_da_Gama_%28Livro_de_Lisuarte_de_Abreu%29.jpg/800px-Vasco_da_Gama_%28Livro_de_Lisuarte_de_Abreu%29.jpg" '
    'alt="A 16th-century Portuguese illustration of Vasco da Gama" loading="lazy">'
    '<p class="image-caption">Vasco da Gama \u2014 the Portuguese explorer who found the sea route from Europe to India</p>'
    '</div>'

    '<p>The brass telescope was warm to the touch. William turned the hourglass dial, '
    'and the bedroom walls dissolved into the sound of creaking wood and snapping canvas. '
    'The brothers were standing on the deck of a Portuguese <strong>carrack</strong> \u2014 '
    'a massive sailing ship with billowing white sails marked with red crosses.</p>'

    '<p>\u201cWhere are we?\u201d Robert asked, gripping the railing as the ship rolled over a wave.</p>'

    '<p>\u201cThe Indian Ocean, 1498,\u201d William said. \u201cWe\u2019re aboard the <em>S\u00e3o Gabriel</em>, '
    'flagship of <strong>Vasco da Gama</strong>. He\u2019s about to become the first European '
    'to reach India by sea \u2014 and it\u2019s going to change the world.\u201d</p>'

    '<h3>Portugal\u2019s Dream</h3>'

    '<p>\u201cTo understand why this voyage mattered, you have to go back almost a hundred years,\u201d '
    'William said. \u201cIn the early 1400s, Europe was desperate for <strong>spices</strong> \u2014 '
    'pepper, cinnamon, cloves, nutmeg. Spices preserved food, flavored bland meals, '
    'and were used in medicine. They came from India and Southeast Asia, '
    'but they traveled overland through dozens of middlemen \u2014 '
    'Arab merchants, Persian traders, Venetian ships \u2014 '
    'and by the time they reached European markets, the price had been marked up a thousandfold. '
    'A bag of pepper could be worth more than a man\u2019s annual wages.\u201d</p>'

    '<p>\u201cPortugal was a small, poor kingdom on the western edge of Europe, '
    'with no access to the overland spice routes. But it had one advantage: '
    'it faced the Atlantic Ocean. And it had a prince with a vision.\u201d</p>'

    '<h3>Prince Henry the Navigator</h3>'

    '<p>\u201c<strong>Prince Henry the Navigator</strong> never actually sailed on the great voyages himself,\u201d '
    'William explained. \u201cBut starting around 1418, he turned Portugal into the world\u2019s '
    'greatest maritime power. He gathered astronomers, mapmakers, and shipbuilders at Sagres, '
    'on Portugal\u2019s southern tip, and funded expedition after expedition down the coast of Africa.\u201d</p>'

    '<p>\u201cHenry\u2019s captains pushed farther south each year, mapping coastlines no European had ever seen. '
    'They developed a revolutionary ship called the <strong>caravel</strong> \u2014 '
    'small, fast, and able to sail against the wind using triangular <strong>lateen sails</strong> '
    'borrowed from Arab designs. They improved the <strong>astrolabe</strong> and <strong>compass</strong> '
    'for ocean navigation. They charted currents, winds, and stars.\u201d</p>'

    '<p>\u201cHenry died in 1460, but the exploration machine he built kept running. '
    'Portuguese sailors crept down Africa\u2019s west coast \u2014 past Senegal, past the Gold Coast, '
    'past the Congo. They were looking for one thing: a way around the bottom of Africa '
    'that would open a direct sea route to India and its fabled spices.\u201d</p>'

    '<h3>Dias Rounds the Cape</h3>'

    '<p>\u201cIn 1488, <strong>Bartolomeu Dias</strong> finally did it,\u201d William said. '
    '\u201cHe sailed into a terrible storm near the southern tip of Africa. '
    'For thirteen days his ships were battered by wind and waves. '
    'When the storm cleared, Dias realized the coast was now running northeast \u2014 '
    'he had been blown around the bottom of Africa without even seeing it.\u201d</p>'

    '<p>\u201cDias wanted to call it the <strong>Cape of Storms</strong>, but King Jo\u00e3o II of Portugal '
    'renamed it the <strong>Cape of Good Hope</strong> \u2014 because rounding it meant there was '
    'finally hope of reaching India by sea. Dias himself never made it to India. '
    'His terrified crew forced him to turn back. But the path was now known.\u201d</p>'

    '<p>Robert looked out at the endless blue water. \u201cSo that\u2019s where da Gama comes in?\u201d</p>'

    '<h3>Vasco da Gama\u2019s Voyage</h3>'

    '<p>\u201cExactly,\u201d William said. \u201cNine years later, in July 1497, '
    '<strong>Vasco da Gama</strong> left Lisbon with four ships and about 170 men. '
    'His mission: finish what Dias started \u2014 sail around Africa and reach India.\u201d</p>'

    '<p>\u201cThe voyage was brutal. Da Gama didn\u2019t hug the African coast like previous explorers. '
    'Instead, he swung far out into the Atlantic \u2014 a daring maneuver to catch favorable winds \u2014 '
    'spending 96 days out of sight of land, the longest open-ocean voyage anyone had ever attempted. '
    'Scurvy ravaged his crew. Their gums bled, their teeth fell out, '
    'and men died in the swaying darkness below deck.\u201d</p>'

    '<p>\u201cHe rounded the Cape of Good Hope in November 1497, '
    'then sailed up Africa\u2019s east coast. In Malindi (modern Kenya), '
    'he hired an Arab navigator named <strong>Ahmad ibn Majid</strong> '
    'who knew the monsoon winds of the Indian Ocean. '
    'With ibn Majid\u2019s guidance, da Gama crossed the Indian Ocean in just 23 days.\u201d</p>'

    '<p>\u201cOn May 20, 1498, the <em>S\u00e3o Gabriel</em> dropped anchor at <strong>Calicut</strong> '
    '(modern Kozhikode) on India\u2019s southwest coast. Da Gama had done it. '
    'The sea route from Europe to India was open.\u201d</p>'

    '<h3>The Spice Trade Transformed</h3>'

    '<p>\u201cThe local ruler, the <strong>Zamorin</strong> of Calicut, was unimpressed,\u201d William said. '
    '\u201cDa Gama\u2019s gifts \u2014 cloth, honey, and coral \u2014 were laughable compared to '
    'what Arab and Chinese merchants brought. The Zamorin said, '
    '\u2018The poorest merchant from Mecca brings more than this.\u2019\u201d</p>'

    '<p>\u201cBut it didn\u2019t matter. Da Gama loaded his ships with pepper and cinnamon '
    'and sailed home. When he arrived in Lisbon in September 1499 \u2014 '
    'after two years and 24,000 miles \u2014 his cargo was worth 60 times the cost of the entire expedition. '
    'Portugal had struck gold. Or rather, it had struck pepper, '
    'which at the time was just as valuable.\u201d</p>'

    '<p>\u201cWithin a decade, Portugal built a <strong>trading empire</strong> '
    'stretching from Brazil to Japan. They established fortified trading posts \u2014 '
    'called <strong>feitorias</strong> \u2014 at Goa, Malacca, Hormuz, and Macau. '
    'They didn\u2019t conquer vast territories like the Romans. '
    'Instead, they controlled the <strong>chokepoints</strong> of global trade \u2014 '
    'the straits, harbors, and islands where goods had to pass.\u201d</p>'

    '<h3>Impact on the Indian Ocean World</h3>'

    '<p>\u201cFor centuries before Portugal arrived, the Indian Ocean had been a peaceful trading network,\u201d '
    'William said. \u201cArab, Indian, Chinese, Malay, and East African merchants '
    'traded freely without any single power controlling the sea lanes. '
    'Ships sailed with the monsoon winds \u2014 southwest in summer, northeast in winter \u2014 '
    'in a rhythm that had worked for a thousand years.\u201d</p>'

    '<p>\u201cPortugal shattered that system. They brought <strong>cannons</strong> to a world '
    'where merchant ships were unarmed. Under commanders like <strong>Afonso de Albuquerque</strong>, '
    'the Portuguese demanded that every ship in the Indian Ocean buy a license (<strong>cartaz</strong>) '
    'or be sunk. They bombarded cities that resisted \u2014 '
    'Calicut, Kilwa, Mombasa. They seized Goa in 1510 and made it their Asian capital.\u201d</p>'

    '<p>\u201cThe ancient, open trading world of the Indian Ocean '
    'was replaced by a system enforced at cannon-point. '
    'It was the beginning of European colonial power in Asia \u2014 '
    'a story that would unfold over the next 450 years.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 140" width="700" height="140" xmlns="http://www.w3.org/2000/svg" aria-label="Portuguese Exploration Timeline">'
    '<rect width="700" height="140" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Portugal\u2019s Age of Exploration</text>'

    '<line x1="80" y1="45" x2="620" y2="45" stroke="#b8a88a" stroke-width="2"/>'

    '<circle cx="100" cy="45" r="5" fill="#e8a838"/>'
    '<text x="100" y="38" text-anchor="middle" fill="#e8a838" font-size="8" font-weight="bold">1418</text>'
    '<text x="100" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Prince Henry</text>'
    '<text x="100" y="72" text-anchor="middle" fill="#b8a88a" font-size="7">begins voyages</text>'

    '<circle cx="240" cy="45" r="5" fill="#e74c3c"/>'
    '<text x="240" y="38" text-anchor="middle" fill="#e74c3c" font-size="8" font-weight="bold">1488</text>'
    '<text x="240" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Dias rounds</text>'
    '<text x="240" y="72" text-anchor="middle" fill="#b8a88a" font-size="7">Cape of Good Hope</text>'

    '<circle cx="380" cy="45" r="5" fill="#4a90d9"/>'
    '<text x="380" y="38" text-anchor="middle" fill="#4a90d9" font-size="8" font-weight="bold">1498</text>'
    '<text x="380" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Da Gama</text>'
    '<text x="380" y="72" text-anchor="middle" fill="#b8a88a" font-size="7">reaches India</text>'

    '<circle cx="500" cy="45" r="5" fill="#2ecc71"/>'
    '<text x="500" y="38" text-anchor="middle" fill="#2ecc71" font-size="8" font-weight="bold">1510</text>'
    '<text x="500" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Albuquerque</text>'
    '<text x="500" y="72" text-anchor="middle" fill="#b8a88a" font-size="7">seizes Goa</text>'

    '<circle cx="600" cy="45" r="5" fill="#9b59b6"/>'
    '<text x="600" y="38" text-anchor="middle" fill="#9b59b6" font-size="8" font-weight="bold">1550s</text>'
    '<text x="600" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Trading posts</text>'
    '<text x="600" y="72" text-anchor="middle" fill="#b8a88a" font-size="7">Brazil to Japan</text>'

    '<text x="350" y="100" text-anchor="middle" fill="#b8a88a" font-size="9">Lisbon \u2192 Cape of Good Hope \u2192 Calicut: 24,000 miles round trip</text>'
    '<text x="350" y="115" text-anchor="middle" fill="#b8a88a" font-size="9">Da Gama\u2019s cargo was worth 60\u00d7 the cost of the expedition</text>'
    '<text x="350" y="130" text-anchor="middle" fill="#b8a88a" font-size="9">96 days out of sight of land \u2014 longest open-ocean voyage ever attempted</text>'
    '</svg>'
    '</div>'

    '<p>The telescope glowed, and the brothers were back in their room. '
    'Robert could still taste the salt air.</p>'

    '<p>\u201cA bag of pepper changed the world,\u201d Robert said quietly.</p>'

    '<p>\u201cPeople will do extraordinary things for ordinary things,\u201d William replied. '
    '\u201cEspecially when those ordinary things cost a fortune. '
    'Goodnight, explorers.\u201d</p>'

    '<p>\u201cGoodnight, spice ships.\u201d</p>'
)

disc_67 = [
    "Prince Henry the Navigator never sailed on the great voyages himself, but he made them all possible by funding exploration and gathering experts. Can you think of other examples where someone who didn\u2019t do the famous deed was just as important as the person who did?",
    "The Portuguese brought cannons to an Indian Ocean world where merchant ships were unarmed. Was their trading empire built on innovation or on violence? Can it be both at the same time?",
    "Da Gama\u2019s cargo was worth 60 times the cost of his expedition, but many of his sailors died of scurvy along the way. When is a discovery \u2018worth the cost\u2019 and who gets to decide?"
]

quiz_67 = [
    {
        "q": "Who organized Portugal\u2019s early exploration voyages down the coast of Africa?",
        "options": [
            "Vasco da Gama",
            "Bartolomeu Dias",
            "Prince Henry the Navigator",
            "Afonso de Albuquerque"
        ],
        "correct": 2
    },
    {
        "q": "What did Bartolomeu Dias accomplish in 1488?",
        "options": [
            "Reached India by sea",
            "Sailed around the Cape of Good Hope",
            "Discovered Brazil",
            "Conquered Goa"
        ],
        "correct": 1
    },
    {
        "q": "Why was Vasco da Gama\u2019s 1498 voyage to India so important?",
        "options": [
            "He discovered a new continent",
            "He opened a direct sea route from Europe to India\u2019s spice trade",
            "He defeated the Ottoman Empire at sea",
            "He mapped the entire Pacific Ocean"
        ],
        "correct": 1
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 67:
        lessons[i] = {
            "id": 67,
            "type": "history",
            "topic": "Exploration",
            "title": "Vasco da Gama and New Sea Routes",
            "readingTime": "10 min",
            "story": story_67,
            "discussion": disc_67,
            "quiz": quiz_67
        }
        print("Updated lesson 67: Vasco da Gama and New Sea Routes")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
