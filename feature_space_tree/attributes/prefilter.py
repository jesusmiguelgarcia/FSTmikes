#!/usr/local/bin/python
# coding: utf-8

# Copyright (C) 2011-2012 FeatureSpaceTree Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ==============================================================================
# FeatureSpaceTree:
#
# Author: Adrian Pastor Lopez-Monroy <pastor@ccc.inaoep.mx>
# URL: <https://github.com/beiceman/FeatureSpaceTree>
#
# Language Technologies Lab,
# Department of Computer Science,
# Instituto Nacional de Astrofísica, Óptica y Electrónica
#
# For license information, see:
#  * The header of this file
#  * The LICENSE.TXT included in the project dir
# ==============================================================================

#===============================================================================
# Modes are Templates to choose how the terms will be calculated. The ModeCorpus
# receive the object corpus in kwargs["corpus"] and a list of files(can be a
# list of one)in kwargs[sources]; it iterates and get the respective tokens.
# The ModeString calculates the tokens in kwargs["string"].
#===============================================================================

import re
import codecs
import attr_util
from abc import ABCMeta, abstractmethod
from nltk.corpus import stopwords

class RawStringNormalizer(object):

    __metaclass__ = ABCMeta

    def __init__(self, raw_string):
        self._raw_string = raw_string

    @abstractmethod
    def get_raw_string(self):
        return self._raw_string


class EmptyRawStringNormalizer(RawStringNormalizer):

    def __init__(self, raw_string):
        super(EmptyRawStringNormalizer, self).__init__(raw_string)

    def get_raw_string(self):
        return self._raw_string


class DecoratorRawStringNormalizer(RawStringNormalizer):

    __metaclass__ = ABCMeta

    def __init__(self, raw_string_normalizer):
        self._raw_string_normalizer = raw_string_normalizer

    @abstractmethod
    def get_raw_string(self):
        return self._raw_string_normalizer.get_raw_string()


class ToLowerDecoratorRawStringNormalizer(DecoratorRawStringNormalizer):

    def __init__(self, raw_string_normalizer):
        super(ToLowerDecoratorRawStringNormalizer, self).__init__(raw_string_normalizer)

    def get_raw_string(self):

        old_raw_string = self._raw_string_normalizer.get_raw_string()

        new_raw_string = old_raw_string.lower()

        return new_raw_string


#---------------------------------------
#NoAcentosDecoratorRawStringNormalizer
class NoAcentosDecoratorRawStringNormalizer(DecoratorRawStringNormalizer):

    def __init__(self, raw_string_normalizer):
        super(NoAcentosDecoratorRawStringNormalizer, self).__init__(raw_string_normalizer)

    def get_raw_string(self):

        old_raw_string = self._raw_string_normalizer.get_raw_string()

        new_raw_string = old_raw_string.encode("utf8").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")

        return new_raw_string




#nueva clase para remover las palabras vacias en español del texto raw
#------------------------------------------------------------------------------


class NoStopwordSpanishDecoratorRawStringNormalizer(DecoratorRawStringNormalizer):

    def __init__(self, raw_string_normalizer):
        super(NoStopwordSpanishDecoratorRawStringNormalizer, self).__init__(raw_string_normalizer)

    def get_raw_string(self):

        old_raw_string = self._raw_string_normalizer.get_raw_string()

        #transformacion a cadena original
	new_raw_string =old_raw_string
	
	#imprimir con utf8
	#f_ignored_strings = codecs.open(old_raw_string, encoding='utf-8')
	
	#print "old_raw_string",f_ignored_strings

	#f_ignored_strings.close()
	# fi imprimir utf 8
        
        #new_raw_string = old_raw_string.lower()

	#remove punctuation and split into seperate words

	#words = re.findall(r"[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+-*[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+|[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+", old_raw_string,flags = re.UNICODE | re.LOCALE) 

	#This is the more pythonic way

	#print words	

	#important_words = filter(lambda x: x not in stopwords.words('spanish'), words)
	#new_raw_string = " ".join(important_words)
	

	print new_raw_string.encode('utf-8')

        #fin transformacion
        

        return new_raw_string

#fin clase nueva --------------------------------------------------------------------------

class ToUpperDecoratorRawStringNormalizer(DecoratorRawStringNormalizer):

    def __init__(self, raw_string_normalizer):
        super(ToUpperDecoratorRawStringNormalizer, self).__init__(raw_string_normalizer)

    def get_raw_string(self):

        old_raw_string = self._raw_string_normalizer.get_raw_string()

        new_raw_string = old_raw_string.upper()

        return new_raw_string


class JustRegExpDecoratorRawStringNormalizer(DecoratorRawStringNormalizer):
    '''
    This decorator returns an string just with the tokens extracted using the
    regular expression in regexp. One use of this filter is when you want to
    get n-grams but just using the words, and omiting all other tokens, for
    instace punctuation marks and numbers.

    If you want the inverse thing (ignore specific character or tokens), you
    should use/build another filter.
    '''

    def __init__(self, raw_string_normalizer, regexp):
        super(JustRegExpDecoratorRawStringNormalizer, self).__init__(raw_string_normalizer)
        self.regexp = regexp

    def get_raw_string(self):

        old_raw_string = self._raw_string_normalizer.get_raw_string()

        list_of_tokens = attr_util.Util.calc_regexp(old_raw_string, self.regexp)

        new_raw_string = " ".join(list_of_tokens)

        return new_raw_string


class ReplaceRegExpDecoratorRawStringNormalizer(DecoratorRawStringNormalizer):
    '''
    '''

    def __init__(self, raw_string_normalizer, regexp, replacement):
        super(ReplaceRegExpDecoratorRawStringNormalizer, self).__init__(raw_string_normalizer)
        self.regexp = regexp
        self.replacement = replacement

    def get_raw_string(self):

        old_raw_string = self._raw_string_normalizer.get_raw_string()
        #print self.regexp
	#old_raw_string=old_raw_string.replace(u"á",u"a").replace(u"é",u"e").replace(u"í",u"i").replace(u"ó",u"o").replace(u"ú",u"u")
	#print "debug",self.replacement
        #print old_raw_string.encode('utf-8')
        #print re.findall(self.regexp,old_raw_string)
        old_raw_string = re.sub(self.regexp, self.replacement, old_raw_string)

        new_raw_string = old_raw_string

        return new_raw_string     
