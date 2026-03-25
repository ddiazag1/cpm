import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_90 = (
    '<h2>Connecting the Dots</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/800px-Image_created_with_a_mobile_phone.png" '
    'alt="A view of Earth from space showing the blue planet against the darkness of space" loading="lazy">'
    '<p class="image-caption">Our pale blue dot \u2014 home to every story ever told</p>'
    '</div>'

    '<p>Evelyn found The Living World sitting on the table where it always sat. '
    'But tonight, something was different. The brass clasp was warm to the touch, '
    'and a faint golden light pulsed along the spine, like a heartbeat.</p>'

    '<p>\u201cJason,\u201d she whispered. \u201cThe book is glowing.\u201d</p>'

    '<p>Jason sat down beside her and placed his hand on the cover. '
    'He could feel it too \u2014 a hum, gentle and deep, like the book was full of voices.</p>'

    '<p>\u201cI think it wants to take us on one last journey,\u201d he said.</p>'

    '<p>Evelyn opened the book. The green light flared brighter than it ever had before, '
    'and suddenly they were not in one place, but in <em>all</em> of them.</p>'

    '<h3>A River of Time</h3>'

    '<p>They stood on a vast, shimmering plain that stretched in every direction. '
    'Below their feet, images moved like a river \u2014 scenes from every story '
    'they had ever visited, flowing and connecting in ways they had never noticed before.</p>'

    '<p>\u201cLook,\u201d Jason said. \u201cThe <strong>Mesopotamians</strong> invented writing, '
    'and that idea flowed to <strong>Egypt</strong>, where scribes recorded the pharaohs\u2019 deeds. '
    'Egypt\u2019s knowledge passed to <strong>Greece</strong>, where philosophers asked new questions. '
    'Greece\u2019s ideas were preserved by <strong>Rome</strong>, and when Rome fell, '
    'it was <strong>Islamic scholars</strong> in Baghdad who kept those ideas alive '
    'during Europe\u2019s Dark Ages. When those texts returned to Europe, '
    'they sparked the <strong>Renaissance</strong> \u2014 which led to the <strong>Scientific Revolution</strong> \u2014 '
    'which led to the <strong>Enlightenment</strong> \u2014 which inspired the <strong>American</strong> '
    'and <strong>French Revolutions</strong>.\u201d</p>'

    '<p>Evelyn watched the images flow. \u201cIt\u2019s all connected.\u201d</p>'

    '<p>\u201cEvery bit of it,\u201d Jason said. \u201c<strong>Chinese</strong> papermakers invented paper, '
    'which traveled the Silk Road to the Islamic world, which brought it to Europe, '
    'where <strong>Gutenberg</strong> used it for his printing press, '
    'which spread the ideas that fueled the Reformation, the Enlightenment, '
    'and eventually the Declaration of Independence. '
    'One invention in China changed the course of history in America \u2014 '
    'a thousand years later.\u201d</p>'

    '<h3>The Threads Between Stories</h3>'

    '<p>\u201c<strong>Trade routes</strong> carried more than goods,\u201d Jason continued. '
    '\u201cThe Silk Road, the Indian Ocean trade, the trans-Saharan routes \u2014 '
    'they carried <strong>ideas</strong>, <strong>religions</strong>, <strong>languages</strong>, '
    'and <strong>technologies</strong>. Gunpowder was invented in China, '
    'perfected in the Islamic world, and used by Europeans to build empires. '
    'Spices from India drove Columbus west, which led to the Columbian Exchange, '
    'which transformed food, disease, and populations on every continent.\u201d</p>'

    '<p>\u201c<strong>Migrations</strong> reshaped the world,\u201d he said. '
    '\u201cHumans walked out of Africa and settled every continent. '
    'Bantu peoples spread agriculture across sub-Saharan Africa. '
    'Polynesians sailed thousands of miles across the Pacific. '
    'The Great Migration brought millions of African Americans north. '
    'Refugees and immigrants have carried their cultures to new lands '
    'in every century of human history.\u201d</p>'

    '<p>\u201cAnd <strong>inventions</strong> built on each other,\u201d Evelyn added, '
    'surprising herself. \u201cFarming led to cities. Cities led to writing. '
    'Writing led to laws. Laws led to empires. Empires built roads. '
    'Roads spread ideas. Ideas led to science. Science led to machines. '
    'Machines led to computers. Computers connected the whole world.\u201d</p>'

    '<p>Jason looked at her and smiled. \u201cYou just told the story of civilization '
    'in eight sentences.\u201d</p>'

    '<h3>What History Teaches</h3>'

    '<p>\u201cWe\u2019ve traveled from the first campfires in Africa to the Moon,\u201d Jason said. '
    '\u201cWe\u2019ve met pharaohs and philosophers, emperors and explorers, '
    'scientists and dreamers. We\u2019ve seen empires rise and fall. '
    'We\u2019ve watched people build extraordinary things \u2014 '
    'and do terrible things to each other.\u201d</p>'

    '<p>\u201cIf there\u2019s one lesson from all these stories, it\u2019s this: '
    '<strong>progress is not a straight line</strong>. '
    'Civilizations rise, and they fall. Knowledge is gained, and sometimes lost. '
    'People fight for freedom, and others try to take it away. '
    'Every generation has to choose what kind of world it wants to build \u2014 '
    'and that choice never ends.\u201d</p>'

    '<p>\u201cBut here\u2019s what gives me hope,\u201d he said. '
    '\u201cIn every era, in every civilization, in every dark chapter of history, '
    'there were people who chose courage over fear, compassion over cruelty, '
    'and knowledge over ignorance. <strong>They are the reason we are here.</strong>\u201d</p>'

    '<h3>The Book\u2019s Last Gift</h3>'

    '<p>As Jason spoke, the pages of The Living World began to turn on their own. '
    'Faster and faster they turned, and from each page, a faint golden light rose '
    'like a firefly and drifted toward Evelyn and Jason. The lights were warm '
    'and gentle, and each one carried a whisper \u2014 a word, a name, a moment.</p>'

    '<p><em>Mesopotamia\u2026 pyramids\u2026 democracy\u2026 the Silk Road\u2026 '
    'the printing press\u2026 the Renaissance\u2026 gravity\u2026 liberty\u2026 '
    'the railroad\u2026 the Moon\u2026 I have a dream\u2026</em></p>'

    '<p>The lights settled on them like snowflakes, sinking in and disappearing. '
    'Evelyn felt warm all over. She felt like she was carrying something precious '
    'inside her chest \u2014 not heavy, but <em>full</em>.</p>'

    '<p>Then the book\u2019s pages stopped turning. The brass clasp dimmed. '
    'The hourglass symbol on the cover, which had always glowed faintly green, '
    'flickered once\u2026 twice\u2026 and then gently faded away.</p>'

    '<p>Evelyn reached out and touched the cover. It was cool now. '
    'Just leather and paper and old binding.</p>'

    '<p>\u201cIs it\u2026 gone?\u201d she asked, her voice small.</p>'

    '<p>\u201cThe magic is,\u201d Jason said softly. \u201cBut the stories aren\u2019t. '
    'They\u2019re in you now. Every one of them.\u201d</p>'

    '<p>Evelyn held the book to her chest. \u201cI don\u2019t need the green light anymore, '
    'do I?\u201d</p>'

    '<p>\u201cNo,\u201d Jason said. \u201cThe green light showed you the past. '
    'But you can carry these stories forward all on your own. '
    'Every time you read a book, ask a question, listen to someone different from you, '
    'or stand up for what\u2019s right \u2014 you\u2019re doing exactly what that book taught you to do. '
    'You\u2019re connecting the dots.\u201d</p>'

    '<p>Evelyn looked out the window one last time. The stars were bright. '
    'Somewhere out there were the pyramids and the Great Wall and the Moon '
    'with footprints that would last forever.</p>'

    '<p>\u201cGoodnight, Jason,\u201d she said.</p>'

    '<p>\u201cGoodnight, Evelyn.\u201d</p>'

    '<p>She paused at the door and turned back. '
    '\u201cGoodnight, Living World. Thank you for everything.\u201d</p>'

    '<p>And somewhere, deep in the pages of the old book, '
    'a faint green light flickered \u2014 just for a moment \u2014 '
    'as if to say: <em>the story is yours now.</em></p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Journey Through History">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Our Journey Through History \u2014 All Connected</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Ancient Foundations</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Mesopotamia, Egypt, Greece, Rome</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Writing, law, democracy, roads</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Exchange &amp; Rebirth</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Silk Road, Islam, Renaissance</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Ideas travel, knowledge revives</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Revolution &amp; Industry</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Science, liberty, steam, steel</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">People demand freedom</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Modern World</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">World wars, rights, space, digital</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">The story continues with you</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Every civilization built on what came before \u2014 history is one long, connected story</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">The stories live inside you now \u2014 carry them forward</text>'
    '</svg>'
    '</div>'
)

