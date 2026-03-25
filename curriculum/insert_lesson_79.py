import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_79 = (
    '<h2>Cowboys and Frontiers</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Emanuel_Leutze_-_Westward_the_Course_of_Empire_Takes_Its_Way_-_Capitol.jpg/800px-Emanuel_Leutze_-_Westward_the_Course_of_Empire_Takes_Its_Way_-_Capitol.jpg" '
    'alt="Emanuel Leutze mural Westward the Course of Empire Takes Its Way showing pioneers crossing the Rocky Mountains" loading="lazy">'
    '<p class="image-caption">Westward the Course of Empire Takes Its Way by Emanuel Leutze (1862) \u2014 celebrating the spirit of Manifest Destiny</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass dial turned, and the brothers found themselves standing '
    'on an endless prairie. Tall grass rippled like an ocean under a sky so wide '
    'it seemed to curve at the edges. A line of covered wagons creaked along a dusty trail.</p>'

    '<p>\u201cWhere are we?\u201d Robert asked.</p>'

    '<p>\u201cThe middle of nowhere,\u201d William said with a grin. '
    '\u201cAlso known as the <strong>Oregon Trail</strong>, about 1845. '
    'We\u2019re watching America push westward.\u201d</p>'

    '<h3>Manifest Destiny</h3>'

    '<p>\u201cAmericans in the 1800s believed it was their God-given right \u2014 their destiny \u2014 '
    'to spread across the entire continent from the Atlantic to the Pacific,\u201d William said. '
    '\u201cThey called this idea <strong>Manifest Destiny</strong>. Newspaper editors, politicians, '
    'and preachers all said the same thing: the West was empty land waiting to be claimed.\u201d</p>'

    '<p>\u201cBut it wasn\u2019t empty, was it?\u201d Robert said.</p>'

    '<p>\u201cNot even close,\u201d William replied. \u201cMillions of <strong>Native Americans</strong> '
    'had lived on those lands for thousands of years. They had nations, languages, trade routes, '
    'and cultures older than any European country. But to the settlers, '
    'the land was there for the taking.\u201d</p>'

    '<h3>The Trail of Tears</h3>'

    '<p>\u201cThe displacement started even before the westward push,\u201d William said quietly. '
    '\u201cIn 1830, President <strong>Andrew Jackson</strong> signed the <strong>Indian Removal Act</strong>, '
    'forcing the <strong>Cherokee, Choctaw, Chickasaw, Creek, and Seminole</strong> nations '
    'out of their ancestral homelands in the Southeast. Between 1831 and 1838, '
    'about <strong>60,000 Native Americans</strong> were forced to march hundreds of miles '
    'to \u201cIndian Territory\u201d in present-day Oklahoma.\u201d</p>'

    '<p>\u201cThe Cherokee called their forced march the <strong>Trail of Tears</strong>. '
    'An estimated <strong>4,000 Cherokee</strong> died of cold, disease, and starvation along the way. '
    'Soldiers drove them at bayonet point through freezing winters. '
    'Families buried children beside the trail and had to keep walking.\u201d</p>'

    '<p>Robert was quiet. \u201cThe Supreme Court had even ruled in their favor, hadn\u2019t it?\u201d</p>'

    '<p>\u201cYes. Chief Justice John Marshall ruled that the Cherokee Nation was sovereign. '
    'But Jackson reportedly said: \u201cJohn Marshall has made his decision; now let him enforce it.\u201d '
    'The president simply ignored the law.\u201d</p>'

    '<h3>The Gold Rush</h3>'

    '<p>\u201cIn January 1848, a carpenter named <strong>James Marshall</strong> found gold flakes '
    'in a riverbed at <strong>Sutter\u2019s Mill</strong> in California,\u201d William said. '
    '\u201cWord spread, and by 1849, about <strong>300,000 people</strong> had rushed to California '
    'from all over the world \u2014 from the eastern United States, Mexico, China, Europe, and South America. '
    'They were called the <strong>Forty-Niners</strong>.\u201d</p>'

    '<p>\u201cMost found nothing. A few struck it rich, but the people who made the real money '
    'were the ones selling supplies \u2014 picks, shovels, tents, and blue jeans. '
    'A man named <strong>Levi Strauss</strong> made his fortune selling durable pants to miners. '
    'California\u2019s population exploded, and it became a state in 1850.\u201d</p>'

    '<h3>Cowboys and Cattle Drives</h3>'

    '<p>\u201cAfter the Civil War, the <strong>cowboy era</strong> began,\u201d William said. '
    '\u201cMillions of longhorn cattle roamed wild in Texas, and Northern cities were hungry for beef. '
    'Cowboys drove herds of <strong>3,000 or more cattle</strong> along trails like the <strong>Chisholm Trail</strong>, '
    'covering 1,000 miles from Texas to the railroad towns of Kansas \u2014 '
    '<strong>Abilene, Dodge City, and Wichita</strong>.\u201d</p>'

    '<p>\u201cThe real cowboys were nothing like the movies,\u201d William added. '
    '\u201cAbout <strong>one in four cowboys was Black</strong>, many were Mexican <strong>vaqueros</strong> '
    'who invented most cowboy techniques, and some were Native Americans. '
    'The work was brutal \u2014 months on horseback in dust, heat, and thunderstorms, '
    'earning about a dollar a day. The average cattle drive took two to three months.\u201d</p>'

    '<h3>The Transcontinental Railroad</h3>'

    '<p>\u201cThe single biggest change to the West was the <strong>transcontinental railroad</strong>,\u201d '
    'William said. \u201cStarting in 1863, two companies raced toward each other \u2014 '
    'the <strong>Central Pacific</strong> building east from Sacramento, and the <strong>Union Pacific</strong> '
    'building west from Omaha. On <strong>May 10, 1869</strong>, they met at <strong>Promontory Summit, Utah</strong>, '
    'and a golden spike was driven to connect the rails.\u201d</p>'

    '<p>\u201cAbout <strong>12,000 Chinese immigrants</strong> did the most dangerous work on the Central Pacific, '
    'blasting tunnels through the Sierra Nevada mountains with nitroglycerin. '
    'Hundreds died in explosions and avalanches. They were paid less than white workers '
    'and given the most hazardous assignments. Yet their contribution was barely acknowledged '
    'at the golden spike ceremony \u2014 not a single Chinese worker appeared in the famous photograph.\u201d</p>'

    '<p>\u201cThe railroad shrank a journey that took six months by wagon to just six days by train. '
    'It transformed the West overnight.\u201d</p>'

    '<h3>The End of the Frontier</h3>'

    '<p>\u201cAs settlers poured west, the <strong>Native American way of life was systematically destroyed</strong>,\u201d '
    'William said. \u201cThe U.S. Army and hunters slaughtered the great <strong>buffalo herds</strong> \u2014 '
    'from an estimated 30 million down to fewer than 1,000 by the 1880s. '
    'Without the buffalo, the Plains nations lost their food, clothing, and shelter.\u201d</p>'

    '<p>\u201cNative Americans were forced onto <strong>reservations</strong> \u2014 often the worst land, '
    'far from their homelands. Those who resisted were crushed. '
    'The final tragedy came at <strong>Wounded Knee, South Dakota</strong>, on December 29, 1890, '
    'when U.S. soldiers massacred nearly <strong>300 Lakota men, women, and children</strong>. '
    'It marked the end of the Indian Wars and the closing of the American frontier.\u201d</p>'

    '<p>\u201cIn 1890, the U.S. Census declared that there was no longer a continuous frontier line. '
    'The West had been \u201csettled.\u201d But for Native Americans, it had been stolen.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="American West">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The American West \u2014 Expansion and Its Cost</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Trail of Tears (1830s)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">60,000 Native Americans removed</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">4,000 Cherokee died on the march</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Gold Rush (1849)</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">300,000 Forty-Niners rush west</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">California becomes a state (1850)</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Railroad (1869)</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Transcontinental rail completed</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">12,000 Chinese workers, many died</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Wounded Knee (1890)</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">300 Lakota massacred</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">End of the frontier era</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Manifest Destiny drove a nation westward \u2014 but at a devastating cost to Native peoples</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">The real cowboys were Black, Mexican, and Native American \u2014 not just the ones in movies</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. Robert looked out the window '
    'at the flat land stretching to the horizon.</p>'

    '<p>\u201cWe call it the Wild West like it\u2019s an adventure story,\u201d Robert said. '
    '\u201cBut it wasn\u2019t an adventure for everyone, was it?\u201d</p>'

    '<p>\u201cNo,\u201d William said. \u201cFor some it was a dream. For others it was a nightmare. '
    'The honest story includes both. '
    'Goodnight, endless prairie.\u201d</p>'

    '<p>\u201cGoodnight, forgotten cowboys.\u201d</p>'
)

