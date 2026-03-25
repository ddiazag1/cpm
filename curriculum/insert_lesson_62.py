import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_62 = (
    '<h2>The Horsemen of the Steppe</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Mongol_Empire_map.gif/800px-Mongol_Empire_map.gif" '
    'alt="Map of the Mongol Empire at its greatest extent" loading="lazy">'
    '<p class="image-caption">The Mongol Empire at its height \u2014 the largest contiguous land empire in human history</p>'
    '</div>'

    '<p>Jason opened The Living World and turned the brass clasp. '
    'The green light swallowed the room, and when it cleared, the children stood '
    'on an endless grassland that stretched to the horizon in every direction. '
    'The wind carried the smell of horses and campfire smoke. '
    'In the distance, thousands of round felt tents \u2014 <strong>gers</strong>, sometimes called yurts \u2014 '
    'dotted the plain like scattered white stones.</p>'

    '<p>\u201cThis is the Mongolian steppe,\u201d Jason said. \u201cAround the year 1200. '
    'And the man walking toward that tent is about to build the largest land empire '
    'the world has ever seen.\u201d</p>'

    '<h3>Temujin Becomes Genghis Khan</h3>'

    '<p>\u201cThe Mongol people were <strong>nomads</strong> \u2014 herders who followed their livestock '
    'across the vast grasslands of Central Asia,\u201d Jason said. '
    '\u201cThey lived in scattered, feuding tribes. They were superb riders (children learned to ride '
    'before they could walk) and deadly archers, but they had no cities, no written language, '
    'and no central government. No one thought they could threaten the great empires around them.\u201d</p>'

    '<p>\u201cThen came <strong>Temujin</strong>. Born around 1162 into a minor noble family, '
    'he endured a brutal childhood \u2014 his father was poisoned by a rival tribe, '
    'his family was abandoned on the steppe, and he was captured and enslaved as a teenager. '
    'But through a combination of military genius, personal charisma, and ruthless determination, '
    'he slowly united the warring Mongol tribes.\u201d</p>'

    '<p>\u201cIn 1206, a great assembly of tribes proclaimed him <strong>Genghis Khan</strong> \u2014 '
    'meaning \u2018Universal Ruler.\u2019 He was about 44 years old. '
    'He immediately set about transforming the Mongols from a loose confederation of nomads '
    'into the most disciplined and effective military force on Earth.\u201d</p>'

    '<h3>The Mongol War Machine</h3>'

    '<p>\u201cWhat made the Mongol army so devastating?\u201d Evelyn asked.</p>'

    '<p>\u201cEverything,\u201d Jason said. \u201cGenghis Khan reorganized his entire society around warfare. '
    'He broke up the old tribal loyalties and organized his army into units of 10, 100, 1,000, and 10,000 \u2014 '
    'called <strong>arbans, zuuns, mingghans, and tumens</strong>. Soldiers were loyal to their unit, '
    'not their tribe. Promotion was based on merit, not birth.\u201d</p>'

    '<p>\u201cEvery Mongol warrior was a <strong>horse archer</strong> \u2014 '
    'able to shoot accurately at a full gallop in any direction, including backward. '
    'Each warrior brought three to five horses on campaign and rotated between them, '
    'meaning the Mongol army could cover <strong>60 to 100 miles per day</strong> \u2014 '
    'a speed no other army could match until the invention of the railroad.\u201d</p>'

    '<p>\u201cThey also mastered <strong>psychological warfare</strong>. Before attacking a city, '
    'they would send spies and merchants ahead to gather intelligence. '
    'They spread terrifying stories about their own brutality \u2014 sometimes exaggerated, sometimes not \u2014 '
    'so that cities would surrender without a fight. They used feigned retreats, drawing enemies '
    'into ambushes. They diverted rivers, catapulted plague-ridden corpses over walls, '
    'and lit thousands of extra campfires to make their army look larger than it was.\u201d</p>'

    '<h3>The Conquests</h3>'

    '<p>\u201cBetween 1209 and 1227 \u2014 just 18 years \u2014 Genghis Khan conquered '
    'northern China, Central Asia, Persia, and parts of Eastern Europe,\u201d Jason said. '
    '\u201cHe destroyed the powerful <strong>Khwarezmian Empire</strong> after its sultan '
    'killed Mongol ambassadors (Genghis Khan took diplomatic insults very seriously). '
    'Cities that resisted were annihilated. Cities that surrendered were spared.\u201d</p>'

    '<p>\u201cThe destruction was staggering. Baghdad, the jewel of the Islamic world, '
    'was sacked by Genghis Khan\u2019s grandson <strong>Hulagu</strong> in 1258. '
    'The Tigris River reportedly ran black with ink from the libraries\u2019 destroyed books, '
    'then red with blood. Estimates suggest that Mongol conquests killed '
    '<strong>30 to 40 million people</strong> \u2014 roughly 10 percent of the world\u2019s population.\u201d</p>'

    '<p>Evelyn shivered. \u201cThat\u2019s horrible.\u201d</p>'

    '<p>\u201cIt was,\u201d Jason agreed. \u201cBut what came after the conquests was more complicated '
    'than simple destruction.\u201d</p>'

    '<h3>The Pax Mongolica</h3>'

    '<p>\u201cOnce the killing stopped, something remarkable happened,\u201d Jason said. '
    '\u201cThe Mongol Empire stretched from Korea to Hungary \u2014 '
    'the <strong>largest contiguous land empire in history</strong>. '
    'And Genghis Khan and his successors created a system that brought '
    'an extraordinary period of peace and exchange called the <strong>Pax Mongolica</strong> \u2014 '
    'the Mongol Peace.\u201d</p>'

    '<p>\u201cThe <strong>Silk Road</strong>, which had been fragmented and dangerous for centuries, '
    'became safe under Mongol protection. A merchant could travel from Beijing to Baghdad '
    'without fear of bandits. The Mongols established a <strong>postal relay system</strong> '
    '(the <strong>Yam</strong>) with stations every 25 miles across the empire, '
    'carrying messages at incredible speed.\u201d</p>'

    '<p>\u201cGenghis Khan also decreed <strong>religious tolerance</strong>. '
    'Christians, Muslims, Buddhists, and Taoists all practiced freely within the empire. '
    'He created a written Mongol legal code (the <strong>Yasa</strong>), abolished torture of prisoners, '
    'exempted clergy and scholars from taxation, and promoted trade above all else.\u201d</p>'

    '<h3>Kublai Khan and Marco Polo</h3>'

    '<p>\u201cGenghis Khan died in 1227. His empire was divided among his sons and grandsons. '
    'The most famous was <strong>Kublai Khan</strong>, who completed the conquest of China '
    'and founded the <strong>Yuan Dynasty</strong> in 1271. Kublai moved his capital to '
    'what is now <strong>Beijing</strong> and ruled over the wealthiest nation on Earth.\u201d</p>'

    '<p>\u201cKublai was fascinated by Chinese culture. He employed scholars, promoted trade, '
    'extended the Grand Canal, introduced paper money across his domain, '
    'and welcomed visitors from all over the world. The most famous visitor was '
    '<strong>Marco Polo</strong>, a young merchant from Venice who arrived in China around 1275 '
    'and claimed to have served in Kublai\u2019s court for 17 years.\u201d</p>'

    '<p>\u201cMarco Polo\u2019s account, <em>The Travels of Marco Polo</em>, described a world '
    'of unimaginable wealth and sophistication \u2014 paper money, coal heating, a postal system, '
    'cities larger than anything in Europe. Many Europeans didn\u2019t believe him. '
    'But his book inspired generations of explorers, including Christopher Columbus, '
    'who carried a well-worn copy on his voyage to America.\u201d</p>'

    '<h3>Decline and Fragmentation</h3>'

    '<p>\u201cAn empire built on horseback was hard to hold together,\u201d Jason said. '
    '\u201cAfter Kublai Khan died in 1294, the Yuan Dynasty weakened under rebellions and famines. '
    'In 1368, the Chinese drove the Mongols out and established the <strong>Ming Dynasty</strong>. '
    'The western portions of the empire had already fractured into separate khanates \u2014 '
    'the <strong>Golden Horde</strong> in Russia, the <strong>Chagatai Khanate</strong> in Central Asia, '
    'and the <strong>Ilkhanate</strong> in Persia. Each gradually adopted the local religion and culture, '
    'and the great unified empire faded.\u201d</p>'

    '<p>\u201cBut the Mongol legacy endured. They connected East and West in ways '
    'that had never existed before. Gunpowder, printing, the compass, and the plague '
    'all traveled the Silk Road during the Pax Mongolica. '
    'The modern nations of China, Russia, Iran, and Korea were all shaped by Mongol rule. '
    'And Genghis Khan\u2019s DNA lives on \u2014 genetic studies suggest that roughly 16 million men alive today '
    'may be his direct descendants.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 150" width="700" height="150" xmlns="http://www.w3.org/2000/svg" aria-label="Mongol Empire timeline">'
    '<rect width="700" height="150" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Mongol Empire (1206\u20131368)</text>'

    '<line x1="60" y1="42" x2="640" y2="42" stroke="#b8a88a" stroke-width="2"/>'

    '<circle cx="100" cy="42" r="4" fill="#e8a838"/>'
    '<text x="100" y="58" text-anchor="middle" fill="#e8a838" font-size="8" font-weight="bold">1206</text>'
    '<text x="100" y="70" text-anchor="middle" fill="#b8a88a" font-size="7">Temujin becomes</text>'
    '<text x="100" y="80" text-anchor="middle" fill="#b8a88a" font-size="7">Genghis Khan</text>'

    '<circle cx="230" cy="42" r="4" fill="#e74c3c"/>'
    '<text x="230" y="58" text-anchor="middle" fill="#e74c3c" font-size="8" font-weight="bold">1227</text>'
    '<text x="230" y="70" text-anchor="middle" fill="#b8a88a" font-size="7">Genghis Khan dies</text>'
    '<text x="230" y="80" text-anchor="middle" fill="#b8a88a" font-size="7">Empire split among sons</text>'

    '<circle cx="370" cy="42" r="4" fill="#4a90d9"/>'
    '<text x="370" y="58" text-anchor="middle" fill="#4a90d9" font-size="8" font-weight="bold">1258</text>'
    '<text x="370" y="70" text-anchor="middle" fill="#b8a88a" font-size="7">Hulagu sacks Baghdad</text>'
    '<text x="370" y="80" text-anchor="middle" fill="#b8a88a" font-size="7">End of Abbasid Caliphate</text>'

    '<circle cx="480" cy="42" r="4" fill="#2ecc71"/>'
    '<text x="480" y="58" text-anchor="middle" fill="#2ecc71" font-size="8" font-weight="bold">1271</text>'
    '<text x="480" y="70" text-anchor="middle" fill="#b8a88a" font-size="7">Kublai Khan founds</text>'
    '<text x="480" y="80" text-anchor="middle" fill="#b8a88a" font-size="7">Yuan Dynasty (China)</text>'

    '<circle cx="600" cy="42" r="4" fill="#e8a838"/>'
    '<text x="600" y="58" text-anchor="middle" fill="#e8a838" font-size="8" font-weight="bold">1368</text>'
    '<text x="600" y="70" text-anchor="middle" fill="#b8a88a" font-size="7">Ming Dynasty expels</text>'
    '<text x="600" y="80" text-anchor="middle" fill="#b8a88a" font-size="7">Mongols from China</text>'

    '<text x="350" y="108" text-anchor="middle" fill="#b8a88a" font-size="9">Largest contiguous land empire: Korea to Hungary</text>'
    '<text x="350" y="122" text-anchor="middle" fill="#e8a838" font-size="8">Pax Mongolica: safe Silk Road \u2022 religious tolerance \u2022 postal system (Yam)</text>'
    '<text x="350" y="136" text-anchor="middle" fill="#b8a88a" font-size="8">Gunpowder, printing, compass, and plague all spread along Mongol trade routes</text>'
    '</svg>'
    '</div>'

    '<p>The green light carried them home. The endless steppe was gone, '
    'replaced by the quiet hum of their room.</p>'

    '<p>Evelyn was quiet for a long time. \u201cThey destroyed so much,\u201d she said. '
    '\u201cBut they also connected everything.\u201d</p>'

    '<p>\u201cThat\u2019s the hardest thing about history,\u201d Jason said. '
    '\u201cThe same people can be the destroyers and the builders. '
    'Goodnight, horsemen of the steppe.\u201d</p>'

    '<p>\u201cGoodnight, Mongol Empire.\u201d</p>'
)

