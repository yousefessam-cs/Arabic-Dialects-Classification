from nltk.corpus import stopwords
import re


class Preprocess():
    def __init__(self) -> None:
        self.stop_words = set(stopwords.words('arabic'))

    def remove_stopwords(self, text):
        words = text.split()
        filtered_words = [word for word in words if word.lower() not in self.stop_words]
        return ' '.join(filtered_words)


    def remove_usernames(self, text):
        clean_text = re.sub(r'@\w+', '', text)
        return clean_text


    def remove_emojis(self, text):
        clean_text = re.sub(r'[^\w\s#@/:%.,_-]', '', text)
        return clean_text


    def remove_numbers(self, text):
        clean_text = re.sub(r'\d+', '', text)
        return clean_text


    def remove_links(self, text):
        URL_REGEXES = [
            r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)",
            r"@(https?|ftp)://(-\.)?([^\s/?\.#-]+\.?)+(/[^\s]*)?$@iS",
            r"http[s]?://[a-zA-Z0-9_\-./~\?=%&]+",
            r"www[a-zA-Z0-9_\-?=%&/.~]+",
            r"[a-zA-Z]+\.com",
            r"(?=http)[^\s]+",
            r"(?=www)[^\s]+",
            r"://",
        ]

        for reg in URL_REGEXES:
            text = re.sub(reg, '', text)
        return text


    def remove_english(self, text):
        english_pattern = re.compile(r'[a-zA-Z]+')
        cleaned_text = re.sub(english_pattern, '', text)
        return cleaned_text


    def remove_diacritics(self, text):
        arabic_diacritics = re.compile("""
                                     ّ    | # Tashdid
                                     َ    | # Fatha
                                     ً    | # Tanwin Fath
                                     ُ    | # Damma
                                     ٌ    | # Tanwin Damm
                                     ِ    | # Kasra
                                     ٍ    | # Tanwin Kasr
                                     ْ    | # Sukun
                                    ـ    | # Tatwil/Kashida
                                 """, re.VERBOSE)
        return re.sub(arabic_diacritics, '', text)


    def normalize_chars(self, text):
        preprocessed_text = re.sub("[إأآا]", "ا", text)
        preprocessed_text = re.sub("ى", "ي", preprocessed_text)
        preprocessed_text = re.sub("ؤ", "ء", preprocessed_text)
        preprocessed_text = re.sub("ئ", "ء", preprocessed_text)
        preprocessed_text = re.sub("ة", "ه", preprocessed_text)
        preprocessed_text = re.sub("گ", "ك", preprocessed_text)
        preprocessed_text = re.sub("ڤ", "ف", preprocessed_text)
        preprocessed_text = re.sub("چ", "ج", preprocessed_text)
        preprocessed_text = re.sub("ژ", "ز", preprocessed_text)
        preprocessed_text = re.sub("پ", "ب", preprocessed_text)
        return preprocessed_text


    def remove_special_chars(self, text):
        '''
         The regular expression r'[^\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\d\s]+'
          matches any characters that are not in the specified range of
          Arabic Unicode characters (\u0600-\u06FF, \u0750-\u077F, and \u08A0-\u08FF),
          digits (\d), or whitespace (\s).
        '''
        special_chars_pattern = re.compile(r'[^\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\d# ]+')

        cleaned_text = re.sub(special_chars_pattern, ' ', text)
        return cleaned_text


    def remove_punctuation(self, text):
        pun = r"([!\"#\$%\'\(\)\*\+,\.:;\-<=·>?@\[\\\]\^_ـ`{\|}~—٪’،؟`୍“؛”ۚ【»؛\s+«–…‘])"
        cleaned_text = re.sub(pun, ' ', text)
        return cleaned_text


    def remove_extra_whitespaces(self, text):
        clean_text = re.sub(r'\s+', ' ', text)
        return clean_text.strip()


    def remove_repeated_chars(self, text):
        pattern = re.compile(r"(.)\1{2,}")
        clean_text = pattern.sub(r"\1\1", text)
        return clean_text


    def remove_all(self, text):
        # stop_words
        text = self.remove_stopwords(text)

        # user_names
        text = self.remove_usernames(text)

        # emojies
        text = self.remove_emojis(text)

        # numbers
        text = self.remove_numbers(text)

        # links
        text = self.remove_links(text)

        # English
        text = self.remove_english(text)

        # tashkel
        text = self.remove_diacritics(text)

        # normalizeChars
        text = self.normalize_chars(text)

        # special chars
        text = self.remove_special_chars(text)

        # punctuation
        text = self.remove_punctuation(text)

        # white_space
        text = self.remove_extra_whitespaces(text)

        # repeated charachters
        text = self.remove_repeated_chars(text)

        return text

