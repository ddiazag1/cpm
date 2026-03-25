import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_87 = (
    '<h2>Marching for Justice</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Civil_Rights_March_on_Washington%2C_D.C._%28Dr._Martin_Luther_King%2C_Jr._and_Mathew_Ahmann_in_a_crowd.%29_-_NARA_-_542015_-_Restoration.jpg/800px-Civil_Rights_March_on_Washington%2C_D.C._%28Dr._Martin_Luther_King%2C_Jr._and_Mathew_Ahmann_in_a_crowd.%29_-_NARA_-_542015_-_Restoration.jpg" '
    'alt="Dr. Martin Luther King Jr. at the March on Washington in 1963" loading="lazy">'
    '<p class="image-caption">Dr. Martin Luther King Jr. at the March on Washington \u2014 August 28, 1963</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass dial turned, and the brothers found themselves standing '
    'on a wide sidewalk in a Southern city. The summer heat was suffocating. '
    'Two water fountains stood side by side on a brick wall \u2014 '
    'one labeled \u201cWhite\u201d and the other \u201cColored.\u201d</p>'

    '<p>Robert stared at the signs. \u201cWhat does that mean?\u201d</p>'

    '<p>\u201cIt means we\u2019ve arrived in the <strong>Jim Crow South</strong>,\u201d William said quietly. '
    '\u201cAnd the story of how Americans fought to tear those signs down '
    'is one of the most important stories in all of history.\u201d</p>'

    '<h3>Jim Crow</h3>'

    '<p>\u201cAfter the Civil War ended slavery in 1865, the Southern states passed laws '
    'called <strong>Jim Crow laws</strong> that kept Black and white Americans separated,\u201d William said. '
    '\u201cSeparate schools. Separate restaurants. Separate hospitals. Separate water fountains. '
    'Separate seats on buses \u2014 Black passengers had to sit in the back. '
    'The law said \u201cseparate but equal,\u201d but nothing was ever equal. '
    'Black schools got old textbooks. Black hospitals were underfunded. '
    'And if a Black person tried to vote, they might face impossible literacy tests, '
    'poll taxes, or threats of violence.\u201d</p>'

    '<p>\u201cFor nearly a hundred years after slavery ended, '
    'millions of Americans were treated as second-class citizens in their own country. '
    'But in the 1950s, people began to stand up \u2014 and sit down \u2014 to change that.\u201d</p>'

    '<h3>Rosa Parks and the Bus Boycott</h3>'

    '<p>\u201cOn <strong>December 1, 1955</strong>, a 42-year-old seamstress named <strong>Rosa Parks</strong> '
    'boarded a city bus in <strong>Montgomery, Alabama</strong>,\u201d William said. '
    '\u201cWhen the white section filled up, the bus driver ordered Rosa and three other Black passengers '
    'to give up their seats. The other three moved. Rosa did not.\u201d</p>'

    '<p>\u201cWhy not?\u201d Robert asked.</p>'

    '<p>\u201cShe later said: \u201cI was tired of giving in.\u201d She was arrested. '
    'But her act of quiet courage set off a revolution.\u201d</p>'

    '<p>\u201cThe Black community of Montgomery organized a <strong>bus boycott</strong>. '
    'For <strong>381 days</strong> \u2014 more than a year \u2014 they refused to ride the city buses. '
    'They walked to work, organized carpools, and endured threats and bombings. '
    'A young pastor named <strong>Dr. Martin Luther King Jr.</strong>, just 26 years old, '
    'emerged as the boycott\u2019s leader. The Supreme Court eventually ruled '
    'that bus segregation was unconstitutional. The boycott had worked.\u201d</p>'

    '<h3>Sit-ins and Freedom Riders</h3>'

    '<p>\u201cThe movement spread,\u201d William continued. '
    '\u201cOn February 1, 1960, four Black college students in <strong>Greensboro, North Carolina</strong> '
    'sat down at a \u201cwhites only\u201d lunch counter at Woolworth\u2019s and politely asked to be served. '
    'They were refused, but they didn\u2019t leave. They sat there quietly, day after day. '
    'Within weeks, <strong>sit-ins</strong> had spread to dozens of cities. '
    'Students endured food being dumped on them, being punched and kicked, '
    'and being arrested \u2014 but they never fought back. '
    'Their weapon was <strong>nonviolent resistance</strong>.\u201d</p>'

    '<p>\u201cIn 1961, groups of Black and white activists called <strong>Freedom Riders</strong> '
    'rode buses together into the segregated South to test whether federal desegregation laws '
    'were being obeyed. They weren\u2019t. In Alabama, mobs firebombed their bus '
    'and beat the riders with pipes and bats. The images shocked the nation '
    'and the world.\u201d</p>'

    '<h3>\u201cI Have a Dream\u201d</h3>'

    '<p>\u201cOn <strong>August 28, 1963</strong>, more than <strong>250,000 people</strong> '
    'gathered at the Lincoln Memorial in Washington, D.C., '
    'for the <strong>March on Washington for Jobs and Freedom</strong>,\u201d William said. '
    '\u201cIt was the largest peaceful protest in American history up to that point.\u201d</p>'

    '<p>\u201cDr. King stood before that vast crowd and delivered one of the greatest speeches '
    'ever given. He said: <strong>\u201cI have a dream that my four little children '
    'will one day live in a nation where they will not be judged by the color of their skin '
    'but by the content of their character.\u201d</strong>\u201d</p>'

    '<p>\u201cThe speech was broadcast on television across America. '
    'Millions of people \u2014 Black, white, and every background \u2014 '
    'heard his words and felt their hearts change. '
    'The moral power of the movement was becoming impossible to ignore.\u201d</p>'

    '<h3>The Laws That Changed America</h3>'

    '<p>\u201cPresident <strong>Lyndon B. Johnson</strong> pushed two landmark laws through Congress,\u201d '
    'William said. \u201cThe <strong>Civil Rights Act of 1964</strong> outlawed segregation '
    'in public places and made it illegal to discriminate in hiring based on race, color, '
    'religion, sex, or national origin. The <strong>Voting Rights Act of 1965</strong> '
    'struck down the tricks \u2014 literacy tests, poll taxes, intimidation \u2014 '
    'that had kept Black Americans from voting. '
    'In the first year after the Voting Rights Act passed, '
    '<strong>250,000</strong> new Black voters registered in the South.\u201d</p>'

    '<p>\u201cThese laws didn\u2019t fix everything overnight,\u201d William said. '
    '\u201cThe struggle for equality continued \u2014 and continues today. '
    'But the Civil Rights Movement proved that ordinary people, '
    'armed with nothing but courage and moral conviction, '
    'can change an entire nation\u2019s laws.\u201d</p>'

    '<h3>The Cost of Courage</h3>'

    '<p>\u201cThe movement had a terrible cost,\u201d William said quietly. '
    '\u201cMedgar Evers, an NAACP leader, was shot in his driveway in 1963. '
    'Four young girls \u2014 Addie Mae Collins, Cynthia Wesley, Carole Robertson, and Carol Denise McNair \u2014 '
    'were killed when a bomb exploded at the 16th Street Baptist Church in Birmingham. '
    'And on <strong>April 4, 1968</strong>, Dr. Martin Luther King Jr. was assassinated in Memphis, Tennessee. '
    'He was only 39 years old.\u201d</p>'

    '<p>Robert was quiet. \u201cThey were so brave.\u201d</p>'

    '<p>\u201cThey were,\u201d William said. \u201cAnd their bravery lives on. '
    'Every time someone stands up against injustice peacefully and refuses to be silent, '
    'they are carrying on the work that Rosa Parks, Dr. King, '
    'the Freedom Riders, and hundreds of thousands of ordinary Americans began.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Civil Rights Movement Timeline">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Civil Rights Movement (1955\u20131968)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Bus Boycott (1955)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Rosa Parks refuses to move</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">381 days, MLK emerges as leader</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Sit-ins &amp; Riders (1960\u201361)</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Nonviolent resistance spreads</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Students endure violence peacefully</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">March on Washington (1963)</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">\u201cI Have a Dream\u201d</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">250,000 people, Lincoln Memorial</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Laws Passed (1964\u201365)</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Civil Rights Act &amp; Voting Rights Act</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Segregation outlawed by law</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Nonviolent resistance proved that moral courage can change a nation\u2019s laws</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">Dr. King was 26 during the boycott and 39 when he was assassinated \u2014 he changed the world in 13 years</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. The room was dark and still.</p>'

    '<p>Robert thought about Rosa Parks, sitting quietly on that bus, '
    'refusing to move. \u201cShe didn\u2019t throw a punch. She didn\u2019t shout. '
    'She just said no.\u201d</p>'

    '<p>\u201cSometimes the bravest thing you can do is sit still and refuse to accept '
    'what\u2019s wrong,\u201d William said. \u201cGoodnight, dreamer.\u201d</p>'

    '<p>\u201cGoodnight, marchers.\u201d</p>'
)

