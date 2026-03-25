import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_83 = (
    '<h2>The World at War \u2014 Part 1</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Omaha_Beach_Landing_Craft_Approaches.jpg/800px-Omaha_Beach_Landing_Craft_Approaches.jpg" '
    'alt="American troops approaching Omaha Beach on D-Day, June 6, 1944" loading="lazy">'
    '<p class="image-caption">American soldiers approach Omaha Beach on D-Day \u2014 June 6, 1944, the beginning of the liberation of Europe</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass dial turned slowly, and the brothers found themselves '
    'standing on a cobblestone street in a European city. Shop windows were smashed. '
    'Yellow stars had been painted on doors. The air smelled like smoke.</p>'

    '<p>\u201cThis is the hardest story we\u2019ve ever told,\u201d William said quietly. '
    '\u201cThis is the story of World War II in Europe.\u201d</p>'

    '<h3>A Dictator Rises</h3>'

    '<p>\u201cAfter World War I, Germany was in ruins,\u201d William said. '
    '\u201cThe <strong>Treaty of Versailles</strong> forced Germany to accept blame for the entire war, '
    'pay enormous fines, and give up territory. The German people were humiliated, hungry, and angry. '
    'Then the <strong>Great Depression</strong> hit in 1929, and millions more lost their jobs.\u201d</p>'

    '<p>\u201cInto that despair walked <strong>Adolf Hitler</strong> and his <strong>Nazi Party</strong>. '
    'Hitler was a powerful speaker who told the German people that all their problems '
    'were caused by others \u2014 especially <strong>Jewish people</strong>. '
    'He promised to make Germany great again. Desperate and afraid, '
    'millions of Germans believed him. In 1933, Hitler became the leader of Germany '
    'and quickly turned it into a <strong>dictatorship</strong> \u2014 a country ruled by one man '
    'with total power and no elections.\u201d</p>'

    '<p>\u201cHitler banned other political parties, burned books he disagreed with, '
    'and began stripping Jewish people of their rights \u2014 their businesses, their citizenship, '
    'their dignity. It started with laws and ended with something far, far worse.\u201d</p>'

    '<h3>Appeasement Fails</h3>'

    '<p>\u201cOther countries watched Hitler grow stronger and did nothing,\u201d William said. '
    '\u201cWhen Hitler took over Austria in 1938, they did nothing. '
    'When he demanded part of Czechoslovakia, Britain and France gave it to him, '
    'hoping it would satisfy him. British Prime Minister <strong>Neville Chamberlain</strong> '
    'came home waving an agreement and promising \u201cpeace for our time.\u201d '
    'This policy of giving in to avoid conflict was called <strong>appeasement</strong>.\u201d</p>'

    '<p>\u201cBut you can\u2019t satisfy a bully by giving him what he wants,\u201d Robert said.</p>'

    '<p>\u201cNo,\u201d William said. \u201cYou can\u2019t. Six months later, Hitler took the rest of Czechoslovakia. '
    'Appeasement had failed completely.\u201d</p>'

    '<h3>War Begins</h3>'

    '<p>\u201cOn <strong>September 1, 1939</strong>, Germany invaded <strong>Poland</strong> '
    'using a terrifying new tactic called <strong>Blitzkrieg</strong> \u2014 \u2018lightning war.\u2019 '
    'Tanks, planes, and soldiers attacked together with overwhelming speed. '
    'Poland fell in just five weeks. Britain and France finally declared war on Germany. '
    'World War II had begun.\u201d</p>'

    '<p>\u201cIn the spring of 1940, Hitler\u2019s armies swept through Denmark, Norway, Belgium, '
    'and the Netherlands. Then came the unthinkable: <strong>France fell</strong> in just six weeks. '
    'The most powerful army in Europe had been defeated. Britain stood alone.\u201d</p>'

    '<h3>The Battle of Britain</h3>'

    '<p>\u201cHitler expected Britain to surrender, but he didn\u2019t count on '
    '<strong>Winston Churchill</strong>,\u201d William said. \u201cChurchill became Prime Minister in May 1940 '
    'and gave one of the most famous speeches in history: '
    '<strong>\u201cWe shall fight on the beaches, we shall fight on the landing grounds, '
    'we shall fight in the fields and in the streets\u2026 we shall never surrender.\u201d</strong>\u201d</p>'

    '<p>\u201cThe German air force \u2014 the <strong>Luftwaffe</strong> \u2014 bombed London and other British cities '
    'night after night for months. This was called the <strong>Blitz</strong>. '
    'Families huddled in subway stations while bombs exploded above them. '
    'But the <strong>Royal Air Force (RAF)</strong> fought back with incredible bravery, '
    'and Hitler was never able to invade Britain. Churchill said of the RAF pilots: '
    '\u201cNever in the field of human conflict was so much owed by so many to so few.\u201d\u201d</p>'

    '<h3>The Holocaust</h3>'

    '<p>William\u2019s voice became very quiet. \u201cNow I have to tell you about the worst thing '
    'human beings have ever done to other human beings.\u201d</p>'

    '<p>\u201cThe Nazis didn\u2019t just take away Jewish people\u2019s rights. They planned to destroy '
    'the entire Jewish population of Europe. They called it the \u2018Final Solution.\u2019 '
    'The Nazis built <strong>concentration camps</strong> and <strong>death camps</strong> '
    'across occupied Europe. Jewish men, women, and children were rounded up from their homes, '
    'packed into trains, and sent to these camps.\u201d</p>'

    '<p>\u201cIn the camps, prisoners were starved, worked to death, and murdered. '
    'By the end of the war, the Nazis had killed <strong>six million Jewish people</strong> \u2014 '
    'nearly two out of every three Jews in Europe. They also murdered Roma people, '
    'disabled people, political opponents, and others \u2014 millions more. '
    'This is called the <strong>Holocaust</strong>.\u201d</p>'

    '<p>\u201cWhy?\u201d Robert whispered.</p>'

    '<p>\u201cBecause hatred, once it is allowed to grow unchecked, can lead to unimaginable evil,\u201d '
    'William said. \u201cThe Holocaust happened because ordinary people chose to look away, '
    'because leaders chose fear over courage, and because an entire nation was taught to see '
    'other human beings as less than human. We remember it so that we never let it happen again.\u201d</p>'

    '<h3>D-Day and the Fall of Berlin</h3>'

    '<p>\u201cBy 1944, the Allies \u2014 led by Britain, the United States, and the Soviet Union \u2014 '
    'were ready to liberate Europe,\u201d William said. '
    '\u201cOn <strong>June 6, 1944</strong> \u2014 known as <strong>D-Day</strong> \u2014 '
    'the largest seaborne invasion in history landed on the beaches of Normandy, France. '
    'Over <strong>156,000 Allied soldiers</strong> stormed five beaches under heavy fire. '
    'Thousands died on the first day, but the Allies held the beaches and began pushing inland.\u201d</p>'

    '<p>\u201cFrom the east, the <strong>Soviet Union</strong> \u2014 which had lost more than '
    '<strong>20 million people</strong> in the war, more than any other nation \u2014 '
    'was driving the German army back toward Berlin. The Soviets fought with ferocious determination, '
    'having endured the brutal <strong>Siege of Stalingrad</strong>, '
    'one of the deadliest battles in human history.\u201d</p>'

    '<p>\u201cIn April 1945, Soviet forces surrounded Berlin. Hitler, hiding in an underground bunker, '
    'took his own life on April 30. On <strong>May 8, 1945</strong> \u2014 <strong>V-E Day</strong>, '
    'Victory in Europe Day \u2014 Germany surrendered. The war in Europe was over.\u201d</p>'

    '<p>\u201cBut the world would never be the same,\u201d William said. \u201cMore than <strong>40 million Europeans</strong> '
    'had died. Cities lay in rubble. And the full horror of the Holocaust was revealed '
    'as Allied soldiers liberated the camps and saw with their own eyes what had been done.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="WWII European Theater">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">World War II in Europe (1939\u20131945)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Hitler\u2019s Rise (1933)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Nazi dictatorship, antisemitism</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Appeasement fails</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Blitzkrieg (1939\u201340)</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Poland, France fall</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Britain stands alone</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">The Holocaust</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">6 million Jews murdered</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Never again</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">D-Day to V-E Day</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Normandy (June 6, 1944)</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Germany surrenders May 1945</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">40 million Europeans died \u2014 the deadliest conflict in human history</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">We remember so we never allow hatred to grow unchecked again</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. The room was very still.</p>'

    '<p>Robert stared at the floor for a long time. \u201cSix million people,\u201d he said.</p>'

    '<p>\u201cChildren, too,\u201d William said. \u201cThat\u2019s why we never look away. '
    'That\u2019s why we speak up when people are being treated as less than human, '
    'even when it\u2019s hard, even when it\u2019s just words. '
    'Because it always starts with words. '
    'Goodnight, Europe.\u201d</p>'

    '<p>\u201cGoodnight, brave ones.\u201d</p>'
)

