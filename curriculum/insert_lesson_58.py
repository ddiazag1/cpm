import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_58 = (
    '<h2>The Way of the Samurai</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Samurai_with_sword.jpg/800px-Samurai_with_sword.jpg" '
    'alt="A samurai warrior in traditional armor" loading="lazy">'
    '<p class="image-caption">A samurai warrior \u2014 Japan\u2019s elite military class for over 700 years</p>'
    '</div>'

    '<p>Jason opened The Living World and turned the brass clasp to the hourglass. '
    '\u201cTonight we\u2019re visiting an island where warriors followed a code of honor '
    'that shaped an entire civilization.\u201d</p>'

    '<p>The green light carried them across an ocean to a misty mountainside. '
    'Cherry blossoms drifted through the air, and below them a castle with gracefully curved roofs '
    'rose above a moat of still water.</p>'

    '<h3>The Land of the Rising Sun</h3>'

    '<p>\u201c<strong>Japan</strong> is an archipelago \u2014 a chain of nearly 7,000 islands '
    'off the east coast of Asia,\u201d Jason said. \u201cThe Japanese call their country <strong>Nihon</strong>, '
    'which means \u2018origin of the sun\u2019 \u2014 because from China\u2019s perspective, '
    'the sun rose from Japan\u2019s direction.\u201d</p>'

    '<p>\u201cJapan\u2019s geography shaped everything about its history. '
    'Mountains cover 73 percent of the islands, so people crowded into coastal plains and river valleys. '
    'The surrounding ocean isolated Japan from invasions \u2014 '
    'it was never successfully conquered by a foreign power in its ancient or medieval history. '
    'This isolation let Japan develop a culture unlike anywhere else on Earth.\u201d</p>'

    '<h3>The Rise of the Samurai</h3>'

    '<p>\u201cIn the early centuries, Japan was ruled by an <strong>emperor</strong> '
    'who was considered a living descendant of the sun goddess <strong>Amaterasu</strong>,\u201d Jason said. '
    '\u201cBut by the 1100s, powerful warrior clans had gained so much power '
    'that the real rulers became military leaders called <strong>shoguns</strong>. '
    'The emperor became a figurehead \u2014 respected but powerless \u2014 '
    'while the shogun commanded the armies and governed the country.\u201d</p>'

    '<p>\u201cThe shogun\u2019s warriors were the <strong>samurai</strong> \u2014 '
    'an elite class of professional soldiers who served their lords with absolute loyalty. '
    'The word <em>samurai</em> means \u2018one who serves.\u2019 '
    'They followed a strict code of honor called <strong>bushido</strong> \u2014 '
    '\u2018the way of the warrior\u2019 \u2014 which demanded courage, loyalty, self-discipline, '
    'honor, and respect. A samurai would rather die than bring shame upon his family or lord.\u201d</p>'

    '<h3>The Samurai\u2019s World</h3>'

    '<p>\u201cSamurai trained from childhood,\u201d Jason continued. '
    '\u201cTheir primary weapon was the <strong>katana</strong> \u2014 '
    'a curved steel sword considered the soul of the samurai. '
    'Japanese swordsmiths folded the steel thousands of times, '
    'creating blades so sharp they could cut through armor. '
    'A master swordsmith might spend months forging a single blade.\u201d</p>'

    '<p>\u201cBut samurai weren\u2019t just fighters. Bushido required them to be cultured as well. '
    'A true samurai studied <strong>calligraphy</strong> (beautiful writing), '
    '<strong>poetry</strong>, the <strong>tea ceremony</strong>, and <strong>flower arranging</strong>. '
    'The idea was that a warrior should be equally skilled with a sword and a paintbrush. '
    'Many of Japan\u2019s greatest poets, artists, and philosophers were samurai.\u201d</p>'

    '<h3>Castles, Shoguns, and Feudal Japan</h3>'

    '<p>\u201cJapan\u2019s feudal period lasted from the 1100s to the 1800s,\u201d Jason said. '
    '\u201cDuring this time, powerful lords called <strong>daimyo</strong> '
    'controlled different regions, each with their own samurai armies. '
    'They built magnificent castles with stone walls and wooden towers \u2014 '
    '<strong>Himeji Castle</strong>, built in the 1300s and expanded in the 1600s, '
    'still stands today and is called the \u2018White Heron\u2019 for its elegant white walls.\u201d</p>'

    '<p>\u201cIn 1600, <strong>Tokugawa Ieyasu</strong> won a great battle and unified Japan '
    'under the <strong>Tokugawa Shogunate</strong>. For the next 250 years \u2014 '
    'the <strong>Edo period</strong> \u2014 Japan experienced peace, '
    'but the shoguns closed the country to almost all foreign contact. '
    'No one could leave Japan, and almost no one could enter. '
    'During this isolation, Japanese art, theater (<strong>kabuki</strong> and <strong>noh</strong>), '
    'and culture flourished in unique ways.\u201d</p>'

    '<h3>The Kamikaze \u2014 Divine Wind</h3>'

    '<p>\u201cTwice, in 1274 and 1281, the <strong>Mongol Empire</strong> under Kublai Khan '
    'sent massive invasion fleets to conquer Japan,\u201d Jason said. '
    '\u201cBoth times, devastating typhoons destroyed the Mongol ships. '
    'The Japanese called these storms <strong>kamikaze</strong> \u2014 \u2018divine wind\u2019 \u2014 '
    'believing the gods themselves were protecting Japan.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Feudal Japan">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Feudal Japan\u2019s Social Order</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Emperor</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Divine figurehead</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Respected but powerless</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Shogun &amp; Daimyo</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Military rulers &amp; regional lords</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Held the real power</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Samurai</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Warrior class, bushido code</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Sword + poetry + honor</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Farmers &amp; Artisans</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">90% of the population</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Fed and built the nation</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">250 years of peace under the Tokugawa (1603\u20131868) \u2014 one of the longest peaceful periods in history</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">Japan closed itself to the world, creating a unique culture found nowhere else</text>'
    '</svg>'
    '</div>'

    '<p>The book carried them home. The cherry blossoms faded, '
    'but the image of the castle on the misty mountain remained.</p>'

    '<p>\u201cA warrior who writes poetry,\u201d Evelyn said. \u201cI like that.\u201d</p>'

    '<p>\u201cStrength and beauty together,\u201d Jason said. \u201cThat\u2019s what bushido teaches. '
    'Goodnight, samurai.\u201d</p>'

    '<p>\u201cGoodnight, white heron castle.\u201d</p>'
)