disc_62 = [
    "The Mongol conquests killed millions of people, but the Pax Mongolica that followed connected civilizations and spread knowledge across continents. Can something terrible lead to something good? How should we think about that?",
    "Genghis Khan promoted people based on ability instead of birth and decreed religious tolerance across his empire. These seem like modern ideas. Why do you think a 13th-century nomadic warrior adopted them?",
    "Marco Polo described a world of wealth and sophistication in China, but many Europeans didn\u2019t believe him. Why is it sometimes hard for people to accept that other civilizations might be more advanced than their own?"
]

quiz_62 = [
    {
        "q": "What does \u2018Genghis Khan\u2019 mean?",
        "options": [
            "Great Warrior",
            "Universal Ruler",
            "King of Horses",
            "Lord of the Steppe"
        ],
        "correct": 1
    },
    {
        "q": "What was the Pax Mongolica?",
        "options": [
            "A religious text written by Mongol scholars",
            "The Mongol legal code created by Genghis Khan",
            "A period of peace and trade across the Mongol Empire",
            "A peace treaty between the Mongols and China"
        ],
        "correct": 2
    },
    {
        "q": "Which dynasty did Kublai Khan establish in China?",
        "options": ["Ming Dynasty", "Song Dynasty", "Tang Dynasty", "Yuan Dynasty"],
        "correct": 3
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 62:
        lessons[i] = {
            "id": 62,
            "type": "history",
            "topic": "Mongols",
            "title": "The Horsemen of the Steppe",
            "readingTime": "10 min",
            "story": story_62,
            "discussion": disc_62,
            "quiz": quiz_62
        }
        print("Updated lesson 62: The Horsemen of the Steppe")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
