import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_64 = (
    '<h2>The Rebirth of Art</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Florence_Duomo_from_Michelangelo_Hill.jpg/800px-Florence_Duomo_from_Michelangelo_Hill.jpg" '
    'alt="The Florence Cathedral with Brunelleschi\u2019s dome rising above the city skyline" loading="lazy">'
    '<p class="image-caption">Florence, Italy \u2014 birthplace of the Renaissance, with Brunelleschi\u2019s magnificent dome crowning the cathedral</p>'
    '</div>'

    '<p>Evelyn had been staring at a painting in a library book \u2014 a ceiling covered in swirling figures, '
    'muscles and clouds and reaching hands. \u201cJason, who painted that?\u201d</p>'

    '<p>Jason opened The Living World and turned the brass clasp. The hourglass glowed. '
    '\u201cSomeone who lay on his back on scaffolding for four years to do it. Let\u2019s go meet him.\u201d</p>'

    '<p>The green light set them down on a stone bridge over a river that sparkled '
    'in warm afternoon sun. Red-roofed buildings rose on every side. Church bells rang. '
    'Artists with paint-stained hands hurried past carrying wooden panels, '
    'and the smell of wet plaster drifted from an open workshop door.</p>'

    '<h3>A World Wakes Up</h3>'

    '<p>\u201cWe\u2019re in <strong>Florence, Italy</strong>, around 1490,\u201d Jason said. '
    '\u201cThis is the heart of the <strong>Renaissance</strong> \u2014 a word that means '
    '\u2018<strong>rebirth</strong>.\u2019 For a thousand years during the Middle Ages, '
    'most European art and learning had been focused on religion. '
    'The Church controlled education. Most people couldn\u2019t read. '
    'Ancient Greek and Roman ideas about science, philosophy, and beauty '
    'had been largely forgotten in western Europe.\u201d</p>'

    '<p>\u201cThen, starting in the 1300s, something changed. Italian scholars rediscovered '
    'ancient Greek and Roman texts \u2014 works by Plato, Aristotle, Cicero, and others \u2014 '
    'many of which had been preserved by Islamic scholars in the Middle East. '
    'These old books sparked a new way of thinking called <strong>humanism</strong>. '
    'Humanists believed that <strong>human beings</strong> \u2014 not just God and the Church \u2014 '
    'were worthy of study. They asked: What can a person achieve? '
    'How beautiful can art be? How far can the mind reach?\u201d</p>'

    '<h3>Florence and the Medici</h3>'

    '<p>\u201cFlorence became the birthplace of the Renaissance because of money, geography, and one powerful family,\u201d '
    'Jason said. \u201cFlorence was a wealthy trading city. Wool, silk, and banking made its merchants rich. '
    'And the richest family of all was the <strong>Medici</strong>.\u201d</p>'

    '<p>\u201cThe Medici were bankers who became the unofficial rulers of Florence. '
    '<strong>Lorenzo de\u2019 Medici</strong> \u2014 called \u2018Lorenzo the Magnificent\u2019 \u2014 '
    'used his fortune to support artists, architects, philosophers, and scientists. '
    'This support was called <strong>patronage</strong>. Without wealthy patrons like the Medici, '
    'most Renaissance artists could never have afforded to spend years on a single masterpiece. '
    'Lorenzo didn\u2019t just pay for art \u2014 he invited artists to live in his palace, '
    'dine at his table, and debate ideas with scholars. One of the young artists '
    'he mentored was a teenager named Michelangelo.\u201d</p>'

    '<h3>Michelangelo \u2014 The Divine Artist</h3>'

    '<p>\u201c<strong>Michelangelo Buonarroti</strong> is considered one of the greatest artists '
    'who ever lived,\u201d Jason said. \u201cHe was a sculptor, painter, architect, and poet. '
    'He believed the human body was the most beautiful thing God had created, '
    'and he spent his life trying to capture that beauty in stone and paint.\u201d</p>'

    '<p>\u201cHis sculpture of <strong>David</strong> \u2014 carved from a single block of marble '
    'that other sculptors had given up on \u2014 stands 17 feet tall and shows the biblical hero '
    'at the moment before he faces Goliath. Every muscle, every vein, every tendon is perfect. '
    'Michelangelo was only 26 years old when he finished it.\u201d</p>'

    '<p>\u201cBut his most famous work is the ceiling of the <strong>Sistine Chapel</strong> in Rome. '
    'Pope Julius II commissioned Michelangelo to paint the entire ceiling \u2014 over 5,000 square feet. '
    'Michelangelo worked for four years, mostly alone, lying on scaffolding high above the floor, '
    'paint dripping into his eyes. He painted more than 300 figures telling stories from the Bible. '
    'The most famous scene \u2014 God reaching out to touch Adam\u2019s finger \u2014 '
    'has become one of the most recognizable images in all of art.\u201d</p>'

    '<h3>Raphael and the Art of Perfection</h3>'

    '<p>\u201c<strong>Raphael Sanzio</strong> was another giant of the Renaissance,\u201d Jason continued. '
    '\u201cWhere Michelangelo was intense and brooding, Raphael was charming and graceful. '
    'His painting <em>The School of Athens</em> shows the great thinkers of ancient Greece \u2014 '
    'Plato, Aristotle, Socrates, Pythagoras \u2014 all gathered in a grand hall. '
    'It\u2019s a celebration of human reason and knowledge. '
    'Raphael was so admired that when he died at just 37, all of Rome wept.\u201d</p>'

    '<h3>Brunelleschi\u2019s Impossible Dome</h3>'

    '<p>\u201cThe Renaissance wasn\u2019t just painting,\u201d Jason said, pointing upward at the enormous dome '
    'that rose above the city. \u201c<strong>Filippo Brunelleschi</strong> built the dome of the '
    '<strong>Florence Cathedral</strong> \u2014 and no one thought it could be done. '
    'The opening was 143 feet across, far too wide for the wooden scaffolding techniques of the time. '
    'Brunelleschi invented a completely new method: a double-shell dome built with interlocking bricks '
    'in a herringbone pattern, so the dome essentially held itself up as it was being built. '
    'It took 16 years to complete and remains the largest masonry dome ever constructed. '
    'Brunelleschi proved that with mathematics and engineering, '
    'humans could accomplish things the ancient Romans never imagined.\u201d</p>'

    '<h3>Perspective \u2014 Seeing Depth on a Flat Surface</h3>'

    '<p>\u201cRenaissance artists also revolutionized <strong>how</strong> we see art,\u201d Jason said. '
    '\u201cMedieval paintings looked flat \u2014 figures floated in golden backgrounds '
    'with no sense of depth or distance. Then Brunelleschi and other artists discovered '
    '<strong>linear perspective</strong> \u2014 a mathematical technique that creates the illusion '
    'of three-dimensional space on a flat surface. '
    'Lines converge toward a <strong>vanishing point</strong> on the horizon, '
    'and objects get smaller as they recede. Suddenly, paintings looked like windows into real rooms '
    'and real landscapes. This one idea transformed Western art forever.\u201d</p>'

    '<h3>From Florence to the World</h3>'

    '<p>\u201cThe Renaissance didn\u2019t stay in Florence,\u201d Jason said. '
    '\u201cIt spread to Rome, Venice, Milan, and eventually across the Alps to France, England, '
    'Germany, and the Netherlands. One invention supercharged the spread: '
    'the <strong>printing press</strong>. In 1440, <strong>Johannes Gutenberg</strong> in Germany '
    'invented movable type printing. Before Gutenberg, every book was copied by hand \u2014 '
    'a single book could take a monk a year. With the printing press, hundreds of copies '
    'could be produced in days. Ideas that once circulated among a handful of scholars '
    'could now reach thousands. The printing press didn\u2019t just spread the Renaissance \u2014 '
    'it made the modern world possible.\u201d</p>'

    '<p>\u201cThe Renaissance was the moment Europe shifted from the medieval to the modern,\u201d '
    'Jason said. \u201cPeople stopped asking only \u2018What does God want?\u2019 and started also asking '
    '\u2018What can <em>I</em> achieve?\u2019 That shift \u2014 from obedience to curiosity, '
    'from tradition to innovation \u2014 is still the engine that drives our world today.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 140" width="700" height="140" xmlns="http://www.w3.org/2000/svg" aria-label="Renaissance timeline and key figures">'
    '<rect width="700" height="140" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Renaissance \u2014 Key Figures &amp; Ideas</text>'

    '<rect x="20" y="30" width="155" height="55" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Michelangelo</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Sistine Chapel ceiling</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">David \u2014 17 ft marble statue</text>'
    '<text x="97" y="84" text-anchor="middle" fill="#b8a88a" font-size="7">Sculptor, painter, architect</text>'

    '<rect x="190" y="30" width="155" height="55" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Brunelleschi</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Florence Cathedral dome</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">143 ft wide \u2014 largest masonry dome</text>'
    '<text x="267" y="84" text-anchor="middle" fill="#b8a88a" font-size="7">Invented linear perspective</text>'

    '<rect x="360" y="30" width="155" height="55" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Raphael</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">The School of Athens</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Celebrated human reason</text>'
    '<text x="437" y="84" text-anchor="middle" fill="#b8a88a" font-size="7">Died at 37 \u2014 all Rome wept</text>'

    '<rect x="530" y="30" width="150" height="55" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Gutenberg</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Printing press (1440)</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Spread Renaissance ideas</text>'
    '<text x="605" y="84" text-anchor="middle" fill="#b8a88a" font-size="7">Made the modern world possible</text>'

    '<text x="350" y="110" text-anchor="middle" fill="#b8a88a" font-size="9">Humanism: the belief that human achievement, reason, and beauty deserve study</text>'
    '<text x="350" y="125" text-anchor="middle" fill="#b8a88a" font-size="9">The Medici family funded Florence\u2019s transformation from trading city to art capital</text>'
    '</svg>'
    '</div>'

    '<p>The book carried them home. Evelyn stared at her hands.</p>'

    '<p>\u201cMichelangelo lay on his back for four years painting a ceiling,\u201d she said quietly. '
    '\u201cI complain when my arm gets tired coloring.\u201d</p>'

    '<p>\u201cGreat things take great patience,\u201d Jason said. '
    '\u201cGoodnight, Florence.\u201d</p>'

    '<p>\u201cGoodnight, reaching fingers.\u201d</p>'
)

