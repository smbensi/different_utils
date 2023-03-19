# BUGS

# AMELIORATIONS

1. [ ] tester le RNN-T de NeMo
2. [ ] Whisper comprendre pourquoi c'est trop lourd pour le Xavier
3. [ ] utiliser la speaker diarization pour reconnaitre la personne disant le wakeword et la differencier par la suite par rapport aux autres personnes qui parlent (a part si une personne dit le wakeword pr qq un dautres)


# probleme en python

1. est ce que quand j'importe un fichier et  quil y a une fonction dedans qui est appele cela l'apelle? \
**REPONSE** apparemment **OUI** meme si on appelle que une partie du module

2. qu'est ce qu'une @staticmethod? \
**REPONSE** c'est un operateur built-in qui definit une methode static a la classe. elle ne peut recevoir aucun argument qu'elle soit appele par une instance or par la classe elle meme
pas de `cls` ou de `self` et elle ne peut pas avoir acces aux attributs de la classe ou de l'instance. cela peut retourner un object de la classe

# comprehension du code

## Rajouter des mots
* Dans le wakewords.json  alors dans "base" rajouter:
```json
"mot a reconnaitre": {
    "spellings":["orthographe1","ortho2",....]
}
```
et dnas "phonetic intents" rajouter
```json
"mot a reconnaitre":["chaine de mots pour le trigger"]
```
si on veut rajouter des samples 
> python -m asr.applications.process_dataset -d <dataset_path> -o <output_path>

les samples doivent etre en 16kHz monosample 
>sox input.wav -r 16000 -c 1 output.wav 

>ffmpeg -i input.wav -ar 16000 -ac 1 output.wav

## difference wakeword et wakeword_Detect
detect renvoie direct l'autre attend la fin de la phrase

## Questions
* quest ce que model_wrapper

## COmment on load les JSON
le STT load le JSON dans `asr/wakeword/logit_sequences.py` dans la fonction `load_wakewords` qui est appele dans le meme script

Dans `wakeword_params["json_definition"]` on garde tout ce qui est dans "Phonetic"

Dans `additional_spelling` on va loader ce qui est defini dans sample_json


## Comment se pase les callbacks

Pour le triton model il faut aller chercher dans token_stt_Streaming c'est dans la fonction `predict_queue` ligne 292 et c'est la bas qu'on fait appelle a tous les callbacks \
les callbacks sont aussi appeles dans `publish_Sentence`


> commment on initie le wrapper?

pour `triton` on cree un NemoFrameAsr.build_frame_model \
pour `google` on fait appel a GoogleFrameAsr.build_frame_model 

> comment se passe le self.overlaper ? 
