import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_40 = (
    '<h2>The Great Animal Journeys</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Monarch_Butterfly_Danaus_plexippus_Migration.jpg/800px-Monarch_Butterfly_Danaus_plexippus_Migration.jpg" '
    'alt="Monarch butterflies clustered together during their migration" loading="lazy">'
    '<p class="image-caption">Monarch butterflies gathering by the millions during their incredible migration</p>'
    '</div>'

    '<p>Evelyn stood at the window, watching a V-shaped line of geese disappear into the sunset. '
    '\u201cJason, where are they all going? And how do they know the way?\u201d</p>'

    '<p>Jason reached for the green leather book on the nightstand. The brass clasp clicked open, '
    'and golden words appeared on the first page: <em>The Greatest Travelers on Earth.</em></p>'

    '<p>\u201cThose geese are on a <strong>migration</strong>,\u201d Jason said. '
    '\u201cA journey some animals make every year, traveling hundreds or even thousands of miles '
    'to find food, warmth, or safe places to have babies. And geese are just the beginning.\u201d</p>'

    '<p>The book\u2019s pages glowed, and the siblings were lifted into the sky, '
    'soaring alongside the geese as the world shrank below them.</p>'

    '<h3>The Arctic Tern \u2014 Champion of Champions</h3>'

    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Arctic_tern_%28Sterna_paradisaea%29.jpg/800px-Arctic_tern_%28Sterna_paradisaea%29.jpg" '
    'alt="An Arctic tern in flight over the ocean" loading="lazy">'
    '<p class="image-caption">The Arctic tern \u2014 a small bird that flies pole to pole each year</p>'
    '</div>'

    '<p>The book carried them to the Arctic, where a small white bird with a red beak '
    'was lifting off from a rocky shore.</p>'

    '<p>\u201cThis is the <strong>Arctic tern</strong>,\u201d Jason said, '
    '\u201cand it makes the longest migration of any animal on Earth \u2014 '
    'about <strong>44,000 miles</strong> round trip every year. '
    'It flies from the Arctic to Antarctica and back again, '
    'chasing endless summer so it sees more daylight than any other creature alive.\u201d</p>'

    '<p>\u201cOver its lifetime of 30 years, a single Arctic tern flies roughly '
    '<strong>1.5 million miles</strong> \u2014 enough to fly to the Moon and back three times.\u201d</p>'

    '<p>\u201cHow does something so small fly so far?\u201d Evelyn asked, watching the bird '
    'glide effortlessly on the ocean winds.</p>'

    '<p>\u201cIt rides the wind. Instead of flying in a straight line, it follows curving wind patterns '
    'across the Atlantic, using air currents like invisible highways. '
    'It barely needs to flap its wings \u2014 it\u2019s one of the most efficient flyers in nature.\u201d</p>'

    '<h3>The Wildebeest \u2014 A River of Hooves</h3>'

    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Wildebeest-during-Great-Migration_%28cropped%29.jpg/800px-Wildebeest-during-Great-Migration_%28cropped%29.jpg" '
    'alt="Vast herds of wildebeest migrating across the African savanna" loading="lazy">'
    '<p class="image-caption">The Great Migration \u2014 1.5 million wildebeest crossing the Serengeti</p>'
    '</div>'

    '<p>The book swept them to the golden plains of East Africa, and Evelyn gasped. '
    'The ground was moving. As far as she could see in every direction, '
    'wildebeest were marching \u2014 a living river of animals stretching to the horizon.</p>'

    '<p>\u201cThis is the <strong>Great Migration</strong>,\u201d Jason said. '
    '\u201cAbout <strong>1.5 million wildebeest</strong>, along with hundreds of thousands of zebras and gazelles, '
    'travel in a giant clockwise loop across the Serengeti in Tanzania '
    'and the Masai Mara in Kenya. They cover about 1,800 miles each year, '
    'always following the rains and the fresh green grass.\u201d</p>'

    '<p>\u201cThe most dangerous part is the river crossings. '
    'At the Mara River, thousands of wildebeest plunge into crocodile-filled waters. '
    'Many don\u2019t make it. But the herd is so enormous that the species survives. '
    'About 250,000 wildebeest die each year during the migration \u2014 '
    'from drowning, predators, and exhaustion \u2014 but about 500,000 calves are born, '
    'so the herd keeps growing.\u201d</p>'

    '<h3>The Gray Whale \u2014 Ocean Marathon</h3>'

    '<p>The book plunged them into cold Pacific waters, where an enormous gray shape '
    'glided past \u2014 a mother gray whale with her calf swimming alongside.</p>'

    '<p>\u201c<strong>Gray whales</strong> migrate about <strong>12,000 miles</strong> round trip each year,\u201d '
    'Jason said. \u201cThey spend summer feeding in the icy, food-rich waters of Alaska and the Bering Sea, '
    'stuffing themselves with tiny shrimp-like creatures. Then, as winter approaches, '
    'they swim south along the California coast all the way to the warm lagoons of Baja Mexico, '
    'where mothers give birth to their calves in calm, protected waters.\u201d</p>'

    '<p>\u201cThe calves need warm water because they\u2019re born without the thick blubber layer '
    'that keeps adults warm. They drink 50 gallons of their mother\u2019s rich milk every day, '
    'gaining about 60 pounds daily until they\u2019re strong enough for the swim back north.\u201d</p>'

    '<h3>The Salmon \u2014 Swimming Home to Die</h3>'

    '<p>They surfaced in a rushing river in the Pacific Northwest, '
    'surrounded by leaping silvery fish fighting their way upstream.</p>'

    '<p>\u201c<strong>Salmon</strong> are born in freshwater streams, then swim downstream to the ocean, '
    'where they spend years growing and feeding,\u201d Jason explained. '
    '\u201cBut when it\u2019s time to reproduce, something incredible happens: '
    'they navigate thousands of miles back to the exact stream where they were born. '
    'They fight against the current, leap up waterfalls, '
    'and use their sense of smell to find their birth stream.\u201d</p>'

    '<p>\u201cOnce they arrive, they lay their eggs and then \u2014 exhausted and battered \u2014 they die. '
    'Their bodies decompose and fertilize the stream, feeding the next generation. '
    'Bears, eagles, and other animals feast on the salmon, carrying nutrients into the forest. '
    'A single salmon run feeds an entire ecosystem.\u201d</p>'

    '<h3>The Monarch Butterfly \u2014 A Multi-Generation Relay</h3>'

    '<p>The book brought them to a forest in central Mexico, '
    'and Evelyn thought the trees were on fire. But it wasn\u2019t fire \u2014 '
    'it was <strong>millions of monarch butterflies</strong>, their orange wings '
    'covering every branch and trunk like a living blanket.</p>'

    '<p>\u201cMonarchs migrate up to <strong>3,000 miles</strong> from Canada and the northern United States '
    'to these mountain forests in Mexico,\u201d Jason said. '
    '\u201cBut here\u2019s what\u2019s truly amazing: no single butterfly makes the entire round trip. '
    'It takes <strong>four or five generations</strong> to complete the journey. '
    'The butterflies that fly south in autumn are the great-great-grandchildren '
    'of the ones that left Mexico the previous spring.\u201d</p>'

    '<p>\u201cHow do they know where to go if they\u2019ve never been there?\u201d Evelyn whispered.</p>'

    '<p>\u201cScientists believe the directions are written in their DNA \u2014 '
    'a kind of inherited GPS. They use the position of the Sun and the Earth\u2019s magnetic field '
    'to navigate. One generation is born knowing the way to a place it\u2019s never seen.\u201d</p>'

    '<h3>The Bar-Tailed Godwit \u2014 Nonstop Champion</h3>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 140" width="700" height="140" xmlns="http://www.w3.org/2000/svg" '
    'aria-label="Migration distance comparison chart">'
    '<rect width="700" height="140" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">'
    'Greatest Animal Migrations (round trip miles per year)</text>'

    '<rect x="20" y="30" width="600" height="12" rx="3" fill="#e74c3c" opacity="0.8"/>'
    '<text x="625" y="40" fill="#b8a88a" font-size="8">Arctic Tern: 44,000 mi</text>'

    '<rect x="20" y="48" width="163" height="12" rx="3" fill="#e8a838" opacity="0.8"/>'
    '<text x="188" y="58" fill="#b8a88a" font-size="8">Gray Whale: 12,000 mi</text>'

    '<rect x="20" y="66" width="95" height="12" rx="3" fill="#4a90d9" opacity="0.8"/>'
    '<text x="120" y="76" fill="#b8a88a" font-size="8">Bar-Tailed Godwit: 7,000 mi nonstop</text>'

    '<rect x="20" y="84" width="41" height="12" rx="3" fill="#2ecc71" opacity="0.8"/>'
    '<text x="66" y="94" fill="#b8a88a" font-size="8">Monarch Butterfly: 3,000 mi</text>'

    '<rect x="20" y="102" width="25" height="12" rx="3" fill="#9b59b6" opacity="0.8"/>'
    '<text x="50" y="112" fill="#b8a88a" font-size="8">Wildebeest: 1,800 mi</text>'

    '<text x="350" y="133" text-anchor="middle" fill="#b8a88a" font-size="8" font-style="italic">'
    'The bar-tailed godwit holds the record for longest nonstop flight of any bird</text>'
    '</svg>'
    '</div>'

    '<p>\u201cIf the Arctic tern wins the distance prize, the <strong>bar-tailed godwit</strong> '
    'wins the endurance prize,\u201d Jason said. \u201cThis shorebird flies from Alaska to New Zealand \u2014 '
    'about <strong>7,000 miles</strong> \u2014 in a single nonstop flight. '
    'No food, no water, no rest, no landing. Just nine straight days of flying over open ocean.\u201d</p>'

    '<p>\u201cBefore departure, the godwit eats so much that its body weight nearly doubles. '
    'Its internal organs actually <em>shrink</em> to make room for extra fat fuel. '
    'Its intestines and kidneys get smaller, and its flight muscles get bigger. '
    'When it finally lands in New Zealand, it has burned through every scrap of fat '
    'and lost half its body weight.\u201d</p>'

    '<h3>Humpback Whale Songs \u2014 Music Across the Ocean</h3>'

    '<p>The book dropped them deep underwater, where a haunting, beautiful sound '
    'echoed through the dark blue sea \u2014 the song of a <strong>humpback whale</strong>.</p>'

    '<p>\u201cHumpback whales migrate up to 10,000 miles round trip between polar feeding grounds '
    'and tropical breeding grounds,\u201d Jason said. \u201cBut what makes them truly special is their singing. '
    'Male humpbacks sing complex songs that can last up to 20 minutes, '
    'then repeat them for hours. Every male in the same ocean sings the same song, '
    'and the song slowly changes over the season \u2014 as if they\u2019re all composing together.\u201d</p>'

    '<p>\u201cTheir songs can travel over 10,000 miles through the ocean. '
    'No one fully understands why they sing \u2014 it may attract mates, '
    'warn rivals, or help with navigation. It\u2019s one of the great mysteries of the animal kingdom.\u201d</p>'

    '<p>The book closed gently, and the siblings were back in their bedroom. '
    'Through the window, the last of the geese had vanished into the darkening sky.</p>'

    '<p>\u201cThey\u2019re flying thousands of miles with no map, no phone, no road,\u201d Evelyn said softly. '
    '\u201cJust wings and instinct.\u201d</p>'

    '<p>\u201cEvery year, billions of animals set off on impossible journeys,\u201d Jason said, '
    'closing the book. \u201cAnd most of them make it. Goodnight, Evelyn.\u201d</p>'

    '<p>\u201cGoodnight, great travelers.\u201d</p>'
)

