import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_44 = (
    '<h2>The World Beneath Your Feet</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Stagnogley_-_geograph.org.uk_-_444030.jpg/800px-Stagnogley_-_geograph.org.uk_-_444030.jpg" '
    'alt="A cross-section of soil showing distinct horizontal layers from dark topsoil to lighter subsoil and rock" loading="lazy">'
    '<p class="image-caption">A soil profile revealing the hidden layers beneath our feet</p>'
    '</div>'

    '<p>Evelyn knelt in the garden and scooped up a handful of dark, crumbly dirt. '
    '\u201cJason, why is dirt so\u2026 dirty? What even <em>is</em> it?\u201d</p>'

    '<p>Jason laughed and opened The Living World. '
    '\u201cThat\u2019s not just dirt, Evelyn. That\u2019s <strong>soil</strong> \u2014 '
    'and it\u2019s one of the most important things on Earth. '
    'Without it, there would be no plants, no food, and no us.\u201d</p>'

    '<p>The brass clasp glowed green, and the siblings sank downward \u2014 '
    'through the grass, past tangled roots, into the dark, cool world beneath their feet.</p>'

    '<h3>What Soil Is Made Of</h3>'

    '<p>\u201cSoil isn\u2019t just one thing,\u201d Jason said as they floated through the darkness. '
    '\u201cIt\u2019s a mixture of four ingredients: roughly <strong>45 percent minerals</strong> '
    '(tiny broken pieces of rock), <strong>25 percent water</strong>, '
    '<strong>25 percent air</strong>, and <strong>5 percent organic matter</strong> \u2014 '
    'decomposed leaves, roots, dead insects, and microorganisms.\u201d</p>'

    '<p>\u201cThat 5 percent organic matter is the most important part. '
    'It\u2019s called <strong>humus</strong> (pronounced HEW-mus, not like the food). '
    'Humus is dark, spongy, and rich with nutrients. '
    'It\u2019s what gives healthy soil its dark brown or black color. '
    'Humus holds water like a sponge, feeds plant roots, '
    'and glues mineral particles together into crumbly clumps '
    'that let air and water flow through the soil.\u201d</p>'

    '<h3>Layers of the Earth \u2014 Soil Horizons</h3>'

    '<p>As they sank deeper, the soil changed. '
    'Jason pointed to distinct layers, like a cake sliced open.</p>'

    '<p>\u201cScientists call these layers <strong>soil horizons</strong>,\u201d he said. '
    '\u201cEvery soil profile tells a story millions of years in the making.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 260" width="700" height="260" xmlns="http://www.w3.org/2000/svg" aria-label="Soil horizons diagram">'
    '<rect width="700" height="260" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Soil Horizons (Layers)</text>'

    '<rect x="50" y="30" width="400" height="30" rx="3" fill="#3a2f1a"/>'
    '<text x="460" y="50" fill="#e8a838" font-size="10" font-weight="bold">O Horizon \u2014 Organic Layer</text>'
    '<text x="250" y="50" text-anchor="middle" fill="#b8a88a" font-size="8">Dead leaves, twigs, decomposing matter</text>'

    '<rect x="50" y="62" width="400" height="40" rx="3" fill="#4a3a20"/>'
    '<text x="460" y="80" fill="#e8a838" font-size="10" font-weight="bold">A Horizon \u2014 Topsoil</text>'
    '<text x="250" y="87" text-anchor="middle" fill="#b8a88a" font-size="8">Dark, humus-rich, full of roots + life</text>'
    '<text x="460" y="96" fill="#b8a88a" font-size="8">Takes 500\u20131,000 years to form 1 inch!</text>'

    '<rect x="50" y="104" width="400" height="40" rx="3" fill="#7a6040"/>'
    '<text x="460" y="122" fill="#e8a838" font-size="10" font-weight="bold">B Horizon \u2014 Subsoil</text>'
    '<text x="250" y="129" text-anchor="middle" fill="#b8a88a" font-size="8">Clay + minerals washed down from above</text>'
    '<text x="460" y="138" fill="#b8a88a" font-size="8">Less organic matter, lighter color</text>'

    '<rect x="50" y="146" width="400" height="40" rx="3" fill="#9a8a6a"/>'
    '<text x="460" y="164" fill="#e8a838" font-size="10" font-weight="bold">C Horizon \u2014 Parent Material</text>'
    '<text x="250" y="171" text-anchor="middle" fill="#b8a88a" font-size="8">Broken, weathered rock fragments</text>'
    '<text x="460" y="180" fill="#b8a88a" font-size="8">Not yet turned into true soil</text>'

    '<rect x="50" y="188" width="400" height="40" rx="3" fill="#6a6a6a"/>'
    '<text x="460" y="206" fill="#e8a838" font-size="10" font-weight="bold">Bedrock</text>'
    '<text x="250" y="213" text-anchor="middle" fill="#b8a88a" font-size="8">Solid, unbroken rock</text>'
    '<text x="460" y="222" fill="#b8a88a" font-size="8">The foundation everything rests on</text>'

    '<text x="350" y="248" text-anchor="middle" fill="#b8a88a" font-size="9" font-style="italic">Topsoil is where nearly all life lives \u2014 and it\u2019s the thinnest layer</text>'
    '</svg>'
    '</div>'

    '<p>\u201cThe <strong>O horizon</strong> is the very top \u2014 a thin carpet of dead leaves, '
    'twigs, and decomposing matter. Below that is the <strong>A horizon</strong>, or <strong>topsoil</strong> \u2014 '
    'the dark, crumbly layer where most roots grow and most soil creatures live. '
    'This is the layer farmers care about most.\u201d</p>'

    '<p>\u201cBelow topsoil is the <strong>B horizon</strong>, or <strong>subsoil</strong>. '
    'It\u2019s lighter in color and packed with clay and minerals that water has washed down from above. '
    'Deeper still is the <strong>C horizon</strong> \u2014 chunks of partially broken rock, '
    'called <strong>parent material</strong>, that hasn\u2019t fully become soil yet. '
    'And at the very bottom: <strong>bedrock</strong> \u2014 the solid, unbroken rock beneath everything.\u201d</p>'

    '<h3>How Rock Becomes Soil \u2014 Weathering</h3>'

    '<p>\u201cBut how does solid rock turn into crumbly soil?\u201d Evelyn asked.</p>'

    '<p>\u201cThrough <strong>weathering</strong> \u2014 the slow destruction of rock,\u201d Jason said. '
    '\u201cThere are three kinds. <strong>Physical weathering</strong> breaks rock '
    'without changing its chemistry \u2014 water seeps into cracks and freezes, expanding and splitting the rock. '
    'Tree roots pry rocks apart. Temperature changes cause rock to expand and contract until it cracks.\u201d</p>'

    '<p>\u201c<strong>Chemical weathering</strong> changes the rock\u2019s composition. '
    'Rainwater is slightly acidic (it absorbs CO\u2082 from the air), '
    'and over time it dissolves minerals like limestone. '
    'Iron in rocks reacts with oxygen and water, forming rust that weakens the stone.\u201d</p>'

    '<p>\u201c<strong>Biological weathering</strong> is caused by living things. '
    'Lichens produce acids that eat into rock surfaces. Burrowing animals and growing roots '
    'physically break rock apart. Bacteria and fungi chemically decompose minerals.\u201d</p>'

    '<p>\u201cThis process is extraordinarily slow. It takes <strong>500 to 1,000 years</strong> '
    'to form just one inch of topsoil. That handful of dirt in your hand, Evelyn, '
    'is older than most civilizations.\u201d</p>'

    '<h3>Earthworms \u2014 The Underground Engineers</h3>'

    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Regenwurm1.jpg/800px-Regenwurm1.jpg" '
    'alt="An earthworm moving through dark, moist soil" loading="lazy">'
    '<p class="image-caption">An earthworm \u2014 nature\u2019s greatest soil engineer</p>'
    '</div>'

    '<p>A long, pink creature tunneled past them, swallowing soil as it went.</p>'

    '<p>\u201cEarthworms!\u201d Evelyn cried.</p>'

    '<p>\u201cThey\u2019re the most important animals in the soil,\u201d Jason said. '
    '\u201c<strong>Charles Darwin</strong> \u2014 the same scientist who developed the theory of evolution \u2014 '
    'spent his last years studying earthworms. He wrote an entire book about them in 1881 '
    'and called them the most important creatures in the history of the world.\u201d</p>'

    '<p>\u201cEarthworms eat dead leaves and soil, digest them, and leave behind '
    '<strong>castings</strong> (worm poop) that are incredibly rich in nutrients \u2014 '
    'five times richer in nitrogen, seven times richer in phosphorus, '
    'and eleven times richer in potassium than the surrounding soil. '
    'Their tunnels create channels for air and water to reach plant roots. '
    'A healthy acre of farmland might contain over a million earthworms, '
    'and together they can move 18 tons of soil per year.\u201d</p>'

    '<h3>The Soil Food Web</h3>'

    '<p>\u201cEarthworms aren\u2019t alone down here,\u201d Jason continued. '
    '\u201cA single teaspoon of healthy soil contains more living organisms '
    'than there are people on Earth: billions of <strong>bacteria</strong>, '
    'millions of <strong>fungi</strong>, thousands of <strong>protozoa</strong>, '
    'and dozens of <strong>nematodes</strong> (microscopic worms).\u201d</p>'

    '<p>\u201cThey form a <strong>soil food web</strong>. '
    'Bacteria and fungi decompose dead plants and animals, recycling nutrients back into the soil. '
    'Protozoa eat bacteria and release nitrogen that plants can absorb. '
    'Nematodes eat everything. Mites and springtails shred dead leaves into smaller pieces. '
    'Beetles, ants, and millipedes mix and aerate the soil. '
    'Together, this underground community keeps the soil alive and fertile.\u201d</p>'

    '<p>\u201cWithout decomposers, dead leaves and trees would pile up forever,\u201d Jason said. '
    '\u201cNutrients would be locked away. Nothing new could grow. '
    'Decomposition is nature\u2019s recycling program.\u201d</p>'

    '<h3>Why Soil Matters</h3>'

    '<p>\u201cNearly 95 percent of the world\u2019s food grows in soil,\u201d Jason said. '
    '\u201cSoil filters and cleans water as it percolates downward. '
    'Soil stores more carbon than all the world\u2019s plants and atmosphere combined \u2014 '
    'making it critical for regulating climate. '
    'And soil is <em>not</em> renewable on human timescales. '
    'When topsoil erodes away \u2014 from wind, water, or poor farming \u2014 '
    'it takes centuries to rebuild.\u201d</p>'

    '<p>\u201cThe Dust Bowl of the 1930s showed what happens when topsoil is destroyed. '
    'Farmers in the American Great Plains plowed up millions of acres of native grassland. '
    'When drought came, there were no roots to hold the soil. '
    'Winds carried 300 million tons of topsoil into the air in massive dust storms, '
    'burying farms and forcing hundreds of thousands of people to flee.\u201d</p>'

    '<p>The book\u2019s green glow lifted them back to the garden. '
    'Evelyn looked at the dirt still on her hands \u2014 the same dirt, but utterly transformed in her mind.</p>'

    '<p>\u201cThis isn\u2019t just dirt,\u201d she whispered. \u201cIt\u2019s a whole world.\u201d</p>'

    '<p>\u201cBillions of living things, thousands of years of history, '
    'right there between your fingers,\u201d Jason said. '
    '\u201cGoodnight, world beneath our feet.\u201d</p>'

    '<p>\u201cGoodnight, earthworms,\u201d Evelyn smiled. '
    '\u201cKeep digging.\u201d</p>'
)

