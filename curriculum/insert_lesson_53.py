import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_53 = (
    '<h2>The Empire of Kings</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Persepolis_24.11.2009_11-12-14.jpg/800px-Persepolis_24.11.2009_11-12-14.jpg" '
    'alt="The ruins of Persepolis, the ceremonial capital of the Persian Empire" loading="lazy">'
    '<p class="image-caption">Persepolis \u2014 the magnificent ceremonial capital of the Persian Empire</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass dial glowed, and the brothers appeared on a wide stone terrace. '
    'Enormous columns rose around them, carved with winged bulls and bearded warriors. '
    'Below, a grand staircase depicted people from dozens of nations bringing gifts.</p>'

    '<p>\u201cThis is <strong>Persepolis</strong>,\u201d William said. \u201cThe heart of the largest empire '
    'the world has ever seen \u2014 so far.\u201d</p>'

    '<h3>Cyrus the Great</h3>'

    '<p>\u201cThe Persian Empire began with one man: <strong>Cyrus the Great</strong>,\u201d William said. '
    '\u201cIn 550 BC, Cyrus was the king of a small kingdom called Persia, in what is now Iran. '
    'Within 20 years, he conquered the <strong>Medes</strong>, the <strong>Lydians</strong>, '
    'and the <strong>Babylonians</strong>, creating an empire stretching from the Aegean Sea to Central Asia.\u201d</p>'

    '<p>\u201cBut what made Cyrus special wasn\u2019t just his military genius \u2014 it was his mercy. '
    'When he conquered Babylon in 539 BC, instead of destroying the city and enslaving its people, '
    'he freed the captives, restored their temples, and allowed exiled peoples to return home. '
    'This included the <strong>Jewish people</strong>, who had been held captive in Babylon for nearly 50 years. '
    'Cyrus let them return to Jerusalem and rebuild their temple.\u201d</p>'

    '<p>\u201cCyrus issued what many scholars consider the first declaration of <strong>human rights</strong> \u2014 '
    'the <strong>Cyrus Cylinder</strong>, a clay document declaring that conquered peoples '
    'could keep their religions, customs, and traditions. A replica sits at the United Nations today.\u201d</p>'

    '<h3>Darius and the Empire\u2019s Peak</h3>'

    '<p>\u201cUnder <strong>Darius I</strong> (who ruled from 522\u2013486 BC), '
    'the empire reached its greatest extent,\u201d William continued. '
    '\u201cIt stretched from <strong>Egypt and Libya</strong> in the west '
    'to the <strong>Indus River</strong> in the east \u2014 over 3 million square miles, '
    'ruling perhaps 44 percent of the world\u2019s population. '
    'No empire in history has ever contained a higher percentage of humanity.\u201d</p>'

    '<p>\u201cDarius was a brilliant administrator. He divided the empire into '
    '<strong>20 provinces called satrapies</strong>, each governed by a <strong>satrap</strong> (governor) '
    'who collected taxes and kept order. He built the <strong>Royal Road</strong> \u2014 '
    'a 1,600-mile highway from Susa to Sardis with relay stations where mounted couriers '
    'could change horses. A message could travel the entire length in just 7 days \u2014 '
    'a speed not matched until the telegraph, 2,300 years later.\u201d</p>'

    '<p>\u201cDarius also introduced a standard currency \u2014 the <strong>gold daric</strong> \u2014 '
    'which made trade across the empire far easier. He built canals, standardized weights and measures, '
    'and commissioned this very palace \u2014 Persepolis \u2014 as the ceremonial showpiece of his empire.\u201d</p>'

    '<h3>The Persian Wars</h3>'

    '<p>\u201cThe Persians\u2019 greatest challenge came from a collection of tiny city-states '
    'on the western edge of their empire: <strong>Greece</strong>,\u201d William said. '
    '\u201cIn 490 BC, Darius sent an army to punish Athens for supporting a revolt. '
    'Against all odds, the Athenians defeated the Persians at the <strong>Battle of Marathon</strong>. '
    'Legend says a messenger ran 26 miles from Marathon to Athens to announce the victory \u2014 '
    'that\u2019s where the modern marathon race gets its name and distance.\u201d</p>'

    '<p>\u201cTen years later, Darius\u2019s son <strong>Xerxes</strong> returned with an even larger army \u2014 '
    'perhaps 200,000 soldiers. At the narrow pass of <strong>Thermopylae</strong>, '
    '300 Spartan warriors and a few thousand Greek allies held off the entire Persian army '
    'for three days, buying time for Greece to organize its defense. '
    'The Greeks eventually defeated the Persian fleet at the <strong>Battle of Salamis</strong>, '
    'and the Persian invasion of Europe was over.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Persian Empire">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Persian (Achaemenid) Empire</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Cyrus the Great</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Founded empire (550 BC)</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">First human rights declaration</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Darius I</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Peak: 44% of world population</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Royal Road, gold daric, satrapies</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Persian Wars</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Marathon (490 BC)</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Thermopylae &amp; Salamis (480 BC)</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Legacy</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Model for future empires</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Tolerance + infrastructure</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">The Persians proved that a vast empire could be held together by roads, laws, and tolerance</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">\u2014 not just by fear and force</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. Robert was quiet for a moment.</p>'

    '<p>\u201cCyrus freed people instead of enslaving them,\u201d he said. '
    '\u201cThat\u2019s not what I expected from an ancient conqueror.\u201d</p>'

    '<p>\u201cThe best leaders build things that outlast them,\u201d William said. '
    '\u201cGoodnight, empire of kings.\u201d</p>'

    '<p>\u201cGoodnight, Royal Road.\u201d</p>'
)

disc_53 = [
    "Cyrus the Great conquered a vast empire but was famous for his tolerance and mercy. Is it possible to be both a conqueror and a just ruler? Can you think of modern examples?",
    "The Cyrus Cylinder is sometimes called the first declaration of human rights. Why is it important that a powerful ruler chose to protect the rights of conquered peoples?",
    "300 Spartans held off the Persian army at Thermopylae. What makes the story of a small group standing against overwhelming odds so inspiring across cultures and centuries?"
]

quiz_53 = [
    {
        "q": "What is the Cyrus Cylinder sometimes called?",
        "options": [
            "The first book of law",
            "The first declaration of human rights",
            "The first peace treaty",
            "The first constitution"
        ],
        "correct": 1
    },
    {
        "q": "How did Darius I organize his vast empire?",
        "options": [
            "He let each city govern itself",
            "He divided it into 20 provinces called satrapies",
            "He appointed a single governor for the whole empire",
            "He ruled each province personally"
        ],
        "correct": 1
    },
    {
        "q": "Where does the modern marathon race get its name and distance?",
        "options": [
            "A Greek soldier who ran from Marathon to Athens",
            "A Persian courier on the Royal Road",
            "An Olympic event in ancient Persia",
            "A footrace through the streets of Sparta"
        ],
        "correct": 0
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 53:
        lessons[i] = {
            "id": 53,
            "type": "history",
            "topic": "Persia",
            "title": "The Empire of Kings",
            "readingTime": "10 min",
            "story": story_53,
            "discussion": disc_53,
            "quiz": quiz_53
        }
        print("Updated lesson 53: The Empire of Kings")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
