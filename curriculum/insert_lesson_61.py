import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_61 = (
    '<h2>The Golden Age of Learning</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Abbasids850.png/800px-Abbasids850.png" '
    'alt="Map of the Abbasid Caliphate at its greatest extent" loading="lazy">'
    '<p class="image-caption">The Abbasid Caliphate at its height \u2014 stretching from North Africa to Central Asia</p>'
    '</div>'

    '<p>The brass telescope felt warm in William\u2019s hands. He turned the hourglass dial '
    'and the world blurred into a swirl of gold and blue. When the brothers landed, '
    'they stood in a courtyard paved with geometric tiles, surrounded by arched colonnades '
    'and the gentle splash of a marble fountain. Scholars in flowing robes moved between '
    'towering shelves of books, speaking in a dozen different languages.</p>'

    '<p>\u201cWhere are we?\u201d Robert whispered.</p>'

    '<p>\u201cBaghdad,\u201d William said. \u201cAround the year 830 AD. '
    'This is the <strong>House of Wisdom</strong> \u2014 the greatest library and research center '
    'on Earth. And we\u2019re standing in the middle of the <strong>Islamic Golden Age</strong>.\u201d</p>'

    '<h3>The Abbasid Caliphate</h3>'

    '<p>\u201cAfter the Prophet Muhammad founded Islam in the 600s, Muslim armies rapidly conquered '
    'a vast empire stretching from Spain to India,\u201d William explained. '
    '\u201cBy 750 AD, the <strong>Abbasid Caliphate</strong> took power and moved the capital '
    'to a brand-new city: <strong>Baghdad</strong>. Within a century, Baghdad became the largest '
    'city in the world \u2014 over a million people, with paved streets, public hospitals, '
    'and hundreds of bookshops.\u201d</p>'

    '<p>\u201cThe Abbasid caliphs, especially <strong>Harun al-Rashid</strong> and his son '
    '<strong>al-Ma\u2019mun</strong>, believed knowledge was sacred. They didn\u2019t care where '
    'an idea came from \u2014 Greece, Persia, India, China \u2014 if it was true, it was worth preserving. '
    'That attitude changed the world.\u201d</p>'

    '<h3>The House of Wisdom and the Translation Movement</h3>'

    '<p>\u201cAl-Ma\u2019mun founded the <strong>House of Wisdom</strong> (in Arabic, <strong>Bayt al-Hikma</strong>) '
    'around 830 AD,\u201d William said. \u201cIt was part library, part university, part translation bureau. '
    'He sent scholars across the known world to buy manuscripts \u2014 Greek texts by Aristotle, Plato, '
    'and Euclid; Persian histories; Indian mathematics. Then he hired the best translators alive '
    'to render them into Arabic.\u201d</p>'

    '<p>\u201cThis was called the <strong>Translation Movement</strong>. '
    'It was one of the most important intellectual projects in human history. '
    'Without it, the works of ancient Greek philosophers and scientists might have been lost forever. '
    'Europe was deep in its Dark Ages, and many classical texts survived only because Muslim scholars '
    'translated and preserved them. Centuries later, Europeans would re-discover Aristotle and Euclid '
    'by translating them <em>back</em> from Arabic into Latin.\u201d</p>'

    '<h3>Al-Khwarizmi \u2014 The Father of Algebra</h3>'

    '<p>William led Robert to a desk where a bearded man was writing numbers in a system '
    'Robert had never seen. \u201cThat is <strong>Muhammad ibn Musa al-Khwarizmi</strong>,\u201d '
    'William said quietly. \u201cHe\u2019s about to change mathematics forever.\u201d</p>'

    '<p>\u201cAl-Khwarizmi wrote a book called <em>al-Kitab al-Mukhtasar fi Hisab al-Jabr wal-Muqabala</em>. '
    'The word <strong>al-Jabr</strong> in the title became our word <strong>algebra</strong>. '
    'He didn\u2019t just solve equations \u2014 he created a systematic method for solving them, '
    'turning mathematics from a collection of tricks into a logical science.\u201d</p>'

    '<p>\u201cHe also championed the <strong>Hindu-Arabic numeral system</strong> \u2014 '
    'the digits 0 through 9 that we still use today. These numerals originally came from India, '
    'but al-Khwarizmi\u2019s writings introduced them to the Islamic world and eventually to Europe. '
    'Before this, Europeans used Roman numerals. Try multiplying XLVII by CXII \u2014 '
    'it\u2019s nearly impossible. The Hindu-Arabic system, with its place values and the revolutionary '
    'concept of <strong>zero</strong>, made complex calculation practical.\u201d</p>'

    '<p>\u201cAnd his name?\u201d William smiled. \u201cWhen his works were translated into Latin, '
    '\u2018al-Khwarizmi\u2019 became <strong>Algoritmi</strong> \u2014 giving us the word <strong>algorithm</strong>. '
    'Every computer program, every search engine, every GPS direction runs on algorithms. '
    'They all trace back to this man in this room.\u201d</p>'

    '<h3>Ibn al-Haytham \u2014 The First True Scientist</h3>'

    '<p>\u201cCome forward about 200 years,\u201d William said, adjusting the dial. They appeared '
    'in a darker room in Cairo where a man was experimenting with beams of light passing through a tiny hole. '
    '\u201cThis is <strong>Ibn al-Haytham</strong>, also known as <strong>Alhazen</strong>. '
    'Many historians consider him the <strong>father of modern optics</strong> \u2014 '
    'and the first person to use what we now call the <strong>scientific method</strong>.\u201d</p>'

    '<p>\u201cBefore Ibn al-Haytham, most people \u2014 including the ancient Greeks \u2014 believed that '
    'your eyes <em>sent out</em> rays of light, like invisible beams scanning the world. '
    'Ibn al-Haytham proved the opposite: light enters the eye from external sources. '
    'He proved this through careful experiments, not just philosophical arguments. '
    'He built the first <strong>camera obscura</strong> (a dark room with a pinhole that projects '
    'an upside-down image of the outside world), studied refraction, reflection, and the nature of shadows, '
    'and insisted that all scientific claims must be tested by experiment.\u201d</p>'

    '<p>\u201cHis book <em>Kitab al-Manazir</em> (Book of Optics) was translated into Latin '
    'and influenced European scientists for 600 years, including Roger Bacon, Kepler, and Newton.\u201d</p>'

    '<h3>Avicenna \u2014 The Prince of Physicians</h3>'

    '<p>\u201cMedieval Islamic scholars also revolutionized medicine,\u201d William continued. '
    '\u201cThe greatest was <strong>Ibn Sina</strong>, known in Europe as <strong>Avicenna</strong>. '
    'Born in Persia around 980 AD, he was a child prodigy who memorized the Quran by age 10 '
    'and was practicing medicine by age 16.\u201d</p>'

    '<p>\u201cHis masterwork, <em>The Canon of Medicine</em>, was a million-word encyclopedia '
    'that organized all known medical knowledge into a logical system. '
    'It described contagious diseases, recognized that tuberculosis was infectious, '
    'introduced the concept of quarantine, cataloged over 700 medications, '
    'and laid out clinical trial methods for testing drugs. '
    'European medical schools used <em>The Canon</em> as their primary textbook '
    'for <strong>over 500 years</strong> \u2014 longer than any medical text before or since.\u201d</p>'

    '<h3>Astronomy, Chemistry, and Beyond</h3>'

    '<p>\u201cThe Golden Age produced breakthroughs in almost every field,\u201d William said. '
    '\u201cIn <strong>astronomy</strong>, scholars built enormous observatories, '
    'calculated the Earth\u2019s circumference with remarkable accuracy, '
    'cataloged thousands of stars (many of which still carry their Arabic names \u2014 '
    'Aldebaran, Betelgeuse, Rigel, Altair), and refined the astrolabe, '
    'the most sophisticated scientific instrument of the medieval world.\u201d</p>'

    '<p>\u201cIn <strong>chemistry</strong> \u2014 a word that itself comes from the Arabic <em>al-kimiya</em> \u2014 '
    '<strong>Jabir ibn Hayyan</strong> (known as Geber) developed processes like distillation, crystallization, '
    'and filtration that are still used in laboratories today. '
    'He moved alchemy from mystical speculation toward experimental science.\u201d</p>'

    '<p>\u201cMuslim engineers invented or improved the <strong>waterwheel</strong>, the <strong>windmill</strong>, '
    'advanced irrigation systems, mechanical clocks, and even early flying machines designed by '
    '<strong>Abbas ibn Firnas</strong>, who attempted a controlled glider flight in 875 AD \u2014 '
    'a thousand years before the Wright Brothers.\u201d</p>'

    '<h3>Libraries and Universities</h3>'

    '<p>\u201cThe Islamic world built a <strong>culture of learning</strong> that had no parallel in its time,\u201d '
    'William said. \u201cBaghdad alone had 36 public libraries. Cordoba in Muslim Spain had 70 libraries, '
    'and its royal library held 400,000 volumes \u2014 at a time when the largest library in Christian Europe '
    'had perhaps 400. The <strong>University of al-Qarawiyyin</strong> in Fez, Morocco, founded in 859 AD, '
    'is recognized by UNESCO as the <strong>oldest continuously operating university in the world</strong>.\u201d</p>'

    '<p>\u201cPaper-making, learned from Chinese prisoners of war after the Battle of Talas in 751, '
    'spread across the Islamic world and eventually to Europe. '
    'Cheap paper replaced expensive parchment, making books affordable '
    'and knowledge accessible to a far wider audience. '
    'It was a revolution as important as the printing press would be centuries later.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 150" width="700" height="150" xmlns="http://www.w3.org/2000/svg" aria-label="Islamic Golden Age scholars and contributions">'
    '<rect width="700" height="150" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Giants of the Islamic Golden Age (c. 750\u20131258 AD)</text>'

    '<rect x="20" y="30" width="155" height="55" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Al-Khwarizmi</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Algebra &amp; Algorithms</text>'
    '<text x="97" y="76" text-anchor="middle" fill="#b8a88a" font-size="7">Hindu-Arabic numerals to Europe</text>'

    '<rect x="190" y="30" width="155" height="55" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Ibn al-Haytham</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Optics &amp; Scientific Method</text>'
    '<text x="267" y="76" text-anchor="middle" fill="#b8a88a" font-size="7">Camera obscura, Book of Optics</text>'

    '<rect x="360" y="30" width="155" height="55" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Avicenna (Ibn Sina)</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Canon of Medicine</text>'
    '<text x="437" y="76" text-anchor="middle" fill="#b8a88a" font-size="7">Used in Europe for 500+ years</text>'

    '<rect x="530" y="30" width="150" height="55" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Jabir ibn Hayyan</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Chemistry (al-kimiya)</text>'
    '<text x="605" y="76" text-anchor="middle" fill="#b8a88a" font-size="7">Distillation, crystallization</text>'

    '<text x="350" y="110" text-anchor="middle" fill="#b8a88a" font-size="9">algebra \u2022 algorithm \u2022 chemistry \u2022 zero \u2022 camera obscura \u2022 Arabic numerals</text>'
    '<text x="350" y="126" text-anchor="middle" fill="#e8a838" font-size="8">Preserved Greek &amp; Roman knowledge that Europe had lost \u2014 then added centuries of original discovery</text>'
    '<text x="350" y="142" text-anchor="middle" fill="#b8a88a" font-size="8">Stars still carry Arabic names: Aldebaran, Betelgeuse, Rigel, Altair</text>'
    '</svg>'
    '</div>'

    '<p>The telescope carried them home. The courtyard, the fountain, the shelves of books \u2014 '
    'all faded into the quiet of their room.</p>'

    '<p>Robert looked at the clock on the wall. \u201cWe use their numbers every day,\u201d he said slowly. '
    '\u201cAnd I never knew.\u201d</p>'

    '<p>\u201cMost people don\u2019t,\u201d William said. \u201cThat\u2019s the strange thing about the Golden Age. '
    'It shaped everything \u2014 our math, our science, our medicine, our words \u2014 '
    'and most of the world forgot where it all came from.\u201d</p>'

    '<p>\u201cGoodnight, House of Wisdom.\u201d</p>'

    '<p>\u201cGoodnight, al-Khwarizmi \u2014 and your algorithms.\u201d</p>'
)

