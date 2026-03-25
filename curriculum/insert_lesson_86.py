import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_86 = (
    '<h2>The Race to the Moon</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Aldrin_Apollo_11_original.jpg/800px-Aldrin_Apollo_11_original.jpg" '
    'alt="Buzz Aldrin standing on the surface of the Moon during Apollo 11" loading="lazy">'
    '<p class="image-caption">Buzz Aldrin on the Moon \u2014 July 20, 1969, photographed by Neil Armstrong</p>'
    '</div>'

    '<p>Evelyn was staring up at the night sky through her bedroom window. '
    'The Moon hung low and bright, its craters clearly visible. '
    '\u201cDo you think people will ever go back there?\u201d she asked.</p>'

    '<p>Jason smiled and opened The Living World, turning the brass clasp. '
    '\u201cBefore we look forward, let\u2019s look back \u2014 '
    'to the incredible story of how humans got there in the first place.\u201d</p>'

    '<p>The green light carried them to a dusty field in Kazakhstan. '
    'A massive silver rocket stood on a launchpad, hissing and steaming in the cold October air. '
    'Men in white coats scurried around the base, shouting in Russian.</p>'

    '<h3>The Beep That Changed Everything</h3>'

    '<p>\u201cThe year is 1957,\u201d Jason said. \u201cThe <strong>Cold War</strong> between '
    'the United States and the Soviet Union is at its height. '
    'Both superpowers are competing to prove which system is superior \u2014 '
    'American democracy or Soviet communism. And on October 4, 1957, '
    'the Soviets did something that stunned the entire world.\u201d</p>'

    '<p>The rocket roared to life, fire pouring from its engines, '
    'and climbed into the darkening sky. Minutes later, a tiny silver sphere '
    'the size of a beach ball was orbiting the Earth. '
    'From its four trailing antennas came a simple sound: <em>beep\u2026 beep\u2026 beep\u2026</em></p>'

    '<p>\u201cThat\u2019s <strong>Sputnik</strong> \u2014 the first artificial satellite,\u201d Jason said. '
    '\u201cIt weighed only 184 pounds and did nothing but send radio beeps. '
    'But those beeps terrified America. If the Soviets could put a satellite in orbit, '
    'could they also launch a nuclear weapon over the ocean? '
    'The <strong>Space Race</strong> had begun.\u201d</p>'

    '<h3>First Human in Space</h3>'

    '<p>\u201cThe Soviets kept winning,\u201d Jason continued. \u201cIn 1957, they launched <strong>Laika</strong>, '
    'a stray dog from Moscow, aboard Sputnik 2 \u2014 the first living creature in orbit. '
    'Sadly, Laika did not survive the trip. But then, on <strong>April 12, 1961</strong>, '
    'Soviet cosmonaut <strong>Yuri Gagarin</strong> became the first human being to fly in space. '
    'His spacecraft, <strong>Vostok 1</strong>, orbited the Earth once in 108 minutes. '
    'When he saw our planet from above, Gagarin said: '
    '\u201cI see Earth! It is so beautiful!\u201d\u201d</p>'

    '<p>\u201cAmerica was desperate to catch up,\u201d Jason said. \u201cAlan Shepard became the first American in space '
    'just three weeks later, but it was only a brief 15-minute flight \u2014 '
    'not a full orbit. America was still behind.\u201d</p>'

    '<h3>JFK\u2019s Bold Challenge</h3>'

    '<p>\u201cOn May 25, 1961, President <strong>John F. Kennedy</strong> stood before Congress '
    'and made one of the boldest promises in history,\u201d Jason said. '
    '\u201cHe declared: <strong>\u201cI believe that this nation should commit itself to achieving the goal, '
    'before this decade is out, of landing a man on the Moon and returning him safely to the Earth.\u201d</strong>\u201d</p>'

    '<p>Evelyn\u2019s eyes went wide. \u201cBefore the decade was out? '
    'That was less than nine years away!\u201d</p>'

    '<p>\u201cExactly,\u201d Jason said. \u201cAt the time, America had only 15 minutes of spaceflight experience. '
    'No one knew how to get to the Moon, how to land on it, or how to survive there. '
    'Kennedy was betting on American ingenuity to figure it all out \u2014 fast.\u201d</p>'

    '<h3>Mercury, Gemini, Apollo</h3>'

    '<p>\u201cNASA tackled the problem in three steps,\u201d Jason explained. '
    '\u201cFirst, the <strong>Mercury program</strong> (1961\u20131963) proved that humans could survive in space '
    'and orbit the Earth. John Glenn became the first American to orbit in February 1962, '
    'circling the globe three times.\u201d</p>'

    '<p>\u201cNext, the <strong>Gemini program</strong> (1965\u20131966) practiced the skills needed for a Moon mission \u2014 '
    'spacewalks, docking two spacecraft together in orbit, and longer flights '
    'to test whether astronauts could endure the time it would take to reach the Moon and return.\u201d</p>'

    '<p>\u201cFinally, the <strong>Apollo program</strong> began. But it started with tragedy. '
    'On January 27, 1967, a fire during a launch rehearsal killed three astronauts \u2014 '
    '<strong>Gus Grissom</strong>, <strong>Ed White</strong>, and <strong>Roger Chaffee</strong> \u2014 '
    'inside their Apollo 1 capsule. The nation grieved, and NASA redesigned the spacecraft '
    'from the ground up. They would not let those deaths be in vain.\u201d</p>'

    '<h3>One Giant Leap</h3>'

    '<p>\u201cOn <strong>July 16, 1969</strong>, Apollo 11 launched from Kennedy Space Center in Florida,\u201d '
    'Jason said. \u201cThree astronauts were aboard: '
    '<strong>Neil Armstrong</strong> (commander), <strong>Buzz Aldrin</strong> (lunar module pilot), '
    'and <strong>Michael Collins</strong> (command module pilot). '
    'The Saturn V rocket that carried them was 363 feet tall \u2014 taller than the Statue of Liberty \u2014 '
    'and remains the most powerful machine ever built by humans.\u201d</p>'

    '<p>\u201cFour days later, on <strong>July 20, 1969</strong>, Armstrong and Aldrin descended '
    'to the lunar surface in the <strong>Eagle</strong> landing module. '
    'The landing was terrifying \u2014 the computer overloaded with alarms, '
    'and Armstrong had to fly manually past a boulder field with only 25 seconds of fuel remaining. '
    'When the module finally touched down, Armstrong radioed Mission Control: '
    '<strong>\u201cHouston, Tranquility Base here. The Eagle has landed.\u201d</strong>\u201d</p>'

    '<p>\u201cBack in Houston, Charlie Duke, the capsule communicator, replied: '
    '\u201cRoger, Tranquility, we copy you on the ground. You got a bunch of guys about to turn blue. '
    'We\u2019re breathing again. Thanks a lot.\u201d\u201d</p>'

    '<p>\u201cAt 10:56 PM Eastern Time, Neil Armstrong stepped off the ladder and placed '
    'his left foot on the Moon\u2019s surface. He said: '
    '<strong>\u201cThat\u2019s one small step for man, one giant leap for mankind.\u201d</strong> '
    'An estimated <strong>600 million people</strong> watched on television \u2014 '
    'the largest audience for any event in human history up to that point.\u201d</p>'

    '<h3>The People Behind the Mission</h3>'

    '<p>\u201cWhat most people don\u2019t realize,\u201d Jason said, \u201cis that it took '
    '<strong>400,000 people</strong> to put those two men on the Moon. '
    'Engineers, mathematicians, seamstresses who sewed spacesuits by hand, '
    'welders, computer programmers, and scientists from every field imaginable. '
    '<strong>Margaret Hamilton</strong>, a software engineer, wrote the code that saved the landing '
    'when the computer overloaded. <strong>Katherine Johnson</strong>, a Black mathematician '
    'who worked at NASA during the era of segregation, calculated the orbital trajectories '
    'that made the mission possible.\u201d</p>'

    '<p>\u201cThe Apollo program cost about <strong>$25 billion</strong> in 1960s dollars \u2014 '
    'roughly $200 billion today. '
    'It remains the most ambitious engineering project in human history.\u201d</p>'

    '<p>Evelyn was quiet for a moment. \u201cSo it wasn\u2019t just about beating the Soviets?\u201d</p>'

    '<p>\u201cIt started that way,\u201d Jason said. \u201cBut when Armstrong stood on the Moon, '
    'the plaque on the Eagle didn\u2019t say \u2018America was here.\u2019 It said: '
    '<strong>\u2018We came in peace for all mankind.\u2019</strong> '
    'Competition got us there. But the achievement belonged to everyone.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Space Race Timeline">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Space Race (1957\u20131969)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Sputnik (1957)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">First satellite in orbit</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Soviet Union shocks the world</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Gagarin (1961)</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">First human in space</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">JFK pledges Moon by decade\u2019s end</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Gemini (1965\u20131966)</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Spacewalks &amp; docking</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Practice for the Moon</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Apollo 11 (1969)</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Armstrong walks on Moon</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">600 million watch on TV</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">400,000 people worked together to make the Moon landing possible</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">\u201cWe came in peace for all mankind\u201d \u2014 plaque left on the Moon</text>'
    '</svg>'
    '</div>'

    '<p>The book brought them home. Through the window, the Moon still glowed.</p>'

    '<p>Evelyn looked up at it with new eyes. '
    '\u201cThere are footprints up there right now,\u201d she whispered. '
    '\u201cAnd because there\u2019s no wind on the Moon, they\u2019ll be there forever.\u201d</p>'

    '<p>\u201cForever,\u201d Jason agreed. \u201cA reminder that when humans work together, '
    'nothing is impossible. Goodnight, giant leap.\u201d</p>'

    '<p>\u201cGoodnight, Moon.\u201d</p>'
)

