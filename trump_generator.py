import markovify
import nltk
import  random

speeches = ["speech"+str(i)+".txt" for i in range(1,5)]
models = []

for speech in speeches:
    with open("./trumptext/"+speech) as f:
        text = f.read()

    models += [markovify.Text(text)]

comb_model = markovify.combine(models)


while True:
    user_input = raw_input("Say something to OKTrump (x to exit): ")
    if user_input == "x":
        break
    inp_tokens = nltk.word_tokenize(user_input)
    inp_tags = nltk.pos_tag(inp_tokens)
    inp_pos = {}
    for tag in inp_tags:
        if tag[1].startswith('NN') or tag[1].startswith('V'):
            inp_pos[tag[1]] = tag[0]

    sentence = comb_model.make_sentence() + comb_model.make_sentence() + comb_model.make_sentence()

    print sentence

    tokens = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(tokens)

    new_sentence = ""
    for tag in tags:
        if tag[1].startswith('NN') or tag[1].startswith('V'):
            if tag[1] in inp_pos:
                if random.random() > 0.5:
                    new_sentence += " " + inp_pos[tag[1]]
                    continue
        new_sentence += " " + tag[0]

    print new_sentence
