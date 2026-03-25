import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_37 = (
    '<h2>Galaxies and the Universe</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/NGC_4414_%28NASA-med%29.jpg/800px-NGC_4414_%28NASA-med%29.jpg" '
    'alt="A spiral galaxy photographed by the Hubble Space Telescope" loading="lazy">'
    '<p class="image-caption">A spiral galaxy \u2014 billions of stars orbiting a central core</p>'
    '</div>'

    '<p>William lay on his back in the yard, staring at the faint white smear of the Milky Way. '
    '\u201cRobert, is the Milky Way the whole universe?\u201d</p>'

    '<p>Robert laughed softly. \u201cNot even close. Let me show you.\u201d</p>'

    '<p>The telescope\u2019s golden light launched them upward \u2014 past the Moon, past the planets, '
    'past the Sun, and out of the solar system entirely. They kept going \u2014 '
    'past neighboring stars, past nebulae \u2014 until they hovered far enough away '
    'to see the entire Milky Way spread below them like a glowing pinwheel of light.</p>'

    '<h3>Our Galaxy \u2014 The Milky Way</h3>'

    '<p>\u201cThe Milky Way is a <strong>barred spiral galaxy</strong>,\u201d Robert said. '
    '\u201cIt contains between 100 billion and 400 billion stars arranged in spiraling arms '
    'that wind outward from a dense central bar. It\u2019s about 100,000 light-years across \u2014 '
    'that means even at the speed of light, it would take 100,000 years to travel from one side to the other.\u201d</p>'

    '<p>\u201cOur Sun is just one of those billions of stars, located about 26,000 light-years from the center, '
    'in a smaller arm called the <strong>Orion Arm</strong>. '
    'The Sun takes about 230 million years to complete one orbit around the galactic center \u2014 '
    'a period called a <strong>galactic year</strong>. The Sun has completed this orbit about 20 times '
    'since it was born.\u201d</p>'

    '<p>\u201cAt the very center of the Milky Way lurks a supermassive <strong>black hole</strong> '
    'called <strong>Sagittarius A*</strong>, with a mass of about 4 million Suns. '
    'It\u2019s so dense that nothing \u2014 not even light \u2014 can escape its gravitational pull.\u201d</p>'

    '<h3>Types of Galaxies</h3>'

    '<p>The telescope pulled them farther out, and more galaxies appeared \u2014 thousands, millions \u2014 '
    'in every shape imaginable.</p>'

    '<p>\u201cEdwin Hubble classified galaxies into three main types,\u201d Robert said.</p>'

    '<p>\u201c<strong>Spiral galaxies</strong> like our Milky Way have sweeping arms of stars, '
    'gas, and dust spiraling outward. They\u2019re actively forming new stars. '
    'The <strong>Andromeda Galaxy</strong>, our nearest large neighbor at 2.5 million light-years away, '
    'is a spiral galaxy you can actually see with the naked eye on a clear night.\u201d</p>'

    '<p>\u201c<strong>Elliptical galaxies</strong> are smooth, rounded blobs of older, reddish stars. '
    'They\u2019ve used up most of their gas and dust, so they don\u2019t form many new stars. '
    'The largest galaxies in the universe are ellipticals \u2014 some contain over a trillion stars.\u201d</p>'

    '<p>\u201c<strong>Irregular galaxies</strong> have no particular shape. '
    'They\u2019re often smaller and messier, sometimes distorted by the gravity of a nearby galaxy. '
    'The <strong>Large and Small Magellanic Clouds</strong>, visible from the Southern Hemisphere, '
    'are irregular dwarf galaxies orbiting the Milky Way.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 120" width="700" height="120" xmlns="http://www.w3.org/2000/svg" aria-label="Galaxy types">'
    '<rect width="700" height="120" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Three Types of Galaxies</text>'

    '<ellipse cx="130" cy="60" rx="50" ry="20" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="130" y="65" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Spiral</text>'
    '<text x="130" y="95" text-anchor="middle" fill="#b8a88a" font-size="8">Arms of stars + active</text>'
    '<text x="130" y="107" text-anchor="middle" fill="#b8a88a" font-size="8">star formation</text>'

    '<ellipse cx="350" cy="60" rx="45" ry="35" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="350" y="65" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Elliptical</text>'
    '<text x="350" y="95" text-anchor="middle" fill="#b8a88a" font-size="8">Smooth, older stars</text>'
    '<text x="350" y="107" text-anchor="middle" fill="#b8a88a" font-size="8">Few new stars forming</text>'

    '<path d="M530,40 Q560,50 540,65 Q570,75 550,85" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="570" y="65" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Irregular</text>'
    '<text x="570" y="95" text-anchor="middle" fill="#b8a88a" font-size="8">No defined shape</text>'
    '<text x="570" y="107" text-anchor="middle" fill="#b8a88a" font-size="8">Often small, chaotic</text>'
    '</svg>'
    '</div>'

    '<h3>The Expanding Universe</h3>'

    '<p>\u201cIn 1929, Edwin Hubble made one of the most important discoveries in science,\u201d Robert said. '
    '\u201cHe found that nearly every galaxy is moving <em>away</em> from every other galaxy. '
    'The farther away a galaxy is, the faster it\u2019s receding. '
    'This means the universe itself is <strong>expanding</strong> \u2014 space is stretching like the surface '
    'of a balloon being inflated.\u201d</p>'

    '<p>\u201cIf you rewind that expansion backward in time, everything was once packed into an '
    'incredibly tiny, incredibly hot, incredibly dense point. '
    'The moment that point began expanding, about <strong>13.8 billion years ago</strong>, '
    'is called the <strong>Big Bang</strong>. It wasn\u2019t an explosion <em>in</em> space \u2014 '
    'it was the expansion <em>of</em> space itself. Space, time, energy, and matter '
    'all came into existence in that moment.\u201d</p>'

    '<h3>The Observable Universe</h3>'

    '<p>\u201cThe <strong>observable universe</strong> \u2014 the part we can see \u2014 is about '
    '93 billion light-years across. It contains roughly <strong>2 trillion galaxies</strong>, '
    'each with billions of stars. And that\u2019s just the part we can observe. '
    'The full universe may be much larger \u2014 possibly infinite.\u201d</p>'

    '<p>William was speechless. The numbers were too big to imagine.</p>'

    '<p>\u201cAnd the Milky Way is heading toward the Andromeda Galaxy right now,\u201d Robert added. '
    '\u201cIn about 4.5 billion years, the two will collide and merge into one giant galaxy. '
    'But don\u2019t worry \u2014 the stars are so far apart that almost none will actually hit each other. '
    'It\u2019ll be more like two swarms of bees passing through each other.\u201d</p>'

    '<p>The telescope brought them home. The Milky Way still stretched overhead, '
    'but now it felt both immensely grand and strangely small \u2014 '
    'just one galaxy among two trillion.</p>'

    '<p>\u201cWe\u2019re so tiny,\u201d William whispered.</p>'

    '<p>\u201cBut we\u2019re the only part of the universe that can look up and ask \u2018why,\u2019\u201d '
    'Robert said. \u201cGoodnight, universe.\u201d</p>'

    '<p>\u201cGoodnight, 2 trillion galaxies.\u201d</p>'
)

