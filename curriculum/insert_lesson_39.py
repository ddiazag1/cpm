import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_39 = (
    '<h2>Hot and Cold</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Thermometer_CF.svg/400px-Thermometer_CF.svg.png" '
    'alt="A thermometer showing both Celsius and Fahrenheit scales" loading="lazy">'
    '<p class="image-caption">A thermometer \u2014 our tool for measuring the invisible energy of heat</p>'
    '</div>'

    '<p>William pressed his nose against the cold windowpane, watching his breath fog the glass. '
    '\u201cRobert, why does my breath make fog on the window but not on the wall?\u201d</p>'

    '<p>Robert picked up the old brass telescope and smiled. '
    '\u201cBecause the window is cold enough to steal heat from your breath. '
    'Tonight, let\u2019s go where heat begins \u2014 and where it ends.\u201d</p>'

    '<p>The telescope\u2019s golden light enveloped them, and the brothers felt themselves shrinking '
    'until they were smaller than a grain of sand, standing on a kitchen countertop '
    'beside a steaming mug of hot cocoa.</p>'

    '<h3>What Is Temperature?</h3>'

    '<p>\u201cEverything around us is made of atoms and molecules,\u201d Robert began, '
    '\u201cand those tiny particles are always moving \u2014 vibrating, bouncing, spinning. '
    '<strong>Temperature</strong> is a measure of how fast those particles are moving. '
    'The faster they jiggle, the hotter something feels. The slower they move, the colder it feels.\u201d</p>'

    '<p>They peered into the mug of cocoa, and the telescope let them see the molecules. '
    'Water molecules were rocketing around in every direction, crashing into each other '
    'like bumper cars at a fair. Steam rose from the surface as the fastest molecules '
    'escaped into the air.</p>'

    '<p>\u201cNow look at this ice cube,\u201d Robert said, pointing to one sitting on the counter. '
    'Inside the ice, the water molecules were barely moving at all \u2014 locked in a rigid crystal pattern, '
    'gently vibrating in place but never breaking free.</p>'

    '<p>\u201cSame molecule \u2014 H\u2082O \u2014 but the hot ones in the cocoa move about twenty times faster '
    'than the cold ones in the ice. That difference in speed is the difference between '
    '190 degrees Fahrenheit and 32 degrees Fahrenheit.\u201d</p>'

    '<h3>Absolute Zero \u2014 The Coldest Possible Temperature</h3>'

    '<p>The telescope whisked them away to a laboratory filled with strange equipment. '
    'Scientists in white coats were using lasers to slow atoms almost to a standstill.</p>'

    '<p>\u201cThere\u2019s a limit to how cold something can get,\u201d Robert said. '
    '\u201cIt\u2019s called <strong>absolute zero</strong>: \u2212459.67 degrees Fahrenheit, '
    'or \u22120 Kelvin, or \u2212273.15 degrees Celsius. '
    'At absolute zero, particles would have almost no motion at all. '
    'Scientists have cooled atoms to within a billionth of a degree above absolute zero, '
    'but they\u2019ve never quite reached it \u2014 the laws of physics say you never can.\u201d</p>'

    '<p>\u201cBut there\u2019s no upper limit for heat?\u201d William asked.</p>'

    '<p>\u201cNot really. The center of the Sun is about 27 million degrees Fahrenheit. '
    'A supernova explosion can reach 180 <em>billion</em> degrees. '
    'And the instant of the Big Bang was the hottest moment ever \u2014 '
    'trillions upon trillions of degrees.\u201d</p>'

    '<h3>How Heat Travels \u2014 Three Ways</h3>'

    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Fireplace_Burning.jpg/800px-Fireplace_Burning.jpg" '
    'alt="A fireplace with burning logs radiating heat" loading="lazy">'
    '<p class="image-caption">A fireplace demonstrates all three types of heat transfer at once</p>'
    '</div>'

    '<p>The telescope carried the brothers to a cozy cabin with a roaring fireplace.</p>'

    '<p>\u201cHeat always moves from something hot to something cold \u2014 never the other way around,\u201d '
    'Robert said. \u201cAnd it travels in three different ways.\u201d</p>'

    '<p>\u201cThe first is <strong>conduction</strong> \u2014 heat traveling through direct contact. '
    'Touch the iron poker resting in the fire: the end in the flames gets hot first, '
    'then the heat travels atom by atom along the metal to the handle. '
    'Each vibrating atom bumps its neighbor, passing kinetic energy along like a row of dominoes. '
    'Metals are great conductors \u2014 that\u2019s why a metal spoon in hot soup gets hot fast. '
    'Wood and plastic are poor conductors, which is why pot handles are often made of them.\u201d</p>'

    '<p>\u201cThe second is <strong>convection</strong> \u2014 heat traveling through moving fluid (liquid or gas). '
    'Watch the air near the fireplace: hot air rises because it expands and becomes less dense. '
    'Cooler, denser air sinks to take its place. This creates a circular flow called a '
    '<strong>convection current</strong>. That\u2019s why the upstairs of a house is warmer than the basement, '
    'why winds blow, and why ocean currents circulate.\u201d</p>'

    '<p>\u201cThe third is <strong>radiation</strong> \u2014 heat traveling as invisible waves of energy, '
    'called <strong>infrared radiation</strong>, that move at the speed of light. '
    'You can feel the fire\u2019s heat on your face from across the room \u2014 '
    'that warmth reaches you by radiation, right through the air, without needing to touch anything. '
    'This is how the Sun heats the Earth across 93 million miles of empty space.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 160" width="700" height="160" xmlns="http://www.w3.org/2000/svg" '
    'aria-label="Three methods of heat transfer">'
    '<rect width="700" height="160" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">'
    'Three Ways Heat Travels</text>'

    '<rect x="20" y="30" width="200" height="80" rx="6" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="120" y="50" text-anchor="middle" fill="#e74c3c" font-size="10" font-weight="bold">Conduction</text>'
    '<text x="120" y="66" text-anchor="middle" fill="#b8a88a" font-size="8">Direct contact</text>'
    '<text x="120" y="78" text-anchor="middle" fill="#b8a88a" font-size="8">Atom bumps neighbor</text>'
    '<text x="120" y="90" text-anchor="middle" fill="#b8a88a" font-size="8">Metal spoon in hot soup</text>'
    '<text x="120" y="102" text-anchor="middle" fill="#b8a88a" font-size="7">Solid \u2192 solid</text>'

    '<rect x="250" y="30" width="200" height="80" rx="6" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="350" y="50" text-anchor="middle" fill="#e8a838" font-size="10" font-weight="bold">Convection</text>'
    '<text x="350" y="66" text-anchor="middle" fill="#b8a88a" font-size="8">Moving fluid</text>'
    '<text x="350" y="78" text-anchor="middle" fill="#b8a88a" font-size="8">Hot rises, cold sinks</text>'
    '<text x="350" y="90" text-anchor="middle" fill="#b8a88a" font-size="8">Boiling water, wind</text>'
    '<text x="350" y="102" text-anchor="middle" fill="#b8a88a" font-size="7">Liquid or gas</text>'

    '<rect x="480" y="30" width="200" height="80" rx="6" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="580" y="50" text-anchor="middle" fill="#4a90d9" font-size="10" font-weight="bold">Radiation</text>'
    '<text x="580" y="66" text-anchor="middle" fill="#b8a88a" font-size="8">Energy waves (infrared)</text>'
    '<text x="580" y="78" text-anchor="middle" fill="#b8a88a" font-size="8">No contact needed</text>'
    '<text x="580" y="90" text-anchor="middle" fill="#b8a88a" font-size="8">Sun\u2019s warmth, campfire glow</text>'
    '<text x="580" y="102" text-anchor="middle" fill="#b8a88a" font-size="7">Works through empty space</text>'

    '<text x="350" y="135" text-anchor="middle" fill="#b8a88a" font-size="9" font-style="italic">'
    'Heat ALWAYS flows from hot to cold \u2014 never the other way</text>'
    '<text x="350" y="150" text-anchor="middle" fill="#b8a88a" font-size="9" font-style="italic">'
    'This is the Second Law of Thermodynamics</text>'
    '</svg>'
    '</div>'

    '<h3>Thermal Expansion \u2014 When Heat Makes Things Grow</h3>'

    '<p>The telescope took them to the top of the Eiffel Tower on a blazing summer day.</p>'

    '<p>\u201cDid you know the Eiffel Tower is about six inches taller in summer than in winter?\u201d '
    'Robert said. \u201cWhen atoms heat up and vibrate faster, they push farther apart. '
    'This is called <strong>thermal expansion</strong>. The iron in the tower expands '
    'when it\u2019s hot and contracts when it\u2019s cold.\u201d</p>'

    '<p>\u201cEngineers have to plan for this. Bridges have <strong>expansion joints</strong> \u2014 '
    'gaps in the roadway that let the bridge grow and shrink without cracking. '
    'Railroad tracks have small gaps between sections for the same reason. '
    'Without those gaps, hot summer days could buckle the tracks into dangerous curves.\u201d</p>'

    '<p>\u201cLiquids expand too. That\u2019s exactly how a <strong>thermometer</strong> works.\u201d</p>'

    '<h3>How Thermometers Work</h3>'

    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Mercury_Thermometer.jpg/220px-Mercury_Thermometer.jpg" '
    'alt="A mercury thermometer showing temperature markings" loading="lazy">'
    '<p class="image-caption">A liquid thermometer \u2014 the fluid inside rises as temperature increases</p>'
    '</div>'

    '<p>\u201cOld-fashioned thermometers use a thin glass tube filled with mercury or colored alcohol,\u201d '
    'Robert explained. \u201cWhen the temperature rises, the liquid expands and climbs up the tube. '
    'When it cools, the liquid contracts and drops. Marks on the tube let you read the temperature.\u201d</p>'

    '<p>\u201c<strong>Daniel Fahrenheit</strong> invented the mercury thermometer in 1714 '
    'and created the Fahrenheit scale. He set 32\u00b0F as the freezing point of water '
    'and 212\u00b0F as the boiling point. '
    '<strong>Anders Celsius</strong> later created a simpler scale: 0\u00b0C for freezing, '
    '100\u00b0C for boiling. Most of the world uses Celsius today.\u201d</p>'

    '<p>\u201cModern digital thermometers use a <strong>thermocouple</strong> or <strong>thermistor</strong> \u2014 '
    'materials whose electrical properties change with temperature. '
    'And <strong>infrared thermometers</strong> (like the ones used to check your forehead) '
    'detect the infrared radiation your body emits \u2014 the hotter you are, '
    'the more radiation you give off.\u201d</p>'

    '<h3>Insulators \u2014 Keeping Heat In (or Out)</h3>'

    '<p>\u201cIf heat always flows from hot to cold, how do we keep things hot?\u201d William asked.</p>'

    '<p>\u201cWith <strong>insulators</strong> \u2014 materials that slow down heat transfer,\u201d Robert said. '
    '\u201cWool, feathers, foam, and air are all great insulators. '
    'A winter coat doesn\u2019t make heat \u2014 it traps your body\u2019s heat inside a layer of still air. '
    'A thermos keeps coffee hot (or lemonade cold) by using a vacuum between two walls \u2014 '
    'since there\u2019s no matter in a vacuum, conduction and convection can\u2019t happen.\u201d</p>'

    '<p>\u201cAnimals use insulation too. Polar bears have two layers of fur and a thick layer of blubber '
    'to survive \u221240\u00b0F Arctic winters. Emperor penguins huddle in groups of thousands, '
    'rotating who stands on the cold outside, sharing body heat to survive Antarctic blizzards.\u201d</p>'

    '<p>The telescope brought them home. William pressed his hand against the cold window again, '
    'watching the warmth flow from his fingers into the glass.</p>'

    '<p>\u201cI can feel it now,\u201d he said. \u201cThe heat leaving my hand.\u201d</p>'

    '<p>\u201cHeat never stops moving,\u201d Robert said, pulling the blanket over his brother. '
    '\u201cBut tonight, we\u2019ll trap as much as we can. Goodnight, William.\u201d</p>'

    '<p>\u201cGoodnight, vibrating atoms.\u201d</p>'
)