disc_87 = [
    "Dr. King and the Civil Rights Movement used nonviolent resistance \u2014 refusing to fight back even when attacked. Why do you think this strategy was so powerful? Could it work in every situation?",
    "Rosa Parks said she was \u2018tired of giving in.\u2019 Can you think of a time when staying quiet felt easier, but speaking up was the right thing to do?",
    "The Civil Rights Act passed in 1964, but the struggle for equality continues today. Why do you think changing laws is only the first step toward changing how people treat each other?"
]

quiz_87 = [
    {
        "q": "How long did the Montgomery Bus Boycott last?",
        "options": ["30 days", "100 days", "381 days", "Two years"],
        "correct": 2
    },
    {
        "q": "What strategy did the Civil Rights Movement use to fight injustice?",
        "options": [
            "Armed rebellion",
            "Nonviolent resistance",
            "Economic sanctions from other countries",
            "Running candidates for president"
        ],
        "correct": 1
    },
    {
        "q": "What did the Voting Rights Act of 1965 do?",
        "options": [
            "Gave women the right to vote",
            "Lowered the voting age to 18",
            "Removed barriers that kept Black Americans from voting",
            "Created the Electoral College"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 87:
        lessons[i] = {
            "id": 87,
            "type": "history",
            "topic": "CivilRights",
            "title": "Marching for Justice",
            "readingTime": "10 min",
            "story": story_87,
            "discussion": disc_87,
            "quiz": quiz_87
        }
        print("Updated lesson 87: Marching for Justice")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
