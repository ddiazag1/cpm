import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_85 = (
    '<h2>A World in Two Halves</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Berlinermauer.jpg/800px-Berlinermauer.jpg" '
    'alt="The Berlin Wall with graffiti on the western side" loading="lazy">'
    '<p class="image-caption">The Berlin Wall \u2014 for 28 years, a concrete barrier divided a city and symbolized a world split in two</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass dial turned, and the brothers appeared '
    'on a wide avenue in a gray city. On one side of the street, shops glowed with neon signs '
    'and people walked freely. On the other side, a massive concrete wall topped with barbed wire '
    'blocked everything from view. Armed soldiers patrolled a strip of empty ground '
    'between the two halves.</p>'

    '<p>\u201cThis is <strong>Berlin</strong>,\u201d William said. \u201cOne city, split in two. '
    'Just like the entire world.\u201d</p>'

    '<h3>Two Superpowers</h3>'

    '<p>\u201cWhen World War II ended in 1945, the two strongest nations left standing '
    'were the <strong>United States</strong> and the <strong>Soviet Union</strong>,\u201d William said. '
    '\u201cThey had fought together to defeat Hitler, but they agreed on almost nothing else. '
    'The United States believed in <strong>democracy</strong>, individual freedom, and <strong>capitalism</strong> \u2014 '
    'an economy where people own businesses and compete in a free market. '
    'The Soviet Union believed in <strong>communism</strong> \u2014 a system where the government '
    'controlled the economy, owned the factories, and made decisions for everyone.\u201d</p>'

    '<p>\u201cEach side was convinced the other\u2019s system was dangerous and had to be stopped. '
    'This standoff lasted from about <strong>1947 to 1991</strong> and was called the <strong>Cold War</strong> \u2014 '
    '\u2018cold\u2019 because the two superpowers never fought each other directly, '
    'but the threat of war hung over every single day.\u201d</p>'

    '<h3>The Iron Curtain</h3>'

    '<p>\u201cAfter the war, the Soviet Union took control of Eastern Europe \u2014 '
    'Poland, Czechoslovakia, Hungary, East Germany, Romania, Bulgaria, and others,\u201d William said. '
    '\u201cThese countries were forced to adopt communist governments loyal to Moscow. '
    'British leader <strong>Winston Churchill</strong> said it was as if an '
    '<strong>\u201ciron curtain\u201d</strong> had fallen across Europe, '
    'dividing the free West from the communist East.\u201d</p>'

    '<p>\u201cNowhere was this division more visible than in <strong>Berlin</strong>. '
    'The city sat deep inside communist East Germany, but it was split into four zones '
    'controlled by the Allies. In 1948, the Soviets blocked all roads and railways into West Berlin, '
    'trying to starve the city into surrendering. The Americans and British responded with the '
    '<strong>Berlin Airlift</strong> \u2014 for 11 months, planes landed every few minutes, '
    'delivering food, fuel, and medicine to 2 million people. The Soviets backed down.\u201d</p>'

    '<p>\u201cBut in <strong>1961</strong>, the East German government built a wall right through the middle '
    'of Berlin \u2014 the <strong>Berlin Wall</strong>. Families were separated overnight. '
    'Guards had orders to shoot anyone trying to escape to the West. '
    'Over 28 years, at least 140 people were killed trying to cross.\u201d</p>'

    '<h3>The Nuclear Shadow</h3>'

    '<p>\u201cBoth superpowers built <strong>nuclear weapons</strong> \u2014 bombs powerful enough '
    'to destroy entire cities,\u201d William said. \u201cThe United States tested the first atomic bomb in 1945. '
    'The Soviet Union built its own in 1949. Then both sides raced to build even bigger ones \u2014 '
    '<strong>hydrogen bombs</strong> a thousand times more powerful than the bomb dropped on Hiroshima.\u201d</p>'

    '<p>\u201cBy the 1960s, both sides had enough nuclear weapons to destroy the entire world '
    'several times over. This terrifying balance was called '
    '<strong>MAD \u2014 Mutually Assured Destruction</strong>. '
    'The idea was that neither side would ever start a nuclear war '
    'because both sides would be completely destroyed. '
    'It was a strange kind of peace \u2014 built on fear.\u201d</p>'

    '<p>\u201cSchoolchildren in America practiced \u2018duck and cover\u2019 drills, '
    'hiding under their desks in case of a nuclear attack. Families built bomb shelters '
    'in their backyards. The whole world lived under a shadow.\u201d</p>'

    '<h3>The Cuban Missile Crisis</h3>'

    '<p>\u201cThe closest the world ever came to nuclear war was in <strong>October 1962</strong>,\u201d '
    'William said. \u201cAmerican spy planes discovered that the Soviet Union was secretly building '
    '<strong>nuclear missile bases</strong> on the island of <strong>Cuba</strong> \u2014 '
    'just 90 miles from Florida.\u201d</p>'

    '<p>\u201cPresident <strong>John F. Kennedy</strong> demanded the missiles be removed '
    'and ordered the U.S. Navy to blockade Cuba. For <strong>13 days</strong>, '
    'the world held its breath. Soviet ships carrying more missiles sailed toward the blockade. '
    'If they didn\u2019t stop, war could begin. Nuclear war.\u201d</p>'

    '<p>\u201cFinally, Soviet leader <strong>Nikita Khrushchev</strong> agreed to remove the missiles '
    'in exchange for a promise that the U.S. would not invade Cuba. '
    'The ships turned around. The world exhaled. '
    'But for 13 days, human civilization had been one wrong decision away from ending.\u201d</p>'

    '<p>Robert shivered. \u201cThirteen days?\u201d</p>'

    '<p>\u201cThirteen days,\u201d William repeated. \u201cThat\u2019s how close it was.\u201d</p>'

    '<h3>Proxy Wars: Korea and Vietnam</h3>'

    '<p>\u201cAlthough the U.S. and the Soviet Union never fought each other directly, '
    'they fought through other countries,\u201d William said. \u201cThese were called <strong>proxy wars</strong>.\u201d</p>'

    '<p>\u201cIn <strong>Korea</strong> (1950\u20131953), communist North Korea, backed by China and the Soviet Union, '
    'invaded South Korea. The United States led a United Nations force to defend the South. '
    'After three years of brutal fighting that killed over 2.5 million people, '
    'the border ended up almost exactly where it started. Korea remains divided to this day.\u201d</p>'

    '<p>\u201cIn <strong>Vietnam</strong> (1955\u20131975), the United States sent over 2.7 million soldiers '
    'to try to prevent communist North Vietnam from taking over South Vietnam. '
    'It became America\u2019s longest and most divisive war. Over <strong>58,000 Americans</strong> '
    'and an estimated <strong>2 million Vietnamese</strong> were killed. '
    'Protests erupted across America. In 1975, North Vietnam won the war. '
    'It was the first war the United States clearly lost, and it left deep scars.\u201d</p>'

    '<h3>The Space Race (A Preview)</h3>'

    '<p>\u201cNot everything about the Cold War was about weapons and fear,\u201d William said. '
    '\u201cThe two superpowers also competed to explore <strong>space</strong>. '
    'In 1957, the Soviet Union launched <strong>Sputnik</strong>, the first satellite, '
    'shocking the world. In 1961, Soviet cosmonaut <strong>Yuri Gagarin</strong> became '
    'the first human in space. America was behind \u2014 and determined to catch up. '
    'President Kennedy promised to land a man on the moon before the decade was over. '
    'But that\u2019s a story for another night.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="The Cold War">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Cold War (1947\u20131991)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Iron Curtain</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Europe divided: West vs. East</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Berlin Wall (1961\u20131989)</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Nuclear Arms Race</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">MAD: Mutually Assured Destruction</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Cuban Missile Crisis (1962)</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Proxy Wars</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Korea (1950\u201353), Vietnam (1955\u201375)</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Millions killed, no clear winners</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Space Race</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Sputnik (1957), Gagarin (1961)</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Competition that reached the stars</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Two superpowers, two systems, one terrifying question: Could humanity survive itself?</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">The Cold War lasted 44 years \u2014 and the world was never the same</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. Robert went to the window and looked up at the stars.</p>'

    '<p>\u201cThey pointed missiles at each other,\u201d he said. '
    '\u201cBut they also raced each other to the stars.\u201d</p>'

    '<p>\u201cThat\u2019s the strange thing about people,\u201d William said. '
    '\u201cWe can build weapons that destroy the world and rockets that leave it \u2014 '
    'sometimes at the same time. The question is always which impulse wins. '
    'Goodnight, divided world.\u201d</p>'

    '<p>\u201cGoodnight, Cold War.\u201d</p>'
)

