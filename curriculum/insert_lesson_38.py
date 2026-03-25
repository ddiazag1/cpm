import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_38 = (
    '<h2>When Things Go Fizz and Bang</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Burning_iron_wool.jpg/800px-Burning_iron_wool.jpg" '
    'alt="Steel wool burning with bright orange sparks" loading="lazy">'
    '<p class="image-caption">Steel wool burning \u2014 iron reacting with oxygen in a brilliant chemical reaction</p>'
    '</div>'

    '<p>Evelyn dropped a fizzy tablet into a glass of water and watched it erupt in a storm of bubbles. '
    '\u201cJason, what\u2019s happening? Where are those bubbles coming from?\u201d</p>'

    '<p>Jason opened The Living World. \u201cThose bubbles are a brand new substance '
    'that didn\u2019t exist five seconds ago. That\u2019s the magic of chemical reactions.\u201d</p>'

    '<p>The brass clasp glowed, and the siblings shrank into the glass, '
    'watching molecules break apart and recombine into completely new arrangements.</p>'

    '<h3>What Is a Chemical Reaction?</h3>'

    '<p>\u201cA <strong>chemical reaction</strong> happens when atoms rearrange,\u201d Jason said. '
    '\u201cBonds between atoms break, and new bonds form, creating entirely new substances '
    'with different properties. The starting substances are called <strong>reactants</strong>, '
    'and what you get afterward are called <strong>products</strong>.\u201d</p>'

    '<p>\u201cThat fizzy tablet contains citric acid and baking soda (sodium bicarbonate). '
    'When water brings them together, they react and produce <strong>carbon dioxide gas</strong> \u2014 '
    'that\u2019s the bubbles. The CO\u2082 didn\u2019t exist before the reaction. '
    'It was created by rearranging the atoms.\u201d</p>'

    '<h3>Signs of a Reaction</h3>'

    '<p>\u201cHow do you know a chemical reaction is happening?\u201d Jason asked. '
    '\u201cLook for clues: <strong>gas bubbles</strong> forming (like your fizzy tablet), '
    'a <strong>color change</strong> (iron turning rust-red), '
    'a <strong>temperature change</strong> (hand warmers getting hot), '
    'a <strong>new smell</strong> (bread baking), '
    'or a <strong>precipitate</strong> (a solid forming in a liquid, like milk curdling).\u201d</p>'

    '<h3>Reactions All Around Us</h3>'

    '<p>\u201c<strong>Combustion</strong> (burning) is a reaction between fuel and oxygen that releases heat and light. '
    'A candle flame is wax reacting with oxygen, producing carbon dioxide and water vapor. '
    'A campfire is wood reacting with oxygen. Your body runs on slow combustion \u2014 '
    'cells \u2018burn\u2019 glucose with oxygen to release energy.\u201d</p>'

    '<p>\u201c<strong>Rusting</strong> is iron reacting with oxygen and water to form iron oxide. '
    'It\u2019s the same basic reaction as fire \u2014 iron combining with oxygen \u2014 but so slow '
    'it takes weeks or months instead of seconds.\u201d</p>'

    '<p>\u201c<strong>Cooking</strong> is full of chemical reactions. When you fry an egg, '
    'heat unravels the protein molecules and they bond in new ways \u2014 that\u2019s why a cooked egg '
    'is white and firm instead of clear and runny. You can\u2019t un-cook an egg '
    'because the chemical change is irreversible.\u201d</p>'

    '<p>\u201c<strong>Photosynthesis</strong> (CO\u2082 + water + light \u2192 sugar + oxygen) '
    'and <strong>cellular respiration</strong> (sugar + oxygen \u2192 CO\u2082 + water + energy) '
    'are opposite reactions that together form the foundation of life on Earth.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 140" width="700" height="140" xmlns="http://www.w3.org/2000/svg" aria-label="Types of reactions">'
    '<rect width="700" height="140" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Everyday Chemical Reactions</text>'

    '<rect x="20" y="30" width="155" height="55" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Combustion</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Fuel + O\u2082 \u2192 CO\u2082 + H\u2082O</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Fire, engines, body energy</text>'

    '<rect x="190" y="30" width="155" height="55" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Oxidation</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Iron + O\u2082 + H\u2082O \u2192 rust</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Slow \u201cburning\u201d over weeks</text>'

    '<rect x="360" y="30" width="155" height="55" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Acid-Base</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Acid + base \u2192 salt + water</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Antacids, baking, fizz</text>'

    '<rect x="530" y="30" width="150" height="55" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Cooking</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="7">Heat \u2192 proteins change</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Irreversible, new flavors</text>'

    '<text x="350" y="108" text-anchor="middle" fill="#b8a88a" font-size="9">Key rule: atoms are never created or destroyed \u2014 just rearranged</text>'
    '<text x="350" y="123" text-anchor="middle" fill="#b8a88a" font-size="9">This is the Law of Conservation of Mass (Antoine Lavoisier, 1789)</text>'
    '</svg>'
    '</div>'

    '<h3>Exothermic vs. Endothermic</h3>'

    '<p>\u201cSome reactions <strong>release</strong> energy as heat \u2014 these are called '
    '<strong>exothermic</strong>,\u201d Jason said. \u201cFire, hand warmers, and your body\u2019s metabolism '
    'are all exothermic. Others <strong>absorb</strong> energy \u2014 '
    'these are <strong>endothermic</strong>. Ice packs get cold because the reaction inside '
    'absorbs heat from your skin. Photosynthesis is endothermic \u2014 it absorbs sunlight energy.\u201d</p>'

    '<h3>The Law That Governs It All</h3>'

    '<p>\u201cIn 1789, <strong>Antoine Lavoisier</strong> discovered the <strong>Law of Conservation of Mass</strong>: '
    'in a chemical reaction, matter is neither created nor destroyed. '
    'The total mass of the reactants always equals the total mass of the products. '
    'Every atom that goes in must come out \u2014 just rearranged.\u201d</p>'

    '<p>\u201cSo when wood burns, the wood doesn\u2019t disappear?\u201d Evelyn asked.</p>'

    '<p>\u201cNot one atom of it. The carbon in the wood combines with oxygen and becomes CO\u2082 gas '
    'that floats away. The hydrogen becomes water vapor. The minerals become ash. '
    'If you could weigh all the gases, ash, and smoke, they\u2019d weigh exactly the same '
    'as the original wood plus the oxygen it consumed.\u201d</p>'

    '<p>The book brought them back to the kitchen. The fizzy tablet was gone, '
    'replaced by a glass of clear, slightly salty liquid.</p>'

    '<p>\u201cThe tablet is gone but its atoms aren\u2019t,\u201d Evelyn said. '
    '\u201cThey\u2019re in the water and in the air.\u201d</p>'

    '<p>\u201cNothing is ever really gone,\u201d Jason smiled. \u201cGoodnight, rearranged atoms.\u201d</p>'

    '<p>\u201cGoodnight, fizz and bang.\u201d</p>'
)

