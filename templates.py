class Prompt:
    @staticmethod
    def infinitive(infinitive: str, present_on: str) -> str:
        with open('static/templates/misc/infinitive.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, present_on=present_on)

    @staticmethod
    def verbal_noun(infinitive: str, verbal_noun: str) -> str:
        with open('static/templates/misc/verbal noun.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, verbal_noun=verbal_noun)

    @staticmethod
    def present_active_participle(infinitive: str, present_active_participle: str) -> str:
        with open('static/templates/participles/present active participle.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, present_active_participle=present_active_participle)

    @staticmethod
    def past_active_participle(infinitive: str, past_active_participle: str) -> str:
        with open('static/templates/participles/past active participle.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past_active_participle=past_active_participle)

    @staticmethod
    def past_passive_participle(infinitive: str, past_passive_participle: str) -> str:
        with open('static/templates/participles/past passive participle.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past_passive_participle=past_passive_participle)

    @staticmethod
    def present_tense(infinitive: str, present: str, pronoun: str) -> str:
        with open('static/templates/present/present tense.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, present=present, pronoun=pronoun)

    @staticmethod
    def present_tense_on_ona_ono(infinitive: str, present: str) -> str:
        with open('static/templates/present/present tense (on, ona, ono).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, present=present)

    @staticmethod
    def present_tense_ony_oni(infinitive: str, present: str) -> str:
        with open('static/templates/present/present tense (ony, oni).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, present=present)

    @staticmethod
    def past_tense(infinitive: str, past: str, pronoun: str) -> str:
        with open('static/templates/past/past tense.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past=past, pronoun=pronoun)

    @staticmethod
    def past_perfect_tense(infinitive: str, past_perfect: str, pronoun: str) -> str:
        with open('static/templates/past/past perfect tense.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past_perfect=past_perfect, pronoun=pronoun)

    @staticmethod
    def future_tense(infinitive: str, future: str, pronoun: str) -> str:
        with open('static/templates/future/future tense.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, future=future, pronoun=pronoun)

    @staticmethod
    def future_tense_on_ona_ono(infinitive: str, future: str) -> str:
        with open('static/templates/future/future tense (on, ona, ono).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, future=future)

    @staticmethod
    def future_tense_ony_oni(infinitive: str, future: str) -> str:
        with open('static/templates/future/future tense (ony, oni).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, future=future)

    @staticmethod
    def present_conditional(infinitive: str, present_conditional: str, pronoun: str) -> str:
        with open('static/templates/conditional/present conditional tense.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, present_conditional=present_conditional,
                                          pronoun=pronoun)

    @staticmethod
    def past_conditional(infinitive: str, past_conditional: str, pronoun: str) -> str:
        with open('static/templates/conditional/past conditional tense.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past_conditional=past_conditional, pronoun=pronoun)

    @staticmethod
    def imperative_tense(infinitive: str, imperative: str, pronoun: str) -> str:
        with open('static/templates/imperative/imperative tense.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, imperative=imperative, pronoun=pronoun)

    @staticmethod
    def imperative_tense_on_ona_ono(infinitive: str, imperative: str) -> str:
        with open('static/templates/imperative/imperative tense (on, ona, ono).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, imperative=imperative)

    @staticmethod
    def imperative_tense_ony_oni(infinitive: str, imperative: str) -> str:
        with open('static/templates/imperative/imperative tense (ony, oni).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, imperative=imperative)
