from __future__ import print_function
from tc1_infer import initialize_parameters
from tc1_infer import run

import json
import os
from os.path import expanduser
import requests

from keras import backend as K
import unittest
import io
import xmlrunner


def create_file():
    print("started create")
    home = expanduser("~")
    modac_token_dir =  os.path.abspath(os.path.join(home,".nci-modac"))
    modac_token_file = "credentials.json"
    user_attr = "modac_user"
    token_attr = "modac_token"
    modac_token_path = os.path.join(modac_token_dir, modac_token_file)
    credentials_dic = {}
    auth = ("ksr3089@gmail.com", "Pin@1234")
    auth_url = 'https://modac.cancer.gov/api/authenticate'
    response = requests.get(auth_url, auth = auth, stream = True)
    token = response.text
    save_token = True
    if not os.path.isdir(modac_token_dir):
        os.mkdir(modac_token_dir)
    credentials_dic[user_attr] = "ksr3089@gmail"
    credentials_dic[token_attr] =  token
    with open(modac_token_path, "w") as outfile:
        json.dump(credentials_dic, outfile, indent=4)
    print("Created")

  
class TC1_Validations(unittest.TestCase):
    create_file()
    gParameters = initialize_parameters()
    score_json = run(gParameters, "testing")

    def test_jsonScore(self):
        print('json Test score:', self.score_json[0])
        self.assertEqual(self.score_json[0], 0.12268449479403595, "json Test Score")

    def test_jsonAccuracy(self):
        print('json Test accuracy:', self.score_json[1])
        self.assertEqual(self.score_json[1], 0.9712962967378121, "json Test Accuracy")


if __name__ == '__main__':
    
    with open('C:/Windows/System32/config/systemprofile/AppData/Local/Jenkins/.jenkins/workspace/clone-modac-using-https_tc1_qc/Pilot1/TC1/results12.xml', 'wb') as output:
    
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
    try:
        K.clear_session()
    except AttributeError:      # theano does not have this function
        pass

