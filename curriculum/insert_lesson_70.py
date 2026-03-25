import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_70 = (
    '<h2>The Jewel of India</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Taj_Mahal%2C_Agra%2C_India_edit3.jpg/800px-Taj_Mahal%2C_Agra%2C_India_edit3.jpg" '
    'alt="The Taj Mahal in Agra, India" loading="lazy">'
    '<p class="image-caption">The Taj Mahal \u2014 built by Mughal Emperor Shah Jahan as a monument to love</p>'
    '</div>'

    '<p>Evelyn was looking at a photograph of a white marble building with a perfect dome '
    'reflected in a long pool of water. \u201cIs that real?\u201d she asked. '
    '\u201cIt looks like something from a dream.\u201d</p>'

    '<p>Jason opened The Living World and turned the brass clasp. '
    '\u201cIt\u2019s real. And the story behind it is even more extraordinary than the building. '
    'Let\u2019s go see it.\u201d</p>'

    '<p>The green light set them down on a dusty road outside the walls of a magnificent city. '
    'Elephants draped in silk carried nobles through gates inlaid with precious stones. '
    'Bazaars overflowed with spices, jewels, and bolts of fabric in every color imaginable. '
    'The air smelled of cardamom and sandalwood.</p>'

    '<p>\u201cWelcome to <strong>Mughal India</strong>,\u201d Jason said. \u201cOne of the richest, '
    'most powerful, and most beautiful empires the world has ever seen.\u201d</p>'

    '<h3>Babur the Tiger</h3>'

    '<p>\u201cThe Mughal Empire began with a man named <strong>Babur</strong>,\u201d Jason said. '
    '\u201cHis name means \u2018tiger,\u2019 and he earned it. '
    'Babur was a Central Asian prince descended from two of history\u2019s greatest conquerors: '
    '<strong>Genghis Khan</strong> on his mother\u2019s side and <strong>Tamerlane</strong> on his father\u2019s. '
    'By age 14, he had conquered the ancient city of Samarkand. '
    'By age 21, he had lost it twice.\u201d</p>'

    '<p>\u201cPushed out of Central Asia by stronger rivals, Babur turned his eyes south to <strong>India</strong> \u2014 '
    'a land of legendary wealth. In 1526, with an army of only about 12,000 men, '
    'he faced the Sultan of Delhi\u2019s force of 100,000 soldiers and 1,000 war elephants '
    'at the <strong>Battle of Panipat</strong>. '
    'Babur had something the Sultan didn\u2019t: <strong>cannons and muskets</strong>. '
    'He arranged his guns behind a line of carts tied together with ropes, '
    'creating a wall the elephants couldn\u2019t breach. '
    'The gunfire terrified the elephants, which stampeded back through their own army. '
    'Babur won, and the Mughal Empire was born.\u201d</p>'

    '<p>\u201cThe word \u2018Mughal\u2019 is actually a Persian version of \u2018Mongol\u2019 \u2014 '
    'a nod to Babur\u2019s Mongol ancestry. But the Mughals were culturally Persian, '
    'religiously Muslim, and ruling a land that was predominantly Hindu. '
    'How they managed that balance would define the empire.\u201d</p>'

    '<h3>Akbar the Great</h3>'

    '<p>\u201cBabur\u2019s grandson <strong>Akbar</strong> became emperor at age 13 '
    'and ruled for 49 years (1556\u20131605),\u201d Jason said. '
    '\u201cHe is considered the greatest Mughal emperor \u2014 and possibly one of the greatest rulers '
    'in all of history \u2014 because he figured out something that had eluded empires for centuries: '
    'how to govern people who are different from you.\u201d</p>'

    '<p>\u201cAkbar was Muslim, but about 80 percent of his subjects were <strong>Hindu</strong>. '
    'Instead of forcing them to convert, Akbar did something revolutionary: '
    'he practiced <strong>religious tolerance</strong>. '
    'He abolished the <strong>jizya</strong> \u2014 a special tax that non-Muslims had to pay. '
    'He married Hindu princesses and gave their families positions of power. '
    'He appointed Hindu generals, governors, and ministers. '
    'He invited scholars from every religion \u2014 Hindu, Muslim, Christian, Jain, Zoroastrian \u2014 '
    'to his court to debate philosophy and theology.\u201d</p>'

    '<p>\u201cAkbar even created a new religion called <strong>Din-i Ilahi</strong> '
    '(\u2018Divine Faith\u2019), which tried to blend the best ideas from every religion. '
    'It didn\u2019t catch on \u2014 almost no one converted \u2014 '
    'but the effort itself showed how seriously Akbar took the idea of religious harmony.\u201d</p>'

    '<p>\u201cHe also built a brilliant <strong>administrative system</strong>. '
    'He divided the empire into provinces, each governed by appointed officials '
    'who were regularly rotated to prevent them from building independent power. '
    'He standardized weights, measures, and currency. '
    'He reformed the tax system so peasants paid based on the actual harvest, '
    'not a fixed amount \u2014 which meant farmers didn\u2019t starve in bad years. '
    'It was remarkably modern for the 1500s.\u201d</p>'

    '<p>Evelyn looked impressed. \u201cHe sounds like a really smart leader.\u201d</p>'

    '<p>\u201cHere\u2019s the ironic part,\u201d Jason said. \u201cAkbar couldn\u2019t read. '
    'He was probably dyslexic. But he had people read to him constantly '
    'and had a memory that amazed everyone around him. '
    'He proved that wisdom and literacy are not the same thing.\u201d</p>'

    '<h3>Shah Jahan and the Taj Mahal</h3>'

    '<p>\u201cAkbar\u2019s grandson <strong>Shah Jahan</strong> (ruled 1628\u20131658) '
    'took Mughal architecture to its absolute peak,\u201d Jason said. '
    '\u201cHe rebuilt large sections of Delhi and Agra with white marble, '
    'precious stones, and geometric gardens. '
    'The <strong>Red Fort</strong> in Delhi and the <strong>Jama Masjid</strong> '
    '(one of the largest mosques in India) were his creations.\u201d</p>'

    '<p>\u201cBut his greatest achievement was born from grief. '
    'In 1631, Shah Jahan\u2019s beloved wife <strong>Mumtaz Mahal</strong> died giving birth '
    'to their fourteenth child. The emperor was devastated. '
    'His hair turned white. He locked himself away for a week. '
    'And then he ordered the construction of the most beautiful building on Earth '
    'as her tomb.\u201d</p>'

    '<p>\u201cThe <strong>Taj Mahal</strong> took 22 years and 20,000 workers to build. '
    'It is made of white marble inlaid with 28 types of precious and semi-precious stones \u2014 '
    'jade from China, turquoise from Tibet, lapis lazuli from Afghanistan, '
    'sapphires from Sri Lanka. The marble changes color throughout the day: '
    'pinkish in the morning, white at noon, golden in the evening, '
    'and silver-blue under moonlight. '
    'The entire structure is perfectly symmetrical. '
    'The gardens, water channels, and reflecting pools are designed '
    'to mirror the Quran\u2019s description of paradise.\u201d</p>'

    '<p>\u201cToday it is considered one of the <strong>New Seven Wonders of the World</strong> '
    'and is visited by 7\u20138 million people every year.\u201d</p>'

    '<h3>A Blending of Cultures</h3>'

    '<p>\u201cWhat made Mughal India truly remarkable was its <strong>cultural fusion</strong>,\u201d '
    'Jason said. \u201cMughal art blended Persian miniature painting with Hindu color and detail. '
    'Mughal architecture combined Islamic geometric patterns with Hindu craftsmanship. '
    'The Persian language mixed with local languages to create <strong>Urdu</strong> \u2014 '
    'still spoken by hundreds of millions of people today.\u201d</p>'

    '<p>\u201cMughal cuisine fused Central Asian meat dishes with Indian spices '
    'to create foods that are now beloved worldwide: <strong>biryani</strong>, '
    '<strong>korma</strong>, <strong>naan bread</strong>, <strong>samosas</strong>. '
    'If you\u2019ve ever eaten Indian food at a restaurant, '
    'you\u2019ve tasted the Mughal legacy.\u201d</p>'

    '<p>\u201cThe Mughals also introduced <strong>polo</strong> to India, built vast road networks, '
    'established a postal system, and created gardens so magnificent that the English word '
    '\u2018paradise\u2019 comes from the Persian <em>pairidaeza</em>, meaning \u2018walled garden.\u2019\u201d</p>'

    '<h3>Decline and the British Arrival</h3>'

    '<p>\u201cThe empire began to crack under <strong>Aurangzeb</strong> (ruled 1658\u20131707), '
    'Shah Jahan\u2019s son,\u201d Jason said. \u201cAurangzeb reversed Akbar\u2019s policies of tolerance. '
    'He reimposed the <strong>jizya</strong> tax on Hindus. '
    'He destroyed Hindu temples and banned music at court. '
    'He spent decades fighting costly wars to expand the empire into southern India \u2014 '
    'wars he technically won but which drained the treasury and turned millions against Mughal rule.\u201d</p>'

    '<p>\u201cAfter Aurangzeb died in 1707, the empire fractured. '
    'Regional governors declared independence. '
    'The <strong>Maratha Confederacy</strong>, a Hindu warrior alliance, '
    'seized huge territories. Persian and Afghan invaders sacked Delhi. '
    'By the mid-1700s, the Mughal emperor controlled little more than the city of Delhi itself.\u201d</p>'

    '<p>\u201cAnd waiting in the wings was a new power: '
    'the <strong>British East India Company</strong>. '
    'A private trading company backed by British military force, '
    'it had been establishing coastal trading posts since the early 1600s. '
    'As the Mughal Empire weakened, the Company stepped into the power vacuum, '
    'playing local rulers against each other, winning battles with superior weapons, '
    'and gradually taking control of the subcontinent. '
    'By 1857, the last Mughal emperor was deposed by the British, '
    'and India became part of the <strong>British Empire</strong>.\u201d</p>'

    '<p>\u201cBut the Mughal legacy never disappeared,\u201d Jason said. '
    '\u201cThe Taj Mahal still stands. Urdu is still spoken. Biryani is still served. '
    'And Akbar\u2019s radical idea \u2014 that a ruler should respect the beliefs of all his people \u2014 '
    'is still one of the most important ideas in the world.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 140" width="700" height="140" xmlns="http://www.w3.org/2000/svg" aria-label="Mughal Empire Timeline">'
    '<rect width="700" height="140" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Mughal Empire (1526\u20131857)</text>'

    '<line x1="60" y1="45" x2="640" y2="45" stroke="#b8a88a" stroke-width="2"/>'

    '<circle cx="80" cy="45" r="5" fill="#e8a838"/>'
    '<text x="80" y="38" text-anchor="middle" fill="#e8a838" font-size="8" font-weight="bold">1526</text>'
    '<text x="80" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Babur wins</text>'
    '<text x="80" y="72" text-anchor="middle" fill="#b8a88a" font-size="7">Battle of Panipat</text>'

    '<circle cx="210" cy="45" r="5" fill="#2ecc71"/>'
    '<text x="210" y="38" text-anchor="middle" fill="#2ecc71" font-size="8" font-weight="bold">1556\u20131605</text>'
    '<text x="210" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Akbar the Great</text>'
    '<text x="210" y="72" text-anchor="middle" fill="#b8a88a" font-size="7">Religious tolerance</text>'

    '<circle cx="350" cy="45" r="5" fill="#4a90d9"/>'
    '<text x="350" y="38" text-anchor="middle" fill="#4a90d9" font-size="8" font-weight="bold">1632\u20131653</text>'
    '<text x="350" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Shah Jahan builds</text>'
    '<text x="350" y="72" text-anchor="middle" fill="#b8a88a" font-size="7">the Taj Mahal</text>'

    '<circle cx="480" cy="45" r="5" fill="#e74c3c"/>'
    '<text x="480" y="38" text-anchor="middle" fill="#e74c3c" font-size="8" font-weight="bold">1658\u20131707</text>'
    '<text x="480" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Aurangzeb reverses</text>'
    '<text x="480" y="72" text-anchor="middle" fill="#b8a88a" font-size="7">tolerance, expands wars</text>'

    '<circle cx="610" cy="45" r="5" fill="#9b59b6"/>'
    '<text x="610" y="38" text-anchor="middle" fill="#9b59b6" font-size="8" font-weight="bold">1857</text>'
    '<text x="610" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Last emperor</text>'
    '<text x="610" y="72" text-anchor="middle" fill="#b8a88a" font-size="7">deposed by British</text>'

    '<text x="350" y="100" text-anchor="middle" fill="#b8a88a" font-size="9">At its peak: 150 million people \u2014 25% of the world\u2019s population</text>'
    '<text x="350" y="115" text-anchor="middle" fill="#b8a88a" font-size="9">Taj Mahal: 22 years, 20,000 workers, 28 types of precious stones</text>'
    '<text x="350" y="130" text-anchor="middle" fill="#b8a88a" font-size="9">Legacy: Urdu language, biryani, Mughal architecture, religious pluralism</text>'
    '</svg>'
    '</div>'

    '<p>The book carried them home. '
    'Evelyn could still smell cardamom and see white marble glowing in the moonlight.</p>'

    '<p>\u201cAkbar couldn\u2019t read, but he was one of the wisest rulers in history,\u201d '
    'she said. \u201cThat\u2019s amazing.\u201d</p>'

    '<p>\u201cWisdom isn\u2019t about what you read,\u201d Jason said. '
    '\u201cIt\u2019s about what you do with what you learn. '
    'Goodnight, jewel of India.\u201d</p>'

    '<p>\u201cGoodnight, Taj Mahal.\u201d</p>'
)