disc_38 = [
    "You can\u2019t un-cook an egg or un-burn a log. What makes some chemical reactions irreversible while others (like dissolving salt in water) can be reversed?",
    "Your body runs on slow combustion \u2014 burning glucose with oxygen. How is your body similar to a fire? How is it different?",
    "Lavoisier proved that matter is never created or destroyed, just rearranged. How does this law help explain the water cycle and the carbon cycle?"
]

quiz_38 = [
    {
        "q": "What is the Law of Conservation of Mass?",
        "options": [
            "Energy cannot be created or destroyed",
            "Matter cannot be created or destroyed in a chemical reaction",
            "The speed of light is constant",
            "Every reaction needs a catalyst"
        ],
        "correct": 1
    },
    {
        "q": "What type of reaction releases heat?",
        "options": ["Endothermic", "Exothermic", "Catalytic", "Neutral"],
        "correct": 1
    },
    {
        "q": "Which of these is NOT a sign that a chemical reaction is occurring?",
        "options": ["Gas bubbles forming", "Color change", "Object getting heavier from gravity", "Temperature change"],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 38:
        lessons[i] = {
            "id": 38,
            "type": "science",
            "topic": "Chemistry",
            "title": "When Things Go Fizz and Bang",
            "readingTime": "10 min",
            "story": story_38,
            "discussion": disc_38,
            "quiz": quiz_38
        }
        print("Updated lesson 38: When Things Go Fizz and Bang")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
