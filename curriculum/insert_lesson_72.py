import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_72 = (
    '<h2>A New World</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jamestown_Church_Tower_Colonial_National_Historical_Park_%28Part_of_Colonial_Parkway%29.jpg/800px-Jamestown_Church_Tower_Colonial_National_Historical_Park_%28Part_of_Colonial_Parkway%29.jpg" '
    'alt="The ruins of the original Jamestown church tower in Virginia" loading="lazy">'
    '<p class="image-caption">The Jamestown church tower \u2014 the only standing structure from the first permanent English settlement in America (1607)</p>'
    '</div>'

    '<p>Evelyn was looking at a map of the world. \u201cJason, when did people from Europe '
    'start living in America?\u201d</p>'

    '<p>Jason opened The Living World and turned the brass clasp. '
    '\u201cThat story starts with a very dangerous ocean crossing.\u201d</p>'

    '<p>The green light carried them to the wooden deck of a small, creaking ship. '
    'Gray waves stretched to every horizon, and the sails snapped in a bitter wind.</p>'

    '<h3>Why Did They Come?</h3>'

    '<p>\u201cAfter Columbus reached the Americas in 1492, European nations raced to claim territory,\u201d '
    'Jason said. \u201cSpain conquered Central and South America, extracting gold and silver '
    'that made it the richest country in Europe. Portugal claimed Brazil. '
    'France claimed vast stretches of Canada. And England, arriving late to the game, '
    'looked to the eastern coast of North America.\u201d</p>'

    '<p>\u201cPeople came for many different reasons. Some came for <strong>wealth</strong> \u2014 '
    'hoping to find gold or get rich from trade. Some came for <strong>land</strong> \u2014 '
    'in Europe, most land belonged to nobles, and ordinary people could never own any. '
    'Some came for <strong>religious freedom</strong> \u2014 to worship in ways forbidden in their home countries. '
    'And some didn\u2019t come by choice at all \u2014 enslaved Africans were forced across the Atlantic '
    'in what is one of the greatest tragedies in human history.\u201d</p>'

    '<h3>Jamestown \u2014 The First Survivors</h3>'

    '<p>\u201cIn 1607, about 100 English settlers established <strong>Jamestown</strong>, Virginia \u2014 '
    'the first permanent English settlement in North America,\u201d Jason said. '
    '\u201cIt was a disaster at first. The settlers chose a swampy location, '
    'many were gentlemen who had never done manual labor, and they spent their time searching for gold '
    'instead of growing food.\u201d</p>'

    '<p>\u201cDuring the first winter, disease, starvation, and conflicts with the local <strong>Powhatan</strong> people '
    'killed most of the colonists. The \u2018Starving Time\u2019 of 1609\u20131610 was so bad '
    'that the population dropped from 500 to 60. They were about to abandon the colony '
    'when supply ships arrived just in time.\u201d</p>'

    '<p>\u201cJamestown was saved by <strong>tobacco</strong>. John Rolfe introduced a sweeter variety '
    'that became wildly popular in England, and suddenly the colony had something profitable to sell. '
    'Tobacco became Virginia\u2019s gold.\u201d</p>'

    '<h3>The Pilgrims and Plymouth</h3>'

    '<p>\u201cIn 1620, a group called the <strong>Pilgrims</strong> sailed on the <strong>Mayflower</strong> '
    'from England to Massachusetts,\u201d Jason continued. '
    '\u201cThey were <strong>Separatists</strong> \u2014 people who wanted to separate from the Church of England '
    'and worship freely. Before landing, 41 men signed the <strong>Mayflower Compact</strong>, '
    'an agreement to govern themselves by majority rule. '
    'It was one of the first examples of <strong>self-government</strong> in America.\u201d</p>'

    '<p>\u201cTheir first winter was brutal \u2014 half the Pilgrims died. '
    'But the <strong>Wampanoag</strong> people, led by <strong>Massasoit</strong>, helped them. '
    'A Patuxet man named <strong>Squanto</strong>, who had been to England and spoke English, '
    'taught them how to plant corn, catch fish, and survive in the new land. '
    'The harvest celebration they shared in the fall of 1621 '
    'is remembered as the \u2018First Thanksgiving.\u2019\u201d</p>'

    '<h3>The Thirteen Colonies</h3>'

    '<p>\u201cOver the next 150 years, the English established <strong>13 colonies</strong> '
    'along the Atlantic coast,\u201d Jason said. \u201cEach was different. '
    '<strong>Massachusetts</strong> was founded by Puritans seeking religious purity. '
    '<strong>Pennsylvania</strong> was founded by William Penn as a haven for <strong>Quakers</strong>. '
    '<strong>Georgia</strong> was founded as a fresh start for debtors. '
    '<strong>Maryland</strong> was founded as a refuge for Catholics.\u201d</p>'

    '<p>\u201cBy the 1750s, about <strong>1.5 million</strong> colonists lived in these 13 colonies. '
    'They had their own legislatures, their own newspapers, and an increasingly independent spirit. '
    'They thought of themselves less and less as English subjects '
    'and more and more as Americans.\u201d</p>'

    '<h3>The Dark Side: Slavery and Indigenous Displacement</h3>'

    '<p>\u201cWe have to talk about what colonization really meant for many people,\u201d '
    'Jason said seriously. \u201cStarting in 1619, enslaved Africans were brought to Virginia. '
    'Over the next 200 years, the <strong>transatlantic slave trade</strong> forcibly brought '
    'an estimated <strong>12.5 million Africans</strong> to the Americas. '
    'About 2 million died during the horrific voyage called the <strong>Middle Passage</strong>. '
    'Those who survived were forced into a lifetime of unpaid labor, separated from families, '
    'and denied basic human rights.\u201d</p>'

    '<p>\u201cAnd for <strong>Native Americans</strong>, colonization was devastating. '
    'European diseases killed an estimated 90 percent of the indigenous population \u2014 '
    'entire nations disappeared. Those who survived were pushed off their ancestral lands '
    'through broken treaties, wars, and forced relocations.\u201d</p>'

    '<p>\u201cUnderstanding this history honestly is essential,\u201d Jason said. '
    '\u201cThe same story that includes the Mayflower Compact and Thanksgiving '
    'also includes slavery and displacement. Real history includes both.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Colonial America">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Colonial America \u2014 Key Milestones</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Jamestown (1607)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">First permanent English colony</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Saved by tobacco</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Plymouth (1620)</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Pilgrims, Mayflower Compact</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Self-government begins</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Slavery (1619+)</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">12.5 million Africans enslaved</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">A tragedy lasting 250 years</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">13 Colonies (1750s)</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">1.5 million colonists</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Growing independent spirit</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">The story of America includes both its highest ideals and its greatest injustices</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">Understanding both honestly is what makes us better</text>'
    '</svg>'
    '</div>'

    '<p>The book brought them home. Evelyn was quiet for a long time.</p>'

    '<p>\u201cIt\u2019s not a simple story, is it?\u201d she said.</p>'

    '<p>\u201cNo,\u201d Jason said. \u201cBut the complicated stories are the ones worth telling honestly. '
    'Goodnight, new world.\u201d</p>'

    '<p>\u201cGoodnight, complicated history.\u201d</p>'
)

