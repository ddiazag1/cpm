import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_42 = (
    '<h2>Why Things Float or Sink</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Container_ship_Reecon_Whale.jpg/800px-Container_ship_Reecon_Whale.jpg" '
    'alt="A massive steel container ship floating on the ocean" loading="lazy">'
    '<p class="image-caption">A steel ship weighing thousands of tons floats because of its shape \u2014 the secret is buoyancy</p>'
    '</div>'

    '<p>Evelyn dropped a coin into the bathtub and watched it sink to the bottom with a clink. '
    'Then she placed a plastic duck on the surface and it bobbed happily on the waves.</p>'

    '<p>\u201cJason, the coin is tiny but it sinks. The duck is bigger but it floats. Why?\u201d</p>'

    '<p>Jason opened The Living World, and the brass clasp glowed green. '
    '\u201cThat question,\u201d he said, \u201cis the same one that made a man named Archimedes '
    'run naked through the streets of ancient Greece shouting \u2018Eureka!\u2019\u201d</p>'

    '<p>The book\u2019s light pulled them into the water, shrinking them down '
    'until they were swimming among the water molecules, watching forces at work '
    'that are invisible to the naked eye.</p>'

    '<h3>Density \u2014 The Key to Floating</h3>'

    '<p>\u201cThe answer to why things float or sink comes down to one word: '
    '<strong>density</strong>,\u201d Jason said. \u201cDensity is how much mass '
    'is packed into a given volume \u2014 how tightly the matter is squeezed together.\u201d</p>'

    '<p>\u201cImagine two boxes the same size. One is filled with feathers, '
    'the other with rocks. The rock box is denser \u2014 more mass in the same space. '
    'If something is <strong>denser</strong> than the liquid it\u2019s placed in, it sinks. '
    'If it\u2019s <strong>less dense</strong>, it floats.\u201d</p>'

    '<p>\u201cYour coin is made of metal, which is much denser than water \u2014 so it sinks. '
    'The plastic duck is mostly hollow air inside, making its overall density '
    'much less than water \u2014 so it floats.\u201d</p>'

    '<h3>Archimedes\u2019 Principle \u2014 The Eureka Moment</h3>'

    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Domenico-Fetti_Archimedes_1620.jpg/450px-Domenico-Fetti_Archimedes_1620.jpg" '
    'alt="A painting of Archimedes by Domenico Fetti" loading="lazy">'
    '<p class="image-caption">Archimedes (287\u2013212 BC) \u2014 the Greek mathematician who discovered the principle of buoyancy</p>'
    '</div>'

    '<p>The book transported them to ancient Syracuse, where a bearded man '
    'was lowering himself into an overflowing bath, deep in thought.</p>'

    '<p>\u201cThis is <strong>Archimedes</strong>, around 250 BC,\u201d Jason whispered. '
    '\u201cThe king had asked him to figure out if his new crown was pure gold '
    'or if the goldsmith had cheated by mixing in cheaper silver. '
    'Archimedes couldn\u2019t melt the crown to test it. He was stuck.\u201d</p>'

    '<p>\u201cBut when he got into the bath, he noticed the water level rose. '
    'The more of his body he lowered in, the more water spilled over the edge. '
    'And in that moment, he realized: <strong>any object placed in a fluid '
    'is pushed upward by a force equal to the weight of the fluid it displaces</strong>.\u201d</p>'

    '<p>\u201cThis upward push is called <strong>buoyancy</strong>, '
    'or the <strong>buoyant force</strong>. If the buoyant force is greater than '
    'the object\u2019s weight, the object floats. If the object\u2019s weight is greater, it sinks.\u201d</p>'

    '<p>\u201cHe realized that gold is denser than silver, so a pure gold crown '
    'would displace less water than a crown mixed with silver (because silver is lighter, '
    'so a mixed crown would need more volume to reach the same weight). '
    'He tested it, proved the goldsmith had cheated, and supposedly ran through the streets '
    'shouting <strong>\u2018Eureka!\u2019</strong> \u2014 Greek for \u2018I found it!\u2019\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 170" width="700" height="170" xmlns="http://www.w3.org/2000/svg" '
    'aria-label="Archimedes principle diagram showing buoyancy">'
    '<rect width="700" height="170" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">'
    'Archimedes\u2019 Principle: Why Things Float or Sink</text>'

    '<rect x="40" y="60" width="180" height="90" rx="4" fill="#1a3055" stroke="#4a90d9" stroke-width="1.5"/>'
    '<text x="130" y="50" text-anchor="middle" fill="#b8a88a" font-size="8">Water surface</text>'
    '<line x1="40" y1="60" x2="220" y2="60" stroke="#4a90d9" stroke-width="2" stroke-dasharray="4"/>'
    '<rect x="100" y="40" width="60" height="50" rx="3" fill="#e8a838" opacity="0.6"/>'
    '<text x="130" y="70" text-anchor="middle" fill="#0f1629" font-size="8" font-weight="bold">Wood</text>'
    '<text x="130" y="160" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">FLOATS</text>'
    '<text x="130" y="30" text-anchor="middle" fill="#b8a88a" font-size="7">Less dense than water</text>'

    '<rect x="260" y="60" width="180" height="90" rx="4" fill="#1a3055" stroke="#4a90d9" stroke-width="1.5"/>'
    '<line x1="260" y1="60" x2="440" y2="60" stroke="#4a90d9" stroke-width="2" stroke-dasharray="4"/>'
    '<rect x="320" y="90" width="60" height="40" rx="3" fill="#aaa" opacity="0.7"/>'
    '<text x="350" y="115" text-anchor="middle" fill="#0f1629" font-size="8" font-weight="bold">Iron</text>'
    '<text x="350" y="160" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">SINKS</text>'
    '<text x="350" y="50" text-anchor="middle" fill="#b8a88a" font-size="7">More dense than water</text>'

    '<rect x="480" y="60" width="180" height="90" rx="4" fill="#1a3055" stroke="#4a90d9" stroke-width="1.5"/>'
    '<line x1="480" y1="60" x2="660" y2="60" stroke="#4a90d9" stroke-width="2" stroke-dasharray="4"/>'
    '<path d="M540,42 L600,42 L600,72 L540,72 Z" fill="none" stroke="#aaa" stroke-width="1.5"/>'
    '<path d="M535,72 L605,72 L610,50 L530,50 Z" fill="#aaa" opacity="0.3"/>'
    '<text x="570" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Hollow hull</text>'
    '<text x="570" y="160" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">FLOATS</text>'
    '<text x="570" y="38" text-anchor="middle" fill="#b8a88a" font-size="7">Steel ship \u2014 shape displaces</text>'
    '<text x="570" y="30" text-anchor="middle" fill="#b8a88a" font-size="7">enough water to float</text>'
    '</svg>'
    '</div>'

    '<h3>Why Steel Ships Float</h3>'

    '<p>\u201cBut wait,\u201d Evelyn said. \u201cSteel is way denser than water. '
    'So how does a steel ship weighing thousands of tons float?\u201d</p>'

    '<p>\u201cBrilliant question,\u201d Jason said. \u201cA solid chunk of steel would absolutely sink. '
    'But a ship isn\u2019t a solid chunk \u2014 it\u2019s a hollow shell. '
    'The hull is shaped like a giant bowl, and inside it\u2019s mostly <strong>air</strong>. '
    'When you calculate the ship\u2019s total density \u2014 steel walls plus all that air inside \u2014 '
    'the <em>average</em> density is less than water.\u201d</p>'

    '<p>\u201cThe wide, bowl-shaped hull pushes aside (displaces) a huge volume of water. '
    'That displaced water pushes back with a buoyant force equal to its weight. '
    'As long as the ship\u2019s weight is less than the weight of water it displaces, '
    'the ship floats. The bigger the hull, the more water it pushes aside, '
    'and the more weight it can carry. That\u2019s why cargo ships have such wide, deep hulls.\u201d</p>'

    '<h3>Why Ice Floats \u2014 Water\u2019s Strange Secret</h3>'

    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Iceberg_in_the_Arctic_with_its_underside_exposed.jpg/800px-Iceberg_in_the_Arctic_with_its_underside_exposed.jpg" '
    'alt="An iceberg showing the large portion beneath the water surface" loading="lazy">'
    '<p class="image-caption">About 90% of an iceberg hides beneath the surface \u2014 ice is slightly less dense than liquid water</p>'
    '</div>'

    '<p>\u201cHere\u2019s something strange,\u201d Jason said. \u201cAlmost every substance in the universe '
    'is denser as a solid than as a liquid. When things freeze, their molecules pack tighter. '
    'But <strong>water is the opposite</strong>. When water freezes into ice, '
    'it actually becomes <em>less</em> dense \u2014 about 9% less dense than liquid water.\u201d</p>'

    '<p>\u201cThis happens because water molecules form a special crystal structure when they freeze. '
    'The hydrogen bonds lock them into a hexagonal lattice \u2014 a pattern with gaps in it, '
    'like a honeycomb. Those gaps make ice take up <em>more</em> space than the same amount '
    'of liquid water. This is called the <strong>anomalous expansion of water</strong>.\u201d</p>'

    '<p>\u201cThis quirk of nature is one of the most important facts in biology. '
    'Because ice floats, lakes and oceans freeze from the <strong>top down</strong>, '
    'not the bottom up. The floating ice forms an insulating lid '
    'that keeps the water below from freezing solid. '
    'Fish, frogs, and other aquatic creatures survive winter beneath that ice. '
    'If ice sank, lakes would freeze from the bottom up, '
    'killing most aquatic life and making Earth\u2019s climate far colder.\u201d</p>'

    '<h3>Submarines \u2014 Masters of Buoyancy</h3>'

    '<p>The book plunged them deep underwater, where a submarine glided silently '
    'through the dark ocean.</p>'

    '<p>\u201cSubmarines control their buoyancy using <strong>ballast tanks</strong>,\u201d Jason explained. '
    '\u201cTo dive, the submarine opens valves and lets seawater flood into its ballast tanks. '
    'This makes the sub heavier \u2014 its overall density increases above that of seawater \u2014 '
    'and it sinks. To rise, compressed air blows the water back out of the tanks, '
    'making the sub lighter, and it floats back up.\u201d</p>'

    '<p>\u201cA fish does the same thing with a <strong>swim bladder</strong> \u2014 '
    'a gas-filled sac inside its body. By adding or removing gas from the bladder, '
    'a fish can hover at any depth without swimming. '
    'Engineers actually studied fish swim bladders when designing submarine ballast systems.\u201d</p>'

    '<h3>Hot Air Balloons \u2014 Buoyancy in the Sky</h3>'

    '<p>The book lifted them into the sky, where a colorful hot air balloon drifted lazily overhead.</p>'

    '<p>\u201cBuoyancy doesn\u2019t just work in water \u2014 it works in <em>any</em> fluid, '
    'including air,\u201d Jason said. \u201cA hot air balloon floats because the air inside the balloon '
    'is heated by a burner. Hot air expands and becomes <strong>less dense</strong> than the cooler air outside. '
    'The balloon\u2019s total weight (hot air + fabric + basket + passengers) '
    'is less than the weight of the cooler air it displaces, so it rises.\u201d</p>'

    '<p>\u201cTo descend, the pilot opens a vent at the top of the balloon, letting hot air escape. '
    'As the air inside cools, the balloon\u2019s density increases and it sinks. '
    'It\u2019s the same principle as a submarine \u2014 just in a different fluid.\u201d</p>'

    '<h3>The Dead Sea \u2014 Where Everyone Floats</h3>'

    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Dead_Sea_by_David_Shankbone.jpg/800px-Dead_Sea_by_David_Shankbone.jpg" '
    'alt="A person floating effortlessly in the Dead Sea while reading a newspaper" loading="lazy">'
    '<p class="image-caption">The Dead Sea is so salty and dense that you float without even trying</p>'
    '</div>'

    '<p>The book swept them to the shores of the Dead Sea, between Israel and Jordan. '
    'People were floating on the surface as easily as corks, some reading books, '
    'others just lying back with their arms behind their heads.</p>'

    '<p>\u201cThe Dead Sea is about <strong>ten times saltier</strong> than the regular ocean,\u201d '
    'Jason said. \u201cAll that dissolved salt makes the water incredibly dense \u2014 '
    'about 1.24 grams per cubic centimeter, compared to 1.025 for normal seawater '
    'and 1.0 for fresh water. Since the human body\u2019s average density '
    'is only about 1.01, the Dead Sea water is denser than you are, '
    'so you float effortlessly. You literally cannot sink.\u201d</p>'

    '<p>\u201cThe Dead Sea is called \u2018dead\u2019 because almost nothing can live in water that salty. '
    'No fish, no seaweed, no coral. Only some bacteria and algae survive. '
    'But for humans, it\u2019s one of the most relaxing places on Earth.\u201d</p>'

    '<p>The book closed, and the siblings were back beside the bathtub. '
    'The coin still sat at the bottom. The duck still bobbed on top.</p>'

    '<p>\u201cSame water, same bathtub,\u201d Evelyn said, \u201cbut now I understand why '
    'one sinks and one floats. It\u2019s all about density.\u201d</p>'

    '<p>\u201cArchimedes figured it out 2,200 years ago in his bathtub,\u201d Jason smiled. '
    '\u201cAnd you figured it out in yours. Goodnight, Evelyn.\u201d</p>'

    '<p>\u201cGoodnight, buoyant world.\u201d</p>'
)

