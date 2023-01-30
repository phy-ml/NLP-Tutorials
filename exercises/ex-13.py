# Q: Extract the top 10 most common words in the given text excluding stopwords.

text="""Junkfood - Food that do no good to our body. And there's no need of them in our body but still we willingly eat them because they are great in taste and easy to cook or ready to eat. Junk foods have no or very less nutritional value and irrespective of the way they are marketed, they are not healthy to consume.The only reason of their gaining popularity and increased trend of consumption is 
that they are ready to eat or easy to cook foods. People, of all age groups are moving towards Junkfood as it is hassle free and often ready to grab and eat. Cold drinks, chips, noodles, pizza, burgers, French fries etc. are few examples from the great variety of junk food available in the market.
 Junkfood is the most dangerous food ever but it is pleasure in eating and it gives a great taste in mouth examples of Junkfood are kurkure and chips.. cold rings are also source of junk food... they shud nt be ate in high amounts as it results fatal to our body... it cn be eated in a limited extend ... in research its found tht ths junk foods r very dangerous fr our health
Junkfood is very harmful that is slowly eating away the health of the present generation. The term itself denotes how dangerous it is for our bodies. Most importantly, it tastes so good that people consume it on a daily basis. However, not much awareness is spread about the harmful effects of Junkfood .
The problem is more serious than you think. Various studies show that Junkfood impacts our health negatively. They contain higher levels of calories, fats, and sugar. On the contrary, they have very low amounts of healthy nutrients and lack dietary fibers. Parents must discourage their children from consuming junk food because of the ill effects it has on one’s health.
Junkfood is the easiest way to gain unhealthy weight. The amount of fats and sugar in the food makes you gain weight rapidly. However, this is not a healthy weight. It is more of fats and cholesterol which will have a harmful impact on your health. Junk food is also one of the main reasons for the increase in obesity nowadays.
This food only looks and tastes good, other than that, it has no positive points. The amount of calorie your body requires to stay fit is not fulfilled by this food. For instance, foods like French fries, burgers, candy, and cookies, all have high amounts of sugar and fats. Therefore, this can result in long-term illnesses like diabetes and high blood pressure. This may also result in kidney failure."""


# use nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import RegexpTokenizer

stop_word = set(stopwords.words('english'))

token_nltk = RegexpTokenizer(r"\w+")

nltk_dict = {}

for token in token_nltk.tokenize(text):
    if token not in stop_word:
        if token not in nltk_dict:
            nltk_dict[token] = 1
        else:
            nltk_dict[token] += 1

# sort the dict
nltk_dict = {k:v for k,v in (sorted(nltk_dict.items(), key=lambda item:item[1], reverse=True))}
print(f"NLTK based corpus :{nltk_dict}")

# use spacy
import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
spacy_word = [token.text for token in doc if token.is_stop == False and token.is_punct == False ]
spacy_dict = {}
for token in spacy_word:
    if token not in spacy_dict:
        spacy_dict[token] = 1
    else:
        spacy_dict[token] += 1

# sort the dict
spacy_dict = {k:v for k,v in (sorted(spacy_dict.items(), key=lambda item:item[1], reverse=True))}
print(f"Spacy based corpus :{spacy_dict}")