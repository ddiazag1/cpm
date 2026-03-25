import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_78 = (
    '<h2>A Nation Divided</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Battle_of_Gettysburg%2C_by_Currier_and_Ives.png/800px-Battle_of_Gettysburg%2C_by_Currier_and_Ives.png" '
    'alt="Currier and Ives lithograph depicting the Battle of Gettysburg in 1863" loading="lazy">'
    '<p class="image-caption">The Battle of Gettysburg (July 1863) \u2014 the bloodiest battle of the Civil War and a turning point for the Union</p>'
    '</div>'

    '<p>Evelyn traced her finger across a map of the United States. '
    '\u201cJason, why is there a line drawn across the middle of this old map?\u201d</p>'

    '<p>Jason opened The Living World and turned the brass clasp. '
    '\u201cThat line divided a nation in two,\u201d he said softly. '
    '\u201cLet me show you the saddest chapter in American history.\u201d</p>'

    '<p>The green light swept them onto a dusty road in South Carolina. '
    'Cannons boomed in the distance, and smoke curled above a brick fort '
    'standing alone in a harbor.</p>'

    '<h3>The Roots of Division</h3>'

    '<p>\u201cFrom the very beginning, the United States was really two countries stitched together,\u201d '
    'Jason said. \u201cThe <strong>Northern states</strong> were building factories, railroads, and cities. '
    'They relied on paid workers and immigrants. The <strong>Southern states</strong> built their entire economy '
    'on <strong>cotton</strong> \u2014 and cotton was picked by <strong>enslaved people</strong>. '
    'By 1860, nearly <strong>4 million</strong> men, women, and children were held in slavery across the South.\u201d</p>'

    '<p>\u201cSoutherners argued that each state had the right to decide its own laws \u2014 '
    'including whether to allow slavery. They called this <strong>states\u2019 rights</strong>. '
    'But at its heart, the conflict was about one thing: whether human beings could be owned as property. '
    'Every compromise Congress tried \u2014 the Missouri Compromise, the Compromise of 1850, '
    'the Kansas-Nebraska Act \u2014 only delayed the inevitable.\u201d</p>'

    '<h3>Abraham Lincoln and Fort Sumter</h3>'

    '<p>\u201cIn November 1860, <strong>Abraham Lincoln</strong> was elected president,\u201d Jason said. '
    '\u201cLincoln was not an abolitionist \u2014 he did not call for an immediate end to slavery everywhere \u2014 '
    'but he firmly opposed slavery\u2019s expansion into new territories. '
    'For the South, that was enough. Within weeks, <strong>South Carolina</strong> seceded from the Union, '
    'and by February 1861, six more states had followed, forming the <strong>Confederate States of America</strong> '
    'under President <strong>Jefferson Davis</strong>.\u201d</p>'

    '<p>\u201cOn <strong>April 12, 1861</strong>, Confederate soldiers opened fire on <strong>Fort Sumter</strong>, '
    'a Union fort in Charleston Harbor. After 34 hours of bombardment, the fort surrendered. '
    'No one was killed in the battle itself \u2014 but the Civil War had begun, '
    'and before it ended, more than <strong>600,000 Americans</strong> would be dead.\u201d</p>'

    '<p>Evelyn watched the shells arc across the harbor. \u201cAmericans fighting Americans,\u201d she whispered.</p>'

    '<p>\u201cBrothers against brothers,\u201d Jason said. \u201cLiterally. Families were torn apart. '
    'Some families had sons fighting on both sides.\u201d</p>'

    '<h3>The Bloodiest Battles</h3>'

    '<p>\u201cEveryone expected a short war,\u201d Jason continued. \u201cNortherners thought the South would '
    'collapse quickly. Southerners believed one or two big victories would convince the North to let them go. '
    'Both were tragically wrong.\u201d</p>'

    '<p>\u201cThe first major battle, <strong>Bull Run</strong> (July 1861), shocked the North. '
    'Confederate forces under General <strong>Thomas \u201cStonewall\u201d Jackson</strong> routed the Union army. '
    'Picnickers from Washington who had come to watch the battle fled in panic alongside retreating soldiers.\u201d</p>'

    '<p>\u201cThe war became a grinding, bloody stalemate. At <strong>Antietam</strong> (September 1862), '
    'nearly 23,000 soldiers were killed, wounded, or missing in a single day \u2014 '
    'the <strong>bloodiest day in American history</strong>. The battle was technically a draw, '
    'but the Confederate retreat gave Lincoln the opportunity he needed.\u201d</p>'

    '<h3>The Emancipation Proclamation</h3>'

    '<p>\u201cFive days after Antietam, Lincoln issued the <strong>Emancipation Proclamation</strong>,\u201d '
    'Jason said. \u201cEffective January 1, 1863, it declared that all enslaved people in Confederate states '
    'were \u201cforever free.\u201d It didn\u2019t immediately free everyone \u2014 the South didn\u2019t recognize '
    'Lincoln\u2019s authority \u2014 but it transformed the war. Now the Union was fighting not just '
    'to preserve the country, but to <strong>end slavery</strong>.\u201d</p>'

    '<p>\u201cNearly <strong>180,000 Black soldiers</strong> enlisted in the Union Army after the Proclamation. '
    'They fought with extraordinary courage, proving their valor at battles like <strong>Fort Wagner</strong>, '
    'where the 54th Massachusetts Infantry \u2014 one of the first Black regiments \u2014 led a legendary charge '
    'against a heavily fortified Confederate position.\u201d</p>'

    '<h3>Gettysburg \u2014 The Turning Point</h3>'

    '<p>\u201cIn July 1863, the two armies collided at <strong>Gettysburg, Pennsylvania</strong>,\u201d Jason said. '
    '\u201cFor three days, 165,000 soldiers fought in the largest battle ever on North American soil. '
    'On the third day, Confederate General <strong>Robert E. Lee</strong> ordered <strong>Pickett\u2019s Charge</strong> \u2014 '
    '12,000 soldiers marching across an open field into withering Union fire. It was a catastrophe. '
    'Nearly half the attackers were killed or wounded.\u201d</p>'

    '<p>\u201cGettysburg cost Lee 28,000 men. He would never invade the North again. '
    'Combined casualties for both sides reached <strong>51,000</strong> \u2014 more than the total American casualties '
    'in the entire Revolutionary War.\u201d</p>'

    '<p>\u201cFour months later, Lincoln delivered the <strong>Gettysburg Address</strong> at the battlefield cemetery. '
    'In just 272 words, he redefined the war as a test of whether a nation \u201cconceived in liberty '
    'and dedicated to the proposition that all men are created equal\u201d could endure.\u201d</p>'

    '<h3>Grant, Sherman, and the End</h3>'

    '<p>\u201cIn 1864, Lincoln found his general: <strong>Ulysses S. Grant</strong>,\u201d Jason said. '
    '\u201cGrant was different from previous Union commanders. He understood that the war would be won '
    'by relentless pressure, not by single battles. He pinned Lee\u2019s army in Virginia '
    'while General <strong>William T. Sherman</strong> marched through Georgia and the Carolinas, '
    'destroying railroads, factories, and farms in his infamous <strong>March to the Sea</strong>.\u201d</p>'

    '<p>\u201cBy April 1865, Lee\u2019s army was starving and surrounded. On <strong>April 9, 1865</strong>, '
    'Lee surrendered to Grant at <strong>Appomattox Court House</strong> in Virginia. '
    'Grant offered generous terms \u2014 Confederate soldiers could go home with their horses '
    'and would not be prosecuted for treason. When Union soldiers began celebrating with cannon fire, '
    'Grant ordered them to stop: \u201cThe war is over. The rebels are our countrymen again.\u201d\u201d</p>'

    '<h3>The Cost and Reconstruction</h3>'

    '<p>\u201cThe numbers are staggering,\u201d Jason said quietly. \u201cMore than <strong>620,000 soldiers dead</strong> \u2014 '
    'more Americans than died in World War I, World War II, Korea, and Vietnam <em>combined</em>. '
    'Entire Southern cities lay in ruins. A generation of young men was gone.\u201d</p>'

    '<p>\u201cJust five days after Lee\u2019s surrender, President Lincoln was <strong>assassinated</strong> '
    'by John Wilkes Booth at Ford\u2019s Theatre. The nation lost the one leader with the wisdom '
    'and compassion to heal its wounds.\u201d</p>'

    '<p>\u201cThe period after the war, called <strong>Reconstruction</strong> (1865\u20131877), '
    'tried to rebuild the South and secure rights for formerly enslaved people. '
    'The <strong>13th Amendment</strong> abolished slavery. The <strong>14th Amendment</strong> guaranteed citizenship and equal protection. '
    'The <strong>15th Amendment</strong> gave Black men the right to vote. '
    'For a brief, hopeful period, Black Americans served in Congress and state governments.\u201d</p>'

    '<p>\u201cBut when Reconstruction ended, Southern states passed <strong>Jim Crow laws</strong> '
    'that stripped away those rights through poll taxes, literacy tests, and violent intimidation. '
    'The promise of equality would not be fulfilled for another century.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="American Civil War">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The American Civil War (1861\u20131865)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Fort Sumter (1861)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">First shots fired</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">11 states secede from Union</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Emancipation (1863)</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Lincoln frees enslaved people</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">180,000 Black soldiers enlist</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Gettysburg (1863)</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">51,000 casualties in 3 days</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Lee never invades North again</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Appomattox (1865)</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Lee surrenders to Grant</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">620,000+ Americans dead</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">The war ended slavery but cost more American lives than all other U.S. wars combined</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">The 13th, 14th, and 15th Amendments promised equality \u2014 a promise still being fulfilled</text>'
    '</svg>'
    '</div>'

    '<p>The book brought them home. Evelyn stared at the map again, '
    'tracing the old dividing line with her finger.</p>'

    '<p>\u201cSo many people died,\u201d she said quietly. \u201cJust because some people '
    'thought they had the right to own other people.\u201d</p>'

    '<p>\u201cThat\u2019s the hardest lesson,\u201d Jason said. \u201cSometimes a country has to fight itself '
    'to become what it promised to be. Goodnight, divided nation.\u201d</p>'

    '<p>\u201cGoodnight, reunited country.\u201d</p>'
)