disc_90 = [
    "We traced how one invention \u2014 like paper from China \u2014 could change history a thousand years later on another continent. Can you think of something happening today that might change the world in ways we can\u2019t predict yet?",
    "Jason said \u2018progress is not a straight line\u2019 \u2014 civilizations rise and fall, knowledge is gained and sometimes lost. Why is it important to remember that progress is never guaranteed?",
    "The magic book\u2019s light faded away, but Evelyn realized the stories live inside her now. What is one story from history that you will carry with you, and why?"
]

quiz_90 = [
    {
        "q": "How did Chinese papermaking eventually affect the American Revolution?",
        "options": [
            "It didn\u2019t \u2014 the two events were unrelated",
            "Paper traveled the Silk Road to Europe, enabling the printing press, which spread the Enlightenment ideas that inspired the Revolution",
            "Chinese soldiers brought paper to America directly",
            "Benjamin Franklin learned papermaking in China"
        ],
        "correct": 1
    },
    {
        "q": "What carried ideas, religions, and technologies between civilizations throughout history?",
        "options": [
            "Satellites",
            "Royal messengers",
            "Trade routes like the Silk Road",
            "Carrier pigeons"
        ],
        "correct": 2
    },
    {
        "q": "What is the main lesson Jason says history teaches us?",
        "options": [
            "The strongest military always wins",
            "Progress is automatic and can never be lost",
            "Progress is not a straight line \u2014 every generation must choose what kind of world to build",
            "Technology is more important than people"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 90:
        lessons[i] = {
            "id": 90,
            "type": "history",
            "topic": "Review",
            "title": "Connecting the Dots",
            "readingTime": "10 min",
            "story": story_90,
            "discussion": disc_90,
            "quiz": quiz_90
        }
        print("Updated lesson 90: Connecting the Dots")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