disc_83 = [
    "Hitler rose to power by blaming Jewish people for Germany\u2019s problems. Why is it dangerous when a leader blames one group of people for everyone\u2019s troubles?",
    "Britain tried appeasement \u2014 giving Hitler what he wanted to avoid war. Why didn\u2019t this work, and what do you think they should have done differently?",
    "William said the Holocaust happened because ordinary people chose to look away. What can regular people do in everyday life to stand up against unfairness and cruelty?"
]

quiz_83 = [
    {
        "q": "What was Blitzkrieg?",
        "options": [
            "A type of submarine warfare",
            "A lightning-fast attack using tanks, planes, and soldiers together",
            "A defensive wall built by Germany",
            "A peace treaty between Germany and Britain"
        ],
        "correct": 1
    },
    {
        "q": "How many Jewish people were killed in the Holocaust?",
        "options": ["1 million", "3 million", "6 million", "10 million"],
        "correct": 2
    },
    {
        "q": "What happened on D-Day (June 6, 1944)?",
        "options": [
            "Germany invaded Poland",
            "Hitler became leader of Germany",
            "Allied forces landed on the beaches of Normandy, France",
            "The war in Europe ended"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 83:
        lessons[i] = {
            "id": 83,
            "type": "history",
            "topic": "WWII",
            "title": "The World at War \u2014 Part 1",
            "readingTime": "10 min",
            "story": story_83,
            "discussion": disc_83,
            "quiz": quiz_83
        }
        print("Updated lesson 83: The World at War \u2014 Part 1")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
