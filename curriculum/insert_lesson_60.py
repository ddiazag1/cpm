import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_60 = (
    '<h2>Castles and Knights</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Carcassonne_wall.jpg/800px-Carcassonne_wall.jpg" '
    'alt="The medieval walled city of Carcassonne, France" loading="lazy">'
    '<p class="image-caption">Carcassonne, France \u2014 one of the best-preserved medieval walled cities in Europe</p>'
    '</div>'

    '<p>Evelyn was reading a fairy tale about a princess in a tower when she looked up. '
    '\u201cJason, were castles real?\u201d</p>'

    '<p>Jason opened The Living World and turned the brass clasp. '
    '\u201cMore real than any fairy tale. Let\u2019s go see one.\u201d</p>'

    '<p>The green light deposited them on a muddy road leading toward an enormous stone fortress. '
    'Banners fluttered from the towers, horses clattered across a drawbridge, '
    'and the smell of woodsmoke and manure filled the air.</p>'

    '<h3>The Middle Ages Begin</h3>'

    '<p>\u201cWe\u2019re in Europe, around 1100 AD \u2014 the heart of the <strong>Middle Ages</strong>,\u201d '
    'Jason said. \u201cAfter the Roman Empire fell in 476 AD, Europe shattered into hundreds '
    'of small kingdoms, duchies, and territories. There was no central government, '
    'no organized army, no common law. People lived in constant fear of attack '
    'from Vikings, bandits, or rival lords.\u201d</p>'

    '<p>\u201cIn this chaos, a system called <strong>feudalism</strong> emerged. '
    'It was a deal: a powerful lord gave land (called a <strong>fief</strong>) to a lesser noble '
    '(a <strong>vassal</strong>), and in return, the vassal pledged military service and loyalty. '
    'The vassal\u2019s land was worked by <strong>peasants</strong> and <strong>serfs</strong>, '
    'who gave most of their harvest to the lord in exchange for protection. '
    'It wasn\u2019t fair, but it was order in a world without order.\u201d</p>'

    '<h3>The Knight\u2019s Life</h3>'

    '<p>\u201c<strong>Knights</strong> were the medieval world\u2019s elite warriors,\u201d Jason said. '
    '\u201cBecoming a knight was a long process. A boy of noble birth would become a <strong>page</strong> at age 7, '
    'learning manners, horsemanship, and basic combat. At 14, he became a <strong>squire</strong>, '
    'serving a knight directly \u2014 carrying his weapons, helping him into his armor, '
    'and training in real combat. If he proved worthy, he was <strong>knighted</strong> at about age 21 '
    'in a solemn ceremony where he swore an oath of chivalry.\u201d</p>'

    '<p>\u201cThe code of <strong>chivalry</strong> demanded that a knight be brave, loyal, '
    'protect the weak, honor women, fight fairly, and serve God. '
    'In reality, many knights fell short of these ideals \u2014 '
    'but the idea of chivalry shaped European culture for centuries.\u201d</p>'

    '<p>\u201cA knight\u2019s armor evolved over the centuries. Early knights wore <strong>chain mail</strong> \u2014 '
    'shirts made of thousands of interlocking metal rings. '
    'By the 1400s, full <strong>plate armor</strong> covered the entire body. '
    'A complete suit weighed 45\u201355 pounds and cost as much as a small farm. '
    'Despite the weight, a trained knight could run, mount a horse, and fight effectively.\u201d</p>'

    '<h3>Castles \u2014 Fortresses of Stone</h3>'

    '<p>\u201cCastles were both homes and military fortresses,\u201d Jason continued. '
    '\u201cThe first castles were simple wooden towers on earthen mounds (<strong>motte-and-bailey</strong>). '
    'By the 1100s, they were massive stone structures with thick walls, moats, drawbridges, '
    'and murder holes (openings in ceilings where defenders poured boiling water or oil on attackers).\u201d</p>'

    '<p>\u201cThe <strong>keep</strong> was the strongest tower \u2014 the last line of defense. '
    'Walls could be 10 feet thick. The tallest towers reached 100 feet. '
    'A well-built castle could hold out against a besieging army for months or even years, '
    'as long as food and water lasted.\u201d</p>'

    '<h3>Life for Everyone Else</h3>'

    '<p>\u201cWhile lords and knights lived in castles, most people were <strong>peasants</strong> '
    'who worked the land,\u201d Jason said. \u201cAbout 90 percent of the population farmed. '
    'Serfs were bound to the land \u2014 they couldn\u2019t leave without the lord\u2019s permission. '
    'They worked from dawn to dusk, gave a portion of their harvest to the lord, '
    'paid taxes to the Church, and lived in small one-room houses with dirt floors.\u201d</p>'

    '<p>\u201cBut medieval life wasn\u2019t all misery. Villages had festivals, fairs, and feast days. '
    'The <strong>Church</strong> was the center of community life. Magnificent <strong>cathedrals</strong> '
    'took generations to build \u2014 Notre-Dame de Paris took nearly 200 years. '
    'Monks in monasteries preserved ancient Roman and Greek texts, brewed beer, '
    'made cheese, and ran the only schools and hospitals.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Feudal system">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Feudal Pyramid</text>'

    '<rect x="250" y="28" width="200" height="22" rx="4" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="350" y="43" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">King</text>'

    '<rect x="190" y="54" width="320" height="22" rx="4" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="350" y="69" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Lords &amp; Nobles (received fiefs)</text>'

    '<rect x="130" y="80" width="440" height="22" rx="4" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="350" y="95" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Knights (military service in exchange for land)</text>'

    '<rect x="70" y="106" width="560" height="22" rx="4" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="350" y="121" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Peasants &amp; Serfs (90% of population \u2014 worked the land)</text>'
    '</svg>'
    '</div>'

    '<p>The book carried them home. Evelyn looked thoughtful.</p>'

    '<p>\u201cThe fairy tales leave out the mud and the smell,\u201d she said.</p>'

    '<p>\u201cAnd the 90 percent who weren\u2019t princesses or knights,\u201d Jason agreed. '
    '\u201cGoodnight, castles.\u201d</p>'

    '<p>\u201cGoodnight, knights in muddy armor.\u201d</p>'
)

disc_60 = [
    "In feudalism, serfs gave up freedom in exchange for protection. Do you think that was a fair trade? Can you think of any modern situations where people trade freedom for security?",
    "Knights swore a code of chivalry but often didn\u2019t follow it. Why do you think societies create ideals that people struggle to live up to? Is the ideal still valuable even if it\u2019s not always followed?",
    "90% of medieval people were peasants who rarely appear in stories or movies. Why does history tend to focus on kings and knights instead of ordinary people?"
]

quiz_60 = [
    {
        "q": "What was the feudal system?",
        "options": [
            "A type of government with elected officials",
            "A system where lords gave land in exchange for military service",
            "A religious organization run by the Church",
            "A trading network between castles"
        ],
        "correct": 1
    },
    {
        "q": "What were the stages of becoming a knight?",
        "options": [
            "Student, apprentice, master",
            "Servant, soldier, captain",
            "Page, squire, knight",
            "Peasant, archer, cavalry"
        ],
        "correct": 2
    },
    {
        "q": "What percentage of medieval Europeans were peasants or serfs?",
        "options": ["About 50%", "About 70%", "About 90%", "About 30%"],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 60:
        lessons[i] = {
            "id": 60,
            "type": "history",
            "topic": "Medieval",
            "title": "Castles and Knights",
            "readingTime": "10 min",
            "story": story_60,
            "discussion": disc_60,
            "quiz": quiz_60
        }
        print("Updated lesson 60: Castles and Knights")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