disc_37 = [
    "The universe is 13.8 billion years old and still expanding. Where do you think it\u2019s going? Does the idea of an infinite universe excite you or frighten you?",
    "The Milky Way and Andromeda will collide in 4.5 billion years. What might the night sky look like for anyone living on Earth at that time?",
    "We are the part of the universe that asks \u2018why.\u2019 Why do you think humans are so driven to understand the cosmos?"
]

quiz_37 = [
    {
        "q": "What type of galaxy is the Milky Way?",
        "options": ["Elliptical", "Irregular", "Barred spiral", "Ring galaxy"],
        "correct": 2
    },
    {
        "q": "About how old is the universe?",
        "options": ["4.5 billion years", "9.2 billion years", "13.8 billion years", "20 billion years"],
        "correct": 2
    },
    {
        "q": "What is the supermassive black hole at the center of our galaxy called?",
        "options": ["Andromeda Core", "Sagittarius A*", "Orion Black", "Hubble Center"],
        "correct": 1
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 37:
        lessons[i] = {
            "id": 37,
            "type": "science",
            "topic": "Space",
            "title": "Galaxies and the Universe",
            "readingTime": "10 min",
            "story": story_37,
            "discussion": disc_37,
            "quiz": quiz_37
        }
        print("Updated lesson 37: Galaxies and the Universe")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
