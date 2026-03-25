import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_71 = (
    '<h2>The Empire at the Crossroads</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Istanbul_panorama_and_skyline.jpg/800px-Istanbul_panorama_and_skyline.jpg" '
    'alt="Panoramic view of Istanbul showing the Hagia Sophia and Blue Mosque" loading="lazy">'
    '<p class="image-caption">Istanbul \u2014 once Constantinople, the capital of the Ottoman Empire for nearly 500 years</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass dial turned, and the brothers stood on the deck of a great warship. '
    'Ahead, massive stone walls rose from the water\u2019s edge, and beyond them, '
    'the dome of an enormous building caught the morning sun like a golden crown.</p>'

    '<p>\u201cWhere are we?\u201d Robert asked.</p>'

    '<p>\u201c<strong>Constantinople</strong>,\u201d William said. \u201cThe year is 1453, '
    'and we\u2019re about to witness the end of one empire and the birth of another.\u201d</p>'

    '<h3>The Fall of Constantinople</h3>'

    '<p>\u201cFor over a thousand years, Constantinople was the capital of the <strong>Byzantine Empire</strong> \u2014 '
    'the eastern half of the Roman Empire that survived long after Rome itself fell,\u201d William said. '
    '\u201cIts walls were considered unbreakable. No army had ever taken the city by force.\u201d</p>'

    '<p>\u201cBut in 1453, a 21-year-old Ottoman sultan named <strong>Mehmed II</strong> \u2014 '
    'later called \u201cthe Conqueror\u201d \u2014 brought 80,000 soldiers and something the world had never seen: '
    'a <strong>giant cannon</strong> called the <strong>Basilica</strong>, 27 feet long, '
    'capable of hurling 600-pound stone balls over a mile. '
    'After a 53-day siege, the walls that had stood for a thousand years finally fell. '
    'Constantinople became <strong>Istanbul</strong>, and it became the capital of the <strong>Ottoman Empire</strong>.\u201d</p>'

    '<h3>Rise of the Ottomans</h3>'

    '<p>\u201cThe Ottoman Empire began around 1299 in northwest Turkey,\u201d William continued. '
    '\u201cIt was founded by a warrior chief named <strong>Osman I</strong> \u2014 '
    'the dynasty was named after him. Over the next 200 years, '
    'the Ottomans expanded steadily, conquering territory in both Europe and Asia.\u201d</p>'

    '<p>\u201cAt its peak under <strong>Suleiman the Magnificent</strong> (ruled 1520\u20131566), '
    'the Ottoman Empire controlled an area stretching from <strong>Hungary</strong> in Europe '
    'to <strong>Algeria</strong> in North Africa to <strong>Iraq</strong> in the Middle East. '
    'It was one of the largest and longest-lasting empires in history, '
    'enduring for over <strong>600 years</strong> until 1922.\u201d</p>'

    '<h3>Suleiman the Magnificent</h3>'

    '<p>\u201cSuleiman was called \u2018the Magnificent\u2019 in Europe, '
    'but his own people called him <strong>Kanuni</strong> \u2014 \u2018the Lawgiver,\u2019\u201d William said. '
    '\u201cHe reformed the empire\u2019s legal system, making laws more fair and consistent. '
    'He built magnificent mosques, bridges, and public baths. '
    'Under his rule, Istanbul became one of the greatest cities in the world, '
    'with a population of over 500,000 \u2014 larger than any European city at the time.\u201d</p>'

    '<p>\u201cThe <strong>Suleymaniye Mosque</strong>, designed by the genius architect '
    '<strong>Mimar Sinan</strong>, is considered one of the greatest works of architecture ever built. '
    'Sinan designed over 300 buildings in his career \u2014 mosques, schools, hospitals, '
    'and public kitchens that fed the poor.\u201d</p>'

    '<h3>The Crossroads of Civilizations</h3>'

    '<p>\u201cWhat made the Ottoman Empire unique was its position,\u201d William said. '
    '\u201cIt sat at the <strong>crossroads</strong> of Europe, Asia, and Africa. '
    'It controlled the land routes between East and West, including the ancient Silk Road. '
    'Istanbul was a melting pot of cultures \u2014 Turkish, Greek, Arab, Persian, Jewish, '
    'and European merchants all lived and traded there.\u201d</p>'

    '<p>\u201cThe Ottomans practiced a degree of <strong>religious tolerance</strong> unusual for the time. '
    'Christians and Jews were recognized as <strong>dhimmi</strong> \u2014 protected minorities. '
    'They could practice their religion, run their own courts, and operate their own schools, '
    'though they paid an additional tax. When Spain expelled its Jewish population in 1492, '
    'the Ottoman Sultan <strong>Bayezid II</strong> welcomed them, reportedly saying: '
    '\u201cYou call Ferdinand a wise king? He impoverishes his country to enrich mine.\u201d\u201d</p>'

    '<h3>The Janissaries</h3>'

    '<p>\u201cThe Ottoman army had an elite unit called the <strong>Janissaries</strong>,\u201d William said. '
    '\u201cThey were originally Christian boys taken from conquered lands through a system called '
    '<strong>devshirme</strong>. These boys were converted to Islam, given rigorous military training, '
    'and became the best-trained soldiers in the world. They owed loyalty only to the sultan.\u201d</p>'

    '<p>\u201cIt sounds unfair,\u201d Robert said.</p>'

    '<p>\u201cIt was,\u201d William agreed. \u201cBeing taken from your family is terrible. '
    'But some Janissaries rose to become powerful governors and viziers. '
    'The system, for all its cruelty, created an army that could challenge any force in Europe '
    'for centuries. History is complicated \u2014 great achievements and great injustices often exist side by side.\u201d</p>'

    '<h3>Ottoman Arts and Innovation</h3>'

    '<p>\u201cThe Ottomans were master artists,\u201d William continued. '
    '\u201cTheir <strong>Iznik tiles</strong> \u2014 decorated with blue, turquoise, and red floral patterns \u2014 '
    'covered mosque walls and are still treasured today. '
    'Ottoman <strong>calligraphy</strong> turned Arabic script into breathtaking visual art. '
    'Their miniature paintings depicted everything from battles to botanical gardens.\u201d</p>'

    '<p>\u201cThey also advanced <strong>military technology</strong>. Those giant cannons that broke Constantinople\u2019s walls '
    'revolutionized warfare. Ottoman engineers built sophisticated siege equipment, '
    'and their navy dominated the Mediterranean for over a century.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Ottoman Empire">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Ottoman Empire (1299\u20131922)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Constantinople (1453)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Mehmed II, age 21</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Giant cannon broke 1,000-yr walls</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Suleiman (1520\u20131566)</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">\u201cThe Lawgiver\u201d</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Largest extent, golden age</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Crossroads</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Europe + Asia + Africa</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Religious tolerance, trade hub</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Legacy</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">600+ years, 3 continents</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Modern Turkey founded 1923</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">The fall of Constantinople (1453) is often used to mark the end of the Middle Ages</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">Istanbul\u2019s Hagia Sophia served as a church, then a mosque, then a museum, and is now a mosque again</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. Robert could still hear the echo of cannons.</p>'

    '<p>\u201cSix hundred years,\u201d he said. \u201cThat\u2019s longer than the United States has existed.\u201d</p>'

    '<p>\u201cAnd it all started with a 21-year-old who refused to believe a wall was unbreakable,\u201d '
    'William said. \u201cGoodnight, empire at the crossroads.\u201d</p>'

    '<p>\u201cGoodnight, magnificent walls.\u201d</p>'
)

