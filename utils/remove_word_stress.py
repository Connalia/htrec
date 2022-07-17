import re
# Replace all the punctiotions
def clear_vowels(df,cols):
  for i in cols:
    df[i] = df[i].apply(lambda x: re.sub(r'ά|α|ὰ|ά|ᾄ|ᾅ|ὰ|ά|ᾳ|ᾴ|ᾶ|ᾷ|ἀ|ἁ|ἂ|ἃ|ἄ|ἅ|ἇ|Ἀ|Ἁ|Ἄ|Ἅ|Α','α',x.lower()))
    df[i] = df[i].apply(lambda x: re.sub(r'έ|ε|ὲ|έ|ἐ|ἑ|ἔ|ἕ|Ἐ|Ἑ|Ἔ|Ἕ|Ε','ε',x))
    df[i] = df[i].apply(lambda x: re.sub(r'ή|ή|η|ᾑ|ᾔ|ᾗ|ὴ|ή|ῃ|ῄ|ῆ|ῇ|ἠ|ἡ|ἢ|ἣ|ἤ|ἥ|ἦ|ἧ|Ἡ|Η','η',x))
    df[i] = df[i].apply(lambda x: re.sub(r'ΐ|ί|ι|ϊ|ὶ|ί|ῒ|ῖ|ἰ|ἱ|ἳ|ἴ|ἵ|ἶ|ἷ|Ἰ|Ἱ|Ἴ','ι',x))
    df[i] = df[i].apply(lambda x: re.sub( r'ο|ό|ὸ|ό|ὀ|ὁ|ὃ|ὄ|ὅ|Ὁ|Ὃ|Ὅ|Ο','ο',x))
    df[i] = df[i].apply(lambda x: re.sub(r'ῤ|ῥ','ρ',x))
    df[i] = df[i].apply(lambda x: re.sub(r'ῦ|υ|ύ|ὺ|ύ|ὐ|ὑ|ὓ|ὔ|ὕ|ὖ|ὗ|Ὑ','υ',x))
    df[i] = df[i].apply(lambda x: re.sub(r'ω|ᾠ|ᾤ|ᾦ|ᾧ|ὼ|ώ|ὠ|ὡ|ὢ|ὣ|ὤ|ὥ|ὦ|ὧ|Ὠ|Ὡ|Ὥ|Ὦ|ῳ|ῴ|ῶ|ῷ|ώ|Ω','ω',x))
    df[i] = df[i].apply(lambda x: re.sub(r'\W',' ',x)) #remove non words characters
    df[i] = df[i].apply(lambda x: re.sub(r'\s\s+',' ',x)) #collapse multiple whitespaces
  return(df)


# clear_vowels(train_df,["HUMAN_TRANSCRIPTION","SYSTEM_TRANSCRIPTION"])
# clear_vowels(test_df,["HUMAN_TRANSCRIPTION","SYSTEM_TRANSCRIPTION"])