disc_44 = [
    "It takes 500 to 1,000 years to form one inch of topsoil. Knowing that, why is it so important to prevent soil erosion? What are some ways farmers and communities can protect their soil?",
    "Darwin called earthworms the most important creatures in the history of the world. Do you agree? What would happen to forests and farms if earthworms disappeared?",
    "A single teaspoon of healthy soil contains more organisms than there are people on Earth. How does this invisible community compare to a human city? What jobs do different soil creatures perform?"
]

quiz_44 = [
    {
        "q": "What are the four main components of soil?",
        "options": [
            "Sand, clay, gravel, and water",
            "Minerals, water, air, and organic matter",
            "Rocks, mud, worms, and roots",
            "Carbon, nitrogen, oxygen, and hydrogen"
        ],
        "correct": 1
    },
    {
        "q": "About how long does it take to form one inch of topsoil?",
        "options": ["5\u201310 years", "50\u2013100 years", "500\u20131,000 years", "5,000\u201310,000 years"],
        "correct": 2
    },
    {
        "q": "Which scientist spent years studying earthworms and wrote a book about their importance?",
        "options": ["Isaac Newton", "Louis Pasteur", "Charles Darwin", "Gregor Mendel"],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 44:
        lessons[i] = {
            "id": 44,
            "type": "science",
            "topic": "Earth Science",
            "title": "The World Beneath Your Feet",
            "readingTime": "10 min",
            "story": story_44,
            "discussion": disc_44,
            "quiz": quiz_44
        }
        print("Updated lesson 44: The World Beneath Your Feet")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