disc_71 = [
    "When Spain expelled its Jews in 1492, the Ottoman sultan welcomed them. What does it tell you about a leader when they accept people that others reject?",
    "The Janissary system took boys from their families but sometimes gave them paths to great power. Can something be both cruel and effective? How should we judge systems like this?",
    "The fall of Constantinople in 1453 is used to mark the end of the Middle Ages. Why do historians pick single events to mark the end of one era and the beginning of another?"
]

quiz_71 = [
    {
        "q": "Who conquered Constantinople in 1453?",
        "options": ["Suleiman the Magnificent", "Osman I", "Mehmed II", "Bayezid II"],
        "correct": 2
    },
    {
        "q": "What did Suleiman\u2019s own people call him?",
        "options": ["The Magnificent", "The Conqueror", "The Lawgiver (Kanuni)", "The Great"],
        "correct": 2
    },
    {
        "q": "How long did the Ottoman Empire last?",
        "options": ["About 200 years", "About 400 years", "About 600 years", "About 800 years"],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 71:
        lessons[i] = {
            "id": 71,
            "type": "history",
            "topic": "Ottoman",
            "title": "The Empire at the Crossroads",
            "readingTime": "10 min",
            "story": story_71,
            "discussion": disc_71,
            "quiz": quiz_71
        }
        print("Updated lesson 71: The Empire at the Crossroads")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