disc_58 = [
    "Bushido required samurai to master both fighting and art \u2014 the sword and the paintbrush. Why do you think combining strength with culture was important to the Japanese?",
    "Japan closed itself to the outside world for 250 years. What are the advantages and disadvantages of a country isolating itself? Could any country do this today?",
    "The Japanese believed divine wind (kamikaze) saved them from the Mongols. How do people explain lucky events through religion or fate? Can you think of other examples?"
]

quiz_58 = [
    {
        "q": "What was the samurai code of honor called?",
        "options": ["Shogunate", "Bushido", "Kamikaze", "Kabuki"],
        "correct": 1
    },
    {
        "q": "Who held the real power in feudal Japan?",
        "options": ["The emperor", "The shogun", "The farmers", "The monks"],
        "correct": 1
    },
    {
        "q": "What does the word \u2018kamikaze\u2019 mean?",
        "options": ["Sacred warrior", "Divine wind", "Eternal honor", "Rising sun"],
        "correct": 1
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 58:
        lessons[i] = {
            "id": 58,
            "type": "history",
            "topic": "Japan",
            "title": "The Way of the Samurai",
            "readingTime": "10 min",
            "story": story_58,
            "discussion": disc_58,
            "quiz": quiz_58
        }
        print("Updated lesson 58: The Way of the Samurai")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