disc_64 = [
    "The Medici family used their wealth to support artists and thinkers. Do you think art and science need wealthy supporters to flourish, or can great work happen without money? What are the advantages and dangers of patronage?",
    "The Renaissance was partly about shifting from \u2018What does God want?\u2019 to \u2018What can I achieve?\u2019 Do you think both questions are important? Can a person be deeply religious and still be a humanist?",
    "Michelangelo spent four years painting the Sistine Chapel ceiling, mostly alone. What does that level of dedication teach us about what it takes to create something truly great?"
]

quiz_64 = [
    {
        "q": "What does the word \u2018Renaissance\u2019 mean?",
        "options": [
            "Revolution",
            "Rebirth",
            "Religion",
            "Republic"
        ],
        "correct": 1
    },
    {
        "q": "Which powerful family funded many Renaissance artists in Florence?",
        "options": [
            "The Borgias",
            "The Tudors",
            "The Medici",
            "The Habsburgs"
        ],
        "correct": 2
    },
    {
        "q": "What technique did Renaissance artists use to create the illusion of depth on a flat surface?",
        "options": [
            "Pointillism",
            "Abstract expressionism",
            "Linear perspective",
            "Mosaic tiling"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 64:
        lessons[i] = {
            "id": 64,
            "type": "history",
            "topic": "Renaissance",
            "title": "The Rebirth of Art",
            "readingTime": "10 min",
            "story": story_64,
            "discussion": disc_64,
            "quiz": quiz_64
        }
        print("Updated lesson 64: The Rebirth of Art")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
