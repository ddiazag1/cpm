import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_66 = (
    '<h2>Columbus and Magellan</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Waldseemuller_map_2.jpg/800px-Waldseemuller_map_2.jpg" '
    'alt="The 1507 Waldseem\u00fcller map, the first to label the Americas" loading="lazy">'
    '<p class="image-caption">The 1507 Waldseem\u00fcller map \u2014 the first map to show the Americas as a separate continent</p>'
    '</div>'

    '<p>Evelyn was spinning a globe in the study, watching the blue oceans blur past. '
    '\u201cJason, who was the first person to go all the way around?\u201d</p>'

    '<p>Jason opened The Living World and turned the brass clasp. The hourglass glowed warm. '
    '\u201cThat\u2019s a story about courage, greed, and a world that turned out to be much bigger '
    'than anyone imagined.\u201d</p>'

    '<p>The green light deposited them on a wooden dock where three small ships rocked in the harbor. '
    'Sailors loaded barrels of salted meat and fresh water. A man in a red doublet '
    'stood at the end of the dock, staring west at the open Atlantic Ocean '
    'as if he could see something no one else could.</p>'

    '<h3>Why Explore?</h3>'

    '<p>\u201cWe\u2019re in Palos de la Frontera, Spain. August 3, 1492,\u201d Jason said. '
    '\u201cThe <strong>Age of Exploration</strong> is about to change the world forever. '
    'But first \u2014 why? Why did Europeans suddenly start sailing into the unknown?\u201d</p>'

    '<p>\u201cThree reasons: <strong>spices, gold, and God</strong>. '
    'Spices like pepper, cinnamon, and cloves came from Asia and were worth more than gold in Europe. '
    'They preserved food, flavored bland meals, and were used in medicines. '
    'But the overland trade routes to Asia were controlled by Ottoman Turks and Italian middlemen, '
    'who charged enormous prices. European kings wanted a sea route to cut out the middlemen.\u201d</p>'

    '<p>\u201cGold and silver drove explorers too \u2014 stories of wealthy kingdoms in Africa and Asia '
    'fired the imagination. And many genuinely believed they had a duty to spread <strong>Christianity</strong> '
    'to the rest of the world. The Spanish and Portuguese monarchs saw exploration as both profit and mission.\u201d</p>'

    '<h3>Columbus \u2014 The Voyage of 1492</h3>'

    '<p>\u201cThat man at the end of the dock is <strong>Christopher Columbus</strong>,\u201d Jason said. '
    '\u201cHe\u2019s an Italian navigator from Genoa, but the Spanish monarchs '
    '<strong>Ferdinand and Isabella</strong> are funding his voyage. '
    'Columbus has a bold idea: instead of sailing east around Africa to reach Asia, '
    'he\u2019ll sail <strong>west</strong> across the Atlantic. He believes the Earth is round \u2014 '
    'which educated people already knew \u2014 but he thinks the distance is much shorter than it actually is. '
    'He\u2019s wrong about the math by thousands of miles.\u201d</p>'

    '<p>\u201cColumbus sets sail with three ships: the <strong>Ni\u00f1a, the Pinta, and the Santa Mar\u00eda</strong>. '
    'The crew is terrified. After five weeks with no sight of land, they threaten mutiny. '
    'Then, on <strong>October 12, 1492</strong>, a lookout spots land. '
    'Columbus falls to his knees on the beach and claims the island for Spain.\u201d</p>'

    '<p>\u201cHe thinks he\u2019s reached the <strong>Indies</strong> \u2014 islands near Asia. '
    'He\u2019s actually in the <strong>Caribbean</strong>, probably the Bahamas. '
    'He calls the native Ta\u00edno people \u2018Indians\u2019 \u2014 a mistake that stuck for centuries. '
    'Columbus made four voyages to the Americas but went to his grave in 1506 '
    'still believing he had reached Asia. He never realized he had stumbled upon '
    'two entire continents that Europeans didn\u2019t know existed.\u201d</p>'

    '<h3>The Impact on Indigenous Peoples</h3>'

    '<p>\u201cThis is where the story gets painful,\u201d Jason said quietly. '
    '\u201cThe people Columbus \u2018discovered\u2019 had been living in the Americas for at least '
    '<strong>15,000 years</strong>. The Ta\u00edno had complex societies, agriculture, trade networks, '
    'and their own history. Columbus and the Spanish conquistadors who followed brought '
    '<strong>violence, enslavement, and forced labor</strong>. Columbus himself enslaved hundreds of Ta\u00edno people '
    'and sent them back to Spain.\u201d</p>'

    '<p>\u201cBut the worst killer was invisible: <strong>disease</strong>. '
    'Europeans carried smallpox, measles, influenza, and typhus \u2014 '
    'diseases that indigenous peoples had no immunity to. '
    'Within 50 years of Columbus\u2019s arrival, the Ta\u00edno population dropped from an estimated '
    '250,000 to near zero. Across the Americas, European diseases killed an estimated '
    '<strong>90 percent</strong> of the indigenous population \u2014 tens of millions of people. '
    'It was the greatest demographic catastrophe in human history.\u201d</p>'

    '<h3>Magellan \u2014 Around the Whole World</h3>'

    '<p>\u201cTwenty-seven years after Columbus, a Portuguese navigator named '
    '<strong>Ferdinand Magellan</strong> attempted something even more audacious,\u201d Jason said. '
    '\u201cHe wanted to sail all the way around the world. '
    'In <strong>September 1519</strong>, he left Spain with <strong>five ships and about 270 men</strong>.\u201d</p>'

    '<p>\u201cThe voyage was brutal. They sailed down the coast of South America '
    'for months looking for a passage to the Pacific. '
    'One ship was wrecked. Another turned around and went home. '
    'Finally, Magellan found a narrow, treacherous strait at the southern tip of South America \u2014 '
    'now called the <strong>Strait of Magellan</strong>. It took 38 days to navigate its twisting channels.\u201d</p>'

    '<p>\u201cWhen they emerged into the vast ocean on the other side, '
    'the water was so calm compared to the Atlantic that Magellan named it the <strong>Pacific</strong> \u2014 '
    'meaning \u2018peaceful.\u2019 But the Pacific turned out to be unimaginably huge. '
    'For 99 days they sailed without seeing land. '
    'The crew ate sawdust, leather strips from the rigging, and rats. '
    'Nineteen men died of scurvy.\u201d</p>'

    '<p>\u201cMagellan himself never completed the journey. '
    'In April 1521, he was <strong>killed in a battle</strong> with warriors on the island of Mactan '
    'in the Philippines. His crew pressed on. Of the original five ships, '
    'only one \u2014 the <strong>Victoria</strong> \u2014 made it back to Spain on <strong>September 6, 1522</strong>, '
    'with just <strong>18 surviving men</strong> out of the original 270. '
    'They had sailed around the entire world \u2014 a voyage of three years and over 42,000 miles. '
    'It proved once and for all that the Earth is a sphere and that all the oceans are connected.\u201d</p>'

    '<h3>The Columbian Exchange</h3>'

    '<p>\u201cThe Age of Exploration didn\u2019t just connect continents \u2014 '
    'it mixed them together,\u201d Jason said. \u201cHistorians call this the '
    '<strong>Columbian Exchange</strong> \u2014 the massive transfer of plants, animals, diseases, '
    'and ideas between the Old World (Europe, Africa, Asia) and the New World (the Americas).\u201d</p>'

    '<p>\u201cFrom the Americas to Europe came <strong>potatoes, tomatoes, corn (maize), chocolate, '
    'tobacco, peppers, squash, and vanilla</strong>. These foods transformed European diets and agriculture. '
    'The potato alone helped feed Europe\u2019s growing population for centuries. '
    'From Europe to the Americas came <strong>horses, cattle, pigs, wheat, sugarcane, '
    'and coffee</strong> \u2014 along with those devastating diseases.\u201d</p>'

    '<p>\u201cThe Columbian Exchange reshaped every ecosystem it touched. '
    'Imagine Italy without tomatoes, Ireland without potatoes, '
    'or the American West without horses \u2014 none of those existed before 1492. '
    'For better and for worse, this exchange created the interconnected world we live in today.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 140" width="700" height="140" xmlns="http://www.w3.org/2000/svg" aria-label="The Columbian Exchange">'
    '<rect width="700" height="140" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Columbian Exchange \u2014 What Crossed the Atlantic</text>'

    '<rect x="30" y="30" width="280" height="60" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="170" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Americas \u2192 Europe</text>'
    '<text x="170" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Potatoes, tomatoes, corn, chocolate</text>'
    '<text x="170" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Tobacco, peppers, squash, vanilla, rubber</text>'
    '<text x="170" y="86" text-anchor="middle" fill="#b8a88a" font-size="7">Gold &amp; silver (fueled European economies)</text>'

    '<text x="350" y="60" text-anchor="middle" fill="#e8a838" font-size="16">\u2194</text>'

    '<rect x="390" y="30" width="280" height="60" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="530" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Europe \u2192 Americas</text>'
    '<text x="530" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Horses, cattle, pigs, wheat, sugarcane</text>'
    '<text x="530" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Coffee, rice, bananas, citrus fruits</text>'
    '<text x="530" y="86" text-anchor="middle" fill="#b8a88a" font-size="7">Smallpox, measles, influenza (killed ~90%)</text>'

    '<text x="350" y="112" text-anchor="middle" fill="#b8a88a" font-size="9">Columbus 1492: 3 ships, thought he reached Asia \u2014 actually the Caribbean</text>'
    '<text x="350" y="127" text-anchor="middle" fill="#b8a88a" font-size="9">Magellan 1519\u20131522: 5 ships, 270 men departed \u2014 1 ship, 18 men returned</text>'
    '</svg>'
    '</div>'

    '<p>The book carried them home. Evelyn was quiet for a long time.</p>'

    '<p>\u201cColumbus thought he was a hero,\u201d she said. \u201cBut he hurt a lot of people.\u201d</p>'

    '<p>\u201cHistory is full of people who did brave things and terrible things at the same time,\u201d '
    'Jason said. \u201cThe courage to cross an ocean and the cruelty of what happened when they arrived \u2014 '
    'both are true. We have to hold both.\u201d</p>'

    '<p>\u201cGoodnight, brave and terrible explorers.\u201d</p>'

    '<p>\u201cGoodnight, round world.\u201d</p>'
)