disc_78 = [
    "The Southern states argued that the Civil War was about states\u2019 rights, but the right they were fighting for was the right to own enslaved people. Why is it important to be honest about what a conflict is really about, even when the truth is uncomfortable?",
    "After the war, Grant told his soldiers to stop celebrating because \u201cthe rebels are our countrymen again.\u201d Why is it important to show compassion to people you have just defeated?",
    "The 13th, 14th, and 15th Amendments promised equality, but Jim Crow laws took those rights away for nearly a century. What does this teach us about the difference between writing a law and actually living by it?"
]

quiz_78 = [
    {
        "q": "What event started the American Civil War in April 1861?",
        "options": [
            "The election of Abraham Lincoln",
            "The Confederate attack on Fort Sumter",
            "The Battle of Gettysburg",
            "The Emancipation Proclamation"
        ],
        "correct": 1
    },
    {
        "q": "What did the Emancipation Proclamation do?",
        "options": [
            "Ended the Civil War",
            "Freed all enslaved people in the entire United States",
            "Declared enslaved people in Confederate states to be free",
            "Gave women the right to vote"
        ],
        "correct": 2
    },
    {
        "q": "Where did General Lee surrender to General Grant, ending the Civil War?",
        "options": ["Gettysburg", "Fort Sumter", "Washington D.C.", "Appomattox Court House"],
        "correct": 3
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 78:
        lessons[i] = {
            "id": 78,
            "type": "history",
            "topic": "CivilWar",
            "title": "A Nation Divided",
            "readingTime": "10 min",
            "story": story_78,
            "discussion": disc_78,
            "quiz": quiz_78
        }
        print("Updated lesson 78: A Nation Divided")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
