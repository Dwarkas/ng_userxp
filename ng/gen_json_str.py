import json

dict_obj = {


	"it" :
    		{
    		"some_id_of_a_string_div": "Sono una stringa" ,
    		"title": "Titolo italiano",
    		"button_next": "Continua",
    		"hearer_header_text": "Sei il HEARER!",
    		"speaker_header_text": "Sei il SPEAKER!",
            "past_interactions": "Interazioni pasate",
            "result_success": "Questa interazione era un SUCCESSO",
            "result_fail": "Questa interazione era una FAILURE",
            "hearer_word_question":"Hai sentito questa parola :",
            "hearer_meaning_question":"De cosa pensi il speaker ha parlato?",
            "speaker_word_question":"Utilizzando che parola?",
            "speaker_meaning_question":"De cosa vuoi parlare?",
            "new_xp": "Quell esperimento ancora non e cominciato.",
            "not_involved": "Non eri parte de quella interazione",
            "not_involved_pre": "Non eri parte de ",
            "not_involved_post": " interazioni",
            "header_inter":"Interazione",
            "homebutton":"Home",
            "new_xp_button":"Nuovo esperimento",
            "new_experiment":"Nuovo esperimento",
            "logoutbutton":"Sconnettarsi",
            "best_scores":"Migliori Giochi",
            "hometitle":"Costruisci un linguagio!",
            "hometext":"Mettite d'accordo su un vocabulario facendo interazioni con individuali da una cera populazione.",
            "button_start":"Comincia",
            "score_header":"Fine dell esperimento",
            "score_text":"Quello e la valore dello tuo score. Prova a fare meglio!",
            "window_title":'Crealang',
            "header_home":"CREALANG",
            }
        ,
    "en" :
            {
            "some_id_of_a_string_div": "I am a string" ,
            "title": "English title",
            "button_next": "Next",
            "hearer_header_text": "You are the HEARER!",
            "speaker_header_text": "You are the SPEAKER!",
            "past_interactions": "Past Interactions",
            "result_success": "This interaction was SUCCESSFUL",
            "result_fail": "This interaction FAILED",
            "hearer_word_question":"You heard this word :",
            "hearer_meaning_question":"What do you think the speaker talked about?",
            "speaker_word_question":"Using which word?",
            "speaker_meaning_question":"What do you want to talk about?",
            "new_xp": "This experiment has not started yet.",
            "not_involved": "You were not involved in this interaction.",
            "not_involved_pre": "You were not involved in ",
            "not_involved_post": " interactions",
            "header_inter":"Interaction",
            "homebutton":"Home",
            "new_xp_button":"New experiment",
            "new_experiment":"New experiment",
            "logoutbutton":"Logout",
            "best_scores":"Best Scores",
            "button_start":"Start",
            "hometitle":"Build a language!",
            "header_home":"CREALANG",
            "hometext":"Set up a vocabulary by interacting with individuals from a given population.",
            "score_header":"End of the experiment",
            "score_text":"This is the score that you obtained. Try to do better!",
            "window_title":'Crealang',
    		}

    }


json_str = "\nvar lang = "+json.dumps(dict_obj)+";\n"

print json_str

with open('static/ng/lang.js','w') as f:
    f.write(json_str)



with open('static/ng/change_lang.js','r') as f:
    s1 = f.read()

split_str = '//LANG GETS DECLARED HERE, this line is used in the python script generating it'

splitted = s1.split(split_str)
assert len(splitted) >= 3
splitted[1] = json_str
s2 = split_str.join(splitted)


with open('static/ng/change_lang.js','w') as f:
    f.write(s2)