disc_39 = [
    "Heat always flows from hot to cold. Why do you think it never goes the other direction? What would happen if it could?",
    "A thermos can keep soup hot for hours or keep lemonade cold. If it works by blocking heat transfer, how does it handle all three methods \u2014 conduction, convection, and radiation?",
    "The Eiffel Tower grows six inches taller in summer. What other everyday objects might expand or shrink with temperature that you\u2019ve never noticed?"
]

quiz_39 = [
    {
        "q": "What is temperature a measure of?",
        "options": [
            "How much matter an object contains",
            "How fast particles are moving",
            "How much space an object takes up",
            "How heavy an object is"
        ],
        "correct": 1
    },
    {
        "q": "Which method of heat transfer does NOT require any matter?",
        "options": ["Conduction", "Convection", "Radiation", "Insulation"],
        "correct": 2
    },
    {
        "q": "What is absolute zero?",
        "options": [
            "The temperature at which water freezes",
            "The coldest temperature ever recorded on Earth",
            "The theoretical lowest possible temperature",
            "The temperature of outer space"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 39:
        lessons[i] = {
            "id": 39,
            "type": "science",
            "topic": "Physics",
            "title": "Hot and Cold",
            "readingTime": "10 min",
            "story": story_39,
            "discussion": disc_39,
            "quiz": quiz_39
        }
        print("Updated lesson 39: Hot and Cold")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
