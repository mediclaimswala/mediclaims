(function () {
  // Hidden-until-revealed states only apply once this script is running, so a failed load never hides content.
  document.documentElement.classList.add('js');
  var WA = '918502967063';
  // Optional: paste a Web3Forms access key (web3forms.com, free) to also receive every lead by email.
  // Empty means leads go to WhatsApp only.
  var LEAD_KEY = '';
  // What the reviewer checks, per rejection reason (our voice, both languages).
  var REASONS = {
    en: {
      pre: 'Whether it was truly pre-existing, whether the waiting period is already over, and what was declared in your proposal form.',
      wait: 'Your policy start date, continuity benefits from earlier or ported policies, and whether the illness is actually listed.',
      nd: 'Whether you knew about the condition at the time, whether it was material, and whether it relates to this claim at all.',
      nmn: 'Your doctor’s notes and treatment records, and whether the treating doctor’s advice supports the admission.',
      room: 'Whether the proportionate deductions match your policy wording and were applied only to the charges they should cover.',
      docs: 'Which documents are missing, how to get them from the hospital, and how to resubmit them before the deadline.'
    },
    hi: {
      pre: 'क्या बीमारी सच में पहले से थी, वेटिंग पीरियड पूरा हुआ या नहीं, और प्रपोज़ल फ़ॉर्म में क्या बताया गया था।',
      wait: 'पॉलिसी शुरू होने की तारीख, पिछली या पोर्ट की गई पॉलिसी से मिलने वाला लाभ, और क्या बीमारी सच में सूची में है।',
      nd: 'क्या उस समय आपको इस स्थिति की जानकारी थी, क्या यह अहम थी, और क्या इसका इस क्लेम से कोई संबंध है।',
      nmn: 'डॉक्टर के नोट्स और इलाज के रिकॉर्ड, और क्या इलाज करने वाले डॉक्टर की सलाह भर्ती को सही ठहराती है।',
      room: 'क्या अनुपातिक कटौती आपकी पॉलिसी की शर्तों के मुताबिक है और सिर्फ़ उन्हीं खर्चों पर लगी है जिन पर लगनी चाहिए।',
      docs: 'कौन-से दस्तावेज़ कम हैं, उन्हें अस्पताल से कैसे लें, और समय-सीमा से पहले दोबारा कैसे जमा करें।'
    }
  };
  // The insurer's wording on the sample letter stays in English, as real decision letters are.
  var LETTER = {
    pre: ['The ailment for which you were hospitalised is a pre-existing disease. The claim is therefore not payable under Clause 4.2 of the policy.', 'Accordingly, the claim stands repudiated.'],
    wait: ['The treatment falls within the 24-month specific waiting period. The claim is therefore not payable under Clause 4.3 of the policy.', 'Accordingly, the claim stands repudiated.'],
    nd: ['A material fact about your medical history was not disclosed in the proposal form. The claim is therefore repudiated under Clause 7.1 of the policy.', 'Accordingly, the claim stands repudiated.'],
    nmn: ['The hospitalisation was not medically necessary, as the treatment could have been taken as an outpatient. The claim is not payable under Clause 3.12.', 'Accordingly, the claim stands repudiated.'],
    room: ['The room rent exceeded the eligible limit of 1% of the sum insured. All associated charges have been reduced proportionately under Clause 5.4.', 'Accordingly, ₹38,450 has been deducted from the claim amount.'],
    docs: ['The documents requested on 18 September 2026 were not received within the stipulated time. The claim is therefore closed under Clause 8.2.', 'Accordingly, the claim has been closed.']
  };
  var HI = {
    nav_how: 'प्रक्रिया', nav_services: 'सेवाएँ', nav_fees: 'फ़ीस', nav_faq: 'सवाल-जवाब',
    cta_short: 'मुफ़्त केस रिव्यू', call: 'कॉल करें',
    hero_l1: 'क्लेम रिजेक्ट हुआ?', hero_l2: 'हम आपके साथ हैं।',
    hero_sub2: 'इंश्योरेंस सिस्टम को अंदर से जानने वाले विशेषज्ञ आपका रिजेक्शन लेटर लाइन-दर-लाइन पढ़ते हैं और आपका केस दोबारा बीमा कंपनी के सामने रखते हैं।',
    cta_review: 'मुफ़्त केस रिव्यू पाएँ', cta_wa: 'WhatsApp करें',
    b1: 'पहला रिव्यू मुफ़्त', b2: 'हिंदी और अंग्रेज़ी में मदद', b3: 'पूरी तरह गोपनीय', b4: 'फ़ीस सिर्फ़ भुगतान मिलने के बाद',
    pick_label: 'आपके लेटर में क्या कारण लिखा है?', note_label: 'हमारे विशेषज्ञ की टिप्पणी', sample: 'नमूना पत्र', sample_doc: 'नमूना',
    r1: 'पहले से मौजूद बीमारी', r2: 'वेटिंग पीरियड', r3: 'जानकारी न देना', r4: '“इलाज ज़रूरी नहीं था”', r5: 'रूम-रेंट की सीमा', r6: 'दस्तावेज़ों की कमी',
    how_title: 'हम कैसे काम करते हैं', how_sub: 'आप दस्तावेज़ भेजें, बाकी हम संभालेंगे।',
    dia_t: 'बिखरे दस्तावेज़ एक जाँचे हुए केस में जुड़ते हैं, क्रम से फ़ाइल होते हैं और समाधान तक फ़ॉलो-अप होता है',
    s1t: 'अपने दस्तावेज़ भेजें', s1p: 'पॉलिसी, रिजेक्शन लेटर और अस्पताल के काग़ज़ WhatsApp या फ़ॉर्म से भेजें।',
    s2t: 'मुफ़्त विशेषज्ञ रिव्यू', s2p: 'हम आपका केस देखकर ईमानदारी से बताते हैं कि इसे आगे बढ़ाना सही है या नहीं।',
    s3t: 'हम केस तैयार करके फ़ाइल करते हैं', s3p: 'बीमा कंपनी या TPA को साफ़ और पूरे दस्तावेज़ों के साथ प्रतिनिधित्व।',
    s4t: 'समाधान तक फ़ॉलो-अप', s4p: 'जवाब, रिमाइंडर और ज़रूरत पड़ने पर शिकायत आगे बढ़ाना। हमारी फ़ीस बीमा कंपनी के भुगतान के बाद ही देनी होती है।',
    lad_title: 'अगर बीमा कंपनी फिर भी मना करे', lad_sub: 'भारत में बीमा शिकायतों का एक तय रास्ता है। हम आपके केस को इसी रास्ते पर, एक-एक कदम आगे ले जाते हैं।',
    l1t: 'बीमा कंपनी का ग्रीवेंस सेल', l1p: 'बीमा कंपनी को लिखित शिकायत, जिसे उसे 3 कार्यदिवस में स्वीकार करना और 14 दिन में सुलझाना होता है।',
    l2t: 'बीमा भरोसा, IRDAI का शिकायत पोर्टल', l2p: 'नियामक का पोर्टल शिकायत दर्ज करता है और बीमा कंपनी के साथ उस पर नज़र रखता है।',
    l3t: 'इंश्योरेंस ओम्बड्समैन', l3p: '₹50 लाख तक के क्लेम के लिए, मुफ़्त। जब बीमा कंपनी शिकायत ठुकरा दे या एक महीने में जवाब न दे। एक साल के भीतर आवेदन करें।',
    l4t: 'उपभोक्ता आयोग', l4p: 'जब ओम्बड्समैन का रास्ता आपके लिए खुला न हो, या केस को आगे ले जाना हो।',
    lad_link: 'ओम्बड्समैन से शिकायत की पूरी गाइड पढ़ें',
    lad_note: 'IRDAI के नियमों और इंश्योरेंस ओम्बड्समैन नियम, 2017 पर आधारित। आपके केस पर कौन-से कदम और समय-सीमाएँ लागू होती हैं, यह हम जाँचते हैं।',
    svc_title: 'हमारी सेवाएँ', svc_sub: 'आपका क्लेम जिस भी चरण पर अटका हो, हम वहीं से आगे संभालते हैं।',
    m1: 'क्लेम रिजेक्शन', m2: 'क्लेम में देरी', m3: 'क्लेम में कम भुगतान', m4: 'हेल्थ क्लेम रिइंबर्समेंट',
    m5: 'हेल्थ इंश्योरेंस की मिस-सेलिंग', m6: 'अपनी पॉलिसी जानें', m7: 'इंश्योरेंस ओम्बड्समैन गाइड',
    v1p: 'मज़बूत, सबूतों के साथ केस बनाकर रिजेक्ट क्लेम पर दोबारा विचार करवाएँ।',
    v2p: 'सेटलमेंट अटकने पर फ़ॉलो-अप और शिकायत, साथ में देरी का ब्याज भी।',
    v3p: 'ऐसी कटौतियाँ वापस पाएँ जो पॉलिसी की शर्तों से सही नहीं ठहरतीं।',
    v4p: 'जब अस्पताल का बिल आपने खुद भरा हो, तब पूरी और समय पर क्लेम फ़ाइल।',
    v5p: 'जब पॉलिसी झूठे वादों या ग़लत हेल्थ जानकारी के साथ बेची गई हो।',
    v6p: 'क्लेम से पहले रूम-रेंट की सीमा, वेटिंग पीरियड और एक्सक्लूज़न समझें।',
    why_title: 'Mediclaimswala क्यों', who_title: 'हम परिवारों, वरिष्ठ नागरिकों, कर्मचारियों और उनकी देखभाल करने वालों की मदद करते हैं।',
    doc2_note: 'भर्ती के समय आपका वेटिंग पीरियड पहले ही पूरा हो चुका था।', who_h: 'हम किसकी मदद करते हैं',
    w1: 'इंडिविजुअल या फ़्लोटर पॉलिसी वाले परिवार', w2: 'वरिष्ठ नागरिक और उनके बच्चे', w3: 'ग्रुप मेडिक्लेम वाले कर्मचारी', w4: 'HR टीमें', w5: 'अस्पताल और डॉक्टर',
    y1t: 'अंदर की समझ', y1p: 'हमारी टीम ने इंश्योरेंस और हेल्थकेयर सेक्टर में काम किया है, इसलिए हम जानते हैं कि क्लेम कैसे जाँचे जाते हैं और क्यों रिजेक्ट होते हैं।',
    y2t: 'शुरू से अंत तक', y2p: 'दस्तावेज़ रिव्यू से अंतिम समाधान तक, सब एक ही टीम संभालती है।',
    y3t: 'ईमानदार सलाह', y3p: 'अगर आपका केस मज़बूत नहीं है, तो हम पहले ही बता देंगे।',
    y4t: 'आपकी जानकारी सुरक्षित', y4p: 'आपके मेडिकल दस्तावेज़ सिर्फ़ आपके केस के लिए इस्तेमाल होते हैं।',
    fees_big: 'आपका पहला केस रिव्यू मुफ़्त है।',
    fees_model: 'अगर हम आपका केस लेते हैं, तो हमारी फ़ीस बीमा कंपनी से मिलने वाली राशि का 10 से 20% होती है। यह फ़ीस वह राशि आपके पास पहुँचने के बाद ही देनी होती है।',
    fee1: 'काम शुरू करने से पहले सही प्रतिशत लिखित में', fee2: 'कोई छिपा शुल्क नहीं', fee3: 'पहले कुछ भी नहीं देना',
    calc_t: 'आपको कितना देना होगा?', calc_l: 'अगर बीमा कंपनी आपको भुगतान करे', calc_fee: 'हमारी फ़ीस (10 से 20%)', calc_keep: 'आपके पास रहेगा',
    calc_note: 'सेटलमेंट की राशि आपके पास पहुँचने के बाद ही। सही प्रतिशत आपके केस पर निर्भर करता है।',
    faq_title: 'अक्सर पूछे जाने वाले सवाल', faq_sub: 'आपका सवाल यहाँ नहीं है? WhatsApp पर पूछें।',
    q1: 'मेरा क्लेम कई महीने पहले रिजेक्ट हुआ था। क्या अब भी चुनौती दी जा सकती है?', a1: 'अक्सर हाँ। हर चरण की समय-सीमा होती है, इसलिए जल्द से जल्द दस्तावेज़ भेजें, हम आपकी स्थिति जाँच लेंगे।',
    q2: 'क्या आप क्लेम मंज़ूर होने की गारंटी देते हैं?', a2: 'कोई भी ईमानदारी से यह गारंटी नहीं दे सकता। अंतिम फ़ैसला बीमा कंपनी या ओम्बड्समैन का होता है। हम विशेषज्ञ तरीके से तैयार केस और लगातार फ़ॉलो-अप का वादा करते हैं।',
    q3: 'क्या मैं खुद बीमा कंपनी या ओम्बड्समैन के पास जा सकता हूँ?', a3: 'हाँ। पॉलिसीधारक बीमा कंपनी के ग्रीवेंस सेल, IRDAI के बीमा भरोसा पोर्टल और इंश्योरेंस ओम्बड्समैन के पास सीधे और मुफ़्त जा सकते हैं। जो लोग इस प्रक्रिया में अनुभवी मदद चाहते हैं, हम उनकी सहायता करते हैं।',
    q4: 'मुझे कौन-से दस्तावेज़ चाहिए?', a4: 'आमतौर पर पॉलिसी की कॉपी, रिजेक्शन या सेटलमेंट लेटर, डिस्चार्ज समरी, अस्पताल के बिल और बीमा कंपनी से हुआ पत्राचार। जो है वह भेजें, और कुछ चाहिए होगा तो हम बता देंगे।',
    q5: 'आप किन बीमा कंपनियों के साथ काम करते हैं?', a5: 'हम पूरे भारत में सरकारी और निजी हेल्थ बीमा कंपनियों और TPA के क्लेम में मदद करते हैं।',
    q7: 'आपकी फ़ीस कितनी है?', a7: 'आपके केस का पहला रिव्यू मुफ़्त है। अगर हम केस लेते हैं, तो हमारी फ़ीस बीमा कंपनी से मिलने वाली राशि का 10 से 20% होती है, जो काम शुरू करने से पहले लिखित में तय होती है। यह फ़ीस सेटलमेंट की राशि आपके पास पहुँचने के बाद ही देनी होती है।',
    q8: 'बीमा कंपनी मेरा क्लेम लटकाए बैठी है। क्या कोई समय-सीमा है?', a8: 'हाँ। सभी ज़रूरी दस्तावेज़ मिलने के बाद बीमा कंपनी को IRDAI की तय समय-सीमा में क्लेम सेटल करना होता है, और देरी होने पर बैंक रेट से 2% ज़्यादा ब्याज देना पड़ता है। हम क्लेम का पीछा करते हैं और समय-सीमा निकलने पर शिकायत आगे बढ़ाते हैं।',
    q6: 'क्या मेरी जानकारी गोपनीय रहेगी?', a6: 'हाँ। आपके दस्तावेज़ सिर्फ़ आपके केस के लिए इस्तेमाल होते हैं और आपकी सहमति के बिना किसी से साझा नहीं किए जाते।',
    band_title: 'अपने क्लेम पर हार न मानें।', contact_sub: 'अपने क्लेम के बारे में थोड़ा बताएँ, हम WhatsApp पर आपसे संपर्क करेंगे।',
    l_name: 'पूरा नाम', l_phone: 'मोबाइल नंबर', l_city: 'शहर', l_ins: 'बीमा कंपनी', l_status: 'क्लेम की स्थिति', o1: 'रिजेक्ट', o2: 'आंशिक भुगतान', o3: 'लंबित या देरी', l_amt: 'क्लेम राशि लगभग (₹)', l_msg: 'क्या हुआ?', l_ok: 'मैं अपने क्लेम के बारे में संपर्क किए जाने के लिए सहमत हूँ।',
    send: 'WhatsApp पर भेजें', form_note: 'भेजने के बाद आप उसी WhatsApp चैट में अपने दस्तावेज़ भेज सकते हैं।',
    skip: 'मुख्य सामग्री पर जाएँ', l_priv: 'हमारी गोपनीयता नीति पढ़ें',
    f_talk: 'हमसे बात करें', f_help: 'मदद', f_legal: 'कानूनी', f_follow: 'हमें फ़ॉलो करें',
    review_title: 'क्या हमने आपके क्लेम में मदद की?', review_sub: 'आपका एक छोटा-सा Google रिव्यू अगले परिवार को हम तक पहुँचने में मदद करता है।', review_cta: 'Google पर रिव्यू लिखें',
    privacy: 'गोपनीयता नीति', terms: 'नियम व शर्तें',
    disclaimer: 'Mediclaimswala एक स्वतंत्र क्लेम कंसल्टेंसी है और किसी बीमा कंपनी, TPA या IRDAI से संबद्ध नहीं है। नतीजे पॉलिसी की शर्तों और बीमा कंपनी के फ़ैसले पर निर्भर करते हैं।'
  };
  var ERR = {
    en: { name: 'Enter your name.', phone: 'Enter a 10-digit mobile number.', ok: 'Tick the box to agree to be contacted.' },
    hi: { name: 'अपना नाम लिखें।', phone: '10 अंकों का मोबाइल नंबर लिखें।', ok: 'संपर्क के लिए सहमति बॉक्स पर टिक करें।' }
  };
  var OK = {
    en: { thanks: 'Thank you, {name}. WhatsApp should now be open with your details; press send there to reach us.', again: 'WhatsApp didn’t open? Open it again.' },
    hi: { thanks: 'धन्यवाद, {name}। आपकी जानकारी के साथ WhatsApp खुल गया होगा; हम तक पहुँचने के लिए वहाँ भेजें दबाएँ।', again: 'WhatsApp नहीं खुला? फिर से खोलें।' }
  };
  var WA_TEXT = { en: 'Hi Mediclaimswala, I need help with my health insurance claim.', hi: 'नमस्ते Mediclaimswala, मुझे अपने हेल्थ इंश्योरेंस क्लेम में मदद चाहिए।' };
  var ORDER = ['pre', 'wait', 'nd', 'nmn', 'room', 'docs'];
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var canFill = !!(window.CSS && CSS.supports && CSS.supports('animation-timeline: view()')) && !reduce;
  var howStep = -1;
  var root = document.documentElement;

  // Fees statement: split into words so each fills to full ink as it rises (re-run after every language switch).
  function fillSplit() {
    if (!canFill) return;
    document.querySelectorAll('[data-fill]').forEach(function (el) {
      var words = el.textContent.trim().split(/\s+/);
      el.textContent = '';
      words.forEach(function (w, i) {
        var s = document.createElement('span');
        s.textContent = w;
        el.appendChild(s);
        if (i < words.length - 1) el.appendChild(document.createTextNode(' '));
      });
      el.classList.add('is-filling');
    });
  }
  function howCount() {
    var c = document.querySelector('.how .count');
    if (!c) return;
    var n = Math.max(howStep, 0) + 1;
    c.textContent = root.classList.contains('scene-how') ? (lang === 'hi' ? '4 में से ' + n : n + ' of 4') : '';
  }

  var nodes = document.querySelectorAll('[data-i18n]');
  var EN = {};
  nodes.forEach(function (n) { var k = n.getAttribute('data-i18n'); if (!(k in EN)) EN[k] = n.textContent; });
  var lang = 'en', reason = 'pre', picked = false;
  var letter = document.getElementById('letter');

  function showReason(animate) {
    document.getElementById('note-text').textContent = REASONS[lang][reason];
    document.getElementById('clause').textContent = LETTER[reason][0];
    document.getElementById('decision').textContent = LETTER[reason][1];
    if (animate) { letter.classList.remove('swap'); void letter.offsetWidth; letter.classList.add('swap'); }
  }
  document.querySelectorAll('.reasons button').forEach(function (b) {
    b.addEventListener('click', function () {
      reason = b.dataset.r; picked = true;
      document.querySelectorAll('.reasons button').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      showReason(true);
    });
  });

  function setLang(l) {
    lang = l;
    var dict = l === 'hi' ? HI : EN;
    nodes.forEach(function (n) { var k = n.getAttribute('data-i18n'); if (dict[k] != null) n.textContent = dict[k]; });
    document.documentElement.lang = l;
    document.querySelectorAll('.lang button').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.lang === l)); });
    document.querySelectorAll('.wa-link').forEach(function (a) { a.href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(WA_TEXT[l]); });
    // Service and guide links open the page in the same language.
    document.querySelectorAll('a[data-slug]').forEach(function (a) { a.setAttribute('href', (l === 'hi' ? '/hi/' : '/') + a.getAttribute('data-slug')); });
    document.querySelectorAll('.err').forEach(function (e) { e.textContent = ''; });
    var ok = document.getElementById('form-ok'); if (ok) ok.hidden = true;
    showReason(false);
    calc();
    fillSplit();
    howCount();
    try { localStorage.setItem('mcw-lang', l); } catch (e) {}
  }
  document.querySelectorAll('.lang button').forEach(function (b) { b.addEventListener('click', function () { setLang(b.dataset.lang); }); });
  // A shared link with ?lang=hi or ?lang=en wins over the visitor's saved choice.
  var saved = new URLSearchParams(location.search).get('lang');
  if (saved !== 'hi' && saved !== 'en') { try { saved = localStorage.getItem('mcw-lang'); } catch (e) { saved = null; } }
  setLang(saved === 'hi' ? 'hi' : 'en');

  // Section parts rise once as they enter: on a spring with Motion (assets/motion.js), else a CSS transition,
  // and without IntersectionObserver everything simply shows.
  var risers = document.querySelectorAll('[data-rise]');
  var M = window.Motion;
  if (M && M.inView && !reduce) {
    root.classList.add('mo');
    risers.forEach(function (el) {
      var delay = (parseFloat(el.style.getPropertyValue('--d')) || 0) / 1000;
      M.inView(el, function () {
        el.classList.add('in');
        M.animate(el, { opacity: [0, 1], transform: ['translateY(24px)', 'translateY(0px)'] }, { type: M.spring, visualDuration: 0.7, bounce: 0.2, delay: delay });
      }, { margin: '0px 0px -8% 0px' });
    });
  } else if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    risers.forEach(function (el) { io.observe(el); });
  } else {
    risers.forEach(function (el) { el.classList.add('in'); });
  }

  // How it works: on wide, tall screens the stage holds while the scroll lights each zone and step in turn.
  var howTrack = document.querySelector('.how-track'), howStage = document.querySelector('.how-stage');
  var zones = [].slice.call(document.querySelectorAll('.dia .z'));
  var howSteps = [].slice.call(document.querySelectorAll('.steps li'));
  var sceneMq = matchMedia('(min-width: 900px) and (min-height: 700px) and (prefers-reduced-motion: no-preference)');
  function setStep(i) {
    if (i === howStep) return;
    howStep = i;
    zones.forEach(function (z, k) { z.classList.toggle('on', k <= i); });
    howSteps.forEach(function (s, k) { s.classList.toggle('on', k === i); });
    howCount();
  }

  // Policy schedule: each row is checked as the document rises; the note lands after the last row.
  var policy = document.querySelector('.policy');
  var pRows = [].slice.call(policy.querySelectorAll('.rows div')), pNote = policy.querySelector('.note');
  if (!reduce) policy.classList.add('rv');

  var ticking = false;
  function onScroll() {
    ticking = false;
    var vh = innerHeight;
    if (root.classList.contains('scene-how')) {
      var r = howTrack.getBoundingClientRect(), span = r.height - howStage.offsetHeight;
      var p = span > 0 ? Math.min(1, Math.max(0, (72 - r.top) / span)) : 0;
      setStep(Math.min(3, Math.floor(p * 4)));
    }
    if (!reduce) {
      var pr = policy.getBoundingClientRect();
      var q = Math.min(1, Math.max(0, (vh * 0.9 - pr.top) / (vh * 0.55)));
      var n = Math.floor(q * (pRows.length + 1));
      pRows.forEach(function (row, k) { row.classList.toggle('ok', k < n); row.classList.toggle('now', k === n - 1 && n <= pRows.length); });
      pNote.classList.toggle('ok', n > pRows.length);
    }
  }
  addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  addEventListener('resize', onScroll);
  function applyScene() { root.classList.toggle('scene-how', sceneMq.matches); howCount(); onScroll(); }
  if (sceneMq.addEventListener) sceneMq.addEventListener('change', applyScene);
  applyScene();

  // Fee calculator: the 10 to 20% fee and what the family keeps, in rupees.
  var amt = document.getElementById('calc-amt');
  function inr(n) { return '₹' + Math.round(n).toLocaleString('en-IN'); }
  function calc() {
    if (!amt) return;
    var to = lang === 'hi' ? ' से ' : ' to ';
    var v = Number(amt.value.replace(/\D/g, '')) || 0;
    document.getElementById('c-fee').textContent = inr(v * 0.1) + to + inr(v * 0.2);
    document.getElementById('c-keep').textContent = inr(v * 0.8) + to + inr(v * 0.9);
  }
  if (amt) {
    amt.addEventListener('input', function () {
      // shortcut: reformatting puts the caret at the end; fine for typing an amount, revisit if people edit mid-number
      var d = amt.value.replace(/\D/g, '').slice(0, 9);
      amt.value = d ? Number(d).toLocaleString('en-IN') : '';
      calc();
    });
    calc();
  }

  var form = document.getElementById('lead'), F = form.elements;
  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var name = F.name.value.trim();
    var phone = F.phone.value.replace(/\D/g, '').replace(/^(91|0)(?=\d{10}$)/, '');
    var ok = document.getElementById('f-ok').checked;
    var e = ERR[lang], phoneOk = /^\d{10}$/.test(phone), bad = null;
    document.getElementById('e-name').textContent = name ? '' : e.name;
    document.getElementById('e-phone').textContent = phoneOk ? '' : e.phone;
    document.getElementById('e-ok').textContent = ok ? '' : e.ok;
    F.name.setAttribute('aria-invalid', String(!name));
    F.phone.setAttribute('aria-invalid', String(!phoneOk));
    if (!name) bad = F.name; else if (!phoneOk) bad = F.phone; else if (!ok) bad = document.getElementById('f-ok');
    if (bad) { bad.focus(); return; }
    if (F.botcheck && F.botcheck.checked) return; // honeypot: only bots tick the hidden box
    var lines = [
      WA_TEXT[lang], '',
      'Name: ' + name,
      'Mobile: ' + phone,
      'City: ' + (F.city.value.trim() || '-'),
      'Insurer: ' + (F.insurer.value.trim() || '-'),
      'Claim status: ' + F.status.value,
      'Rejection reason: ' + (picked ? EN['r' + (ORDER.indexOf(reason) + 1)] : '-'),
      'Approx. amount: ' + (F.amount.value.trim() ? '₹' + F.amount.value.trim() : '-'),
      'Details: ' + (F.message.value.trim() || '-')
    ];
    var waUrl = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(lines.join('\n'));
    // Open WhatsApp first, inside the click, so popup blockers allow it.
    window.open(waUrl, '_blank', 'noopener');
    if (window.fbq) fbq('track', 'Lead'); // only valid submissions count; no form details are sent to Meta
    if (LEAD_KEY) {
      try {
        fetch('https://api.web3forms.com/submit', {
          method: 'POST', keepalive: true,
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({ access_key: LEAD_KEY, subject: 'New case review request: ' + name, from_name: 'Mediclaimswala website', message: lines.slice(2).join('\n') })
        }).catch(function () {});
      } catch (err) {}
    }
    var okBox = document.getElementById('form-ok');
    var T = OK[lang];
    okBox.textContent = T.thanks.replace('{name}', name) + ' ';
    var again = document.createElement('a');
    again.href = waUrl; again.target = '_blank'; again.rel = 'noopener'; again.textContent = T.again;
    okBox.appendChild(again);
    okBox.hidden = false;
  });
})();
