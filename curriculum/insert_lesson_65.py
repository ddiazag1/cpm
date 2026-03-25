import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_65 = (
    '<h2>The Man Who Could Do Everything</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Da_Vinci_Vitruve_Luc_Viatour.jpg/800px-Da_Vinci_Vitruve_Luc_Viatour.jpg" '
    'alt="Leonardo da Vinci\u2019s Vitruvian Man drawing" loading="lazy">'
    '<p class="image-caption">The Vitruvian Man \u2014 Leonardo da Vinci\u2019s study of the ideal human proportions, drawn around 1490</p>'
    '</div>'

    '<p>Robert was sketching a bird in his notebook when William walked in. '
    '\u201cNot bad,\u201d William said, looking over his shoulder. '
    '\u201cBut I know a man who drew birds so carefully that he figured out how to build a flying machine \u2014 '
    '400 years before the Wright Brothers.\u201d</p>'

    '<p>Robert looked up. \u201cWho?\u201d</p>'

    '<p>William picked up the telescope and turned the hourglass dial. '
    '\u201cThe most curious person who ever lived.\u201d</p>'

    '<p>The blue light set them down in a cluttered workshop. Wooden models hung from the ceiling \u2014 '
    'gears, wings, pulleys. Tables were covered with sketches of muscles, rivers, flowers, and war machines. '
    'A man with a long beard and kind eyes was writing something in a notebook, '
    'his hand moving from right to left across the page.</p>'

    '<h3>The Boy from Vinci</h3>'

    '<p>\u201c<strong>Leonardo da Vinci</strong> was born in 1452 in a small town called Vinci, '
    'near Florence, Italy,\u201d William said. \u201cHe was the illegitimate son of a notary and a peasant woman. '
    'Because he was born out of wedlock, he couldn\u2019t attend university or enter most professions. '
    'But his father noticed the boy\u2019s extraordinary talent for drawing and sent him '
    'to study with <strong>Andrea del Verrocchio</strong>, one of Florence\u2019s finest artists.\u201d</p>'

    '<p>\u201cIn Verrocchio\u2019s workshop, Leonardo learned painting, sculpture, metalwork, '
    'and engineering. The story goes that when the young Leonardo painted an angel '
    'in one of Verrocchio\u2019s paintings, the master was so astonished by his pupil\u2019s skill '
    'that he put down his brush and never painted again. '
    'Whether that story is true or not, Leonardo quickly surpassed every artist around him.\u201d</p>'

    '<h3>The Mona Lisa \u2014 The Most Famous Painting in the World</h3>'

    '<p>\u201cLeonardo\u2019s most famous painting is the <strong>Mona Lisa</strong>,\u201d William said. '
    '\u201cIt\u2019s a portrait of a woman named Lisa Gherardini, the wife of a Florentine merchant. '
    'Leonardo worked on it for years, carrying it with him wherever he traveled, '
    'adding thin layer after thin layer of paint in a technique called <strong>sfumato</strong> \u2014 '
    'meaning \u2018smoky.\u2019 The edges blend so softly that her smile seems to change '
    'depending on where you look. Is she smiling? Is she sad? Is she amused? '
    'People have debated it for 500 years.\u201d</p>'

    '<p>\u201cThe Mona Lisa is now behind bulletproof glass at the Louvre museum in Paris. '
    'About 10 million people visit her every year. She\u2019s been stolen once, '
    'had acid thrown at her, and been hit with a rock. '
    'She is the most famous painting on Earth \u2014 and she\u2019s only 30 by 21 inches. '
    'Smaller than most posters.\u201d</p>'

    '<h3>The Last Supper</h3>'

    '<p>\u201cLeonardo\u2019s other masterpiece is <em>The Last Supper</em>,\u201d William continued. '
    '\u201cPainted on a wall in a monastery in Milan, it shows Jesus and his twelve apostles '
    'at the moment Jesus announces that one of them will betray him. '
    'Each face shows a different emotion \u2014 shock, anger, denial, grief. '
    'Leonardo studied real people\u2019s expressions for months before painting each face.\u201d</p>'

    '<p>\u201cBut Leonardo experimented with a new painting technique instead of using traditional fresco '
    '(painting on wet plaster). His method began to flake almost immediately. '
    'The painting has been deteriorating for over 500 years and has been restored many times. '
    'Even damaged, it remains one of the most powerful paintings ever created.\u201d</p>'

    '<h3>The Notebooks \u2014 A Mind Without Limits</h3>'

    '<p>\u201cWhat truly sets Leonardo apart isn\u2019t his paintings \u2014 it\u2019s his <strong>notebooks</strong>,\u201d '
    'William said. \u201cHe filled more than 7,000 pages with drawings, diagrams, observations, '
    'and inventions. These collections, called <strong>codices</strong>, cover '
    'anatomy, engineering, optics, water flow, botany, geology, astronomy, architecture, and music. '
    'No human being has ever studied such a wide range of subjects so deeply.\u201d</p>'

    '<p>\u201cAnd here\u2019s the strangest part: Leonardo wrote everything in <strong>mirror writing</strong> \u2014 '
    'backwards, from right to left, so you need a mirror to read it. '
    'Some historians think he did it to keep his ideas secret. '
    'Others think it was simply more natural for him as a left-handed person, '
    'since writing left to right would smear the ink under his hand. '
    'Whatever the reason, it adds to the mystery of a man who was already the most mysterious genius in history.\u201d</p>'

    '<h3>Anatomist \u2014 Mapping the Human Body</h3>'

    '<p>\u201cLeonardo performed over 30 <strong>dissections</strong> of human bodies,\u201d William said. '
    '\u201cIn an era when cutting open the dead was considered sinful, '
    'Leonardo worked secretly in hospital morgues by candlelight. '
    'He drew the human skeleton, muscles, organs, and blood vessels with a precision '
    'that wouldn\u2019t be matched for 300 years. '
    'He was the first person to accurately draw the human spine\u2019s double-S curve, '
    'the first to illustrate the chambers of the heart, '
    'and the first to show a fetus in the womb.\u201d</p>'

    '<p>\u201cHis most famous anatomical drawing is the <strong>Vitruvian Man</strong> \u2014 '
    'a figure with arms and legs outstretched, inscribed in both a circle and a square. '
    'It illustrates the ideal proportions of the human body as described by '
    'the ancient Roman architect Vitruvius. It\u2019s become a symbol of the connection '
    'between art, science, and the beauty of the human form.\u201d</p>'

    '<h3>Inventor Ahead of His Time</h3>'

    '<p>\u201cLeonardo designed machines that wouldn\u2019t be built for centuries,\u201d William said. '
    '\u201cA <strong>flying machine</strong> (ornithopter) with flapping wings modeled on birds and bats. '
    'A <strong>helicopter</strong>-like aerial screw. A <strong>parachute</strong>. '
    'A <strong>diving suit</strong>. An <strong>armored vehicle</strong> that looks remarkably like a tank. '
    'A <strong>self-propelled cart</strong> \u2014 essentially a robot \u2014 powered by springs. '
    'A machine gun. A revolving bridge. Ball bearings.\u201d</p>'

    '<p>\u201cMost of these inventions were never built in his lifetime. '
    'The technology and materials didn\u2019t exist yet. '
    'But when modern engineers have built Leonardo\u2019s designs using his exact specifications, '
    'many of them actually work. His flying machine was the closest anyone came to flight '
    'before the 20th century. His self-propelled cart was successfully reconstructed in 2004 '
    'and drove exactly as he predicted.\u201d</p>'

    '<h3>Artist, Scientist, Inventor \u2014 The Polymath</h3>'

    '<p>\u201cLeonardo is the greatest example of a <strong>polymath</strong> \u2014 '
    'a person who excels in many different fields,\u201d William said. '
    '\u201cHe didn\u2019t see boundaries between art and science. '
    'To him, painting a face required understanding the muscles beneath the skin. '
    'Designing a bridge required understanding how water flows. '
    'Drawing a bird required understanding the physics of flight. '
    'Everything was connected.\u201d</p>'

    '<p>\u201cHe spent his last years in France, invited by King Francis I, '
    'who adored him. Leonardo died on May 2, 1519, at age 67. '
    'A legend says that King Francis held Leonardo in his arms as he died. '
    'Whether or not that\u2019s true, the king called him \u2018the greatest philosopher '
    'and artist the world has ever produced.\u2019\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 140" width="700" height="140" xmlns="http://www.w3.org/2000/svg" aria-label="Leonardo da Vinci\u2019s genius across fields">'
    '<rect width="700" height="140" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Leonardo da Vinci (1452\u20131519) \u2014 The Ultimate Polymath</text>'

    '<rect x="20" y="30" width="125" height="55" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="82" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Artist</text>'
    '<text x="82" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Mona Lisa</text>'
    '<text x="82" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">The Last Supper</text>'
    '<text x="82" y="84" text-anchor="middle" fill="#b8a88a" font-size="7">Sfumato technique</text>'

    '<rect x="158" y="30" width="125" height="55" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="220" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Anatomist</text>'
    '<text x="220" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">30+ dissections</text>'
    '<text x="220" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Vitruvian Man</text>'
    '<text x="220" y="84" text-anchor="middle" fill="#b8a88a" font-size="7">First accurate fetus drawing</text>'

    '<rect x="296" y="30" width="125" height="55" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="358" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Inventor</text>'
    '<text x="358" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Flying machine</text>'
    '<text x="358" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Tank, parachute, diving suit</text>'
    '<text x="358" y="84" text-anchor="middle" fill="#b8a88a" font-size="7">Self-propelled cart (robot)</text>'

    '<rect x="434" y="30" width="125" height="55" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="496" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Scientist</text>'
    '<text x="496" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Optics &amp; light</text>'
    '<text x="496" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Water flow &amp; geology</text>'
    '<text x="496" y="84" text-anchor="middle" fill="#b8a88a" font-size="7">Botany &amp; astronomy</text>'

    '<rect x="572" y="30" width="110" height="55" rx="5" fill="none" stroke="#9b59b6" stroke-width="2"/>'
    '<text x="627" y="48" text-anchor="middle" fill="#9b59b6" font-size="9" font-weight="bold">Notebooks</text>'
    '<text x="627" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">7,000+ pages</text>'
    '<text x="627" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Mirror writing</text>'
    '<text x="627" y="84" text-anchor="middle" fill="#b8a88a" font-size="7">Called \u201ccodices\u201d</text>'

    '<text x="350" y="110" text-anchor="middle" fill="#b8a88a" font-size="9">\u201cEverything is connected\u201d \u2014 he saw no boundary between art and science</text>'
    '<text x="350" y="125" text-anchor="middle" fill="#b8a88a" font-size="9">King Francis I called him \u201cthe greatest philosopher and artist the world has ever produced\u201d</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. Robert looked down at his bird sketch.</p>'

    '<p>\u201cHe drew birds too,\u201d Robert said quietly. \u201cBut then he tried to figure out how they fly.\u201d</p>'

    '<p>\u201cThat\u2019s the difference between seeing and <em>wondering</em>,\u201d William said. '
    '\u201cGoodnight, Leonardo.\u201d</p>'

    '<p>\u201cGoodnight, man who could do everything.\u201d</p>'
)

