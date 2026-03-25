import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_55 = (
    '<h2>Cities in the Jungle</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Tikal_mbread.jpg/800px-Tikal_mread.jpg" '
    'alt="The towering pyramids of Tikal rising above the jungle canopy in Guatemala" loading="lazy">'
    '<p class="image-caption">Tikal \u2014 the great Maya city whose pyramids rise above the rainforest canopy of Guatemala</p>'
    '</div>'

    '<p>The brass telescope felt warm in Robert\u2019s hands. William turned the hourglass dial '
    'three clicks to the left, and the room dissolved into a wall of green. '
    'Humid air hit them like a warm blanket. Howler monkeys screamed somewhere above, '
    'and parrots streaked through gaps in the canopy like living jewels.</p>'

    '<p>Then Robert looked up \u2014 and gasped. A massive stone pyramid rose through the treetops, '
    'its peak blazing white in the tropical sun, high above the tallest trees.</p>'

    '<p>\u201cWelcome to <strong>Tikal</strong>,\u201d William said. \u201cOne of the greatest cities '
    'of the <strong>Maya civilization</strong> \u2014 and we\u2019re standing in the middle of a jungle.\u201d</p>'

    '<h3>Cities Hidden in the Rainforest</h3>'

    '<p>\u201cThe Maya didn\u2019t build their civilization along a single river like Egypt or Mesopotamia,\u201d '
    'William explained. \u201cThey built it in the <strong>tropical rainforests</strong> of Central America \u2014 '
    'in what is now southern Mexico, Guatemala, Belize, Honduras, and El Salvador. '
    'Their civilization lasted for over <strong>2,000 years</strong>, from roughly 2000 BC to the arrival '
    'of the Spanish in the 1500s.\u201d</p>'

    '<p>\u201cAt its peak, between AD 250 and 900 \u2014 a period scholars call the <strong>Classic Period</strong> \u2014 '
    'the Maya had dozens of powerful city-states, each ruled by its own king called an <strong>ajaw</strong>. '
    'Tikal alone had a population of perhaps <strong>60,000 to 100,000 people</strong>. '
    'Across the Maya world, there may have been <strong>10 million people</strong> living in the jungle.\u201d</p>'

    '<p>\u201cHow did they feed that many people in a rainforest?\u201d Robert asked.</p>'

    '<p>\u201cClever farming,\u201d William said. \u201cThey used a technique called <strong>slash-and-burn agriculture</strong> '
    'to clear fields, and they built <strong>raised garden beds</strong> in swampy areas. '
    'They dug reservoirs to store rainwater. Their main crop was <strong>maize</strong> \u2014 corn \u2014 '
    'which they considered so sacred that their creation myth says the gods made '
    'the first humans out of corn dough.\u201d</p>'

    '<h3>Pyramids and Plazas</h3>'

    '<p>\u201cLook at this pyramid,\u201d William said, pointing upward. \u201cThis is <strong>Temple I</strong>, '
    'also called the <strong>Temple of the Great Jaguar</strong>. It stands about <strong>154 feet tall</strong> \u2014 '
    'roughly a 15-story building \u2014 and it was built around AD 732 as a tomb for the king '
    '<strong>Jasaw Chan K\u2019awiil I</strong>, one of Tikal\u2019s greatest rulers.\u201d</p>'

    '<p>\u201cMaya pyramids were different from Egyptian ones. Egyptian pyramids were sealed tombs. '
    'Maya pyramids had <strong>temples on top</strong> \u2014 small rooms where priests performed rituals. '
    'And the Maya often built new pyramids <em>over</em> old ones, like nesting dolls of stone. '
    'Some pyramids at Tikal have five or six older structures buried inside them.\u201d</p>'

    '<p>\u201cThe city of <strong>Chichen Itza</strong>, far to the north in the Yucatan Peninsula, '
    'has the most famous Maya pyramid of all: <strong>El Castillo</strong>, the Temple of Kukulkan. '
    'It has <strong>365 steps</strong> \u2014 one for each day of the year. '
    'And twice a year, on the spring and fall equinoxes, the setting sun casts a shadow '
    'down the staircase that looks exactly like a serpent slithering to the ground. '
    'The Maya designed that effect on purpose, over a thousand years ago.\u201d</p>'

    '<p>\u201cThat\u2019s incredible,\u201d Robert whispered.</p>'

    '<h3>A Writing System Like No Other</h3>'

    '<p>\u201cThe Maya developed the most advanced <strong>writing system</strong> in the ancient Americas,\u201d '
    'William continued. \u201cThey used <strong>hieroglyphs</strong> \u2014 over 800 different signs. '
    'Some glyphs represented whole words, and some represented sounds, like an alphabet. '
    'They carved them into stone monuments called <strong>stelae</strong>, painted them on pottery, '
    'and wrote them in books made from bark paper called <strong>codices</strong>.\u201d</p>'

    '<p>\u201cThe stelae recorded the births, wars, and deaths of kings, along with precise dates. '
    'The Maya were obsessed with recording history. We know the names of hundreds of Maya kings '
    'and the exact dates of their victories and defeats.\u201d</p>'

    '<p>\u201cBut here is the tragedy: when the Spanish arrived, a Franciscan friar named '
    '<strong>Diego de Landa</strong> ordered nearly all the Maya codices <strong>burned</strong> in 1562, '
    'calling them works of the devil. Only <strong>four Maya books</strong> survive today '
    'out of what were probably thousands. Imagine if someone burned every book in every library, '
    'and only four survived.\u201d</p>'

    '<p>Robert\u2019s eyes went wide. \u201cThat\u2019s terrible.\u201d</p>'

    '<p>\u201cIt is. But the stone carvings survived, and in the 1950s through the 1990s, '
    'scholars finally cracked the code and learned to read Maya hieroglyphs. '
    'The man who made the biggest breakthrough was a Russian linguist named '
    '<strong>Yuri Knorosov</strong>, who figured out that the glyphs represented sounds, not just pictures.\u201d</p>'

    '<h3>The Calendar and the Stars</h3>'

    '<p>\u201cThe Maya didn\u2019t just have <em>one</em> calendar,\u201d William said. '
    '\u201cThey had <strong>three</strong>, all running at the same time.\u201d</p>'

    '<p>\u201cThe <strong>Tzolk\u2019in</strong> was a sacred calendar of <strong>260 days</strong>, '
    'used for religious ceremonies and predicting the future. '
    'The <strong>Haab\u2019</strong> was a solar calendar of <strong>365 days</strong> \u2014 '
    'almost exactly like our modern year. And the <strong>Long Count</strong> was a continuous count '
    'of days from a starting point the Maya calculated as <strong>August 11, 3114 BC</strong> \u2014 '
    'their version of the beginning of the world.\u201d</p>'

    '<p>\u201cIs that the one people said would predict the end of the world in 2012?\u201d Robert asked.</p>'

    '<p>William laughed. \u201cYes \u2014 and they were completely wrong. December 21, 2012, '
    'was simply the end of one Long Count cycle and the beginning of another, '
    'like a car\u2019s odometer rolling over from 99,999 to 00,000. '
    'The Maya themselves never predicted any doomsday.\u201d</p>'

    '<p>\u201cThe Maya were extraordinary <strong>astronomers</strong>. Without telescopes, '
    'they tracked the movements of Venus with an accuracy of <strong>one day in 500 years</strong>. '
    'They predicted solar eclipses. They calculated the length of the solar year '
    'as <strong>365.2420 days</strong> \u2014 the modern measurement is 365.2422 days. '
    'They were off by only <strong>17 seconds per year</strong>.\u201d</p>'

    '<h3>The Invention of Zero</h3>'

    '<p>\u201cHere\u2019s something that might surprise you,\u201d William said. '
    '\u201cThe Maya were one of only <strong>three civilizations in all of human history</strong> '
    'to independently invent the concept of <strong>zero</strong>. '
    'The others were the Babylonians and the Indians.\u201d</p>'

    '<p>\u201cWhy is zero such a big deal?\u201d Robert asked.</p>'

    '<p>\u201cBecause without zero, you can\u2019t do advanced mathematics. You can\u2019t have place value \u2014 '
    'the difference between 1, 10, and 100 depends on zeros. '
    'The Maya used a <strong>base-20 number system</strong> (we use base-10). '
    'They wrote numbers using just three symbols: a <strong>dot</strong> for one, '
    'a <strong>bar</strong> for five, and a <strong>shell shape</strong> for zero. '
    'With those three symbols, they could write any number.\u201d</p>'

    '<h3>The Ball Game</h3>'

    '<p>\u201cEvery major Maya city had at least one <strong>ball court</strong>,\u201d William said. '
    '\u201cThe game was called <strong>pitz</strong>, and it was played with a heavy rubber ball '
    'that could weigh up to <strong>9 pounds</strong>. Players used their hips, forearms, and thighs '
    'to keep the ball in play \u2014 no hands or feet allowed. '
    'Some courts had stone rings mounted high on the walls, and getting the ball through the ring '
    'was so difficult it was like scoring a half-court shot in basketball.\u201d</p>'

    '<p>\u201cBut the game wasn\u2019t just sport. It had deep <strong>religious meaning</strong>. '
    'In Maya mythology, the Hero Twins defeated the lords of the underworld by playing the ball game. '
    'Some games were tied to warfare \u2014 captured enemy leaders were sometimes forced to play, '
    'and the losers could be sacrificed. The great ball court at Chichen Itza is the largest '
    'in the Americas: <strong>545 feet long</strong> \u2014 bigger than a football field.\u201d</p>'

    '<h3>Chocolate: Gift of the Gods</h3>'

    '<p>\u201cHere\u2019s my favorite Maya invention,\u201d William grinned. '
    '\u201c<strong>Chocolate</strong>.\u201d</p>'

    '<p>\u201cReally?\u201d Robert said.</p>'

    '<p>\u201cThe Maya were the first people to cultivate <strong>cacao trees</strong> '
    'and turn the beans into a drink. But Maya chocolate was nothing like the sweet candy bars we know. '
    'It was a bitter, frothy drink made from roasted cacao beans, water, chili peppers, and cornmeal, '
    'often poured back and forth between two cups to create a thick foam. '
    'They called it <strong>xocolatl</strong>. Cacao beans were so valuable that the Maya used them '
    'as <strong>money</strong> \u2014 you could buy a rabbit for about 10 cacao beans.\u201d</p>'

    '<h3>The Great Mystery: Why Did the Cities Fall?</h3>'

    '<p>\u201cStarting around AD 800, the great Maya cities of the southern lowlands began to collapse,\u201d '
    'William said, his voice quieter now. \u201cWithin about 150 years, cities like Tikal, '
    '<strong>Calakmul</strong>, <strong>Palenque</strong>, and <strong>Copan</strong> were abandoned. '
    'Populations dropped by 90 percent or more. The jungle swallowed the pyramids.\u201d</p>'

    '<p>\u201cWhat happened?\u201d Robert asked.</p>'

    '<p>\u201cScholars believe it was a combination of factors: a series of <strong>severe droughts</strong> '
    'lasting decades (confirmed by lake sediment studies), made worse by <strong>deforestation</strong> \u2014 '
    'the Maya had cut down so many trees for construction and farming that it may have changed '
    'the local climate. Add <strong>constant warfare</strong> between rival city-states, '
    '<strong>overpopulation</strong>, and the collapse of trade networks, and the system broke.\u201d</p>'

    '<p>\u201cBut the Maya didn\u2019t disappear,\u201d William emphasized. '
    '\u201cCities in the northern Yucatan, like Chichen Itza and <strong>Uxmal</strong>, '
    'continued to thrive for centuries. And today, there are over <strong>6 million Maya people</strong> '
    'living in Mexico, Guatemala, Belize, and Honduras, still speaking '
    '<strong>30 different Maya languages</strong>. Their culture never died \u2014 '
    'it\u2019s one of the longest continuous civilizations on Earth.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Maya Civilization">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Maya Civilization at a Glance</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Great Cities</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Tikal, Chichen Itza, Palenque</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">60,000\u2013100,000 people at Tikal</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Writing &amp; Math</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">800+ hieroglyphs, concept of zero</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Base-20 number system</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Astronomy</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Solar year: 365.2420 days</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Off by only 17 seconds/year</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Legacy</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">6 million Maya people today</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">30 living Maya languages</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Invented chocolate, the concept of zero, and the most advanced writing in the Americas</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">Their civilization spanned over 2,000 years \u2014 and their culture endures today</text>'
    '</svg>'
    '</div>'

    '<p>The telescope\u2019s dial clicked, and the jungle dissolved around them. '
    'They were back in their room, the smell of tropical rain still lingering in their hair.</p>'

    '<p>\u201cThey figured out zero, tracked Venus without a telescope, '
    'and built pyramids that line up with the sun,\u201d Robert said quietly. '
    '\u201cAll in a jungle.\u201d</p>'

    '<p>\u201cAnd someone burned almost all their books,\u201d William said. '
    '\u201cRemember that. Knowledge is precious. Goodnight, cities in the jungle.\u201d</p>'

    '<p>\u201cGoodnight, chocolate money.\u201d</p>'
)