disc_40 = [
    "The monarch butterfly\u2019s migration takes four or five generations to complete. How is it possible that a butterfly knows how to fly to a place it\u2019s never been?",
    "The bar-tailed godwit flies 7,000 miles nonstop. If you had to prepare your body for an incredible endurance challenge, what changes would be most helpful?",
    "Many migrations are becoming harder because of climate change and habitat loss. What might happen to ecosystems if a major migration \u2014 like the wildebeest\u2019s \u2014 stopped?"
]

quiz_40 = [
    {
        "q": "Which animal makes the longest migration of any creature on Earth?",
        "options": ["Gray whale", "Monarch butterfly", "Arctic tern", "Bar-tailed godwit"],
        "correct": 2
    },
    {
        "q": "What happens to salmon after they return to their birth stream to lay eggs?",
        "options": [
            "They swim back to the ocean",
            "They hibernate through winter",
            "They die, and their bodies nourish the ecosystem",
            "They guard the eggs until they hatch"
        ],
        "correct": 2
    },
    {
        "q": "How does the bar-tailed godwit prepare for its 7,000-mile nonstop flight?",
        "options": [
            "It practices flying in short bursts",
            "It eats heavily, nearly doubling its weight, and its organs shrink",
            "It flies in large flocks to share the workload",
            "It sleeps for a week before departure"
        ],
        "correct": 1
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 40:
        lessons[i] = {
            "id": 40,
            "type": "science",
            "topic": "Biology",
            "title": "The Great Animal Journeys",
            "readingTime": "10 min",
            "story": story_40,
            "discussion": disc_40,
            "quiz": quiz_40
        }
        print("Updated lesson 40: The Great Animal Journeys")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
