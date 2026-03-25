import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_52 = (
    '<h2>The People Who Gave Us Letters</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Sarcophagus_of_Ahiram_inscription.jpg/800px-Sarcophagus_of_Ahiram_inscription.jpg" '
    'alt="Ancient Phoenician inscription on the sarcophagus of Ahiram" loading="lazy">'
    '<p class="image-caption">The sarcophagus of King Ahiram \u2014 bearing one of the oldest known alphabetic inscriptions (c. 1000 BC)</p>'
    '</div>'

    '<p>Evelyn was tracing the alphabet on a piece of paper \u2014 A, B, C, D \u2014 '
    'when she stopped. \u201cJason, who invented the alphabet?\u201d</p>'

    '<p>Jason opened The Living World and turned the brass clasp to the hourglass symbol. '
    '\u201cLet\u2019s go meet them.\u201d</p>'

    '<p>The green light swirled, and they stood on a busy wooden dock. '
    'Ships with bright purple sails crowded the harbor, and the air smelled of salt, cedar, and dye.</p>'

    '<h3>The Phoenicians \u2014 Sailors and Traders</h3>'

    '<p>\u201cWe\u2019re in <strong>Tyre</strong>, one of the great cities of <strong>Phoenicia</strong>,\u201d Jason said. '
    '\u201cAbout 1000 BC. The Phoenicians lived along a narrow strip of coast '
    'on the eastern Mediterranean \u2014 roughly where <strong>Lebanon</strong> is today. '
    'They never built a great empire or conquered vast lands. '
    'Instead, they did something far more lasting: they became the greatest <strong>sailors and traders</strong> '
    'the ancient world had ever seen.\u201d</p>'

    '<p>\u201cPhoenician ships sailed the entire Mediterranean Sea. They established <strong>trading colonies</strong> '
    'on distant shores \u2014 the most famous being <strong>Carthage</strong> in North Africa, '
    'which would one day challenge Rome itself. They may have even sailed around the entire continent of Africa '
    '\u2014 2,000 years before any European managed it.\u201d</p>'

    '<h3>The Purple People</h3>'

    '<p>\u201cSee those purple sails?\u201d Jason pointed. \u201cThe Phoenicians were famous for making '
    '<strong>Tyrian purple</strong> \u2014 a dye so rare and beautiful that it became the color of royalty. '
    'It came from a type of sea snail called the <strong>murex</strong>. '
    'It took about 12,000 snails to produce just 1.5 grams of dye \u2014 '
    'enough to color the trim of a single garment. That\u2019s why purple was worth more than gold.\u201d</p>'

    '<p>\u201cThe word \u2018Phoenician\u2019 probably comes from the Greek word <em>phoinix</em>, '
    'meaning \u2018purple-red.\u2019 They were literally \u2018the purple people.\u2019\u201d</p>'

    '<h3>The Greatest Gift \u2014 The Alphabet</h3>'

    '<p>\u201cBut the Phoenicians\u2019 most important invention wasn\u2019t dye or ships,\u201d Jason said. '
    '\u201cIt was the <strong>alphabet</strong>.\u201d</p>'

    '<p>\u201cBefore the Phoenicians, writing systems were incredibly complicated. '
    'Egyptian hieroglyphics had hundreds of symbols. Mesopotamian cuneiform had over 600. '
    'Chinese characters numbered in the thousands. You had to study for years just to read and write, '
    'which meant literacy was limited to a tiny elite of scribes and priests.\u201d</p>'

    '<p>\u201cAround 1050 BC, the Phoenicians developed something revolutionary: '
    'a writing system with just <strong>22 symbols</strong>, each representing a single consonant sound. '
    'Instead of memorizing hundreds of pictures, you only needed to learn 22 letters. '
    'Suddenly, ordinary merchants and sailors could read and write \u2014 '
    'not just priests and scholars.\u201d</p>'

    '<p>\u201cThe letter <strong>aleph</strong> (\u2018ox\u2019) became our A. '
    '<strong>Beth</strong> (\u2018house\u2019) became B. <strong>Gimel</strong> (\u2018camel\u2019) became C and G. '
    '<strong>Daleth</strong> (\u2018door\u2019) became D. The very word \u2018alphabet\u2019 '
    'comes from the first two Phoenician letters: <em>aleph-beth</em>.\u201d</p>'

    '<h3>From Phoenicia to the World</h3>'

    '<p>\u201cThe Greeks adopted the Phoenician alphabet around 800 BC and made a crucial improvement: '
    'they added <strong>vowels</strong>. The Phoenician system only wrote consonants '
    '\u2014 readers had to figure out the vowels from context. '
    'The Greeks turned unused Phoenician consonant letters into vowel symbols: '
    'aleph became <strong>alpha (A)</strong>, he became <strong>epsilon (E)</strong>.\u201d</p>'

    '<p>\u201cThe Romans then adapted the Greek alphabet into the <strong>Latin alphabet</strong> \u2014 '
    'the same 26 letters you were writing on that paper, Evelyn. '
    'The Arabic, Hebrew, and Aramaic writing systems also descend from the Phoenician alphabet. '
    'So does the script used to write Hindi, Bengali, and dozens of other South Asian languages. '
    'Nearly every alphabet on Earth traces back to those 22 Phoenician symbols.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Evolution of the alphabet">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">From Phoenician Letters to Your ABC\u2019s</text>'

    '<rect x="30" y="32" width="130" height="45" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="95" y="50" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Phoenician</text>'
    '<text x="95" y="63" text-anchor="middle" fill="#b8a88a" font-size="8">22 consonants (~1050 BC)</text>'

    '<text x="175" y="57" fill="#e8a838" font-size="14">\u2192</text>'

    '<rect x="195" y="32" width="130" height="45" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="260" y="50" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Greek</text>'
    '<text x="260" y="63" text-anchor="middle" fill="#b8a88a" font-size="8">Added vowels (~800 BC)</text>'

    '<text x="340" y="57" fill="#e8a838" font-size="14">\u2192</text>'

    '<rect x="360" y="32" width="130" height="45" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="425" y="50" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Latin/Roman</text>'
    '<text x="425" y="63" text-anchor="middle" fill="#b8a88a" font-size="8">26 letters (~600 BC)</text>'

    '<text x="505" y="57" fill="#e8a838" font-size="14">\u2192</text>'

    '<rect x="525" y="32" width="150" height="45" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="600" y="50" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Modern English</text>'
    '<text x="600" y="63" text-anchor="middle" fill="#b8a88a" font-size="8">Same 26 letters today</text>'

    '<text x="350" y="100" text-anchor="middle" fill="#b8a88a" font-size="9">Also spawned: Arabic, Hebrew, Aramaic, Brahmi (Hindi/Bengali/Thai), Cyrillic (Russian)</text>'
    '<text x="350" y="115" text-anchor="middle" fill="#b8a88a" font-size="9">Nearly every alphabet on Earth descends from Phoenician letters</text>'
    '</svg>'
    '</div>'

    '<p>The book brought them home. Evelyn looked at her paper with new eyes.</p>'

    '<p>\u201cA is an upside-down ox head,\u201d she said, turning the letter upside down. '
    '\u201cI can kind of see it.\u201d</p>'

    '<p>\u201cEvery letter you write is a 3,000-year-old invention,\u201d Jason said. '
    '\u201cGoodnight, Phoenicians.\u201d</p>'

    '<p>\u201cGoodnight, aleph-beth.\u201d</p>'
)