disc_55 = [
    "The Maya invented the concept of zero, tracked Venus with extraordinary accuracy, and built pyramids aligned with the equinoxes \u2014 all without metal tools or telescopes. What does this tell us about the relationship between technology and intelligence?",
    "When Diego de Landa burned the Maya codices, nearly an entire civilization\u2019s written knowledge was destroyed. Why is it important to preserve the writings and records of other cultures, even if we don\u2019t understand or agree with them?",
    "The Maya collapse was likely caused by a combination of drought, deforestation, warfare, and overpopulation. Do you see any parallels to challenges the modern world faces today?"
]

quiz_55 = [
    {
        "q": "How many calendars did the Maya use simultaneously?",
        "options": [
            "One \u2014 a 365-day solar calendar",
            "Two \u2014 a sacred calendar and a solar calendar",
            "Three \u2014 the Tzolk\u2019in, the Haab\u2019, and the Long Count",
            "Four \u2014 one for each season"
        ],
        "correct": 2
    },
    {
        "q": "What was special about the Maya concept of zero?",
        "options": [
            "They borrowed it from the Egyptians",
            "They were one of only three civilizations to independently invent it",
            "They used it only for astronomy, not mathematics",
            "It was invented by the Spanish after they arrived"
        ],
        "correct": 1
    },
    {
        "q": "What happened to most of the Maya codices (books)?",
        "options": [
            "They were sent to museums in Europe",
            "They dissolved in the tropical humidity",
            "A Spanish friar ordered them burned in 1562",
            "They were buried in pyramids and never found"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 55:
        lessons[i] = {
            "id": 55,
            "type": "history",
            "topic": "Maya",
            "title": "Cities in the Jungle",
            "readingTime": "10 min",
            "story": story_55,
            "discussion": disc_55,
            "quiz": quiz_55
        }
        print("Updated lesson 55: Cities in the Jungle")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
