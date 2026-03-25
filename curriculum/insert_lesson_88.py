import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_88 = (
    '<h2>The Wall Comes Down</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/West_and_East_Germans_at_the_Brandenburg_Gate_in_1989.jpg/800px-West_and_East_Germans_at_the_Brandenburg_Gate_in_1989.jpg" '
    'alt="Crowds of West and East Germans gathered at the Brandenburg Gate as the Berlin Wall falls in 1989" loading="lazy">'
    '<p class="image-caption">Germans celebrate at the Brandenburg Gate as the Berlin Wall falls \u2014 November 1989</p>'
    '</div>'

    '<p>Evelyn was looking at a photograph of people dancing on top of a graffiti-covered wall. '
    'Some were swinging hammers. Some were crying. All of them were smiling.</p>'

    '<p>\u201cWhy are they so happy?\u201d she asked.</p>'

    '<p>Jason opened The Living World and turned the brass clasp. '
    '\u201cBecause for 28 years, that wall separated families, friends, '
    'and an entire nation. And on one extraordinary night, it came down.\u201d</p>'

    '<p>The green light set them down on a dark street in a gray city. '
    'Concrete apartment blocks rose like dominoes on both sides. '
    'A guard tower stood in the distance, its spotlight sweeping back and forth. '
    'And running through the middle of everything was a long, ugly wall '
    'topped with barbed wire.</p>'

    '<h3>A City Divided</h3>'

    '<p>\u201cAfter World War II, Germany was split in two,\u201d Jason said. '
    '\u201cThe western part became <strong>West Germany</strong>, a democracy allied with the United States. '
    'The eastern part became <strong>East Germany</strong>, a communist state controlled by the Soviet Union. '
    'The capital, <strong>Berlin</strong>, sat deep inside East Germany \u2014 '
    'but it, too, was divided. West Berlin was a small island of freedom '
    'surrounded by communist territory.\u201d</p>'

    '<p>\u201cThe problem for East Germany\u2019s government was simple: '
    'people kept <em>leaving</em>. Life in the West was freer and more prosperous. '
    'Between 1949 and 1961, about <strong>3.5 million East Germans</strong> \u2014 '
    'nearly 20 percent of the entire population \u2014 fled to the West through Berlin. '
    'Doctors, engineers, teachers, and skilled workers were draining away. '
    'The country was bleeding to death.\u201d</p>'

    '<h3>The Wall Goes Up</h3>'

    '<p>\u201cOn the night of <strong>August 13, 1961</strong>, East German soldiers '
    'rolled out barbed wire and began building a wall through the heart of Berlin,\u201d Jason said. '
    '\u201cBy morning, families who had gone to bed in one city woke up in two. '
    'Neighbors who lived across the street from each other could no longer wave hello. '
    'Parents were separated from children. Couples were split apart.\u201d</p>'

    '<p>\u201cOver the following months, the barbed wire was replaced with a concrete wall '
    '12 feet high and nearly 100 miles long. Guard towers, minefields, attack dogs, '
    'and a barren \u201cdeath strip\u201d made escape almost impossible. '
    'Anyone caught trying to cross was shot. Over the wall\u2019s 28-year existence, '
    'at least <strong>140 people</strong> were killed trying to escape to the West.\u201d</p>'

    '<p>Evelyn shivered. \u201cThey built a wall to keep their own people in?\u201d</p>'

    '<p>\u201cThat\u2019s what makes it so chilling,\u201d Jason said. \u201cMost walls in history were built '
    'to keep enemies <em>out</em>. The Berlin Wall was built to keep citizens <em>in</em>. '
    'It was a prison wall around half a country.\u201d</p>'

    '<h3>Life Behind the Wall</h3>'

    '<p>\u201cEast Germans lived under constant surveillance,\u201d Jason continued. '
    '\u201cThe secret police, called the <strong>Stasi</strong>, employed about 90,000 officers '
    'and recruited an estimated <strong>170,000 civilian informants</strong> \u2014 '
    'neighbors spying on neighbors, coworkers reporting coworkers, '
    'even family members informing on each other. '
    'The Stasi kept files on about <strong>6 million people</strong> '
    'out of a population of 16 million.\u201d</p>'

    '<p>\u201cMeanwhile, West Berlin became a symbol of freedom. '
    'In 1963, President Kennedy visited Berlin and declared: '
    '<strong>\u201cIch bin ein Berliner\u201d</strong> \u2014 \u201cI am a Berliner\u201d \u2014 '
    'telling the world that free people everywhere stood with the people of West Berlin.\u201d</p>'

    '<h3>Gorbachev\u2019s Reforms</h3>'

    '<p>\u201cBy the 1980s, the Soviet Union was in trouble,\u201d Jason said. '
    '\u201cIts economy was stagnant, its people were frustrated, and it was spending enormous sums '
    'on its military and the arms race with America. In 1985, a new Soviet leader came to power: '
    '<strong>Mikhail Gorbachev</strong>. He was different from previous Soviet leaders. '
    'He introduced two revolutionary ideas: <strong>glasnost</strong> (openness) '
    'and <strong>perestroika</strong> (restructuring).\u201d</p>'

    '<p>\u201cGlasnost meant more freedom of speech and a freer press. '
    'Perestroika meant reforming the stagnant economy. '
    'Gorbachev wanted to save the Soviet system by modernizing it. '
    'But once people tasted freedom, they wanted more. '
    'Across Eastern Europe, citizens began demanding change. '
    'Poland held free elections. Hungary opened its border with Austria. '
    'And in East Germany, massive protests erupted.\u201d</p>'

    '<h3>The Night the Wall Fell</h3>'

    '<p>\u201cOn <strong>November 9, 1989</strong>, the East German government, '
    'overwhelmed by weeks of protests involving hundreds of thousands of people, '
    'announced that citizens could freely cross the border,\u201d Jason said. '
    '\u201cBut the announcement was confused and premature. '
    'A government spokesman, <strong>G\u00fcnter Schabowski</strong>, was asked when the new policy began. '
    'He shuffled his papers, looked confused, and said: <strong>\u201cImmediately, without delay.\u201d</strong>\u201d</p>'

    '<p>\u201cWord spread like wildfire. Thousands of East Berliners rushed to the wall\u2019s checkpoints. '
    'The guards, overwhelmed and without clear orders, finally opened the gates. '
    'People streamed through, weeping, laughing, hugging strangers. '
    'West Berliners handed them flowers and champagne. '
    'People climbed on top of the wall and began smashing it with hammers and pickaxes. '
    'Families who hadn\u2019t seen each other in 28 years embraced in the street.\u201d</p>'

    '<p>\u201cIt was one of the most joyful nights in human history.\u201d</p>'

    '<h3>The End of the Cold War</h3>'

    '<p>\u201cGermany was officially <strong>reunified on October 3, 1990</strong>,\u201d Jason said. '
    '\u201cAcross Eastern Europe, communist governments fell one after another \u2014 '
    'in Czechoslovakia, Romania, Bulgaria, and the Baltic states. '
    'On <strong>December 26, 1991</strong>, the <strong>Soviet Union itself dissolved</strong>. '
    'The Cold War, which had defined the world for over 40 years '
    'and brought humanity to the brink of nuclear annihilation, was over.\u201d</p>'

    '<p>\u201cNo great army marched in to tear down the Berlin Wall,\u201d Jason said. '
    '\u201cOrdinary people did it \u2014 with hammers, with their bare hands, '
    'and with a courage that had been building for 28 years.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Berlin Wall and Cold War Timeline">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Berlin Wall &amp; End of the Cold War</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Wall Built (1961)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Berlin divided overnight</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">140+ killed trying to escape</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Gorbachev (1985)</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Glasnost &amp; Perestroika</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Openness and reform begin</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Wall Falls (Nov 9, 1989)</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Citizens smash the wall</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Families reunited after 28 years</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">USSR Dissolves (1991)</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Cold War ends</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">40+ years of tension over</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">3.5 million East Germans fled before the wall was built \u2014 20% of the population</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">The wall was torn down not by armies, but by ordinary people with hammers</text>'
    '</svg>'
    '</div>'

    '<p>The book brought them home. Evelyn looked out the window '
    'at the quiet street where no walls divided anyone.</p>'

    '<p>\u201cTwenty-eight years,\u201d she said softly. '
    '\u201cFamilies couldn\u2019t see each other for twenty-eight years.\u201d</p>'

    '<p>\u201cAnd then, in one night, it was over,\u201d Jason said. '
    '\u201cBecause enough people decided they wouldn\u2019t live behind a wall anymore. '
    'Goodnight, free city.\u201d</p>'

    '<p>\u201cGoodnight, broken wall.\u201d</p>'
)