disc_52 = [
    "The Phoenician alphabet had only 22 symbols, while Egyptian hieroglyphics had hundreds. How did making writing simpler change who could participate in civilization?",
    "The Phoenicians never built a great empire, but their alphabet outlasted every empire in history. What does this tell us about what makes a civilization truly influential?",
    "Nearly every alphabet on Earth descends from the Phoenician original. If the Phoenicians hadn\u2019t invented it, do you think someone else would have? Why or why not?"
]

quiz_52 = [
    {
        "q": "How many letters did the original Phoenician alphabet have?",
        "options": ["12", "22", "26", "52"],
        "correct": 1
    },
    {
        "q": "What improvement did the Greeks make to the Phoenician alphabet?",
        "options": [
            "They added numbers",
            "They added vowels",
            "They made it pictographic",
            "They reduced it to 10 letters"
        ],
        "correct": 1
    },
    {
        "q": "What luxury product were the Phoenicians most famous for producing?",
        "options": ["Gold jewelry", "Silk fabric", "Tyrian purple dye", "Perfume"],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 52:
        lessons[i] = {
            "id": 52,
            "type": "history",
            "topic": "Phoenicia",
            "title": "The People Who Gave Us Letters",
            "readingTime": "10 min",
            "story": story_52,
            "discussion": disc_52,
            "quiz": quiz_52
        }
        print("Updated lesson 52: The People Who Gave Us Letters")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