disc_42 = [
    "If ice didn\u2019t float \u2014 if it sank like most frozen substances \u2014 how would life on Earth be different? Could fish survive winter?",
    "A massive steel aircraft carrier floats, but a tiny steel nail sinks. Using what you learned about density and displacement, explain why shape matters more than material.",
    "Archimedes solved the king\u2019s problem by noticing something ordinary \u2014 water rising in a bathtub. What everyday observations have you made that might hold a scientific secret?"
]

quiz_42 = [
    {
        "q": "What determines whether an object floats or sinks?",
        "options": [
            "Its color",
            "Its temperature",
            "Whether it is denser or less dense than the fluid",
            "How fast it is moving"
        ],
        "correct": 2
    },
    {
        "q": "Why does ice float on water?",
        "options": [
            "Ice contains trapped air bubbles",
            "Water molecules form a crystal lattice with gaps, making ice less dense",
            "Ice is warmer than the water below it",
            "Wind pushes ice to the surface"
        ],
        "correct": 1
    },
    {
        "q": "How does a submarine dive deeper?",
        "options": [
            "It points its nose downward and uses engines to push down",
            "It releases heavy anchors that pull it deeper",
            "It floods ballast tanks with seawater, increasing its density",
            "It spins its propeller in reverse"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 42:
        lessons[i] = {
            "id": 42,
            "type": "science",
            "topic": "Physics",
            "title": "Why Things Float or Sink",
            "readingTime": "10 min",
            "story": story_42,
            "discussion": disc_42,
            "quiz": quiz_42
        }
        print("Updated lesson 42: Why Things Float or Sink")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