disc_88 = [
    "The Berlin Wall was built to keep people in, not to keep enemies out. What does it tell you about a government when it has to build a wall to stop its own citizens from leaving?",
    "Gorbachev tried to reform the Soviet Union with glasnost and perestroika, but the changes he started led to the Soviet Union\u2019s collapse. Can you think of other times when trying to fix something actually changed it into something completely different?",
    "The Berlin Wall fell not because of an army, but because ordinary people demanded freedom. What does this tell you about the power of ordinary people when they act together?"
]

quiz_88 = [
    {
        "q": "Why was the Berlin Wall built in 1961?",
        "options": [
            "To protect East Berlin from a Western invasion",
            "To stop East Germans from fleeing to the West",
            "To mark the border between Germany and Poland",
            "To create a military defense line"
        ],
        "correct": 1
    },
    {
        "q": "What were Gorbachev\u2019s two key reform policies called?",
        "options": [
            "Sputnik and Vostok",
            "Glasnost and Perestroika",
            "Detente and Containment",
            "Solidarity and Unity"
        ],
        "correct": 1
    },
    {
        "q": "When did the Berlin Wall fall?",
        "options": ["November 9, 1985", "November 9, 1989", "October 3, 1990", "December 26, 1991"],
        "correct": 1
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 88:
        lessons[i] = {
            "id": 88,
            "type": "history",
            "topic": "ColdWar",
            "title": "The Wall Comes Down",
            "readingTime": "10 min",
            "story": story_88,
            "discussion": disc_88,
            "quiz": quiz_88
        }
        print("Updated lesson 88: The Wall Comes Down")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
