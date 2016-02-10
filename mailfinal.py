#!/usr/local/bin/python

from email.Header import decode_header
import email
from base64 import b64decode
import sys
from email.Parser import Parser
from email.utils import parseaddr
from StringIO import StringIO
import imaplib

class mail:

    def parse(self,content):
        """
        Parse un email et retourne les informations importantes
        """
        msgobj = Parser().parsestr(content)
        if msgobj['Subject'] is not None:
            decodefrag = decode_header(msgobj['Subject'])
            subj_fragments = []
            for s , enc in decodefrag:
                if enc:
                    s = unicode(s , enc).encode('utf8','replace')
                subj_fragments.append(s)
            subject = ''.join(subj_fragments)
        else:
            subject = None

        attachments = []
        body = None 
        html = None 
        for part in msgobj.walk():
            if part.get_content_type() == "text/plain":
                if body is None:
                    body = ""
                body += unicode(
                    part.get_payload(decode=True),
                    part.get_content_charset(),
                    'replace'
                ).encode('utf8','replace')
            elif part.get_content_type() == "text/html":
                if html is None:
                    html = ""
                html += unicode(
                    part.get_payload(decode=True),
                    part.get_content_charset(),
                    'replace'
                ).encode('utf8','replace')
        return {
            'subject' : subject,
            'body' : body,
            'html' : html,
            'from' : parseaddr(msgobj.get('From'))[1],
            'to' : parseaddr(msgobj.get('To'))[1]
        }


    def lisMail(self):
        obj = imaplib.IMAP4_SSL('imap.gmail.com','993')
        obj.login('ralf.eclille','pjandroid')
        obj.select()
        result, data = obj.uid('search', None, "Unseen")
        nonLus = data[0].split()

        nb = len(nonLus)

        if nb == 0:
            return("Votre boite mail est vide")

        else:

                reponse = ''

                reponse += 'Vous avez '
                reponse += str(nb)

                if nb > 1:
                    reponse += ' nouveaux messages'
                else:
                    reponse += ' nouveau message'

                for uid in nonLus:
                    result, data = obj.uid('fetch', uid, '(RFC822)')

                    raw_email = data[0][1]

                    email=self.parse(raw_email)

                    sujet = email['subject'].decode('utf-8')
                    destinataire = email['to']
                    destinateur = email['from']
                    content = email['body'].decode('utf-8')

                    reponse += '\nMessage envoye par '
                    reponse += destinateur
                    reponse += '\n'
                    reponse += sujet
                    reponse += '\n'
                    reponse += content

                return(reponse)
