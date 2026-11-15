# English content for the service and guide pages. tools/build_pages.py turns this into public/<slug>.html.
# Body HTML uses: <h2>, <p>, <ul class="ticks">, <ol class="steps">, <p class="callout">. Internal links are root paths
# like /claim-rejection; the Hindi build rewrites them to /hi/... automatically.
# Facts follow IRDAI rules as of the REVIEWED date; re-check them before changing that date.

REVIEWED = ('2026-11-15', '15 November 2026')

UI = {
    'lang': 'en', 'locale': 'en_IN', 'other_label': 'हिंदी', 'other_lang': 'hi',
    'skip': 'Skip to content', 'home': 'Home', 'services': 'Services', 'guides': 'Guides',
    'how': 'How it works', 'fees': 'Fees', 'faq': 'FAQ',
    'cta_short': 'Free case review', 'cta_review': 'Get a free case review', 'cta_wa': 'WhatsApp us', 'call': 'Call',
    'in_short': 'In short:',
    'fee_t': 'What it costs',
    'fee_p': 'The first review of your case is free. If we take it up, our fee is 10 to 20% of the amount the insurer pays you, agreed in writing before we start.',
    'fee_li': ['Nothing to pay upfront', 'Fee only after the money reaches you', 'No hidden charges'],
    'faq_t': 'Questions people ask', 'related_t': 'Related help',
    'band_t': 'Send us your letter. The first review is free.',
    'band_p': 'Share your policy and the insurer’s letter on WhatsApp. We’ll tell you honestly whether your case is worth pursuing.',
    'reviewed': 'Last reviewed',
    'note': 'This page is general information based on IRDAI rules as of the date above. It is not legal advice. Policy wordings differ, so we check what applies to your case.',
    'f_talk': 'Talk to us', 'f_help': 'Help', 'f_legal': 'Legal', 'privacy': 'Privacy policy', 'terms': 'Terms',
    'b2': 'Help in Hindi and English',
    'disclaimer': 'Mediclaimswala is an independent claim consultancy and is not affiliated with any insurance company, TPA or IRDAI. Outcomes depend on policy terms and the insurer’s decision.',
    'wa_default': 'Hi Mediclaimswala, I need help with my health insurance claim.',
}