disc_65 = [
    "Leonardo didn\u2019t see boundaries between art and science \u2014 to him, they were the same thing. Do you agree? Can studying science make you a better artist, or studying art make you a better scientist?",
    "Many of Leonardo\u2019s inventions were never built because the technology didn\u2019t exist yet. Is it still valuable to design something that can\u2019t be built? What does it mean to be \u2018ahead of your time\u2019?",
    "Leonardo wrote everything in mirror writing. If you could create a secret code for your own ideas, would you? What are the advantages and disadvantages of keeping your ideas secret versus sharing them?"
]

quiz_65 = [
    {
        "q": "What painting technique did Leonardo use on the Mona Lisa to create her mysterious smile?",
        "options": [
            "Fresco",
            "Pointillism",
            "Sfumato",
            "Impasto"
        ],
        "correct": 2
    },
    {
        "q": "What is a polymath?",
        "options": [
            "A person who studies mathematics",
            "A person who excels in many different fields",
            "A type of Renaissance painting",
            "A scholar who translates ancient texts"
        ],
        "correct": 1
    },
    {
        "q": "What was unusual about how Leonardo wrote in his notebooks?",
        "options": [
            "He wrote in ancient Greek",
            "He used invisible ink",
            "He wrote in mirror writing, backwards from right to left",
            "He wrote only in code using symbols"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 65:
        lessons[i] = {
            "id": 65,
            "type": "history",
            "topic": "da Vinci",
            "title": "The Man Who Could Do Everything",
            "readingTime": "10 min",
            "story": story_65,
            "discussion": disc_65,
            "quiz": quiz_65
        }
        print("Updated lesson 65: The Man Who Could Do Everything")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
