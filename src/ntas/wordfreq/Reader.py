''' thanks to https://etienned.github.io/posts/extract-text-from-word-docx-simply '''
try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile


"""
Module that extract text from MS XML Word document (.docx).
(Inspired by python-docx <https://github.com/mikemaccana/python-docx>)
"""

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'


def read_docx(path):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)

    paragraphs = []
    for paragraph in tree.getiterator(PARA):
        texts = [node.text
                 for node in paragraph.getiterator(TEXT)
                 if node.text]
        if texts:
            paragraphs.append(''.join(texts))

    return '\n\n'.join(paragraphs)

# python-docx module
#from docx import Document

# document_text = Document('Homer2.docx')
# for paragraph in document.paragraphs:
#         for word in paragraph.text.split():
#             print (normalizeWord(word))
#             normalizedWord = normalizeWord(word).encode('utf-8').strip().upper()
#             createAndInsertNode(frequencyBST, normalizedWord)
