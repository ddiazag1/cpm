import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_76 = (
    '<h2>The Little General</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Jacques-Louis_David_-_The_Emperor_Napoleon_in_His_Study_at_the_Tuileries_-_Google_Art_Project.jpg/800px-Jacques-Louis_David_-_The_Emperor_Napoleon_in_His_Study_at_the_Tuileries_-_Google_Art_Project.jpg" '
    'alt="Jacques-Louis David painting of Napoleon in his study at the Tuileries" loading="lazy">'
    '<p class="image-caption">Napoleon Bonaparte in his study \u2014 the military genius who rose from a small island to rule most of Europe</p>'
    '</div>'

    '<p>Evelyn was looking at a picture of a man in a big hat. '
    '\u201cJason, who is this? He looks very serious.\u201d</p>'

    '<p>Jason opened The Living World and turned the brass clasp. '
    '\u201cThat\u2019s <strong>Napoleon Bonaparte</strong> \u2014 one of the most extraordinary '
    'and controversial people who ever lived. He went from being a nobody '
    'on a tiny island to ruling almost all of Europe.\u201d</p>'

    '<p>The green light carried them to a rocky coastline overlooking a bright blue sea. '
    'A small boy with dark hair sat on a stone wall, watching ships pass in the distance.</p>'

    '<h3>The Boy from Corsica</h3>'

    '<p>\u201cNapoleon was born on August 15, 1769, on the island of <strong>Corsica</strong>,\u201d '
    'Jason said. \u201cCorsica had been taken over by France just a year before he was born. '
    'His family was minor Italian nobility \u2014 not rich, not poor. '
    'When he was nine, his father sent him to military school in France.\u201d</p>'

    '<p>\u201cThe other boys bullied him for his Corsican accent and his small size. '
    'Napoleon was short \u2014 about five feet six inches, which was actually average for the time, '
    'though his enemies loved to mock him as tiny. He was proud, fiery, and brilliant at mathematics. '
    'He threw himself into studying military strategy and graduated as an artillery officer at just 16.\u201d</p>'

    '<h3>Rising Through the Revolution</h3>'

    '<p>\u201cWhen the French Revolution erupted in 1789, Napoleon was a 20-year-old lieutenant,\u201d '
    'Jason continued. \u201cThe revolution created chaos, but also opportunity. '
    'Many noble-born officers fled France or were executed, '
    'leaving gaps that talented young soldiers could fill. '
    'Napoleon filled them brilliantly.\u201d</p>'

    '<p>\u201cIn 1793, at the siege of <strong>Toulon</strong>, Napoleon placed his cannons so cleverly '
    'that the British fleet was forced to retreat. He was promoted to brigadier general at age 24. '
    'By 1796, he was given command of the French army in <strong>Italy</strong>, '
    'where he won battle after battle against the Austrians '
    'using speed, surprise, and daring tactics that his enemies couldn\u2019t predict.\u201d</p>'

    '<p>\u201cHe didn\u2019t just fight \u2014 he inspired. His soldiers adored him. '
    'He remembered their names, slept in their camps, and shared their hardships. '
    'They called him the \u201cLittle Corporal\u201d and would follow him anywhere.\u201d</p>'

    '<h3>Emperor of France</h3>'

    '<p>\u201cIn 1799, Napoleon overthrew the weak revolutionary government in a <strong>coup d\u2019\u00e9tat</strong> '
    'and made himself <strong>First Consul</strong> of France,\u201d Jason said. '
    '\u201cIn 1804, he crowned himself <strong>Emperor</strong> \u2014 '
    'taking the crown from the Pope\u2019s hands and placing it on his own head, '
    'as if to say: I owe my power to no one but myself.\u201d</p>'

    '<p>Evelyn\u2019s eyes went wide. \u201cHe took the crown from the <em>Pope</em>?\u201d</p>'

    '<p>\u201cHe did,\u201d Jason said. \u201cBut Napoleon wasn\u2019t just a conqueror. '
    'He was also a reformer. He created the <strong>Napoleonic Code</strong> \u2014 '
    'a set of laws that replaced the tangled, unfair legal systems of the old regime. '
    'The Code established that all citizens were equal before the law, '
    'that jobs should go to the most qualified person regardless of birth, '
    'and that property rights were protected. '
    'Versions of the Napoleonic Code are still used in over <strong>40 countries</strong> today.\u201d</p>'

    '<p>\u201cHe also built roads, bridges, and schools. '
    'He established the <strong>Bank of France</strong>, reformed the tax system, '
    'and supported science and education. In many ways, '
    'he made the promises of the revolution into actual, working laws.\u201d</p>'

    '<h3>Master of Europe</h3>'

    '<p>\u201cFrom 1805 to 1812, Napoleon was almost unstoppable,\u201d Jason continued. '
    '\u201cHe crushed the Austrians at <strong>Austerlitz</strong> (1805), '
    'destroyed the Prussian army at <strong>Jena</strong> (1806), '
    'and forced most of Europe into submission or alliance. '
    'At his peak, Napoleon controlled or influenced an empire stretching '
    'from Spain to the borders of Russia.\u201d</p>'

    '<p>\u201cBut he had two enemies he could never defeat. '
    'The first was <strong>Britain</strong>, protected by the English Channel '
    'and the <strong>Royal Navy</strong>, which destroyed the French fleet '
    'at the <strong>Battle of Trafalgar</strong> in 1805. '
    'The second enemy was his own ambition.\u201d</p>'

    '<h3>The Russian Disaster</h3>'

    '<p>\u201cIn June 1812, Napoleon invaded <strong>Russia</strong> '
    'with the <strong>Grande Arm\u00e9e</strong> \u2014 over <strong>600,000 soldiers</strong>, '
    'the largest army Europe had ever seen,\u201d Jason said. '
    '\u201cBut the Russians refused to fight a big battle. '
    'Instead, they retreated, burning crops, villages, and bridges behind them \u2014 '
    'a strategy called <strong>scorched earth</strong>. '
    'Napoleon\u2019s army marched deeper and deeper into Russia, '
    'finding nothing to eat and nowhere to shelter.\u201d</p>'

    '<p>\u201cWhen Napoleon finally reached <strong>Moscow</strong> in September, '
    'the Russians had set the city on fire. There was no food, no surrender, no victory. '
    'Napoleon was forced to retreat as the brutal Russian <strong>winter</strong> arrived. '
    'Temperatures dropped to minus 30 degrees. Soldiers froze, starved, and were picked off '
    'by Russian cavalry. Of the 600,000 who marched in, '
    'fewer than <strong>100,000</strong> made it home.\u201d</p>'

    '<p>Evelyn shivered. \u201cHalf a million soldiers?\u201d</p>'

    '<p>\u201cGone,\u201d Jason said quietly. \u201cIt was one of the greatest military disasters in history.\u201d</p>'

    '<h3>Waterloo and Exile</h3>'

    '<p>\u201cAfter Russia, the nations of Europe united against Napoleon,\u201d Jason said. '
    '\u201cIn 1814, they captured Paris and forced him to abdicate. '
    'He was exiled to the tiny island of <strong>Elba</strong> in the Mediterranean.\u201d</p>'

    '<p>\u201cBut Napoleon escaped. In March 1815, he returned to France, '
    'and soldiers sent to arrest him joined him instead. '
    'He marched into Paris and reclaimed power for what became known as the <strong>Hundred Days</strong>.\u201d</p>'

    '<p>\u201cIt ended at <strong>Waterloo</strong>, Belgium, on June 18, 1815. '
    'A British army under the <strong>Duke of Wellington</strong> '
    'and a Prussian army under <strong>Bl\u00fccher</strong> defeated Napoleon once and for all. '
    'This time, he was exiled to <strong>Saint Helena</strong> \u2014 '
    'a remote island in the South Atlantic, 1,200 miles from the nearest land. '
    'He died there in 1821, at the age of 51.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Napoleon Bonaparte">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Napoleon Bonaparte (1769\u20131821)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Rise (1793\u20131804)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Corsican boy \u2192 Emperor</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Crowned himself at age 35</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Napoleonic Code</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Equality before the law</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Still used in 40+ countries</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Russia (1812)</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">600,000 in, fewer than 100K out</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Scorched earth + winter</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Waterloo (1815)</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Final defeat by Wellington</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Exiled to Saint Helena</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">A military genius whose ambition reshaped Europe \u2014 and destroyed millions of lives</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">His laws outlasted his empire: the Napoleonic Code endures two centuries later</text>'
    '</svg>'
    '</div>'

    '<p>The book brought them home. Evelyn sat still, thinking.</p>'

    '<p>\u201cHe did good things <em>and</em> terrible things,\u201d she said.</p>'

    '<p>\u201cHe did,\u201d Jason said. \u201cGreat power can build schools and write fair laws, '
    'or it can march 600,000 men into a frozen wasteland. '
    'What matters is whether power serves the people or only itself. '
    'Goodnight, little general.\u201d</p>'

    '<p>\u201cGoodnight, Waterloo.\u201d</p>'
)