disc_86 = [
    "The Space Race began because of competition between two rival countries. Do you think great achievements need competition to happen, or can cooperation work just as well?",
    "It took 400,000 people to land two men on the Moon \u2014 engineers, mathematicians, seamstresses, and welders. Why is it important to remember all of the people behind a great achievement, not just the famous names?",
    "The plaque on the Moon says \u2018We came in peace for all mankind.\u2019 Do you think the Moon landing really belongs to everyone, or mainly to the country that did it?"
]

quiz_86 = [
    {
        "q": "What was Sputnik?",
        "options": [
            "The first animal sent to space",
            "The first artificial satellite to orbit Earth",
            "The first manned spacecraft",
            "The first rocket to reach the Moon"
        ],
        "correct": 1
    },
    {
        "q": "Who was the first human being to travel to space?",
        "options": ["Neil Armstrong", "John Glenn", "Alan Shepard", "Yuri Gagarin"],
        "correct": 3
    },
    {
        "q": "Approximately how many people worked on the Apollo program to make the Moon landing possible?",
        "options": ["10,000", "50,000", "400,000", "1 million"],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 86:
        lessons[i] = {
            "id": 86,
            "type": "history",
            "topic": "Space",
            "title": "The Race to the Moon",
            "readingTime": "10 min",
            "story": story_86,
            "discussion": disc_86,
            "quiz": quiz_86
        }
        print("Updated lesson 86: The Race to the Moon")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
