#!/usr/bin/env python3


from flask import Blueprint, render_template
import random

controller = Blueprint('grandpa', __name__, url_prefix='/')


def grandpa_says():
    nouns = ("Puppies", "Cars", "Rabbits", "Cows", "Monkeys")
    verbs = ("run", "hit", "jump", "poop", "barf")
    adv = ("crazily", "dutifully", "foolishly", "frequently", "occasionally")
    num = random.randrange(0, 5)
    return '{0} {1} {2}.'.format(nouns[num], verbs[num], adv[num])


@controller.route('/<sentence>', methods=['GET'])
def grandpa_listens(sentence):
    if sentence.isupper():
        answer = grandpa_says()
        return render_template('grandpa_listening.html', sentence=sentence, answer=answer)
    else:
        return render_template('grandpa_not_listening.html')