disc_85 = [
    "During the Cold War, both sides had enough nuclear weapons to destroy the world many times over. Do you think the fear of total destruction actually kept the peace, or was it just luck that no one pushed the button?",
    "The Berlin Wall separated families and trapped people for 28 years. Why do you think some governments try to keep their people from leaving?",
    "The U.S. and Soviet Union competed in the space race and in building weapons. Why do you think competition can sometimes lead to amazing achievements and terrible dangers at the same time?"
]

quiz_85 = [
    {
        "q": "What did the term \u2018Iron Curtain\u2019 describe?",
        "options": [
            "A new type of military weapon",
            "The division between the free West and communist East in Europe",
            "A wall built around Moscow",
            "The border between North and South Korea"
        ],
        "correct": 1
    },
    {
        "q": "What was MAD (Mutually Assured Destruction)?",
        "options": [
            "A secret weapon program",
            "A peace treaty between the U.S. and Soviet Union",
            "The idea that neither side would start a nuclear war because both would be destroyed",
            "A military alliance in Europe"
        ],
        "correct": 2
    },
    {
        "q": "How close did the Cuban Missile Crisis bring the world to nuclear war?",
        "options": [
            "The crisis lasted 3 days",
            "The crisis lasted 13 days",
            "The crisis lasted 30 days",
            "The crisis lasted 6 months"
        ],
        "correct": 1
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 85:
        lessons[i] = {
            "id": 85,
            "type": "history",
            "topic": "ColdWar",
            "title": "A World in Two Halves",
            "readingTime": "10 min",
            "story": story_85,
            "discussion": disc_85,
            "quiz": quiz_85
        }
        print("Updated lesson 85: A World in Two Halves")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