disc_61 = [
    "The Abbasid caliphs collected knowledge from Greece, Persia, India, and China regardless of its origin. Why is it important for cultures to learn from one another instead of only valuing their own ideas?",
    "Many of the words we use every day \u2014 algebra, algorithm, chemistry, zero \u2014 come from the Islamic Golden Age, but most people don\u2019t know that. Why do you think entire civilizations can be \u2018forgotten\u2019 by history?",
    "Ibn al-Haytham insisted that every scientific claim must be tested by experiment, not just accepted because a famous person said it. Why is testing ideas so important, and how does that principle apply to your own life?"
]

quiz_61 = [
    {
        "q": "What was the House of Wisdom?",
        "options": [
            "A palace where the caliph lived",
            "A library, university, and translation center in Baghdad",
            "A temple for Islamic worship",
            "A marketplace for trading manuscripts"
        ],
        "correct": 1
    },
    {
        "q": "Which scholar\u2019s name gave us the word \u2018algorithm\u2019?",
        "options": ["Ibn al-Haytham", "Avicenna", "Al-Khwarizmi", "Jabir ibn Hayyan"],
        "correct": 2
    },
    {
        "q": "What did Ibn al-Haytham prove about how human vision works?",
        "options": [
            "Eyes send out invisible rays that scan the world",
            "Light enters the eye from external sources",
            "Vision depends only on the brain, not the eyes",
            "Eyes can only see in direct sunlight"
        ],
        "correct": 1
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 61:
        lessons[i] = {
            "id": 61,
            "type": "history",
            "topic": "Islamic Golden Age",
            "title": "The Golden Age of Learning",
            "readingTime": "10 min",
            "story": story_61,
            "discussion": disc_61,
            "quiz": quiz_61
        }
        print("Updated lesson 61: The Golden Age of Learning")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
