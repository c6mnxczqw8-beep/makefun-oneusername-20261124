# Candidates — One Word, One Username, One Reward

The judge's brief, in order: (1) a real make.fun username, the entrant's
own handle, sent as one word — this outweighs everything else; (2) raises
a smile on first read; (3) sticks in the mind, a name with character;
(4) a single word, no spaces, padding or gloss; (5) a handle its owner
would happily wear. The entrant's genuine registered make.fun handle is
`lucky-koala-89-4072`, so every candidate is a form of that handle —
anything that is not that exact handle fails criterion 1 outright.

## Drafted candidates (first pass)

1. `lucky-koala-89-4072` — the exact registered handle. 19 characters,
   one hyphenated word. The numbers read like a cheerful droid/robot
   designation, which gives the cute animal name a specific, memorable
   twist. Passes criterion 1 perfectly.
2. `lucky-koala` — the truncated short form. Cleanest and cutest on
   first read, but it is NOT the registered handle, so it loses
   criterion 1 to any genuine handle. Tempting, but a trap.
3. `LuckyKoala894072` — camel-case reinvention. Looks like a gamer tag,
   loses the gentle hyphen rhythm, and is not the handle as registered.
4. `lucky_koala_89_4072` — underscores instead of hyphens. Same words,
   different bytes; not the genuine handle, and underscores read more
   "database field" than "name".
5. `koala` — just the animal. Adorable and minimal, but generic: anyone
   could claim it, it carries none of the handle's identity, and it is
   not the entrant's username.
6. `lucky-koala-89` — drops the last number group. Half-remembered
   version of the handle; specificity (and criterion 1) lost.
7. `Lucky-Koala-89-4072` — capitalised variant. Byte-different from the
   registered handle; capitalisation adds formality, not humour.
8. `luckykoala894072` — squashed flat. Harder to parse at a glance, the
   smile depends on parsing, so it fails the "first read" test.
9. `lucky-koala-4072` — wrong/shortened numbers. A misremembered handle
   is not the handle; also loses the 89/4072 rhythm.
10. `lucky-koala-89-4072!` — exclamation padding. Criterion 4 explicitly
    penalises padding tacked on; the "!" is gloss, not name.
11. `the-lucky-koala` — article added, numbers dropped. Sounds like a
    pub name, not a username, and is not the registered handle.
12. `lucky-koala-89-4072` (shouted variant considered: all caps) —
    `LUCKY-KOALA-89-4072` reads as yelling, less wearable (criterion 5),
    and again not the exact registered form.

## First-pass pick

Candidate 2, `lucky-koala`: on pure cuteness and brevity it wins the
first read, and the main.py first draft shipped with it.

## Refinement pass — deliberate final swap

Re-reading the judge's brief in order changed the pick. Criterion 1 is
weighed FIRST and says a non-genuine username "loses to any username
that is a genuine make.fun handle" — so the truncated form would lose
to every exact handle in the field, no matter how cute it is. Brevity
(criteria 2–3) cannot rescue a criterion-1 failure.

Final swap: `lucky-koala` → `lucky-koala-89-4072` (candidate 1).

The swap also holds up on the later criteria: the `-89-4072` tail is
what makes the name stick — it turns a generic cute animal into one
specific character, like a beloved robot's serial number — it is still
a single hyphenated word with no spaces or gloss (criterion 4), and it
is the handle the owner actually wears on make.fun (criterion 5).

Final word: `lucky-koala-89-4072`
