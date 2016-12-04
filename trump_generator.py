import markovify
import nltk
import  random

speeches = ["speech"+str(i)+".txt" for i in range(1,5)]
models = []

for speech in speeches:
    with open("./trumptext/"+speech) as f:
        text = f.read()

    models += [markovify.Text(text)]

comb_model = models[2] #markovify.combine(models)


while True:
    user_input = raw_input("Say something to OKTrump (x to exit): ")
    if user_input == "x":
        break
    inp_tokens = nltk.word_tokenize(user_input)
    inp_tags = nltk.pos_tag(inp_tokens)
    inp_pos = {}
    for tag in inp_tags:
        if tag[1].startswith('NN') or tag[1].startswith('V'):
            if not tag[1] in inp_pos:
                inp_pos[tag[1]] = []
            inp_pos[tag[1]] += [tag[0]]


    sentence = comb_model.make_sentence() + comb_model.make_sentence() + comb_model.make_sentence()

    print sentence
    print inp_pos

    tokens = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(tokens)

    new_sentence = ""
    for tag in tags:
        if tag[1].startswith('NN') or tag[1].startswith('V'):
            if tag[1] in inp_pos:
                # there is a 1/(n+1) chance that an item in inp_pos[tag[1]] will replace the item in the sentence.
                # where n = len(inp_pos[tag[1]])
                # that leads to a 1 / (n+1) chance that it wont get replaced

                rand = random.random()
                part = 1.0 / (len(inp_pos[tag[1]]) + 1)
                segment = int(rand / part)
                if segment < len(inp_pos[tag[1]]):
                    new_sentence += " " + inp_pos[tag[1]][segment]
                    print "Replacing %s with %s, rand was %f" % (tag[0], inp_pos[tag[1]][segment], rand)
                    continue
                print "Not replacing %s with %s, rand was %f" % (tag[0], inp_pos[tag[1]], rand)

        new_sentence += " " + tag[0]

    print new_sentence
