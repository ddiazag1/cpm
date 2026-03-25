import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_54 = (
    '<h2>Alexander the Great</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Alexander_the_Great_mosaic_%28crop%29.jpg/800px-Alexander_the_Great_mosaic_%28crop%29.jpg" '
    'alt="Mosaic of Alexander the Great from the Battle of Issus" loading="lazy">'
    '<p class="image-caption">Alexander the Great at the Battle of Issus \u2014 a Roman mosaic found at Pompeii, copied from a Greek painting</p>'
    '</div>'

    '<p>Jason opened The Living World and the brass clasp glowed. '
    '\u201cTonight we\u2019re meeting someone who conquered the known world before he turned 30.\u201d</p>'

    '<p>Evelyn\u2019s eyes went wide. \u201cThat\u2019s younger than Dad.\u201d</p>'

    '<p>The green light carried them to a dusty military camp. Thousands of soldiers '
    'in bronze armor sat around campfires, and in the largest tent, '
    'a young man with wild hair was studying a map by lamplight.</p>'

    '<h3>The Boy Who Would Be King</h3>'

    '<p>\u201c<strong>Alexander</strong> was born in 356 BC in <strong>Macedonia</strong>, '
    'a kingdom in northern Greece,\u201d Jason said. '
    '\u201cHis father was <strong>King Philip II</strong>, a brilliant military leader '
    'who had united the Greek city-states under Macedonian control. '
    'His mother, <strong>Olympias</strong>, told Alexander he was descended from Achilles, '
    'the legendary hero of the Trojan War.\u201d</p>'

    '<p>\u201cFrom age 13 to 16, Alexander\u2019s tutor was none other than <strong>Aristotle</strong> \u2014 '
    'one of the greatest philosophers who ever lived. Aristotle taught him science, medicine, '
    'philosophy, and literature. Alexander carried a copy of Homer\u2019s <em>Iliad</em> '
    'with him for the rest of his life, sleeping with it under his pillow.\u201d</p>'

    '<p>\u201cAt age 16, while his father was away at war, Alexander put down a rebellion on his own. '
    'At 18, he led the cavalry charge that won the decisive <strong>Battle of Chaeronea</strong>. '
    'When Philip was assassinated in 336 BC, Alexander became king at just 20 years old.\u201d</p>'

    '<h3>Conquering the World</h3>'

    '<p>\u201cIn 334 BC, Alexander crossed into Asia with about 37,000 soldiers '
    'and set out to conquer the <strong>Persian Empire</strong> \u2014 '
    'the largest empire on Earth,\u201d Jason said. '
    '\u201cNo one thought he could do it. The Persians had a million soldiers '
    'and limitless wealth.\u201d</p>'

    '<p>\u201cBut Alexander was a military genius. At the <strong>Battle of Issus</strong> (333 BC), '
    'he defeated the Persian King <strong>Darius III</strong> despite being outnumbered. '
    'Darius fled, leaving his family behind. Alexander treated them with respect \u2014 '
    'a move that shocked the ancient world.\u201d</p>'

    '<p>\u201cHe marched south and conquered <strong>Egypt</strong>, where he was welcomed as a liberator '
    'and declared a living god. He founded the city of <strong>Alexandria</strong>, '
    'which would become the intellectual capital of the ancient world, '
    'home to the famous <strong>Library of Alexandria</strong>.\u201d</p>'

    '<p>\u201cThen he turned east and crushed the Persian army for good at the <strong>Battle of Gaugamela</strong> (331 BC). '
    'He burned the Persian capital of Persepolis and marched on \u2014 through Afghanistan, '
    'into Central Asia, and all the way to <strong>India</strong>. '
    'By the time he reached the Indus River in 326 BC, his empire stretched 3,000 miles '
    'from Greece to India \u2014 the largest the Western world had ever seen.\u201d</p>'

    '<h3>The End and the Legacy</h3>'

    '<p>\u201cAlexander\u2019s army finally refused to go further. They were exhausted, '
    'thousands of miles from home, and terrified of the war elephants of India. '
    'Alexander reluctantly turned back.\u201d</p>'

    '<p>\u201cIn June 323 BC, in the city of <strong>Babylon</strong>, Alexander fell ill with a fever. '
    'Ten days later, he was dead. He was <strong>32 years old</strong>. '
    'When asked on his deathbed who should inherit his empire, he reportedly said: '
    '\u201cTo the strongest.\u201d His generals immediately began fighting over the pieces, '
    'splitting the empire into three kingdoms.\u201d</p>'

    '<p>\u201cBut Alexander\u2019s real legacy wasn\u2019t military \u2014 it was cultural. '
    'His conquests spread <strong>Greek language, art, philosophy, and science</strong> '
    'across the Middle East and Asia, creating a blended civilization called the '
    '<strong>Hellenistic world</strong>. Greek became the common language of trade and scholarship '
    'from Egypt to Afghanistan. The New Testament of the Bible was written in Greek '
    'because of Alexander\u2019s influence, 300 years after his death.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Alexander the Great timeline">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Alexander\u2019s Life in 32 Years</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Youth (356\u2013336 BC)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Tutored by Aristotle</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">King at age 20</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Conquest (334\u2013326 BC)</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Defeated Persia, conquered Egypt</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Reached India by age 30</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Death (323 BC)</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Died in Babylon at 32</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">\u201cTo the strongest\u201d</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Legacy</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Hellenistic culture</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Greek became world language</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Founded over 20 cities named Alexandria \u2014 cultural melting pots of Greek and Eastern traditions</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">Never lost a single battle in his entire career</text>'
    '</svg>'
    '</div>'

    '<p>The book brought them home. Evelyn was quiet.</p>'

    '<p>\u201cHe conquered the whole world and then died at 32,\u201d she said. \u201cThat\u2019s sad.\u201d</p>'

    '<p>\u201cBut the world he left behind was completely different from the one he was born into,\u201d '
    'Jason said. \u201cGoodnight, Alexander.\u201d</p>'

    '<p>\u201cGoodnight, greatest of them all.\u201d</p>'
)

disc_54 = [
    "Alexander never lost a battle, but his empire fell apart immediately after his death. What good is a conquest if it doesn\u2019t last? Was Alexander truly \u2018great\u2019?",
    "Alexander\u2019s conquests spread Greek culture across the known world. Is spreading your culture through conquest a good thing, a bad thing, or both?",
    "Alexander was tutored by Aristotle, one of history\u2019s greatest thinkers. How much do you think a great teacher can shape the future through a single student?"
]

quiz_54 = [
    {
        "q": "Who was Alexander the Great\u2019s famous tutor?",
        "options": ["Socrates", "Plato", "Aristotle", "Homer"],
        "correct": 2
    },
    {
        "q": "How old was Alexander when he died?",
        "options": ["25", "32", "40", "50"],
        "correct": 1
    },
    {
        "q": "What cultural era did Alexander\u2019s conquests create?",
        "options": ["The Classical period", "The Hellenistic world", "The Roman era", "The Bronze Age"],
        "correct": 1
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 54:
        lessons[i] = {
            "id": 54,
            "type": "history",
            "topic": "Hellenistic",
            "title": "Alexander the Great",
            "readingTime": "10 min",
            "story": story_54,
            "discussion": disc_54,
            "quiz": quiz_54
        }
        print("Updated lesson 54: Alexander the Great")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
