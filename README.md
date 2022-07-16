# [HTREC 2022](https://www.aicrowd.com/challenges/htrec-2022/): Improving the HTR output of Greek papyri and Byzantine manuscripts

### Ranking

1st place synthetic and original data on leaderboard.

1st place synthetic data.

4th place original data.

The codes are created by Team error_404_name_not_found, @konstantina_liagkou and @manos_papadatos.

The best single model we have obtained during the competition 
was an **Rule Based model** with Public CERR score 0.278 and Private CERR score 0.00. 

### Introduction

The digitization of ancient texts is essential for analyzing ancient corpora and preserving cultural heritage. However, the transcription of ancient handwritten text using optical character recognition (OCR) methods remains challenging. Handwritten text recognition (HTR) concerns the conversion of scanned images of handwritten text into machine-encoded text. In contrast with OCR where the text to be transcribed is printed, HTR is more challenging and can lead to transcribed text that includes many more errors or even to no transcription at all when training data on the specific script (e.g., medieval) are not available.

Existing work on HTR combine OCR models and Natural language processing (NLP) methods from fields such as grammatical error correction (GEC), which can assist with the task of post-correcting transcription errors. The post-correction task has been reported as expensive, time-consuming, and challenging for the human expert, especially for OCRed text of historical newspapers, where the error rate is as low as 10%. The HTREC focus of this challenge will be on the post-correction of HTR transcription errors, attempting to build on recent NLP advances such as the successful applications of Transformers and transfer learning. The ground truth of the evaluation set will be used to score participating systems in terms of character error rate (CER). 

<hr>

### Code

First and foremost, we did exploratory data analysis in greek text, `eda.ipynb`.

The challenge shared some baseline models that we brought it all together, `baselines.ipynb`.

Our initial approach was to apply advanced machine learning techniques. 
The first model that we tried was based on a char-to-char model `lstm_seq2seq.ipynb`.
Then we used bert-to-bert model, which fine-tune either 
[Ancient Greek BERT](https://huggingface.co/pranaydeeps/Ancient-Greek-BERT)
or [Greek BERT](https://huggingface.co/nlpaueb/bert-base-greek-uncased-v1) `bert2bert.ipynb`.
However, the best scores were retrieved from rule based models, `best_RuleBased.ipynb`.
The folder, called `results`, include the inferences of all the models.

In the folder `data`, there are the dataset from the Challenge (`train.csv`,`test.csv`) 
and an ancient greek corpus (`corpus.csv`) 

If you find our work useful to your research, please cite this work as:

```
@inproceedings{liagkou-papadatos-2022-htrec,
    title = "Rule-based technique to improve the HTR output of Greek papyri and Byzantine manuscripts",
    author = "Liagkou, Konstantina  and Papadatos, Emmanouil ",
    booktitle = "HTREC 2022: Improving the HTR output of Greek papyri and Byzantine manuscripts",
    month = August,
    year = "2022",
    address = "Venice, Italy"
}