disc_70 = [
    "Akbar practiced religious tolerance in a time when most rulers forced their subjects to follow one faith. Why do you think tolerance is so hard for powerful people to practice? What made Akbar different?",
    "Aurangzeb reversed Akbar\u2019s tolerance policies and the empire eventually fell apart. Is there a connection between how a ruler treats minorities and how long their empire lasts?",
    "The Mughal Empire blended Hindu and Islamic cultures to create something new \u2014 Urdu, biryani, Mughal architecture. Can you think of examples in your own life where mixing different cultures created something better than either one alone?"
]

quiz_70 = [
    {
        "q": "How did Babur win the Battle of Panipat in 1526 despite being vastly outnumbered?",
        "options": [
            "He used a surprise night attack",
            "He had cannons and muskets that terrified the enemy\u2019s war elephants",
            "He poisoned the enemy\u2019s water supply",
            "He hired mercenaries from Europe"
        ],
        "correct": 1
    },
    {
        "q": "What made Akbar the Great\u2019s rule so remarkable?",
        "options": [
            "He conquered more territory than any other Mughal emperor",
            "He invented the printing press in India",
            "He practiced religious tolerance and included Hindus in government",
            "He built the largest army in the world"
        ],
        "correct": 2
    },
    {
        "q": "Why did Shah Jahan build the Taj Mahal?",
        "options": [
            "As a palace for visiting foreign leaders",
            "As a fortress to defend against invaders",
            "As a tomb for his beloved wife Mumtaz Mahal",
            "As a mosque for daily prayers"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 70:
        lessons[i] = {
            "id": 70,
            "type": "history",
            "topic": "Mughal",
            "title": "The Jewel of India",
            "readingTime": "10 min",
            "story": story_70,
            "discussion": disc_70,
            "quiz": quiz_70
        }
        print("Updated lesson 70: The Jewel of India")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
