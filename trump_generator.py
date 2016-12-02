import markovify

speeches = ["speech"+str(i)+".txt" for i in range(1,5)]
models = []

for speech in speeches:
    with open("./trumptext/"+speech) as f:
        text = f.read()

    models += [markovify.Text(text)]

comb_model = markovify.combine(models)

# Print five randomly-generated sentences
for i in range(5):
    print(comb_model.make_sentence())

# Print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print(comb_model.make_short_sentence(140))