PAGES = [
{
    'slug': 'claim-rejection', 'kind': 'service', 'nav': 'Claim rejection',
    'title': 'Health Insurance Claim Rejected? What to Do Next | Mediclaimswala',
    'description': 'Health insurance claim rejected? See why claims get rejected in India, what to do step by step, and how to challenge the decision. First case review is free.',
    'h1': 'Health insurance claim rejected? Here is what to do',
    'short': 'A rejection is not the final word. Read the reason in the insurer’s letter, check it against your policy wording, and send a written representation to the insurer’s grievance cell with your documents. If that fails, you can escalate to IRDAI’s Bima Bharosa portal and the Insurance Ombudsman, free of cost.',
    'wa': 'Hi Mediclaimswala, my health insurance claim was rejected. Can you review it?',
    'body': '''
<h2>Why health insurance claims get rejected</h2>
<p>The insurer has to give you the reason in writing. These are the reasons we see most often:</p>
<ul class="ticks">
<li><strong>Pre-existing disease.</strong> The insurer says the illness existed before the policy began and its waiting period is not over. Under IRDAI’s 2024 rules, this waiting period cannot be longer than 3 years.</li>
<li><strong>Waiting period.</strong> Most policies do not pay for illness in the first 30 days (accidents are covered), or for listed conditions such as cataract or hernia for a fixed period. Time already served on an earlier or ported policy counts.</li>
<li><strong>Non-disclosure.</strong> The insurer says a health condition was not declared in the proposal form. After 5 years of continuous cover, called the moratorium period, a claim cannot be contested on this ground unless there is proven fraud.</li>
<li><strong>“Not medically necessary”.</strong> The insurer says the treatment could have been given without admission. Your treating doctor’s notes are the main evidence here.</li>
<li><strong>Exclusions.</strong> The treatment falls under an exclusion listed in the policy, such as cosmetic treatment.</li>
<li><strong>Documents or deadlines.</strong> Papers were missing, or the insurer was informed late.</li>
</ul>
<p>Many rejections rest on a narrow reading of one clause. Reading that clause next to your medical records is where most cases are won.</p>

<h2>What to do, step by step</h2>
<ol class="steps">
<li><strong>Read the rejection letter.</strong> Note the clause number and the exact reason. If the reason is vague, ask the insurer or TPA to state it in writing.</li>
<li><strong>Collect your documents.</strong> Policy schedule and wording, a copy of your proposal form, the rejection letter, discharge summary, bills, test reports, doctor’s notes and every email or letter exchanged with the insurer.</li>
<li><strong>Check the reason against your policy.</strong> Was the waiting period already over? Was the condition really pre-existing, or diagnosed after cover began? Does the exclusion actually apply to this treatment?</li>
<li><strong>Write to the insurer’s grievance cell.</strong> Answer the rejection point by point and attach evidence, such as a certificate from your treating doctor. Insurers must acknowledge a complaint within 3 working days and resolve it within 14 days.</li>
<li><strong>Escalate if needed.</strong> Register the complaint on Bima Bharosa. If the insurer rejects your complaint or does not reply within a month, you can go to the Insurance Ombudsman within a year. See <a href="/insurance-ombudsman-complaint">how the Ombudsman works</a>.</li>
</ol>

<h2>Mistakes that weaken a case</h2>
<ul class="ticks">
<li>Arguing in general terms without quoting the clause the insurer relied on.</li>
<li>Sending documents that contradict what was submitted earlier, such as a different date of first diagnosis.</li>
<li>Waiting too long. The Ombudsman route closes one year after the insurer’s reply.</li>
</ul>

<h2>How Mediclaimswala helps</h2>
<p>Our team has worked inside the insurance and healthcare sector, so we know how claims are assessed. We read your letter and policy line by line, tell you honestly whether the case is worth pursuing, draft and file the representation, and follow up through the grievance cell and the Ombudsman until it is resolved.</p>
''',
    'faq': [
        ('Can a rejected health insurance claim be reopened?', 'Yes. You can send a written representation to the insurer’s grievance cell explaining why the rejection is wrong, with evidence. Insurers do reverse decisions when the reason does not hold up against the policy wording, though no one can guarantee the outcome.'),
        ('How long do I have to challenge a rejection?', 'Act as soon as you can. A complaint to the Insurance Ombudsman must be filed within one year of the insurer’s reply, and a consumer complaint is generally due within two years of the dispute arising.'),
        ('Do I need a lawyer?', 'No. The grievance cell, Bima Bharosa and the Insurance Ombudsman are free and do not need a lawyer. We help people who want experienced support through that process.'),
        ('My cashless request was denied. Is my claim rejected?', 'Not necessarily. A cashless denial means you pay the hospital and then file a reimbursement claim, which is assessed separately. See our page on health claim reimbursement.'),
    ],
    'related': ['claim-short-settled', 'insurance-ombudsman-complaint', 'know-your-policy'],
},
{
    'slug': 'delay-in-claim-process', 'kind': 'service', 'nav': 'Delay in claim process',
    'title': 'Health Insurance Claim Delayed? What You Can Do | Mediclaimswala',
    'description': 'Health insurance claim stuck or delayed? Learn the IRDAI time limits for settling claims, the interest owed on late payment, and how to escalate. First review free.',
    'h1': 'Health insurance claim stuck or delayed?',
    'short': 'Once an insurer has every document it needs, IRDAI rules give it a fixed time to settle or reject your claim, and a late payment carries interest at 2% above the bank rate. Get the claim status in writing, answer document requests in one go, and escalate to the grievance cell, Bima Bharosa and the Ombudsman when the deadline passes.',
    'wa': 'Hi Mediclaimswala, my health insurance claim is delayed. Can you help?',
    'body': '''
<h2>Why claims get stuck</h2>
<ul class="ticks">
<li>The insurer or TPA keeps asking for more documents.</li>
<li>The claim has been sent for investigation.</li>
<li>Billing queries go back and forth between the hospital and the TPA.</li>
<li>The claim shows “pending” with no update and no one to answer.</li>
</ul>

<h2>The time limits that apply</h2>
<ul class="ticks">
<li><strong>Cashless.</strong> IRDAI’s 2024 health insurance rules ask insurers to decide a cashless request within 1 hour, and the final discharge authorisation within 3 hours of the hospital’s request.</li>
<li><strong>Settlement.</strong> The insurer must settle or reject a claim within 30 days of receiving the last necessary document. If it investigates the claim, it gets up to 45 days in total.</li>
<li><strong>Interest.</strong> If it pays late, the insurer owes interest at 2% above the bank rate, from the date of the last document until the date of payment.</li>
<li><strong>Documents.</strong> Insurers are expected to ask for all missing documents together, not one at a time.</li>
</ul>
<p class="callout">The clock starts from the date the insurer received your last document, so keep proof of that date: a courier receipt or the email you sent.</p>

<h2>What to do, step by step</h2>
<ol class="steps">
<li><strong>Get the status in writing.</strong> Email the insurer or TPA with your claim number and ask what is pending.</li>
<li><strong>Answer requests completely.</strong> Send everything asked for in one reply, and ask them to confirm nothing else is needed.</li>
<li><strong>Track the deadline.</strong> Count 30 days, or 45 if the claim is under investigation, from the date of your last document.</li>
<li><strong>Write to the grievance officer.</strong> Once the deadline has passed, ask for settlement with interest and quote the dates.</li>
<li><strong>Escalate.</strong> Register on Bima Bharosa, then go to the <a href="/insurance-ombudsman-complaint">Insurance Ombudsman</a> if the insurer still does not act.</li>
</ol>

<h2>How Mediclaimswala helps</h2>
<p>We find out exactly where your claim is stuck, send the missing papers in one complete set, and follow up in writing until the insurer settles. If the deadline has passed, we escalate and ask for the interest you are owed.</p>
''',
    'faq': [
        ('Can I get interest for a delayed claim?', 'Yes. If the insurer settles after the time IRDAI allows, it owes interest at 2% above the bank rate from the date it received the last necessary document until it pays.'),
        ('The TPA says my claim is under investigation. Is that allowed?', 'Insurers may investigate, but the investigation has a time limit too. Ask for the status in writing, and note that the claim must still be settled or rejected within 45 days of the last document.'),
        ('The hospital won’t discharge the patient until cashless approval comes. What can I do?', 'Ask the hospital’s insurance desk for the request time and status, and contact the insurer’s helpline. If approval does not come, you can pay the bill and file a reimbursement claim. Keep every bill and receipt.'),
        ('How long does the Insurance Ombudsman take?', 'The Ombudsman is required to pass an award within three months of receiving everything it needs from you, and the insurer must comply within 30 days of accepting it.'),
    ],
    'related': ['health-claim-reimbursement', 'insurance-ombudsman-complaint', 'claim-rejection'],
},
{
    'slug': 'claim-short-settled', 'kind': 'service', 'nav': 'Claim short-settled',
    'title': 'Health Claim Short-Settled? Recover Unfair Deductions | Mediclaimswala',
    'description': 'Insurer paid less than your hospital bill? Understand room-rent proportionate deductions, non-payable items and co-payment, and how to challenge unfair cuts.',
    'h1': 'Claim paid less than your hospital bill?',
    'short': 'A short-settled claim is one where the insurer paid only part of the bill. Ask for the item-wise breakup of deductions, check each one against your policy, and challenge the ones the policy does not support. For example, proportionate deductions for a higher room cannot be applied to medicines, consumables, implants or diagnostic tests.',
    'wa': 'Hi Mediclaimswala, my health insurance claim was short-settled. Can you check the deductions?',
    'body': '''
<h2>The deductions we see most</h2>
<ul class="ticks">
<li><strong>Room rent and proportionate deduction.</strong> If your policy allows a room of ₹5,000 a day and you stayed in one costing ₹10,000, the insurer may cut many related charges, such as doctor visits, in the same proportion. IRDAI rules do not allow this cut on pharmacy, consumables, implants, medical devices or diagnostics, or in hospitals that charge the same for every room category.</li>
<li><strong>Non-payable items.</strong> IRDAI has a standard list of items that are not payable, such as gloves and masks, unless your policy has a consumables cover.</li>
<li><strong>Co-payment.</strong> Some policies make you pay a fixed share of every claim, often on senior citizen plans.</li>
<li><strong>Sub-limits.</strong> Some treatments, such as cataract surgery, have a fixed maximum regardless of the bill.</li>
<li><strong>“Reasonable and customary” charges.</strong> The insurer says the hospital charged more than usual for a procedure.</li>
<li><strong>Bills left out.</strong> Pre- and post-hospitalisation bills that were never counted.</li>
</ul>

<h2>What to do, step by step</h2>
<ol class="steps">
<li><strong>Get the breakup.</strong> Ask the insurer or TPA for the settlement letter with every deduction listed item by item.</li>
<li><strong>Match each deduction to a clause.</strong> If the letter does not name the clause, ask which one it relies on.</li>
<li><strong>Check proportionate deductions.</strong> Make sure they were not applied to medicines, consumables, implants, devices or tests.</li>
<li><strong>Write to the grievance cell.</strong> List each disputed deduction with the amount and the reason it is wrong.</li>
<li><strong>Escalate.</strong> If the insurer does not correct it, go to Bima Bharosa and the <a href="/insurance-ombudsman-complaint">Insurance Ombudsman</a>.</li>
</ol>

<h2>How Mediclaimswala helps</h2>
<p>We go through the bill and the settlement letter line by line, separate the deductions your policy allows from the ones it does not, and claim back the difference in writing.</p>
''',
    'faq': [
        ('What is a proportionate deduction?', 'When you stay in a room costlier than your policy allows, the insurer may reduce related charges, such as doctor fees and nursing, by the same proportion. It cannot be applied to medicines, consumables, implants, medical devices or diagnostic tests.'),
        ('Are consumables like gloves and masks covered?', 'Usually not. IRDAI has a standard list of non-payable items. They are paid only if your policy includes a consumables cover.'),
        ('I have already received the reduced amount. Can I still dispute it?', 'Yes. You can raise a grievance about the amount that was deducted. If the insurer does not resolve it, you have a year from its reply to approach the Insurance Ombudsman.'),
        ('How do I know which deductions are fair?', 'Compare each deduction with your policy schedule and wording. Room-rent limits, co-payment and sub-limits are written there. Deductions with no clause behind them are the ones to challenge.'),
    ],
    'related': ['know-your-policy', 'claim-rejection', 'insurance-ombudsman-complaint'],
},
{
    'slug': 'health-claim-reimbursement', 'kind': 'service', 'nav': 'Health claim reimbursement',
    'title': 'Health Claim Reimbursement: Documents and Deadlines | Mediclaimswala',
    'description': 'Paid the hospital yourself? A checklist of documents, time limits and steps for a health insurance reimbursement claim, and what to do if it gets stuck.',
    'h1': 'Filing a health insurance reimbursement claim',
    'short': 'In a reimbursement claim you pay the hospital first and claim the money back from the insurer. Inform the insurer on time, keep every original bill and report, and submit the claim form with your documents within the deadline in your policy, which is often 30 days from discharge.',
    'wa': 'Hi Mediclaimswala, I need help with a health insurance reimbursement claim.',
    'body': '''
<h2>When you need a reimbursement claim</h2>
<ul class="ticks">
<li>Treatment at a hospital outside the insurer’s network.</li>
<li>A cashless request that was denied or only partly approved.</li>
<li>Pre- and post-hospitalisation expenses, such as tests before admission and medicines after discharge.</li>
</ul>

<h2>Documents to keep and send</h2>
<ul class="ticks">
<li>The signed claim form, and a copy of your policy or health card.</li>
<li>Photo ID and KYC documents of the policyholder.</li>
<li>Discharge summary.</li>
<li>Final hospital bill with an item-wise breakup, and the payment receipts.</li>
<li>Pharmacy bills with the matching prescriptions.</li>
<li>Test and investigation reports.</li>
<li>Doctor’s consultation notes or certificates.</li>
<li>A cancelled cheque or bank details for the payment.</li>
<li>For accidents, the FIR or medico-legal certificate if one was made.</li>
</ul>

<h2>Time limits to watch</h2>
<ul class="ticks">
<li><strong>Informing the insurer.</strong> Your policy sets a time limit, often within 24 to 48 hours of an emergency admission, or before a planned one.</li>
<li><strong>Submitting the claim.</strong> Usually within a set number of days after discharge, often 30. Post-hospitalisation bills have their own deadline after that period ends.</li>
<li><strong>Late submission.</strong> Policies usually allow a delay to be excused for genuine reasons. Explain the reason in writing.</li>
</ul>

<h2>What to do, step by step</h2>
<ol class="steps">
<li><strong>Inform the insurer or TPA</strong> as soon as the patient is admitted, and note the intimation number.</li>
<li><strong>Collect originals at discharge.</strong> Ask the hospital for the itemised bill, discharge summary and all reports before you leave.</li>
<li><strong>Submit a complete file</strong> within the deadline and keep a copy of everything, with proof of the date you sent it.</li>
<li><strong>Track the claim</strong> and answer any query in one complete reply.</li>
<li><strong>Escalate</strong> if the claim is delayed, cut or rejected. See <a href="/delay-in-claim-process">delayed claims</a>.</li>
</ol>

<h2>How Mediclaimswala helps</h2>
<p>We check your file before it goes, so nothing is missing, and follow up until the money reaches you. If the claim is reduced or rejected, we take it up with the insurer.</p>
''',
    'faq': [
        ('What is the difference between cashless and reimbursement?', 'In a cashless claim the insurer pays the network hospital directly. In a reimbursement claim you pay the hospital and the insurer pays you back after checking your documents.'),
        ('Can I claim reimbursement if my cashless request was rejected?', 'Yes. A cashless denial is not a final rejection of the claim. You can pay the hospital and file for reimbursement with full documents.'),
        ('What if I miss the submission deadline?', 'Submit as soon as you can with a letter explaining the delay. Policies usually allow a delay to be excused for genuine reasons, such as the patient’s illness.'),
        ('Should I send original documents?', 'Follow what your insurer asks for, and always keep a full copy of everything you send, with proof of the date.'),
    ],
    'related': ['delay-in-claim-process', 'claim-short-settled', 'claim-rejection'],
},
{
    'slug': 'mis-selling-of-health-insurance', 'kind': 'service', 'nav': 'Mis-selling of health insurance',
    'title': 'Mis-sold Health Insurance Policy? What You Can Do | Mediclaimswala',
    'description': 'Were you sold the wrong health insurance policy or given false promises? Signs of mis-selling, the 30-day free-look period, and how to complain.',
    'h1': 'Sold the wrong health insurance policy?',
    'short': 'Mis-selling is when a health policy is sold with false promises or hidden facts, for example an agent filling in your health details without asking you, or a fixed-benefit plan sold as full hospital cover. A new policy can be returned within the free-look period. After that, complain to the insurer in writing, then to Bima Bharosa and the Insurance Ombudsman.',
    'wa': 'Hi Mediclaimswala, I think my health insurance policy was mis-sold.',
    'body': '''
<h2>Signs your policy was mis-sold</h2>
<ul class="ticks">
<li>The agent filled in the proposal form or your health details without asking you. This often leads to a non-disclosure rejection later.</li>
<li>You were promised “no waiting period” or “everything covered from day one”.</li>
<li>A fixed-benefit or critical illness plan was sold as hospitalisation cover.</li>
<li>A top-up or super top-up plan was sold as your main cover.</li>
<li>The policy was pushed on you with a loan or another product.</li>
<li>The premium, sum insured or room-rent limit differs from what you were told.</li>
</ul>

<h2>What to do, step by step</h2>
<ol class="steps">
<li><strong>Compare promises with the policy.</strong> Read the policy schedule and wording against what you were told.</li>
<li><strong>Keep your proof.</strong> Messages, emails, brochures, call recordings, and the agent’s name and licence details.</li>
<li><strong>Use the free-look period.</strong> For a new policy, you can return it within the free-look period, now 30 days under IRDAI’s 2024 rules, and get a refund minus small deductions.</li>
<li><strong>Complain in writing.</strong> Write to the insurer’s grievance cell with your evidence.</li>
<li><strong>Escalate.</strong> Go to Bima Bharosa, and then the <a href="/insurance-ombudsman-complaint">Insurance Ombudsman</a>, which also hears complaints about misrepresented policy terms.</li>
</ol>

<p class="callout">If your proposal form has wrong health details, talk to us before you file a claim. Fixing it after a claim is much harder than before.</p>

<h2>How Mediclaimswala helps</h2>
<p>We read your policy against what you were promised, tell you plainly what you have, and help you complain with the right evidence.</p>
''',
    'faq': [
        ('What is the free-look period?', 'It is the time after you receive a new policy during which you can return it if it does not suit you. Under IRDAI’s 2024 rules it is 30 days, and you get your premium back minus small deductions such as stamp duty and medical test costs.'),
        ('The agent filled my health details wrongly. What now?', 'Tell the insurer in writing and ask for the proposal form to be corrected. Doing this before a claim protects you from a non-disclosure rejection later. Talk to us first if you are unsure.'),
        ('Can I complain about mis-selling after the free-look period?', 'Yes. Complain to the insurer’s grievance cell, then Bima Bharosa and the Insurance Ombudsman if needed.'),
        ('Is a critical illness plan the same as health insurance?', 'No. A critical illness plan pays a fixed amount when a listed illness is diagnosed. It does not pay your hospital bills the way a regular health policy does.'),
    ],
    'related': ['know-your-policy', 'claim-rejection', 'insurance-ombudsman-complaint'],
},
{
    'slug': 'know-your-policy', 'kind': 'service', 'nav': 'Know your policy', 'fee': False,
    'title': 'Know Your Health Insurance Policy: What to Check | Mediclaimswala',
    'description': 'The health insurance terms that cause most claim disputes: room-rent limits, co-payment, sub-limits, waiting periods and exclusions. What to check in your policy.',
    'h1': 'Know your health policy before you need it',
    'short': 'Most claim disputes start with something in the policy the family never read: a room-rent limit, a co-payment, a waiting period or a sub-limit. Check these terms in your policy schedule and wording now, while nothing is at stake, and ask the insurer in writing about anything unclear.',
    'wa': 'Hi Mediclaimswala, can you help me understand my health insurance policy?',
    'side_t': 'Send us your policy',
    'side_p': 'Share your policy schedule and wording on WhatsApp. We’ll explain in plain words what it covers and where claims usually go wrong.',
    'body': '''
<h2>The terms to check</h2>
<ul class="ticks">
<li><strong>Sum insured.</strong> The most the insurer pays in a year, and whether it is restored after a claim.</li>
<li><strong>Room-rent limit.</strong> The room you can take, such as a single private room or a percentage of the sum insured. Going above it can reduce the whole claim proportionately.</li>
<li><strong>Co-payment.</strong> The share of each claim you pay yourself.</li>
<li><strong>Sub-limits.</strong> Fixed maximums for treatments such as cataract surgery.</li>
<li><strong>Waiting periods.</strong> Usually 30 days for any illness, a fixed period for listed conditions, and up to 3 years for pre-existing diseases.</li>
<li><strong>Exclusions.</strong> Treatments the policy never pays for.</li>
<li><strong>Pre- and post-hospitalisation.</strong> How many days of expenses before admission and after discharge are covered.</li>
<li><strong>Claim deadlines.</strong> How soon you must inform the insurer and submit a claim.</li>
<li><strong>Network hospitals.</strong> Where you can get cashless treatment.</li>
</ul>

<h2>Your proposal form matters</h2>
<p>The health details in your proposal form are the first thing an insurer checks when a claim comes in. Keep a copy, and make sure every condition and medicine was declared correctly.</p>
<p class="callout">After 5 years of continuous cover, called the moratorium period, a claim cannot be contested for non-disclosure unless there is proven fraud.</p>

<h2>Renewing and porting</h2>
<ul class="ticks">
<li><strong>Renew on time.</strong> A break in cover can restart waiting periods.</li>
<li><strong>Porting.</strong> When you move to another insurer, the waiting period you have already served carries over, up to your earlier sum insured.</li>
</ul>

<h2>How Mediclaimswala helps</h2>
<p>Send us your policy and we will explain, in Hindi or English, what it covers, where claims usually go wrong, and what to keep ready before you need it.</p>
''',
    'faq': [
        ('Where do I find the room-rent limit?', 'In your policy schedule or the policy wording, usually in the section on hospitalisation expenses. It may be a type of room or a percentage of the sum insured per day.'),
        ('What is the waiting period for pre-existing diseases?', 'It depends on your policy, but under IRDAI’s 2024 rules it cannot be longer than 3 years.'),
        ('What is the moratorium period?', 'After 5 years of continuous cover, an insurer cannot contest a claim on the ground of non-disclosure or misrepresentation, except in cases of proven fraud.'),
        ('Do I lose my waiting period if I change insurers?', 'No. When you port your policy, the waiting period you have already served carries over to the new insurer, up to your earlier sum insured.'),
    ],
    'related': ['mis-selling-of-health-insurance', 'claim-short-settled', 'claim-rejection'],
},
{
    'slug': 'insurance-ombudsman-complaint', 'kind': 'guide', 'nav': 'Insurance Ombudsman guide',
    'title': 'How to Complain to the Insurance Ombudsman (Health) | Mediclaimswala',
    'description': 'Step-by-step guide to filing a complaint with the Insurance Ombudsman for a rejected, short-paid or delayed health claim: who can file, time limits, documents.',
    'h1': 'How to complain to the Insurance Ombudsman',
    'short': 'The Insurance Ombudsman is a free forum for disputes with your insurer, including rejected, short-paid and delayed health claims up to ₹50 lakh. Complain to the insurer in writing first. If it rejects your complaint, does not reply within a month, or gives an unsatisfactory reply, you can file with the Ombudsman within one year, online or by post.',
    'wa': 'Hi Mediclaimswala, I want to file a complaint with the Insurance Ombudsman.',
    'body': '''
<h2>Can you go to the Ombudsman?</h2>
<ul class="ticks">
<li>You have first complained to the insurer in writing.</li>
<li>The insurer rejected the complaint, did not reply within a month, or you are not satisfied with its reply.</li>
<li>You file within one year of the insurer’s reply, or of the month passing without one.</li>
<li>The amount in dispute is up to ₹50 lakh.</li>
<li>The same dispute is not already before a court, consumer commission or arbitrator.</li>
</ul>

<h2>Which office to approach</h2>
<p>There are 17 Insurance Ombudsman offices across India. You can file with the office that covers the insurer’s branch you dealt with, or the one that covers where you live.</p>

<h2>How to file, step by step</h2>
<ol class="steps">
<li><strong>Keep your complaint to the insurer ready,</strong> with its reply or proof that a month has passed.</li>
<li><strong>Fill the complaint form.</strong> It is available on the Council for Insurance Ombudsmen website, cioins.co.in, where you can also file online.</li>
<li><strong>Attach your documents:</strong> the policy, claim papers, the rejection or settlement letter, your complaint to the insurer and its reply.</li>
<li><strong>State the relief you want,</strong> with the exact amount, and keep the acknowledgement.</li>
</ol>

<h2>What happens next</h2>
<ul class="ticks">
<li>The Ombudsman first tries to settle the dispute by mediation.</li>
<li>If that fails, it hears both sides, often online, and passes an award within three months of receiving everything it needs.</li>
<li>The award binds the insurer, which must comply within 30 days. It does not bind you: if you do not accept it, you can still go to a consumer commission or court.</li>
</ul>

<h2>How Mediclaimswala helps</h2>
<p>We prepare the complaint, attach the right evidence in order, and support you through the hearing. Filing with the Ombudsman is free, and you can do it yourself; we help people who want an experienced hand.</p>
''',
    'faq': [
        ('Is there a fee to complain to the Insurance Ombudsman?', 'No. Filing a complaint with the Insurance Ombudsman is free, and you do not need a lawyer.'),
        ('What is the time limit to approach the Ombudsman?', 'One year from the insurer’s reply to your complaint, or from the end of the month after you complained if the insurer did not reply.'),
        ('What is the maximum amount the Ombudsman can award?', 'The Ombudsman handles disputes up to ₹50 lakh.'),
        ('Can I go to the Ombudsman if my case is already in consumer court?', 'No. The Ombudsman will not hear a dispute that is already before a court, consumer commission or arbitrator.'),
    ],
    'related': ['claim-rejection', 'claim-short-settled', 'delay-in-claim-process'],
},
]