disc_76 = [
    'Napoleon created fair laws like the Napoleonic Code but also started wars that killed millions. Can someone be both a great leader and a terrible one at the same time? How do we judge people who did both good and bad things?',
    'Napoleon\u2019s soldiers adored him and followed him even into Russia. What makes people willing to follow a leader into danger, and how can that loyalty be both a strength and a weakness?',
    'After being exiled to Elba, Napoleon escaped and returned to power for the Hundred Days. If you were a French citizen in 1815, would you have wanted him back? Why or why not?'
]

quiz_76 = [
    {
        "q": "What was the Napoleonic Code?",
        "options": [
            "A secret military strategy",
            "A set of laws establishing equality before the law",
            "A peace treaty with Britain",
            "A code used to send encrypted messages"
        ],
        "correct": 1
    },
    {
        "q": "What happened to Napoleon\u2019s army during the invasion of Russia in 1812?",
        "options": [
            "They won a great victory in Moscow",
            "They were defeated at the Battle of Trafalgar",
            "Most of the 600,000 soldiers died or were lost to cold and starvation",
            "They conquered Russia and stayed for five years"
        ],
        "correct": 2
    },
    {
        "q": "Where was Napoleon\u2019s final battle?",
        "options": ["Austerlitz", "Moscow", "Trafalgar", "Waterloo"],
        "correct": 3
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 76:
        lessons[i] = {
            "id": 76,
            "type": "history",
            "topic": "Napoleon",
            "title": "The Little General",
            "readingTime": "10 min",
            "story": story_76,
            "discussion": disc_76,
            "quiz": quiz_76
        }
        print("Updated lesson 76: The Little General")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