disc_72 = [
    "The colonists came to America seeking freedom and opportunity, but colonization brought slavery and devastation to Native Americans and Africans. How can the same event be both hopeful and tragic at the same time?",
    "The Mayflower Compact was one of the first agreements for self-government in America. Why is it important for people to agree on rules together rather than having rules imposed on them?",
    "Squanto helped the Pilgrims survive, even though European colonizers had previously kidnapped him. What does his choice tell us about the power of compassion, even toward people who have wronged you?"
]

quiz_72 = [
    {
        "q": "What crop saved the Jamestown colony from failure?",
        "options": ["Cotton", "Corn", "Tobacco", "Rice"],
        "correct": 2
    },
    {
        "q": "What was the Mayflower Compact?",
        "options": [
            "A peace treaty with Native Americans",
            "An agreement for self-government",
            "A declaration of independence from England",
            "A map of the Atlantic Ocean"
        ],
        "correct": 1
    },
    {
        "q": "Approximately how many Africans were forcibly brought to the Americas through the slave trade?",
        "options": ["1 million", "5 million", "12.5 million", "25 million"],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 72:
        lessons[i] = {
            "id": 72,
            "type": "history",
            "topic": "Colonial",
            "title": "A New World",
            "readingTime": "10 min",
            "story": story_72,
            "discussion": disc_72,
            "quiz": quiz_72
        }
        print("Updated lesson 72: A New World")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