disc_79 = [
    "Americans called westward expansion \u2018Manifest Destiny\u2019 and believed it was their right to settle the continent. But the land was already home to millions of Native Americans. Can a dream be inspiring for some people and devastating for others at the same time?",
    "About one in four cowboys was Black and many were Mexican vaqueros, yet movies almost always show cowboys as white. Why does it matter that we tell history accurately, even when the myths are popular?",
    "President Jackson ignored a Supreme Court ruling protecting the Cherokee Nation. What happens to a country when its leaders refuse to follow their own laws?"
]

quiz_79 = [
    {
        "q": "What was Manifest Destiny?",
        "options": [
            "A famous cattle trail",
            "The belief that Americans were destined to expand across the continent",
            "The name of the transcontinental railroad",
            "A treaty with Native Americans"
        ],
        "correct": 1
    },
    {
        "q": "Who did most of the dangerous work building the Central Pacific Railroad through the Sierra Nevada?",
        "options": [
            "African American freedmen",
            "Mexican vaqueros",
            "Chinese immigrants",
            "Irish immigrants"
        ],
        "correct": 2
    },
    {
        "q": "What 1890 event is considered the end of the American frontier era?",
        "options": [
            "The completion of the transcontinental railroad",
            "The last cattle drive on the Chisholm Trail",
            "The massacre at Wounded Knee",
            "The California Gold Rush"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 79:
        lessons[i] = {
            "id": 79,
            "type": "history",
            "topic": "WildWest",
            "title": "Cowboys and Frontiers",
            "readingTime": "10 min",
            "story": story_79,
            "discussion": disc_79,
            "quiz": quiz_79
        }
        print("Updated lesson 79: Cowboys and Frontiers")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
