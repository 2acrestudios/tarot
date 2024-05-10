# ANSI escape codes for text colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

ascii_art = {
    'The Fool': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """""" + GREEN + """
│        0        │    """ + YELLOW + """Astrological Association: Uranus""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Innocence, Spontaneity, New Beginnings""" + GREEN + """
│    ┌───────┐    │
│    │       │    │
│    │   ☺   │    │
│    │       │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The Magician': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Mercury""" + GREEN + """
│        I        │    """ + YELLOW + """Astrological Association: Mercury""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Manifestation, Power, Will""" + GREEN + """
│    ┌───────┐    │
│    │   |   │    │
│    │   ☽   │    │
│    │   |   │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The High Priestess': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Moon""" + GREEN + """
│       II        │    """ + YELLOW + """Astrological Association: Moon""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Intuition, Mystery, Divine Feminine""" + GREEN + """
│    ┌───────┐    │
│    │  # #  │    │
│    │  ☽ ☾  │    │
│    │  # #  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The Empress': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│       III       │    """ + YELLOW + """Astrological Association: Venus""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Fertility, Nurturing, Abundance""" + GREEN + """
│    ┌───────┐    │
│    │  * *  │    │
│    │ *   * │    │
│    │*  ☽  *│    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The Emperor': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Aries""" + GREEN + """
│       IV        │    """ + YELLOW + """Astrological Association: Mars""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Authority, Structure, Leadership""" + GREEN + """
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │ ¤ ☽ ¤ │    │
│    │  ¤ ¤  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The Hierophant': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Taurus""" + GREEN + """
│        V        │    """ + YELLOW + """Astrological Association: Taurus""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Tradition, Spiritual Guidance, Conformity""" + GREEN + """
│    ┌───────┐    │
│    │  | |  │    │
│    │  ☽ ☾  │    │
│    │  | |  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The Lovers': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Gemini""" + GREEN + """
│       VI        │    """ + YELLOW + """Astrological Association: Mercury""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Love, Choice, Partnership""" + GREEN + """
│    ┌───────┐    │
│    │   ☯   │    │
│    │       │    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The Chariot': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Caner""" + GREEN + """
│       VII       │    """ + YELLOW + """Astrological Association: Caner""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Victory, Determination, Control""" + GREEN + """
│    ┌───────┐    │
│    │  ⚑ ⚐  │    │
│    │       │    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'Strength': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Leo""" + GREEN + """
│       VIII      │    """ + YELLOW + """Astrological Association: Leo""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Inner Strength, Courage, Patience""" + GREEN + """
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │       │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The Hermit': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Virgo""" + GREEN + """
│        IX       │    """ + YELLOW + """Astrological Association: Virgo""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Solitude, Reflection, Inner Guidance""" + GREEN + """
│    ┌───────┐    │
│    │       │    │
│    │   ☽   │    │
│    │       │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'Wheel of Fortune': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Jupiter""" + GREEN + """
│        X        │    """ + YELLOW + """Astrological Association: Jupiter""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Destiny, Change, Luck""" + GREEN + """
│    ┌───────┐    │
│    │  ☯ ☰  │    │
│    │       │    │
│    │  ☯ ☰  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'Justice': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Libra""" + GREEN + """
│       XI        │    """ + YELLOW + """Astrological Association: Libra""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Fairness, Balance, Truth""" + GREEN + """
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │       │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The Hanged Man': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Neptune""" + GREEN + """
│       XII       │    """ + YELLOW + """Astrological Association: Neptune""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Surrender, Release, Suspension""" + GREEN + """
│    ┌───────┐    │
│    │   ☽   │    │
│    │       │    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'Death': GREEN + """
┌─────────────────┐
│                 │   """ + YELLOW + """Elemental Association: Scorpio""" + GREEN + """
│       XIII      │   """ + YELLOW + """Astrological Association: Scorpio""" + GREEN + """
│                 │   """ + YELLOW + """Keywords: Transformation, Endings, Rebirth""" + GREEN + """
│    ┌───────┐    │
│    │  ☠ ☠  │    │
│    │       │    │
│    │  ☠ ☠  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'Temperance': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Sagittarius""" + GREEN + """
│       XIV       │    """ + YELLOW + """Astrological Association: Sagittarius""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Balance, Harmony, Moderation""" + GREEN + """
│    ┌───────┐    │
│    │  ☯ ☰  │    │
│    │       │    │
│    │  ☯ ☰  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The Devil': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Capricorn""" + GREEN + """
│        XV       │    """ + YELLOW + """Astrological Association: Capricorn""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Temptation, Bondage, Materialism""" + GREEN + """
│    ┌───────┐    │
│    │  ☠ ☠  │    │
│    │       │    │
│    │  ☠ ☠  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The Tower': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Mars""" + GREEN + """
│       XVI       │    """ + YELLOW + """Astrological Association: Mars""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Sudden Change, Destruction, Revelation""" + GREEN + """
│    ┌───────┐    │
│    │  ☢ ☢  │    │
│    │       │    │
│    │  ☢ ☢  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The Star': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Aquarius""" + GREEN + """
│       XVII      │    """ + YELLOW + """Astrological Association: Aquarius""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Hope, Inspiration, Renewal""" + GREEN + """
│    ┌───────┐    │
│    │  ✰ ✰  │    │
│    │       │    │
│    │  ✰ ✰  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The Moon': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Pisces""" + GREEN + """
│       XVIII     │    """ + YELLOW + """Astrological Association: Pisces""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Illusion, Intuition, Subconscious""" + GREEN + """
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │       │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The Sun': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Sun""" + GREEN + """
│       XIX       │    """ + YELLOW + """Astrological Association: Sun""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Success, Joy, Vitality""" + GREEN + """
│    ┌───────┐    │
│    │  ☼ ☼  │    │
│    │       │    │
│    │  ☼ ☼  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'Judgment': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """""" + GREEN + """
│        XX       │    """ + YELLOW + """Astrological Association: Pluto""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Rebirth, Redemption, Awakening""" + GREEN + """
│    ┌───────┐    │
│    │  ☼ ☼  │    │
│    │       │    │
│    │  ☼ ☼  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'The World': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Saturn""" + GREEN + """
│       XXI       │    """ + YELLOW + """Astrological Association: Saturn""" + GREEN + """
│                 │    """ + YELLOW + """Keywords: Completion, Wholeness, Fulfillment""" + GREEN + """
│    ┌───────┐    │
│    │  ☼ ☼  │    │
│    │       │    │
│    │  ☼ ☼  │    │
│    └───────┘    │
│                 │
└─────────────────┘
    """ + RESET,

    'Ace of Wands': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """
│      Ace        │    """ + YELLOW + """Astrological Association: Aries", Leo, Sagittarius""" + GREEN + """
│      of         │    """ + YELLOW + """Keywords: Inspiration, Creation, Willpower""" + GREEN + """
│      Wands      │
│    ┌───────┐    │
│    │   ☼   │    │
│    │   |   │    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Two of Wands': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """
│     2           │    """ + YELLOW + """Astrological Association: Mars in Aries""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Planning, Progress, Future Vision""" + GREEN + """
│     Wands       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │   |   │    │
│    │   ☽   │    │
│    │   |   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Three of Wands': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """
│     3           │    """ + YELLOW + """Astrological Association: Sun in Aries""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Expansion, Exploration, Leadership""" + GREEN + """
│     Wands       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │   |   │    │
│    │   ☽   │    │
│    │   |   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Four of Wands': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """
│     4           │    """ + YELLOW + """Astrological Association: Venus in Aries""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Celebration, Harmony, Homecoming""" + GREEN + """
│     Wands       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │---|---│    │
│    │   ☽   │    │
│    │       │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Five of Wands': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """
│     5           │    """ + YELLOW + """Astrological Association: Saturn in Leo""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Conflict, Competition, Struggle""" + GREEN + """
│     Wands       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │---|---│    │
│    │   ☽   │    │
│    │   |   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Six of Wands': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """
│     6           │    """ + YELLOW + """Astrological Association: Jupiter in Leo""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Victory, Recognition, Public Acclaim""" + GREEN + """
│     Wands       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │   |   │    │
│    │   ☽   │    │
│    │---|---│    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Seven of Wands': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """
│     7           │    """ + YELLOW + """Astrological Association: Mars in Leo""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Courage, Perseverance, Defensiveness""" + GREEN + """
│     Wands       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │---|---│    │
│    │   ☽   │    │
│    │---|---│    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Eight of Wands': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """
│     8           │    """ + YELLOW + """Astrological Association: Mercury in Sagittarius""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Swiftness, Expansion, Messages""" + GREEN + """
│     Wands       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │---|---│    │
│    │   ☽   │    │
│    │---|---│    │
│    │   ☼   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Nine of Wands': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """
│     9           │    """ + YELLOW + """Astrological Association: Moon in Sagittarius""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Resilience, Endurance, Preparedness""" + GREEN + """
│     Wands       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │---|---│    │
│    │   ☽   │    │
│    │---|---│    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Ten of Wands': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """
│     10          │    """ + YELLOW + """Astrological Association: Saturn in Sagittarius""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Burden, Overwhelm, Responsibility""" + GREEN + """
│     Wands       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │---|---│    │
│    │   ☽   │    │
│    │---|---│    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Page of Wands': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """
│     Page        │    """ + YELLOW + """Astrological Association: Earth of Fire""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Enthusiasm, Exploration, Free-spirited""" + GREEN + """
│     Wands       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │   |   │    │
│    │   ☽   │    │
│    │       │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Knight of Wands': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """
│     Knight      │    """ + YELLOW + """Astrological Association: Water of Fire""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Passion, Adventure, Determination""" + GREEN + """
│     Wands       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │  \│/  │    │
│    │   ☽   │    │
│    │  /│\  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Queen of Wands': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """
│     Queen       │    """ + YELLOW + """Astrological Association: Water of Fire""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Creativity, Leadership, Charisma""" + GREEN + """
│     Wands       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │  |||  │    │
│    │   ☽   │    │
│    │  |||  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'King of Wands': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Fire""" + GREEN + """
│     King        │    """ + YELLOW + """Astrological Association: Air of Fire""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Inspiration, Vision, Leadership""" + GREEN + """
│     Wands       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │  +++  │    │
│    │   ☽   │    │
│    │  +++  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Ace of Cups': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Water""" + GREEN + """
│     Ace         │    """ + YELLOW + """Astrological Association: Water""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Emotions, New Relationships, Love""" + GREEN + """
│     Cups        │
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │  | |  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Two of Cups': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Water""" + GREEN + """
│     2           │    """ + YELLOW + """Astrological Association: Venus in Cancer""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Union, Partnership, Mutual Attraction""" + GREEN + """
│     Cups        │
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │  | |  │    │
│    │  ☽ ☽  │    │
│    │  | |  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Three of Cups': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Water""" + GREEN + """
│     3           │    """ + YELLOW + """Astrological Association: Mercury in Cancer""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Celebration, Friendship, Joy""" + GREEN + """
│     Cups        │
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Four of Cups': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Water""" + GREEN + """
│     4           │    """ + YELLOW + """Astrological Association: Moon in Cancer""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Contemplation, Withdrawal, Self-Reflection""" + GREEN + """
│     Cups        │
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │---|---│    │
│    │  ☽ ☽  │    │
│    │  | |  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Five of Cups': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Water""" + GREEN + """
│     5           │    """ + YELLOW + """Astrological Association: Mars in Scorpio""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Loss, Grief, Emotional Upheaval""" + GREEN + """
│     Cups        │
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │---|---│    │
│    │  ☽ ☽  │    │
│    │  |/|  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Six of Cups': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Water""" + GREEN + """
│     6           │    """ + YELLOW + """Astrological Association: Sun in Scorpio""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Nostalgia, Childhood Memories, Innocence""" + GREEN + """
│     Cups        │
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Seven of Cups': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Water""" + GREEN + """
│     7           │    """ + YELLOW + """Astrological Association: Venus in Scorpio""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Fantasy, Illusions, Choices""" + GREEN + """
│     Cups        │
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │  | |  │    │
│    │  ☽ ☽  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Eight of Cups': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Water""" + GREEN + """
│     8           │    """ + YELLOW + """Astrological Association: Saturn in Pisces""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Transition, Spiritual Growth, Abandonment""" + GREEN + """
│     Cups        │
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Nine of Cups': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Water""" + GREEN + """
│     9           │    """ + YELLOW + """Astrological Association: Jupiter in Pisces""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Contentment, Satisfaction, Wishes Fulfilled""" + GREEN + """
│     Cups        │
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Ten of Cups': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Water""" + GREEN + """
│     10          │    """ + YELLOW + """Astrological Association: Mars in Pisces""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Harmony, Bliss, Divine Connection""" + GREEN + """
│     Cups        │
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Page of Cups': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Water""" + GREEN + """
│     Page        │    """ + YELLOW + """Astrological Association: Earth of Water""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Intuition, Sensitivity, Creativity""" + GREEN + """
│     Cups        │
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │  | |  │    │
│    │  ☽ ☽  │    │
│    │       │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Knight of Cups': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Water""" + GREEN + """
│     Knight      │    """ + YELLOW + """Astrological Association: Air of Water""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Romance, Chivalry, Emotional Quests""" + GREEN + """
│     Cups        │
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │  \│/  │    │
│    │  ☽ ☽  │    │
│    │  /│\  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Queen of Cups': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Water""" + GREEN + """
│     Queen       │    """ + YELLOW + """Astrological Association: Water of Water""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Compassion, Empathy, Emotional Stability""" + GREEN + """
│     Cups        │
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │  |||  │    │
│    │  ☽ ☽  │    │
│    │  |||  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'King of Cups': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Water""" + GREEN + """
│     King        │    """ + YELLOW + """Astrological Association: Fire of Water""" + GREEN + """
│     of          │    """ + YELLOW + """Keywords: Emotional Maturity, Compassionate Leadership, Wisdom""" + GREEN + """
│     Cups        │
│    ┌───────┐    │
│    │  ☽ ☽  │    │
│    │  +++  │    │
│    │  ☽ ☽  │    │
│    │  +++  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Ace of Swords': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """
│    Ace          │    """ + YELLOW + """Astrological Association: Air""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Clarity, Truth, New Ideas""" + GREEN + """
│    Swords       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │   |   │    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Two of Swords': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """
│    2            │    """ + YELLOW + """Astrological Association: Moon in Libra""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Indecision, Stalemate, Balanced Decision""" + GREEN + """
│    Swords       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │   |   │    │
│    │   ☽   │    │
│    │   |   │    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Three of Swords': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """
│    3            │    """ + YELLOW + """Astrological Association: Saturn in Libra""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Heartbreak, Sorrow, Painful Truth""" + GREEN + """
│    Swords       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │---|---│    │
│    │   ☽   │    │
│    │---|---│    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Four of Swords': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """
│    4            │    """ + YELLOW + """Astrological Association: Jupiter in Libra""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Rest, Contemplation, Healing""" + GREEN + """
│    Swords       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │---|---│    │
│    │   ☽   │    │
│    │---|---│    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Five of Swords': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """
│    5            │    """ + YELLOW + """Astrological Association: Venus in Aquarius""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Defeat, Conflict, Loss""" + GREEN + """
│    Swords       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │---|---│    │
│    │   ☽   │    │
│    │---|---│    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Six of Swords': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """
│    6            │    """ + YELLOW + """Astrological Association: Mercury in Aquarius""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Transition, Moving On, Mental Clarity""" + GREEN + """
│    Swords       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │---|---│    │
│    │   ☽   │    │
│    │   |   │    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Seven of Swords': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """
│    7            │    """ + YELLOW + """Astrological Association: Moon in Aquarius""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Deception, Sneakiness, Betrayal""" + GREEN + """
│    Swords       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │---|---│    │
│    │   ☽   │    │
│    │---|---│    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Eight of Swords': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """
│    8            │    """ + YELLOW + """Astrological Association: Jupiter in Gemini""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Restriction, Powerlessness, Self-imposed Prison""" + GREEN + """
│    Swords       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │---|---│    │
│    │   ☽   │    │
│    │---|---│    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Nine of Swords': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """
│    9            │    """ + YELLOW + """Astrological Association: Mars in Gemini""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Anxiety, Nightmares, Inner Turmoil""" + GREEN + """
│    Swords       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │---|---│    │
│    │   ☽   │    │
│    │---|---│    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Ten of Swords': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """
│    10           │    """ + YELLOW + """Astrological Association: Sun in Gemini""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Rock Bottom, Endings, Transformation""" + GREEN + """
│    Swords       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │---|---│    │
│    │   ☽   │    │
│    │---|---│    │
│    │   ☽   │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Page of Swords': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """
│    Page         │    """ + YELLOW + """Astrological Association: Earth of Air""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Curiosity, New Ideas, Communication""" + GREEN + """
│    Swords       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │   |   │    │
│    │   ☽   │    │
│    │       │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Knight of Swords': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """
│    Knight       │    """ + YELLOW + """Astrological Association: Fire of Air""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Ambition, Action, Determination""" + GREEN + """
│    Swords       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │  \│/  │    │
│    │   ☽   │    │
│    │  /│\  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Queen of Swords': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """
│    Queen        │    """ + YELLOW + """Astrological Association: Water of Air""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Independence, Intellect, Clarity""" + GREEN + """
│    Swords       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │  |||  │    │
│    │   ☽   │    │
│    │  |||  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'King of Swords': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Air""" + GREEN + """
│    King         │    """ + YELLOW + """Astrological Association: Fire of Air""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Authority, Truth, Leadership""" + GREEN + """
│    Swords       │
│    ┌───────┐    │
│    │   ☼   │    │
│    │  +++  │    │
│    │   ☽   │    │
│    │  +++  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Ace of Pentacles': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│    Ace          │    """ + YELLOW + """Astrological Association: Earth""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Manifestation, Prosperity, New Beginnings""" + GREEN + """
│    Pentacles    │
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │ ¤ ☽ ¤ │    │
│    │  ¤ ¤  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Two of Pentacles': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│    2            │    """ + YELLOW + """Astrological Association: Jupiter in Capricorn""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Balance, Adaptability, Juggling Priorities""" + GREEN + """
│    Pentacles    │
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │  | |  │    │
│    │  ¤ ¤  │    │
│    │  | |  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Three of Pentacles': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│    3            │    """ + YELLOW + """Astrological Association: Mars in Capricorn""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Teamwork, Collaboration, Skill Development""" + GREEN + """
│    Pentacles    │
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │  | |  │    │
│    │  ¤ ¤  │    │
│    │  | |  │    │
│    │  ¤ ¤  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Four of Pentacles': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│    4            │    """ + YELLOW + """Astrological Association: Sun in Capricorn""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Possessiveness, Security, Financial Stability""" + GREEN + """
│    Pentacles    │
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │---|---│    │
│    │  ¤ ¤  │    │
│    │  | |  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Five of Pentacles': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│    5            │    """ + YELLOW + """Astrological Association: Mercury in Taurus""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Poverty, Hardship, Material Loss""" + GREEN + """
│    Pentacles    │
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │---|---│    │
│    │  ¤ ¤  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Six of Pentacles': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│    6            │    """ + YELLOW + """Astrological Association: Moon in Taurus""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Generosity, Charity, Prosperity""" + GREEN + """
│    Pentacles    │
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │  | |  │    │
│    │  ¤ ¤  │    │
│    │  | |  │    │
│    │  ¤ ¤  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Seven of Pentacles': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│    7            │    """ + YELLOW + """Astrological Association: Saturn in Taurus""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Assessment, Patience, Long-term Vision""" + GREEN + """
│    Pentacles    │
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │  | |  │    │
│    │  ¤ ¤  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Eight of Pentacles': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│    8            │    """ + YELLOW + """Astrological Association: Sun in Virgo""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Craftsmanship, Dedication, Skill Development""" + GREEN + """
│    Pentacles    │
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │  | |  │    │
│    │  ¤ ¤  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Nine of Pentacles': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│    9            │    """ + YELLOW + """Astrological Association: Venus in Virgo""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Abundance, Independence, Self-Sufficiency""" + GREEN + """
│    Pentacles    │
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │  | |  │    │
│    │  ¤ ¤  │    │
│    │  |/|  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Ten of Pentacles': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│    10           │    """ + YELLOW + """Astrological Association: Mercury in Virgo""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Wealth, Legacy, Family""" + GREEN + """
│    Pentacles    │
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │ ¤ ☽ ¤ │    │
│    │  ¤ ¤  │    │
│    │  ☽ ☽  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Page of Pentacles': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│    Page         │    """ + YELLOW + """Astrological Association: Earth""" + GREEN + """ of Earth
│    of           │    """ + YELLOW + """Keywords: Manifestation, Practicality, New Opportunities""" + GREEN + """
│    Pentacles    │
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │  | |  │    │
│    │  ¤ ¤  │    │
│    │       │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Knight of Pentacles': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│    Knight       │    """ + YELLOW + """Astrological Association: Air of Earth""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Dependability, Diligence, Hard Work""" + GREEN + """
│    Pentacles    │
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │  \│/  │    │
│    │  ¤ ¤  │    │
│    │  /│\  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'Queen of Pentacles': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│    Queen        │    """ + YELLOW + """Astrological Association: Water of Earth""" + GREEN + """
│    of           │    """ + YELLOW + """Keywords: Nurturing, Abundance, Practical Wisdom""" + GREEN + """
│    Pentacles    │
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │  |||  │    │
│    │  ¤ ¤  │    │
│    │  |||  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,

'King of Pentacles': GREEN + """
┌─────────────────┐
│                 │    """ + YELLOW + """Elemental Association: Earth""" + GREEN + """
│      King       │    """ + YELLOW + """Astrological Association: Fire of Earth""" + GREEN + """
│      of         │    """ + YELLOW + """Keywords: Wealth, Success, Financial Stability""" + GREEN + """
│   Pentacles     │
│    ┌───────┐    │
│    │  ¤ ¤  │    │
│    │  +++  │    │
│    │  ¤ ¤  │    │
│    │  +++  │    │
│    └───────┘    │
│                 │
└─────────────────┘
""" + RESET,
}