disc_66 = [
    "Columbus is celebrated with a national holiday, but he also enslaved indigenous people and brought devastating diseases. Should we celebrate explorers who did both brave and terrible things? How do we tell the full truth about complicated historical figures?",
    "Of the 270 men who left with Magellan, only 18 returned. Would you have volunteered for a voyage like that, knowing the risks? What drives people to take enormous risks for the sake of discovery?",
    "The Columbian Exchange changed every continent \u2014 imagine Italy without tomatoes or the American West without horses. Can you think of other examples where connecting two cultures changed both of them in unexpected ways?"
]

quiz_66 = [
    {
        "q": "What were the three main motivations for the Age of Exploration?",
        "options": [
            "Democracy, education, and science",
            "Spices, gold, and spreading Christianity",
            "Revenge, conquest, and fishing",
            "Friendship, trade, and tourism"
        ],
        "correct": 1
    },
    {
        "q": "What happened to Magellan during his circumnavigation voyage?",
        "options": [
            "He completed the voyage and returned to Spain a hero",
            "His ships were destroyed in a storm",
            "He was killed in the Philippines, but his crew completed the voyage",
            "He turned back after reaching the Pacific Ocean"
        ],
        "correct": 2
    },
    {
        "q": "What was the Columbian Exchange?",
        "options": [
            "A trade agreement between Columbus and the Spanish crown",
            "The transfer of plants, animals, diseases, and ideas between the Old and New Worlds",
            "A type of currency used by explorers",
            "The exchange of prisoners between Spain and Portugal"
        ],
        "correct": 1
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 66:
        lessons[i] = {
            "id": 66,
            "type": "history",
            "topic": "Exploration",
            "title": "Columbus and Magellan",
            "readingTime": "10 min",
            "story": story_66,
            "discussion": disc_66,
            "quiz": quiz_66
        }
        print("Updated lesson 66: Columbus and Magellan")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
