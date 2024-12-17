from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
import requests
from bs4 import BeautifulSoup as bs

def get_text(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text


def summarize_text(text, sentences_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences_count)
    summary = [str(sentence) for sentence in summary]
    return ' '.join(summary)

link = 'https://n.news.naver.com/mnews/article/018/0005908119?sid=105'
get_con = requests.get(link)
soup_con = bs(get_con.content, 'html.parser')

text = get_text(soup_con)
